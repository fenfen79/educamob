"use client";



import React, { useState, useEffect, useRef } from "react";

import ReactMarkdown from "react-markdown";

import remarkGfm from "remark-gfm";

import remarkMath from "remark-math";

import rehypeKatex from "rehype-katex";

import "katex/dist/katex.min.css";

import { Sun, Moon, Menu, Paperclip, Send, X, Plus, Edit2, User, MessageCircle } from "lucide-react";



type Message = {

  id: string;

  role: "user" | "ai";

  text: string;

  imageUrl?: string;

};



type Session = {

  id: string;

  title: string;

};



const SUGGESTIONS = [

  "📐 Como resolver equações de 2º grau?",

  "🧪 Explique a tabela periódica",

  "📖 Resuma o livro Dom Casmurro",

  "🌍 O que causou a 1ª Guerra Mundial?"

];



const getApiBaseUrl = () => {

  if (typeof window === "undefined") return "http://127.0.0.1:8000";

  const host = window.location.hostname;

  if (host === "educamob.com.br" || host === "app.educamob.com.br") {

    return "https://api.educamob.com.br";

  }

  return "";

};



const sanitizeContent = (content: string) => {
  if (!content) return "";

  // 1. Auto-heal KaTeX double subscript error
  // Caso A: Carga elétrica com sobrescrito seguida de subscrito de estado (ex: \text{HSO}_4^-_{(aq)} -> \text{HSO}_4^-{}_{(aq)})
  let sanitized = content.replace(
    /(\^\{?[^\s_}]+\}?|\^[a-zA-Z0-9+-])_(\{?\([a-zA-Z0-9]+\)\}?|\{?[a-zA-Z0-9]+\}?)/g,
    (m, p1, p2) => p1 + "{}_" + p2
  );

  // Caso B: Subscrito duplo direto (ex: SO_4_{(aq)} -> SO_4{}_{(aq)} ou \text{SO}_4_{(aq)} -> \text{SO}_4{}_{(aq)})
  sanitized = sanitized.replace(
    /(_\{?[0-9a-zA-Z]+\}?)_(\{?\([a-zA-Z0-9]+\)\}?)/g,
    (m, p1, p2) => p1 + "{}_" + p2
  );

  // 2. Normalizar subscritos Unicode em fórmulas químicas (ex: HNO₃ -> HNO_3, H₂SO₄ -> H_2SO_4, Ca(OH)₂ -> Ca(OH)_2)
  const unicodeSubMap: Record<string, string> = {
    '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4',
    '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
  };
  sanitized = sanitized.replace(/([A-Z][a-z]?|\))([₀-₉]+)/g, (m, el, subs) => {
    const converted = subs.split('').map((c: string) => unicodeSubMap[c] || c).join('').replace(/_/g, '');
    return `${el}_${converted}`;
  });

  // 2.1. SEGMENTAÇÃO: Separar blocos matemáticos ($$...$$ e $...$) e código para que o auto-heal de texto
  // JAMAIS corrompa fórmulas LaTeX existentes (ex: S_0, t_0, frações e variáveis dentro de $$...$$)
  const tokenRegex = /(```[\s\S]*?```|\$\$[\s\S]*?\$\$|\$(?:\\.|[^\$\n])+\$)/g;
  const parts = sanitized.split(tokenRegex);

  for (let i = 0; i < parts.length; i++) {
    const part = parts[i];
    // Se o fragmento for código ou bloco de matemática ($$...$$ ou $...$), PRESERVA 100% INTACTO (com auto-heal de chaves desbalanceadas em macros como \text{ mm$)
    if (
      part.startsWith("```") ||
      part.startsWith("$$") ||
      (part.startsWith("$") && part.endsWith("$") && part.length >= 2)
    ) {
      if (!part.startsWith("```")) {
        const isDisp = part.startsWith("$$") && part.endsWith("$$");
        const delim = isDisp ? "$$" : "$";
        let innerMath = isDisp ? part.slice(2, -2) : part.slice(1, -1);
        const openCount = (innerMath.match(/(?<!\\)\{/g) || []).length;
        const closeCount = (innerMath.match(/(?<!\\)\}/g) || []).length;
        if (openCount > closeCount) {
          innerMath = innerMath + "}".repeat(openCount - closeCount);
        }
        parts[i] = delim + innerMath + delim;
      }
      continue;
    }

    // AQUI ESTAMOS EM TEXTO PLANO FORA DE MATH:
    let textPart = part;

    // A) Fórmulas em negrito contendo subscrito com underscore: **H_2S** -> $H_2S$, **H_2SO_4** -> $H_2SO_4$
    textPart = textPart.replace(/\*\*(?:\\\$)?([A-Z][a-zA-Z0-9_()+-]*_[1-9][0-9a-zA-Z]*[a-zA-Z0-9_()+-]*)(?:\\\$)?\*\*/g, (m, f) => `$${f}$`);

    // B) Fórmulas químicas em negrito com números diretos: **H2SO4** -> $H_2SO_4$, **H3PO4** -> $H_3PO_4$, **Ca(OH)2** -> $Ca(OH)_2$
    textPart = textPart.replace(/\*\*([A-Z][a-z]?(?:\([A-Za-z]+\))?\d+(?:[A-Z][a-z]?\d*|\([A-Za-z]+\)\d*)*)\*\*/g, (m, f) => {
      if (/^\d+[ºª]/.test(f)) return m;
      const latexForm = f.replace(/([A-Z][a-z]?|\))(\d+)/g, '$1_$2');
      return `$${latexForm}$`;
    });

    // C) Fórmulas químicas comuns conhecidas em negrito: **HI**, **HF**, **HCl**, **HBr**, **NaCl**, etc. -> $HI$, $HF$, etc.
    textPart = textPart.replace(/\*\*(H[IF]|HCl|HBr|HCN|NaCl|NaOH|KOH|KCl|CO_2|H_2O|NH_3|CH_4)\*\*/g, (m, f) => `$${f}$`);

    // D) Fórmulas químicas soltas com subscrito com underscore fora de math (índices >= 1, nunca _0 que são variáveis de física/matemática como S_0, t_0)
    // Ex: H_2S, H_2SO_4, Ca(OH)_2, Fe_2O_3 -> $H_2S$, $H_2SO_4$
    textPart = textPart.replace(/(?<!\$|\w)([A-Z][a-z]?(?:\([A-Za-z]+\))?_[1-9]\d*(?:[A-Z][a-z]?(?:_[1-9]\d*)?|\([A-Za-z]+\)(?:_[1-9]\d*)?)*)(?!\$|\w)/g, (m, f) => `$${f}$`);

    // E) Quebra de alternativas de múltipla escolha para ficarem uma por linha
    // Caso 1: quebra antes de 'a)' ou 'A)' se estiver grudado em texto introdutório
    textPart = textPart.replace(/([:?.\$!])[ \t]*([aA]\))(?=[ \t]+\S)/g, '$1\n\n$2');
    textPart = textPart.replace(/(respectivamente|abaixo|seguir)[ \t]*:?[ \t]*([aA]\))(?=[ \t]+\S)/gi, '$1:\n\n$2');

    // Caso 2: quebra antes de b), c), d), e) (ou maiúsculas) se estiverem inline na mesma linha
    textPart = textPart.replace(/([^\n])[ \t]+([b-eB-E]\))(?=[ \t]+\S)/g, '$1\n\n$2');

    // Normaliza opções de menu em negrito: 1. **Aprender📚** -> 1. Aprender📚
    textPart = textPart.replace(/(?:^|\n)([1-6])[\.\)\-]?\s*\*\*([^\*\n]+)\*\*/gi, (m, n, rest) => `\n\n${n}. ${rest}`);

    // Normaliza opções das 6 Trilhas mesmo que venham SEM numeração ou com emojis colados (ex: "Aprender📚", "Praticar📝")
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:1[\.\)\-]?\s*|1\uFE0F?\u20E3\s*)?(?:Aprender)\s*📚?/gi, "\n\n1\uFE0F\u20E3 Aprender 📚");
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:2[\.\)\-]?\s*|2\uFE0F?\u20E3\s*)?(?:Praticar)\s*📝?/gi, "\n\n2\uFE0F\u20E3 Praticar 📝");
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:3[\.\)\-]?\s*|3\uFE0F?\u20E3\s*)?(?:Flashcards)\s*🃏?/gi, "\n\n3\uFE0F\u20E3 Flashcards 🃏");
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:4[\.\)\-]?\s*|4\uFE0F?\u20E3\s*)?(?:Resumo)\s*🧠?/gi, "\n\n4\uFE0F\u20E3 Resumo 🧠");
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:5[\.\)\-]?\s*|5\uFE0F?\u20E3\s*)?(?:Enviar\s+quest[ãa]o)\s*🖼️?/gi, "\n\n5\uFE0F\u20E3 Enviar questão 🖼️");
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:6[\.\)\-]?\s*|6\uFE0F?\u20E3\s*)?(?:Finalizar)\s*⏸️?/gi, "\n\n6\uFE0F\u20E3 Finalizar ⏸️");

    // Garante que opções numeradas do menu (1. Aprender, 2. Praticar...) ou keycaps (1️⃣, 2️⃣...) sempre fiquem com badge e parágrafos separados (\n\n)
    textPart = textPart.replace(/(?:^|\n)([1-6])[\.\)\-]?\s*(?=(?:Aprender|Praticar|Flashcards|Resumo|Enviar quest|Finalizar))/gi, (match, num) => `\n\n${num}\uFE0F\u20E3 `);
    textPart = textPart.replace(/([^\n])\n?(([0-9]|10)\uFE0F?\u20E3)/g, "$1\n\n$2");
    textPart = textPart.replace(/(([0-9]|10)\uFE0F?\u20E3[^\n]+)\n([^\n0-9])/g, "$1\n\n$3");

    // Normaliza títulos de Microciclos mesmo se vierem sem ### ou colados no texto
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:###\s*)?(Microciclo\s+\d+[^:\n]*)(?:\n|$)/gi, "\n\n### $1\n\n");

    // Normaliza Objetivo de Aprendizagem isolando em parágrafo próprio
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:\*\*)?Objetivo:(?:\*\*)?\s*([^\n]+)/gi, "\n\n**Objetivo:** $1\n\n");

    // Normaliza Checagem de Compreensão isolando em parágrafo próprio
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:\*\*)?Checagem:(?:\*\*)?\s*([^\n]+)/gi, "\n\n**Checagem:** $1\n\n");

    // Normaliza Destaques Conceituais pedagógicos isolando em parágrafos próprios
    textPart = textPart.replace(/(?:^|\n)[ \t]*(?:\*\*)?(Pense assim:|Em outras palavras:|Importante:|Atenção:|Dica:)(?:\*\*)?\s*([^\n]+)/gi, "\n\n$1 $2\n\n");

    // Normaliza frases de fechamento/prompt do tutor
    textPart = textPart.replace(/([^\n])\n(Qual caminho você prefere|Qual opção você prefere|Fica tranquilo|Aguardo sua resposta|Qual alternativa você acha)/gi, "$1\n\n$2");

    // Isolamento defensivo de títulos Markdown (#, ##, ###, ####) com linhas em branco
    textPart = textPart.replace(/([^\n])\n(#{1,4}\s+[^\n]+)/g, "$1\n\n$2");
    textPart = textPart.replace(/(#{1,4}\s+[^\n]+)\n([^\n#])/g, "$1\n\n$2");

    parts[i] = textPart;
  }

  sanitized = parts.join("");

  // 3. Processamento linha a linha para isolamento perfeito de blocos KaTeX Display e alternativas
  const lines = sanitized.split("\n");
  const processedLines: string[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // Se for linha de tabela Markdown (| ... |), preserva 100% intacta com equações inline
    // Higieniza barras invertidas soltas usadas como separador de títulos (ex: "| Evento A \ B |" -> "| Evento A / B |")
    if (trimmed.startsWith("|") && trimmed.includes("|", 1)) {
      const safeTableLine = line.replace(/\s+\\\s+/g, " / ");
      processedLines.push(safeTableLine);
      continue;
    }

    // Se a linha for uma das opções do Menu de Trilhas (1️⃣ Aprender... 6️⃣ Finalizar)
    const trilhaRegex = /^[ \t]*[1-6]\uFE0F?\u20E3/;
    if (trilhaRegex.test(trimmed)) {
      if (processedLines.length > 0 && processedLines[processedLines.length - 1].trim() !== "") {
        processedLines.push("");
      }
      processedLines.push(line);
      processedLines.push("");
      continue;
    }

    // Se a linha for uma alternativa de múltipla escolha (ex: "a) 18 e 4,5." ou "b) 4,5 e 18.")
    const altRegex = /^[ \t]*[a-eA-E][\)\.]/;
    const promptRegex = /^(?:Qual [eé]|Aguardo|Envie|Digite|Responda|Fica tranquilo)/i;

    if (altRegex.test(trimmed)) {
      if (processedLines.length > 0 && processedLines[processedLines.length - 1].trim() !== "") {
        processedLines.push("");
      }
      processedLines.push(line);
      processedLines.push("");
      continue;
    }

    if (promptRegex.test(trimmed)) {
      if (processedLines.length > 0 && processedLines[processedLines.length - 1].trim() !== "") {
        processedLines.push("");
      }
      processedLines.push(line);
      continue;
    }

    // Caso 1: Linha que contém $$...$$ em linha única (ex: "  $$HA_{(aq)} \rightarrow H^+_{(aq)} + A^-_{(aq)}$$")
    const singleLineBlockMath = /^(\s*)\$\$(.+?)\$\$(\s*)$/;
    const matchBlock = line.match(singleLineBlockMath);
    if (matchBlock) {
      const indent = matchBlock[1] || "";
      const mathContent = matchBlock[2].trim();
      // Quebra em bloco multi-linha com linhas em branco para garantir renderização de katex-display
      processedLines.push("");
      processedLines.push(`${indent}$$\n${indent}${mathContent}\n${indent}$$`);
      processedLines.push("");
      continue;
    }

    // Caso 2: Linha de lista com marcador contendo equação de reação ($... \to ...$)
    // ex: "- **Equação Geral:** $HA_{(aq)} \rightarrow H^+_{(aq)} + A^-_{(aq)}$"
    const listWithFormula = /^(\s*(?:[-*+]|\d+\.)\s+)(.*?)(?<!\$)\$([^\$\r\n]+?(?:\\to|\\rightarrow|\\xrightarrow|\\rightleftharpoons|\\leftrightarrow)[^\$\r\n]*?)\$(?!\$)(.*)$/;
    const matchListItem = line.match(listWithFormula);
    if (matchListItem) {
      const listMarker = matchListItem[1];
      const textBefore = matchListItem[2].trim();
      const formula = matchListItem[3].trim();
      const textAfter = matchListItem[4].trim();

      if (textBefore) {
        processedLines.push(`${listMarker}${textBefore}`);
      }
      processedLines.push("");
      processedLines.push(`  $$\n  ${formula}\n  $$`);
      processedLines.push("");
      if (textAfter) {
        processedLines.push(`  ${textAfter}`);
      }
      continue;
    }

    // Caso 3: Fórmula com seta inline solta no meio de um parágrafo normal
    const arrowRegex = /(?<!\$)\$([^\$\r\n]+?(?:\\to|\\rightarrow|\\xrightarrow|\\rightleftharpoons|\\leftrightarrow)[^\$\r\n]*?)\$(?!\$)/g;
    if (arrowRegex.test(line)) {
      arrowRegex.lastIndex = 0;
      processedLines.push("");
      processedLines.push(line.replace(arrowRegex, "\n\n$$\n$1\n$$\n\n"));
      processedLines.push("");
      continue;
    }

    processedLines.push(line);
  }

  return processedLines.join("\n");
};

const splitMessageMenu = (text: string): { content: string; menu: string | null } => {
  if (!text) return { content: "", menu: null };

  const hasMenu = (text.includes("1️⃣") || text.includes("1. Aprender")) && (
    text.includes("6️⃣") ||
    text.includes("6. Finalizar") ||
    text.includes("Finalizar ⏸️") ||
    text.includes("Aprender") ||
    text.includes("8️⃣") ||
    text.includes("Bora ler!")
  );
  if (!hasMenu) {
    return { content: text, menu: null };
  }

  let menuIndex1 = text.indexOf("1️⃣");
  if (menuIndex1 === -1) {
    menuIndex1 = text.indexOf("1. Aprender");
  }
  if (menuIndex1 <= 0 || menuIndex1 < 120) {
    return { content: text, menu: null };
  }

  const textBefore = text.slice(0, menuIndex1);
  let splitIndex = -1;

  const hrIndex = textBefore.lastIndexOf("\n---\n");
  if (hrIndex !== -1 && hrIndex > 100) {
    splitIndex = hrIndex;
  } else {
    const introPhrases = [
      "agora que você concluiu",
      "agora que você finalizou",
      "escolha o próximo passo",
      "se quiser continuar",
      "qual caminho você prefere",
      "como você prefere começar",
      "tema definido:"
    ];
    const lowerBefore = textBefore.toLowerCase();
    for (const phrase of introPhrases) {
      const idx = lowerBefore.lastIndexOf(phrase);
      if (idx !== -1 && idx > 100) {
        splitIndex = idx;
        break;
      }
    }
  }

  if (splitIndex === -1) {
    const doubleNewline = textBefore.lastIndexOf("\n\n");
    if (doubleNewline !== -1 && doubleNewline > 100) {
      splitIndex = doubleNewline;
    } else {
      splitIndex = menuIndex1;
    }
  }

  const mainContent = text.slice(0, splitIndex).trim();
  const rawMenu = text.slice(splitIndex).trim();
  const lines = rawMenu.split("\n");
  const cleanMenu = (lines[0] && lines[0].trim().replace(/-/g, "") === "")
    ? lines.slice(1).join("\n").trim()
    : rawMenu;

  return { content: mainContent, menu: cleanMenu };
};

const isWidescreenContent = (text: string) => {
  if (!text) return false;
  const lower = text.toLowerCase();
  
  // Detecção de Teoria, Microciclos e E-books (sempre em tela ampla widescreen para leitura confortável)
  const isTeoria = 
    lower.includes("microciclo") ||
    lower.includes("objetivo:") ||
    lower.includes("checagem:") ||
    lower.includes("conexão com o mundo real") ||
    lower.includes("conexao com o mundo real") ||
    lower.includes("conceito central e fundamentos") ||
    lower.includes("atenção aos erros comuns") ||
    lower.includes("atencao aos erros comuns") ||
    text.includes("|");
    
  // Detecção de Resumir (Memorex)
  const isMemorex =
    lower.includes("visão panorâmica") ||
    lower.includes("visao panoramica") ||
    lower.includes("quadro síntese") ||
    lower.includes("quadro sintese") ||
    lower.includes("conceitos fundamentais") ||
    lower.includes("mapa conceitual completo") ||
    lower.includes("dicas de ouro");
    
  return isTeoria || isMemorex;
};



const LOADING_MESSAGES: Record<string, string[]> = {
  teoria: [
    "Consultando o acervo homologado da Educamob... 📚",
    "Preparando o próximo microciclo e checagem... 🎯"
  ],
  flashcards: [
    "Preparando os cartões de recuperação ativa... 🃏",
    "Selecionando os conceitos essenciais do material... 🎯"
  ],
  memorex: [
    "Estruturando a visão panorâmica e o quadro síntese... 🧠",
    "Organizando os conceitos fundamentais do acervo... 📋",
    "Finalizando o resumo para revisão... ⚡"
  ]
};

const getTrackFromInput = (input: string, lastAiText: string = ""): "teoria" | "flashcards" | "memorex" | null => {
  if (!input) return null;
  const text = input.trim().toLowerCase();
  const isTrackMenuOnScreen = (lastAiText.includes("1️⃣") || lastAiText.includes("1. Aprender")) && 
                              (lastAiText.includes("6️⃣") || lastAiText.includes("6. Finalizar") || lastAiText.includes("Finalizar"));
  if (!isTrackMenuOnScreen && ["1", "2", "3", "4", "5", "6"].includes(text)) {
    return null;
  }
  
  // 1. Aprender
  if (
    text === "1" || 
    text.startsWith("1 ") || 
    text.startsWith("1.") || 
    text.includes("1️⃣") || 
    text.includes("aprender") || 
    text.includes("microciclo")
  ) {
    return "teoria";
  }

  // 3. Flashcards
  if (
    text === "3" || 
    text.startsWith("3 ") || 
    text.startsWith("3.") || 
    text.includes("3️⃣") || 
    text.includes("flashcard") || 
    text.includes("flashcards") || 
    text.includes("revisar")
  ) {
    return "flashcards";
  }

  // 4. Resumo
  if (
    text === "4" || 
    text.startsWith("4 ") || 
    text.startsWith("4.") || 
    text.startsWith("4-") || 
    text.includes("4️⃣") || 
    text.includes("resumo") || 
    text.includes("resumir") || 
    text.includes("memorex")
  ) {
    return "memorex";
  }
  
  return null;
};


export default function ChatApp() {

  const [theme, setTheme] = useState<"light" | "dark">("dark");

  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const [messages, setMessages] = useState<Message[]>([]);

  const [input, setInput] = useState("");

  const [isTyping, setIsTyping] = useState(false);
  const [loadingTrack, setLoadingTrack] = useState<"teoria" | "flashcards" | "memorex" | null>(null);
  const [loadingMessageIndex, setLoadingMessageIndex] = useState<number>(0);

  useEffect(() => {
    if (!isTyping || !loadingTrack || !LOADING_MESSAGES[loadingTrack]) {
      setLoadingMessageIndex(0);
      return;
    }
    const list = LOADING_MESSAGES[loadingTrack];
    const interval = setInterval(() => {
      setLoadingMessageIndex(prev => (prev + 1) % list.length);
    }, 3000); // Exatos 3 segundos por mensagem
    return () => clearInterval(interval);
  }, [isTyping, loadingTrack]);

  const [imagePreview, setImagePreview] = useState<string | null>(null);

  const [imageBase64, setImageBase64] = useState<string | null>(null);

  

  const [sessions, setSessions] = useState<Session[]>([]);

  const [currentSessionId, setCurrentSessionId] = useState<string | null>(null);

  const [editingSessionId, setEditingSessionId] = useState<string | null>(null);

  const [editTitle, setEditTitle] = useState("");



  const messagesEndRef = useRef<HTMLDivElement>(null);

  const isStreamingRef = useRef<boolean>(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  const textareaRef = useRef<HTMLTextAreaElement>(null);



  const [isLoadingHistory, setIsLoadingHistory] = useState(false);

  const [keyboardHeight, setKeyboardHeight] = useState(0);



  useEffect(() => {

    // Check if device is iOS

    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

    

    const handleViewportChange = () => {

      if (window.visualViewport) {

        if (isIOS) {

          const layoutH = window.innerHeight;

          const visualH = window.visualViewport.height;

          const diff = layoutH - visualH;

          setKeyboardHeight(diff > 50 ? diff : 0);

          if (window.scrollY > 0) {

            window.scrollTo(0, 0);

          }

        } else {

          // On Android, layout viewport resizes natively, so we don't need translateY hacks.

          // Just ensure scroll stays at 0.

          setKeyboardHeight(0);

          if (window.scrollY > 0) {

            window.scrollTo(0, 0);

          }

        }

      }

    };

    window.visualViewport?.addEventListener('resize', handleViewportChange);

    window.visualViewport?.addEventListener('scroll', handleViewportChange);

    window.addEventListener('resize', handleViewportChange);

    return () => {

      window.visualViewport?.removeEventListener('resize', handleViewportChange);

      window.visualViewport?.removeEventListener('scroll', handleViewportChange);

      window.removeEventListener('resize', handleViewportChange);

    };

  }, []);



  useEffect(() => {

    // Initialize theme from localStorage or default to dark

    const stored = localStorage.getItem("educamob_theme") as "light" | "dark" | null;

    if (stored === "light") {

      setTheme("light");

      document.documentElement.removeAttribute("data-theme");

    } else {

      setTheme("dark");

      document.documentElement.setAttribute("data-theme", "dark");

    }

  }, []);



  useEffect(() => {

    const fetchCloudSessions = async () => {

      try {

        const userId = await getUserId();

        

        const API_BASE = getApiBaseUrl();

        

        const res = await fetch(`${API_BASE}/api/sessions/${userId}`);

        if (res.ok) {

          const data = await res.json();

          // Transform backend format to frontend format

          const formattedSessions: Session[] = data.sessions.map((s: any) => ({

            id: s.id,

            title: s.title || "Conversa",

            date: new Date(s.created_at).getTime(),

            messages: []

          }));

          

          setSessions(formattedSessions);

          

          if (formattedSessions.length > 0) {

            loadSession(formattedSessions[0].id);

          } else {

            startNewSession();

          }

        } else {

          console.error("API retornou erro ao buscar sessões");

          startNewSession();

        }

      } catch (e) {

        console.error("Erro ao buscar sessões na nuvem:", e);

        startNewSession();

      }

    };

    

    fetchCloudSessions();

  }, []);



  const startNewSession = () => {

    setCurrentSessionId(null);

    setMessages([]);

    if (typeof window !== "undefined" && window.innerWidth >= 768) {

      setTimeout(() => textareaRef.current?.focus(), 50);

    }

  };



  const loadSession = async (id: string) => {

    setCurrentSessionId(id);

    setIsSidebarOpen(false);

    setIsLoadingHistory(true);

    

    try {

      const API_BASE = getApiBaseUrl();

      const res = await fetch(`${API_BASE}/api/chat/${id}`);

      if (res.ok) {

        const data = await res.json();

        const formattedMessages: Message[] = data.history.map((msg: any) => ({

          id: msg.id || Date.now().toString() + Math.random(),

          role: msg.role,

          text: msg.content

        }));

        setMessages(formattedMessages);
        setTimeout(() => {
          messagesEndRef.current?.scrollIntoView({ behavior: "auto" });
        }, 100);
      }

    } catch (e) {

      console.error("Erro ao buscar mensagens:", e);

    } finally {

      setIsLoadingHistory(false);

    }

  };



  const deleteSession = (e: React.MouseEvent, id: string) => {

    e.stopPropagation();

    // Apenas oculta visualmente (Opcionalmente, implementar DELETE na API)

    setSessions(prev => {

      const updated = prev.filter(s => s.id !== id);

      if (currentSessionId === id) {

        if (updated.length > 0) {

          loadSession(updated[0].id);

        } else {

          startNewSession();

        }

      }

      return updated;

    });

  };



  const toggleTheme = () => {

    const newTheme = theme === "dark" ? "light" : "dark";

    setTheme(newTheme);

    localStorage.setItem("educamob_theme", newTheme);

    if (newTheme === "dark") {

      document.documentElement.setAttribute("data-theme", "dark");

    } else {

      document.documentElement.removeAttribute("data-theme");

    }

  };



  useEffect(() => {
    if (isStreamingRef.current) {
      messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, isTyping]);



  useEffect(() => {

    if (textareaRef.current) {

      textareaRef.current.style.height = "auto";

      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;

    }

  }, [input]);



  useEffect(() => {

    if (!isTyping && typeof window !== "undefined" && window.innerWidth >= 768) {

      textareaRef.current?.focus();

    }

  }, [isTyping]);



  useEffect(() => {

    if (typeof window !== "undefined" && window.innerWidth >= 768) {

      textareaRef.current?.focus();

    }

  }, []);



  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {

    const file = e.target.files?.[0];

    if (!file) return;

    

    const reader = new FileReader();

    reader.onload = () => {

      const result = reader.result as string;

      setImagePreview(result);

      setImageBase64(result.split(",")[1]);

    };

    reader.readAsDataURL(file);

    e.target.value = "";

  };



  const handlePaste = (e: React.ClipboardEvent<HTMLTextAreaElement>) => {

    const items = e.clipboardData?.items;

    

    if (!items || items.length === 0) {

      console.warn("Nenhum item na área de transferência.");

      return;

    }



    let foundImage = false;

    let types = [];

    

    for (let i = 0; i < items.length; i++) {

      types.push(items[i].type);

      if (items[i].type.indexOf("image") !== -1) {

        foundImage = true;

        e.preventDefault();

        const file = items[i].getAsFile();

        

        if (!file) {

          console.error("Não foi possível extrair o arquivo da imagem.");

          continue;

        }

        

        const reader = new FileReader();

        reader.onload = () => {

          const result = reader.result as string;

          setImagePreview(result);

          setImageBase64(result.split(",")[1]);

          console.log("Imagem processada com sucesso via Ctrl+V");

        };

        reader.readAsDataURL(file);

        break;

      }

    }

    

    if (!foundImage) {

      console.log("Tipos detectados no Ctrl+V:", types);

      // alert apenas para debug rápido se ele colar algo que não é reconhecido como imagem

      // alert("Nenhuma imagem detectada. Tipos encontrados: " + types.join(", "));

    }

  };



  const removeImage = () => {

    setImagePreview(null);

    setImageBase64(null);

  };



  const getUserId = async () => {

    try {

      // @ts-ignore

      if (window.supabase && window.supabase.auth) {

        // @ts-ignore

        const { data } = await window.supabase.auth.getSession();

        if (data?.session?.user) return data.session.user.id;

      }

      

      const token = localStorage.getItem("sb-jaaiyectjtmlymcjzgpb-auth-token");

      if (token) {

        const parsed = JSON.parse(token);

        if (parsed?.user?.id) return parsed.user.id;

      }

    } catch (e) {

      console.error("Erro auth", e);

    }

    return "00000000-0000-0000-0000-000000000001";

  };



  const handleSend = async (textToSend: string = input) => {

    if (!textToSend.trim() && !imageBase64) return;

    if (isTyping) return;



    const newUserMsg: Message = {

      id: Date.now().toString(),

      role: "user",

      text: textToSend,

      imageUrl: imagePreview || undefined

    };



    setMessages(prev => [...prev, newUserMsg]);

    setInput("");

    setImagePreview(null);

    const b64ToSend = imageBase64;

    setImageBase64(null);

    const sendTimestamp = Date.now();
    const lastAiMsg = [...messages].reverse().find(m => m.role === "ai")?.text || "";
    const track = getTrackFromInput(textToSend, lastAiMsg);
    setLoadingTrack(track);
    setLoadingMessageIndex(0);
    setIsTyping(true);
    isStreamingRef.current = true;
    setTimeout(() => {
      messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, 50);

    // Janela mínima de 6s (2 mensagens completas de 3s cada) APENAS para Bora Ler, Flashcards e Memorex
    const minLoadingDuration = track ? 6000 : 0;



    if (textareaRef.current) {

      textareaRef.current.style.height = "auto";

    }



    try {

      const userId = await getUserId();

      

      const payload = {

        message: textToSend,

        session_id: currentSessionId,

        user_id: userId,

        image_base64: b64ToSend

      };



      const API_BASE = getApiBaseUrl();

      const response = await fetch(`${API_BASE}/api/chat`, {

        method: "POST",

        headers: { "Content-Type": "application/json" },

        body: JSON.stringify(payload)

      });



      if (!response.ok) throw new Error("Erro na API");



      const reader = response.body?.getReader();

      const decoder = new TextDecoder("utf-8");

      

      let aiResponseText = "";

      const aiMsgId = (Date.now() + 1).toString();

      

      let buffer = "";
      let isFirstChunk = true;
      let lastRenderTime = 0;

      while (reader) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n\n");
        buffer = lines.pop() || "";

        let hasNewChunkInBatch = false;

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const dataStr = line.slice(6);
            if (dataStr === "[DONE]") continue;

            try {
              const data = JSON.parse(dataStr);
              if (data.session_id && !currentSessionId) {
                setCurrentSessionId(data.session_id);
                setSessions(prev => {
                  if (!prev.find(s => s.id === data.session_id)) {
                    return [{ id: data.session_id, title: textToSend.substring(0, 30) + "..." }, ...prev];
                  }
                  return prev;
                });
              }
              if (data.error) throw new Error(data.error);
              if (data.chunk) {
                aiResponseText += data.chunk;
                hasNewChunkInBatch = true;
              }
            } catch (e) {
              console.error("Parse SSE error", e);
            }
          }
        }

        if (hasNewChunkInBatch) {
          if (isFirstChunk) {
            isFirstChunk = false;
            const elapsed = Date.now() - sendTimestamp;
            const waitTime = Math.max(0, minLoadingDuration - elapsed);
            if (waitTime > 0) {
              await new Promise(resolve => setTimeout(resolve, waitTime));
            }
            // Desativa o scroll para o fundo ANTES de montar a resposta da IA:
            // ancora a tela imediatamente no TOPO da resposta (Seção 1) para leitura imediata aos ~6s!
            isStreamingRef.current = false;
            setIsTyping(false);
            setMessages(prev => [...prev, { id: aiMsgId, role: "ai", text: aiResponseText }]);
            lastRenderTime = Date.now();
            setTimeout(() => {
              const el = document.getElementById(`msg-${aiMsgId}`);
              if (el) {
                el.scrollIntoView({ behavior: "smooth", block: "start" });
              }
            }, 80);
          } else {
            const now = Date.now();
            if (now - lastRenderTime >= 80) {
              lastRenderTime = now;
              setMessages(prev =>
                prev.map(msg => msg.id === aiMsgId ? { ...msg, text: aiResponseText } : msg)
              );
            }
          }
        }
      }

      // Flush final garantido ao término do stream (sem puxar o scroll caso o aluno já esteja lendo)
      isStreamingRef.current = false;
      if (!isFirstChunk) {
        setMessages(prev =>
          prev.map(msg => msg.id === aiMsgId ? { ...msg, text: aiResponseText } : msg)
        );
      }

    } catch (e: any) {

      const errorMsg = e.message.includes("logado") ? `⚠️ Ops! ${e.message}` : `⚠️ DEBUG ERROR: ${e.message}`;

      setMessages(prev => [...prev, { id: Date.now().toString(), role: "ai", text: errorMsg }]);

    } finally {
      isStreamingRef.current = false;
      setIsTyping(false);

      if (typeof window !== "undefined" && window.innerWidth >= 768) {

        setTimeout(() => textareaRef.current?.focus(), 50);

      }

    }

  };



  const handleKeyDown = (e: React.KeyboardEvent) => {

    if (e.key === "Enter" && !e.shiftKey) {

      e.preventDefault();

      if (!isTyping) {

        handleSend();

      }

    }

  };



  // Transforma emojis de nmeros em quadradinhos laranjas com glassmorphism sofisticado
  const renderWithBadges = (text: string) => {
    if (typeof text !== "string") return text;
    const regex = /([0-9]|10)\uFE0F?\u20E3/g;
    const parts = text.split(regex);
    if (parts.length === 1) return text;

    const result: (string | React.ReactNode)[] = [];
    for (let i = 0; i < parts.length; i++) {
      let part = parts[i];
      if (i % 2 === 1) {
        const num = part;
        result.push(
          <button
            key={i}
            type="button"
            className="orange-badge"
            title={`Selecionar opção ${num}`}
            style={{
              backgroundColor: "#ff6b00",
              color: theme === "dark" ? "#ffffff" : "#000000"
            }}
            onClick={(e) => {
              e.stopPropagation();
              if (!isTyping) {
                const trackLabels: Record<string, string> = {
                  "1": "1. Aprender📚",
                  "2": "2. Praticar📝",
                  "3": "3. Flashcards 🃏",
                  "4": "4. Resumo 🧠",
                  "5": "5. Enviar questão 🖼️",
                  "6": "6. Finalizar ⏸️",
                  "8": "6. Finalizar ⏸️"
                };
                handleSend(trackLabels[num] || num);
              }
            }}
          >
            <span
              style={{
                color: theme === "dark" ? "#ffffff" : "#000000",
                fontWeight: 800,
                lineHeight: 1,
                fontSize: "0.9rem"
              }}
            >
              {num}
            </span>
          </button>
        );
      } else {
        if (i > 0 && part.startsWith(" ")) {
          part = part.slice(1);
        }
        if (part) {
          result.push(part);
        }
      }
    }
    return result;
  };

  const processChildren = (children: any): any => {
    return React.Children.map(children, (child) => {
      if (typeof child === "string") {
        return renderWithBadges(child);
      }
      if (React.isValidElement(child) && (child.props as any)?.children) {
        return React.cloneElement(child, {
          ...(child.props as any),
          children: processChildren((child.props as any).children),
        });
      }
      return child;
    });
  };

  const getNodeText = (node: any): string => {
    if (!node) return "";
    if (typeof node === "string") return node;
    if (typeof node === "number") return String(node);
    if (Array.isArray(node)) return node.map(getNodeText).join("");
    if (React.isValidElement(node) && (node.props as any)?.children) {
      return getNodeText((node.props as any).children);
    }
    return "";
  };

  const stripReactPrefix = (children: any, prefix: string): any => {
    const childArray = Array.isArray(children) ? [...children] : [children];
    if (childArray.length === 0) return children;

    const first = childArray[0];
    if (typeof first === "string") {
      const escaped = prefix.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
      const stripped = first.replace(new RegExp("^\\s*" + escaped + "\\s*", "i"), "");
      return [stripped, ...childArray.slice(1)];
    }

    const firstText = (first && first.props && first.props.children ? getNodeText(first.props.children) : "");
    const cleanPrefix = prefix.replace(/:$/, "").trim().toLowerCase();
    if (firstText.trim().toLowerCase().startsWith(cleanPrefix)) {
      const remaining = childArray.slice(1);
      if (remaining.length > 0 && typeof remaining[0] === "string") {
        remaining[0] = remaining[0].replace(/^\s*[:\-–—]?\s*/, "");
      }
      return remaining;
    }
    return children;
  };

  const stripAltPrefix = (children: any): any => {
    const childArray = Array.isArray(children) ? [...children] : [children];
    if (childArray.length === 0) return children;

    const first = childArray[0];
    if (typeof first === "string") {
      const stripped = first.replace(/^[a-eA-E][\)\.][ \t]*/, "");
      return [stripped, ...childArray.slice(1)];
    }
    return children;
  };

  const markdownComponents = {
    p: ({ node, children, ...props }: any) => {
      const textStr = getNodeText(children).trim();

      // 0. Trilhas de Aprendizagem Interativas (Menu de 6 Opções)
      const trilhaMatch = textStr.match(/^([1-6])(?:\uFE0F?\u20E3|[\.\)\-]?\s*)(Aprender|Praticar|Flashcards|Resumo|Enviar\s+quest[ãa]o|Finalizar)/i);
      if (trilhaMatch) {
        const num = trilhaMatch[1];
        const trilhaInfoMap: Record<string, { title: string; emoji: string; desc: string; cmd: string }> = {
          "1": { title: "Aprender", emoji: "📚", desc: "Teoria guiada em microciclos passo a passo", cmd: "1" },
          "2": { title: "Praticar", emoji: "📝", desc: "Lista de exercícios graduados com gabarito oficial", cmd: "2" },
          "3": { title: "Flashcards", emoji: "🃏", desc: "Fixação ativa e repetição espaçada", cmd: "3" },
          "4": { title: "Resumo", emoji: "🧠", desc: "Síntese dos conceitos-chave e mapa mental", cmd: "4" },
          "5": { title: "Enviar questão", emoji: "🖼️", desc: "Tire dúvidas enviando texto ou foto", cmd: "5" },
          "6": { title: "Finalizar", emoji: "⏸️", desc: "Pausar e salvar o progresso da sessão", cmd: "6" },
        };
        const info = trilhaInfoMap[num] || { title: trilhaMatch[2], emoji: "🚀", desc: "Avançar na trilha", cmd: num };

        return (
          <button
            type="button"
            disabled={isTyping}
            onClick={() => {
              if (!isTyping) {
                handleSend(info.cmd);
              }
            }}
            className="w-full text-left my-2 p-3.5 md:p-4 rounded-xl bg-[var(--bg-card)] border border-[var(--border-subtle)] hover:border-[var(--accent-primary)] hover:bg-[var(--bg-hover)] active:scale-[0.99] transition-all duration-150 shadow-sm flex items-center justify-between group cursor-pointer"
            title={`Iniciar trilha: ${info.title}`}
          >
            <div className="flex items-center gap-3.5">
              <span className="w-8 h-8 rounded-lg bg-[var(--accent-primary-light)] text-[var(--accent-primary)] font-extrabold flex items-center justify-center shrink-0 text-sm group-hover:bg-[var(--accent-primary)] group-hover:text-black transition-colors shadow-xs">
                {num}
              </span>
              <div>
                <div className="font-bold text-[var(--text-primary)] text-[0.98rem] flex items-center gap-2">
                  <span>{info.title}</span>
                  <span className="text-base select-none">{info.emoji}</span>
                </div>
                <div className="text-xs text-[var(--text-muted)] font-normal mt-0.5">
                  {info.desc}
                </div>
              </div>
            </div>
            <span className="text-[var(--accent-primary)] text-sm font-semibold opacity-75 group-hover:opacity-100 group-hover:translate-x-1 transition-all flex items-center gap-1 select-none pr-1">
              Começar <span className="text-base">➔</span>
            </span>
          </button>
        );
      }

      // 0.1 Fallback para Título de Microciclo se vier encapsulado em parágrafo <p>
      const microMatch = textStr.match(/^(?:###\s*)?Microciclo\s+(\d+)[\s:—–-]+(.*)/i);
      if (microMatch) {
        return (
          <div className="mt-8 mb-6 p-4 md:p-5 rounded-2xl bg-gradient-to-r from-[var(--accent-primary-light)] via-[var(--bg-elevated)] to-transparent border border-[var(--accent-primary)]/25 border-l-4 border-l-[var(--accent-primary)] shadow-sm w-full">
            <div className="flex items-center gap-2 text-xs font-extrabold uppercase tracking-widest text-[var(--accent-primary)] mb-1.5">
              <span className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-pulse inline-block" />
              <span>Microciclo Formativo {microMatch[1]}</span>
            </div>
            <h3 className="text-xl md:text-2xl font-extrabold text-[var(--text-primary)] tracking-tight leading-snug m-0 p-0 border-0 bg-transparent">
              {microMatch[2] || processChildren(children)}
            </h3>
          </div>
        );
      }

      // 1. Alternativas de Múltipla Escolha: a), b), c), d), e)
      const altMatch = textStr.match(/^([a-eA-E])[\)\.][ \t]+/);
      if (altMatch) {
        const letter = altMatch[1].toUpperCase();
        const contentChildren = stripAltPrefix(children);

        return (
          <button
            type="button"
            disabled={isTyping}
            onClick={() => {
              if (!isTyping) {
                handleSend(letter.toLowerCase());
              }
            }}
            className="w-full text-left my-2 p-3.5 md:p-4 rounded-xl bg-[var(--bg-card)] border border-[var(--border-subtle)] hover:border-[var(--accent-primary)] hover:bg-[var(--bg-hover)] active:scale-[0.99] transition-all duration-150 shadow-sm flex items-start gap-3.5 group cursor-pointer"
            title={`Escolher alternativa ${letter}`}
          >
            <span className="w-7 h-7 rounded-lg bg-[var(--accent-primary-light)] text-[var(--accent-primary)] font-extrabold flex items-center justify-center shrink-0 text-sm group-hover:bg-[var(--accent-primary)] group-hover:text-black transition-colors shadow-xs">
              {letter}
            </span>
            <span className="flex-1 text-[var(--text-primary)] text-[0.96rem] leading-relaxed pt-0.5 font-normal">
              {processChildren(contentChildren)}
            </span>
          </button>
        );
      }

      // 2. Card Destacado para Objetivo de Aprendizagem
      if (textStr.startsWith("Objetivo:")) {
        const contentChildren = stripReactPrefix(children, "Objetivo:");
        return (
          <div className="my-5 p-4 md:p-4.5 rounded-xl bg-[var(--bg-secondary)] border border-[var(--border-subtle)] border-l-4 border-l-[var(--accent-primary)] shadow-sm">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[var(--accent-primary)] mb-1.5">
              <span className="text-sm select-none">🎯</span>
              <span>Objetivo de Aprendizagem</span>
            </div>
            <div className="text-[var(--text-primary)] leading-relaxed text-[0.97rem]">
              {processChildren(contentChildren)}
            </div>
          </div>
        );
      }

      // 3. Card Destacado para Checagem de Compreensão
      if (textStr.startsWith("Checagem:")) {
        const contentChildren = stripReactPrefix(children, "Checagem:");
        return (
          <div className="mt-7 mb-4 p-4.5 md:p-5 rounded-2xl bg-[var(--bg-secondary)] border border-[var(--border-subtle)] border-l-4 border-l-[var(--accent-primary)] shadow-sm">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[var(--accent-primary)] mb-2">
              <span className="text-base select-none">✍️</span>
              <span>Checagem de Compreensão</span>
            </div>
            <div className="text-[var(--text-primary)] font-medium leading-relaxed text-[1rem]">
              {processChildren(contentChildren)}
            </div>
          </div>
        );
      }

      // 4. Callout Pedagógico para Destaques Conceituais
      if (
        textStr.startsWith("Pense assim:") ||
        textStr.startsWith("Em outras palavras:") ||
        textStr.startsWith("Importante:") ||
        textStr.startsWith("Atenção:") ||
        textStr.startsWith("Dica:")
      ) {
        let icon = "💡";
        let label = "Destaque Conceitual";
        if (textStr.startsWith("Pense assim:")) {
          icon = "💡";
          label = "Pense assim";
        } else if (textStr.startsWith("Em outras palavras:")) {
          icon = "💡";
          label = "Em outras palavras";
        } else if (textStr.startsWith("Atenção:")) {
          icon = "⚠️";
          label = "Atenção aos Detalhes";
        } else if (textStr.startsWith("Importante:")) {
          icon = "📌";
          label = "Conceito Fundamental";
        } else if (textStr.startsWith("Dica:")) {
          icon = "✨";
          label = "Dica Prática";
        }

        const prefix = textStr.split(":")[0] + ":";
        const contentChildren = stripReactPrefix(children, prefix);

        return (
          <div className="my-4.5 p-4 rounded-xl bg-[var(--bg-secondary)]/90 border border-[var(--border-subtle)] border-l-4 border-l-[var(--accent-primary)] text-[var(--text-secondary)] leading-relaxed text-[0.96rem] shadow-xs">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[var(--accent-primary)] mb-1.5">
              <span className="text-sm select-none">{icon}</span>
              <span>{label}</span>
            </div>
            <div>
              {processChildren(contentChildren)}
            </div>
          </div>
        );
      }

      // 5. Nota de Rodapé / Mensagem de Encorajamento
      const lower = textStr.toLowerCase();
      if (
        lower.startsWith("fica tranquilo") ||
        lower.startsWith("qual alternativa") ||
        lower.startsWith("aguardo sua resposta") ||
        lower.startsWith("qual opção") ||
        lower.startsWith("envie sua resposta")
      ) {
        return (
          <div className="mt-4 mb-2 p-3 rounded-xl bg-[var(--bg-card)]/60 border border-[var(--border-subtle)]/70 text-xs md:text-sm text-[var(--text-muted)] italic flex items-center gap-2.5">
            <span className="text-base select-none">💡</span>
            <span className="flex-1">{processChildren(children)}</span>
          </div>
        );
      }

      return (
        <p className="my-3 leading-relaxed text-[var(--text-primary)] text-[0.98rem]" {...props}>
          {processChildren(children)}
        </p>
      );
    },
    ol: ({ node, children, ...props }: any) => (
      <ol className="list-decimal pl-6 my-3 space-y-2 marker:text-[var(--accent-primary)] marker:font-bold" {...props}>
        {processChildren(children)}
      </ol>
    ),
    ul: ({ node, children, ...props }: any) => (
      <ul className="list-disc pl-6 my-3 space-y-2 marker:text-[var(--accent-primary)]" {...props}>
        {processChildren(children)}
      </ul>
    ),
    li: ({ node, children, ...props }: any) => (
      <li className="my-1.5 leading-relaxed" {...props}>
        {processChildren(children)}
      </li>
    ),
    strong: ({ node, children, ...props }: any) => (
      <strong className="font-bold text-[var(--text-primary)]" {...props}>
        {processChildren(children)}
      </strong>
    ),
    blockquote: ({ node, children, ...props }: any) => (
      <blockquote className="my-4 p-4 border-l-4 border-[var(--accent-primary)] bg-[var(--bg-secondary)] rounded-r-xl italic text-[var(--text-secondary)] shadow-sm" {...props}>
        {processChildren(children)}
      </blockquote>
    ),
    table: ({ node, children, ...props }: any) => (
      <div className="w-full my-5 overflow-x-auto rounded-xl border border-[var(--border-medium)] shadow-sm">
        <table className="w-full border-collapse text-left text-sm md:text-base" {...props}>
          {processChildren(children)}
        </table>
      </div>
    ),
    th: ({ node, children, ...props }: any) => (
      <th className="bg-[var(--bg-secondary)] text-[var(--accent-primary)] font-bold px-4 py-3 border-b-2 border-[var(--border-medium)]" {...props}>
        {processChildren(children)}
      </th>
    ),
    td: ({ node, children, ...props }: any) => (
      <td className="px-4 py-2.5 border-b border-[var(--border-subtle)] bg-[var(--bg-card)]" {...props}>
        {processChildren(children)}
      </td>
    ),
    h1: ({ node, children, ...props }: any) => (
      <h1 className="text-2xl md:text-3xl font-extrabold mt-8 mb-4 text-[var(--text-primary)] leading-tight border-b-2 border-[var(--border-medium)] pb-2" {...props}>
        {processChildren(children)}
      </h1>
    ),
    h2: ({ node, children, ...props }: any) => (
      <h2 className="text-xl md:text-2xl font-bold mt-7 mb-3.5 pb-2 border-b border-[var(--border-medium)] text-[var(--text-primary)] leading-snug flex items-center gap-2" {...props}>
        {processChildren(children)}
      </h2>
    ),
    h3: ({ node, children, ...props }: any) => {
      const headingText = getNodeText(children).trim();
      const isMicrociclo = headingText.toLowerCase().includes("microciclo");

      if (isMicrociclo) {
        return (
          <div className="mt-8 mb-6 p-4 md:p-5 rounded-2xl bg-gradient-to-r from-[var(--accent-primary-light)] via-[var(--bg-elevated)] to-transparent border border-[var(--accent-primary)]/25 border-l-4 border-l-[var(--accent-primary)] shadow-sm w-full">
            <div className="flex items-center gap-2 text-xs font-extrabold uppercase tracking-widest text-[var(--accent-primary)] mb-1.5">
              <span className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-pulse inline-block" />
              <span>Microciclo Formativo</span>
            </div>
            <h3 className="text-xl md:text-2xl font-extrabold text-[var(--text-primary)] tracking-tight leading-snug m-0 p-0 border-0 bg-transparent" {...props}>
              {processChildren(children)}
            </h3>
          </div>
        );
      }

      return (
        <h3 className="text-lg md:text-xl font-bold mt-7 mb-3.5 text-[var(--accent-primary)] flex items-center gap-2.5 bg-[var(--accent-primary-light)] px-4 py-2.5 rounded-xl border-l-4 border-[var(--accent-primary)] w-full shadow-sm leading-snug" {...props}>
          {processChildren(children)}
        </h3>
      );
    },
    h4: ({ node, children, ...props }: any) => (
      <h4 className="text-base font-semibold mt-4 mb-2 text-[var(--text-primary)]" {...props}>
        {processChildren(children)}
      </h4>
    ),
  };

  return (

    <div className="flex h-screen w-full bg-[var(--bg-primary)] overflow-hidden font-sans">

      

      {/* Sidebar Overlay (Mobile) */}

      {isSidebarOpen && (

        <div 

          className="fixed inset-0 bg-black/50 z-40 md:hidden"

          onClick={() => setIsSidebarOpen(false)}

        />

      )}



      {/* Sidebar */}

      <aside className={`

        fixed inset-y-0 left-0 z-50 w-72 bg-[var(--bg-secondary)] border-r border-[var(--border-subtle)] flex flex-col p-4

        transform transition-transform duration-300 ease-in-out

        ${isSidebarOpen ? "translate-x-0" : "-translate-x-full"}

        md:relative md:translate-x-0

      `}>

        <div className="flex items-center justify-between mb-8">

          <div className="flex items-center gap-3">

            <div className="w-10 h-10 rounded-[12px] bg-[var(--accent-primary)] flex items-center justify-center shadow-sm">

              <img src={theme === "dark" ? "./owl-white.png" : "./owl-black.png"} alt="Mob.me" className="w-6 h-6 object-contain" />

            </div>

            <span className="font-extrabold text-[22px] tracking-tight text-[var(--text-primary)]">Mob.me</span>

          </div>

          <button className="md:hidden p-2 text-[var(--text-secondary)]" onClick={() => setIsSidebarOpen(false)}>

            <X size={20} />

          </button>

        </div>



        <button 

          onClick={() => {

            startNewSession();

            if (window.innerWidth < 768) setIsSidebarOpen(false);

          }}

          className="flex items-center justify-center gap-1.5 w-full py-2.5 mb-8 bg-transparent border border-[var(--border-medium)] rounded-full text-[var(--text-primary)] font-bold text-[15px] hover:bg-[var(--bg-hover)] transition-colors"

        >

          <span>+</span> Nova Conversa

        </button>



        <div className="text-[13px] font-bold text-[var(--text-muted)] uppercase tracking-wider mb-3">Histórico</div>

        

        <div className="flex-1 overflow-y-auto space-y-1">

          {sessions.map(session => (

            <div 

              key={session.id} 

              className={`flex items-center justify-between p-3 rounded-lg cursor-pointer group ${currentSessionId === session.id ? 'bg-[var(--bg-hover)]' : 'hover:bg-[var(--bg-hover)]'}`}

            >

              {editingSessionId === session.id ? (

                <input 

                  type="text" 

                  value={editTitle}

                  onChange={e => setEditTitle(e.target.value)}

                  onBlur={() => {

                    setSessions(prev => prev.map(s => s.id === session.id ? { ...s, title: editTitle } : s));

                    setEditingSessionId(null);

                    const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

                    const API_BASE = isLocalhost ? "http://127.0.0.1:8000" : "https://api.educamob.com.br";

                    fetch(`${API_BASE}/api/sessions/${session.id}/title`, {

                      method: 'PUT',

                      headers: { 'Content-Type': 'application/json' },

                      body: JSON.stringify({ title: editTitle })

                    }).catch(console.error);

                  }}

                  onKeyDown={e => {

                    if (e.key === "Enter") {

                      setSessions(prev => prev.map(s => s.id === session.id ? { ...s, title: editTitle } : s));

                      setEditingSessionId(null);

                      const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

                      const API_BASE = isLocalhost ? "http://127.0.0.1:8000" : "https://api.educamob.com.br";

                      fetch(`${API_BASE}/api/sessions/${session.id}/title`, {

                        method: 'PUT',

                        headers: { 'Content-Type': 'application/json' },

                        body: JSON.stringify({ title: editTitle })

                      }).catch(console.error);

                    }

                  }}

                  autoFocus

                  className="w-full bg-[var(--bg-input)] text-[var(--text-primary)] border border-[var(--accent-primary)] rounded px-2 py-1 text-sm outline-none"

                />

              ) : (

                <>

                  <div 

                    className="flex items-center gap-3 text-[var(--text-secondary)] flex-1 overflow-hidden"

                    onClick={() => loadSession(session.id)}

                  >

                    <MessageCircle size={16} className="shrink-0" />

                    <span className="truncate text-sm">{session.title}</span>

                  </div>

                  <button 

                    onClick={(e) => {

                      e.stopPropagation();

                      setEditTitle(session.title);

                      setEditingSessionId(session.id);

                    }}

                    className="text-[var(--text-muted)] opacity-0 group-hover:opacity-100 hover:text-[var(--text-primary)] transition-opacity p-1"

                  >

                    <Edit2 size={14} />

                  </button>

                </>

              )}

            </div>

          ))}

        </div>

      </aside>



      {/* Main Content */}

      <div className="flex-1 relative min-w-0 w-full min-h-screen">

        

        {/* Header */}

        <header className="fixed top-0 left-0 right-0 h-[68px] md:left-[280px] flex items-center justify-between px-4 py-3 z-30 bg-[var(--bg-primary)]/80 backdrop-blur-md">

          <div className="flex items-center gap-3">

            <button 

              className="md:hidden p-2 -ml-2 text-[var(--text-primary)] bg-[var(--bg-elevated)] border border-[var(--border-medium)] rounded-xl"

              onClick={() => setIsSidebarOpen(true)}

            >

              <Menu size={20} />

            </button>

            <a 

              href="https://educamob.com.br" 

              className="inline-flex items-center px-4 py-2 bg-[var(--bg-elevated)] border border-[var(--border-medium)] rounded-full text-[var(--text-primary)] font-semibold text-sm hover:bg-[var(--bg-hover)] transition-colors no-underline"

            >

              ← Voltar

            </a>

          </div>



          <button 

            onClick={toggleTheme}

            className="flex items-center w-[52px] h-[28px] border-2 border-[var(--text-primary)] rounded-full relative transition-colors cursor-pointer"

            title="Alternar tema"

          >

            {/* Background Icons */}

            <div className="absolute inset-0 flex items-center justify-between px-1.5 w-full pointer-events-none">

              <Sun size={15} className="text-[var(--text-primary)] stroke-[2.5]" />

              <Moon size={13} className="text-[var(--text-primary)] stroke-[2.5] fill-[var(--text-primary)]" />

            </div>

            

            {/* Sliding Thumb */}

            <div 

              className={`w-5 h-5 rounded-full bg-[var(--text-primary)] transform transition-transform duration-300 ease-in-out relative z-10 ${

                theme === "dark" ? "translate-x-[25px]" : "translate-x-[3px]"

              }`}

            />

          </button>

        </header>



        {/* Chat Area */}

        <main className="fixed top-[68px] left-0 right-0 md:left-[280px] overflow-y-auto p-4 flex flex-col items-center z-10" style={{ height: 'calc(100vh - 68px)', paddingBottom: '50vh' }}>
          <div className="w-full flex flex-col items-center">
            {messages.length === 0 ? (
              <div className="flex flex-col items-center justify-center flex-1 h-full min-h-[60vh] w-full max-w-3xl">
                <div className="w-24 h-24 mb-6 bg-[var(--accent-primary)] rounded-3xl flex items-center justify-center shadow-lg shadow-[var(--accent-primary-light)] animate-[float_4s_ease-in-out_infinite]">
                  <img src="./owl-white.png" alt="Mob.me" className="w-16 h-16 object-contain" />
                </div>
                <h1 className="text-2xl md:text-3xl font-bold text-[var(--text-primary)] mb-3 text-center">
                  Oi! Aqui é a <span className="text-[var(--accent-primary)]">Mob.me</span>,<br/> o que vamos aprender hoje?
                </h1>
                <p className="text-[var(--text-secondary)] text-center max-w-md mb-10 text-balance text-sm md:text-base">
                  A Educamob em versão I.A. Envie sua dúvida por texto ou foto e lembre-se: escola é onde você aprende!
                </p>
                <div className="flex flex-wrap justify-center gap-3 w-full max-w-2xl">
                  {SUGGESTIONS.map(s => (
                    <button 
                      key={s}
                      onClick={() => handleSend(s)}
                      className="px-5 py-3 bg-[var(--bg-card)] border border-[var(--border-subtle)] rounded-full text-[var(--text-secondary)] text-sm hover:border-[var(--accent-primary)] hover:text-[var(--text-primary)] transition-all flex items-center gap-2"
                    >
                      {s}
                    </button>
                  ))}
                </div>
              </div>
            ) : (
              <div className="w-full flex flex-col items-center space-y-6">
                {messages.map(msg => {
                  if (msg.role === "user") {
                    return (
                      <div 
                        key={msg.id} 
                        id={`msg-${msg.id}`} 
                        className="w-full flex justify-end max-w-3xl"
                      >
                        <div className="flex gap-4 w-full flex-row-reverse">
                          <div className="w-10 h-10 rounded-xl shrink-0 flex items-center justify-center bg-[var(--accent-primary)]">
                            <User size={20} className="text-white" />
                          </div>
                          <div className="flex flex-col max-w-[85%] md:max-w-[75%] items-end">
                            <div className="px-5 py-4 rounded-2xl overflow-hidden bg-[var(--accent-primary)] text-black rounded-tr-sm">
                              {msg.imageUrl && (
                                <img src={msg.imageUrl} alt="Anexo" className="max-w-full rounded-xl mb-3 max-h-60 object-contain" />
                              )}
                              <div className="whitespace-pre-wrap font-medium">{msg.text}</div>
                            </div>
                          </div>
                        </div>
                      </div>
                    );
                  }

                  // msg.role === "ai"
                  const { content: mainText, menu } = splitMessageMenu(msg.text);
                  const isWide = isWidescreenContent(mainText);

                  return (
                    <div key={msg.id} className="w-full flex flex-col items-center space-y-6">
                      {/* 1. Janela de Leitura / Conteúdo Principal */}
                      <div 
                        id={`msg-${msg.id}`} 
                        className={`w-full flex ${
                          isWide 
                            ? "justify-start max-w-5xl md:max-w-6xl" 
                            : "justify-start max-w-3xl"
                        }`}
                      >
                        <div className="flex gap-4 w-full flex-row">
                          <div className="w-10 h-10 rounded-xl shrink-0 flex items-center justify-center bg-[var(--accent-primary)]">
                            <img src="./owl-white.png" alt="Mob.me" className="w-6 h-6 object-contain" />
                          </div>
                          <div className={`flex flex-col ${
                            isWide 
                              ? "flex-1 w-full max-w-full items-start min-w-0" 
                              : "max-w-[85%] md:max-w-[75%] items-start min-w-0"
                          }`}>
                            <div className={`
                              px-5 py-4 rounded-2xl overflow-hidden
                              ${isWide
                                ? "bg-[var(--bg-elevated)] border border-[var(--border-subtle)] text-[var(--text-primary)] rounded-tl-sm w-full"
                                : "bg-[var(--bg-elevated)] border border-[var(--border-subtle)] text-[var(--text-primary)] rounded-tl-sm"}
                            `}>
                              {msg.imageUrl && (
                                <img src={msg.imageUrl} alt="Anexo" className="max-w-full rounded-xl mb-3 max-h-60 object-contain" />
                              )}
                              <div className="markdown-content prose max-w-none text-[var(--text-primary)]">
                                <ReactMarkdown 
                                  remarkPlugins={[remarkGfm, remarkMath]} 
                                  rehypePlugins={[rehypeKatex]}
                                  components={markdownComponents}
                                >
                                  {sanitizeContent(mainText)}
                                </ReactMarkdown>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>

                      {/* 2. Janela Independente para o Super Menu após Conclusão de Seção */}
                      {menu && (
                        <div 
                          id={`msg-${msg.id}-menu`}
                          className="w-full flex justify-start max-w-3xl animate-[fadeIn_0.3s_ease-in-out]"
                        >
                          <div className="flex gap-4 w-full flex-row">
                            <div className="w-10 h-10 rounded-xl shrink-0 flex items-center justify-center bg-[var(--accent-primary)]">
                              <img src="./owl-white.png" alt="Mob.me" className="w-6 h-6 object-contain" />
                            </div>
                            <div className="flex flex-col max-w-[85%] md:max-w-[75%] items-start min-w-0">
                              <div className="px-5 py-4 rounded-2xl overflow-hidden bg-[var(--bg-elevated)] border border-[var(--border-subtle)] text-[var(--text-primary)] rounded-tl-sm">
                                <div className="markdown-content prose max-w-none text-[var(--text-primary)]">
                                  <ReactMarkdown 
                                    remarkPlugins={[remarkGfm, remarkMath]} 
                                    rehypePlugins={[rehypeKatex]}
                                    components={markdownComponents}
                                  >
                                    {sanitizeContent(menu)}
                                  </ReactMarkdown>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
                
                {isTyping && (
                  <div className="w-full max-w-3xl flex justify-start animate-[fadeIn_0.3s_ease-in-out]">
                    <div className="flex gap-4 flex-row items-center">
                      <div className={`w-10 h-10 rounded-xl shrink-0 bg-[var(--accent-primary)] flex items-center justify-center ${loadingTrack ? "shadow-md animate-pulse" : ""}`}>
                        <img src="./owl-white.png" alt="Mob.me" className="w-6 h-6 object-contain" />
                      </div>
                      {loadingTrack && LOADING_MESSAGES[loadingTrack] ? (
                        <div className="flex items-center gap-3.5 px-5 py-3.5 bg-[var(--bg-elevated)] border border-[var(--border-subtle)] rounded-2xl rounded-tl-sm shadow-sm max-w-[90%] md:max-w-[80%] min-h-[52px] transition-all duration-300">
                          <div className="flex gap-1.5 shrink-0">
                            <div className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-bounce" style={{ animationDelay: "0ms" }} />
                            <div className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-bounce" style={{ animationDelay: "150ms" }} />
                            <div className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-bounce" style={{ animationDelay: "300ms" }} />
                          </div>
                          <span 
                            key={loadingMessageIndex} 
                            className="text-sm font-medium text-[var(--text-secondary)] animate-[fadeIn_0.3s_ease-in-out]"
                          >
                            {LOADING_MESSAGES[loadingTrack][loadingMessageIndex % LOADING_MESSAGES[loadingTrack].length]}
                          </span>
                        </div>
                      ) : (
                        <div className="flex items-center px-4 bg-[var(--bg-elevated)] border border-[var(--border-subtle)] rounded-2xl rounded-tl-sm h-12">
                          <div className="flex gap-1.5">
                            <div className="w-2 h-2 rounded-full bg-[var(--text-muted)] animate-bounce" style={{ animationDelay: "0ms" }} />
                            <div className="w-2 h-2 rounded-full bg-[var(--text-muted)] animate-bounce" style={{ animationDelay: "150ms" }} />
                            <div className="w-2 h-2 rounded-full bg-[var(--text-muted)] animate-bounce" style={{ animationDelay: "300ms" }} />
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>
            )}
          </div>
        </main>



        {/* Input Area */}

        <footer className="fixed bottom-0 left-0 right-0 md:left-[280px] bg-[var(--bg-primary)] pt-3 pb-3 px-4 flex flex-col items-center shadow-[0_-10px_40px_rgba(0,0,0,0.1)] z-20 transition-transform duration-150 ease-out " style={{ transform: `translateY(-${keyboardHeight}px)` }}>

          <div className="w-full max-w-4xl flex flex-col relative">

            

            {imagePreview && (

              <div className="absolute bottom-full mb-3 left-4 p-2 bg-[var(--bg-elevated)] border border-[var(--border-medium)] rounded-xl shadow-lg w-24 h-24 group">

                <img src={imagePreview} alt="Preview" className="w-full h-full object-cover rounded-lg" />

                <button 

                  onClick={removeImage}

                  className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 rounded-full flex items-center justify-center text-white opacity-0 group-hover:opacity-100 transition-opacity"

                >

                  <X size={12} />

                </button>

              </div>

            )}



            <form 

              onSubmit={(e) => { e.preventDefault(); handleSend(); }}

              className="flex items-end gap-2 p-1.5 bg-[var(--bg-input)] border border-[var(--border-medium)] rounded-3xl shadow-sm focus-within:border-[var(--accent-primary)] transition-all"

            >

              <input 

                type="file" 

                accept="image/*" 

                className="hidden" 

                ref={fileInputRef}

                onChange={handleImageUpload}

              />

              <button 

                type="button" 

                onClick={() => fileInputRef.current?.click()}

                className="p-3 text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors shrink-0 mb-0.5"

              >

                <Paperclip size={20} />

              </button>

              

              <textarea

                ref={textareaRef}

                rows={1}

                value={input}

                onChange={e => setInput(e.target.value)}

                onKeyDown={handleKeyDown}

                onPaste={handlePaste}

                placeholder={isTyping ? "Mob.me pensando..." : "Digite sua dúvida ou envie uma foto..."}

                className="flex-1 max-h-40 bg-transparent text-[var(--text-primary)] placeholder:text-[var(--text-muted)] resize-none py-3.5 px-2 outline-none"

              />

              

              <button 

                type="submit"

                disabled={isTyping || (!input.trim() && !imageBase64)}

                className="p-3.5 rounded-full shrink-0 transition-colors bg-[var(--accent-primary)] text-white disabled:opacity-50 disabled:cursor-not-allowed m-0.5 shadow-md"

              >

                <Send size={18} />

              </button>

            </form>

            

            <p className="text-center text-xs text-[var(--text-muted)] mt-2">

              Eu sei muito e sigo estudando, mas não sou perfeita. Se você desconfiar da minha resposta, fale com seu professor(a) da Educamob.

            </p>

          </div>

        </footer>

      </div>

    </div>

  );

}

