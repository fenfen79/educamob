"use client";



import { useState, useEffect, useRef } from "react";

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
  // 1. Auto-heal KaTeX double subscript error (ex: SO_4^{2-}_{(aq)})
  let sanitized = content.replace(
    /([A-Za-z0-9]+_[0-9]+(?:\^\{?[^}]+\}?)?)_(\{?\([a-z0-9]+\)\}?)/g,
    (match, p1, p2) => "{" + p1 + "}_" + p2
  );

  // 2. Auto-promover equações com setas para $$ APENAS fora de linhas de tabela Markdown
  const arrowRegex = new RegExp('(?<!\\$)\\$([^\\$\\r\\n]+?(?:\\\\to|\\\\rightarrow|\\\\xrightarrow|\\\\rightleftharpoons|\\\\leftrightarrow)[^\\$\\r\\n]*?)\\$(?!\\$)', 'g');
  const lines = sanitized.split("\n");
  const processedLines = lines.map(line => {
    const trimmed = line.trim();
    // Se for linha de tabela Markdown (começa com | e tem | subsequente), preserva inline para não quebrar a tabela
    if (trimmed.startsWith("|") && trimmed.includes("|", 1)) {
      return line;
    }
    // Fora de tabela, promove equações com setas para blocos destacados centralizados
    if (arrowRegex.test(line)) {
      arrowRegex.lastIndex = 0;
      return line.replace(arrowRegex, "\n\n$$\n$1\n$$\n\n");
    }
    return line;
  });

  return processedLines.join("\n");
};

const splitMessageMenu = (text: string): { content: string; menu: string | null } => {
  if (!text) return { content: "", menu: null };

  const hasMenu = text.includes("1️⃣") && (text.includes("8️⃣") || text.includes("Bora ler!"));
  if (!hasMenu) {
    return { content: text, menu: null };
  }

  const menuIndex1 = text.indexOf("1️⃣");
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
      "como você prefere começar"
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
  
  // Detecção de Bora ler! (Teoria densa)
  const isTeoria = 
    lower.includes("conexão com o mundo real") ||
    lower.includes("conexao com o mundo real") ||
    lower.includes("conceito central e fundamentos") ||
    lower.includes("atenção aos erros comuns") ||
    lower.includes("atencao aos erros comuns");
    
  // Detecção de Memorex (Resumo panorâmico)
  const isMemorex =
    lower.includes("visão panorâmica") ||
    lower.includes("visao panoramica") ||
    lower.includes("mapa conceitual completo") ||
    lower.includes("dicas de ouro");
    
  return isTeoria || isMemorex;
};



const LOADING_MESSAGES: Record<string, string[]> = {
  teoria: [
    "Abrindo os manuscritos da biblioteca da Educamob... 📚",
    "Garimpando exemplos reais no mundo prático... 🌍",
    "Desenhando tabelas comparativas sem decoreba... 🧠",
    "Mapeando as pegadinhas clássicas de provas... ⚠️",
    "Dando o polimento final... já vai começar! ✨"
  ],
  flashcards: [
    "Embaralhando o baralho da memória ativa... 🃏",
    "Separando os conceitos mais traiçoeiros do assunto... 🎯",
    "Aquecendo seus neurônios para o teste rápido... 🧠⚡",
    "Quase pronto para o desafio mental! 🚀"
  ],
  memorex: [
    "Passando o conteúdo no liquidificador sintético... 🌪️",
    "Filtrando apenas o ouro puro do assunto... 🍯",
    "Montando sua folha de consulta rápida autorizada! 📋",
    "Finalizando o panorama completo... ⚡"
  ],
  treino: [
    "Garimpando as melhores questões no nosso banco... 📝",
    "Calibrando a régua de dificuldade... sem pegadinhas! 🎯",
    "Conferindo os passos e dicas pedagógicas... 💡",
    "Exercícios prontos na bancada! 🧗"
  ],
  desafio: [
    "Subindo o nível! Selecionando questões cascudas... 🧗‍♂️",
    "Ajustando os desafios em duas etapas lógicas... ⚙️",
    "Preparando a arena de raciocínio profundo... 🥊",
    "O desafio já vai começar! Força mental! 🚀"
  ],
  conversa: [
    "Organizando a roda de conversa socrática... 🗣️",
    "Pensando na primeira pergunta instigante... 🤔",
    "Afiando as ideias para trocarmos uma ideia boa... 💡"
  ],
  sos: [
    "Ativando o radar de resgate pedagógico! 🆘",
    "Localizando a rota mais simples para clarear sua dúvida... 🧭",
    "Descomplicando os pontos obscuros... 💡"
  ],
  geral: [
    "Consultando o acervo oficial da Educamob... 🦉",
    "Aquecendo os neurônios e conectando ideias... 🧪",
    "Estruturando a melhor explicação para você... 💡",
    "Ajustando a rota pedagógica... quase pronto! 🚀"
  ]
};

const getTrackFromInput = (input: string): string => {
  if (!input) return "geral";
  const text = input.trim().toLowerCase();
  
  if (text === "1" || text.includes("bora ler") || text.includes("teoria")) {
    return "teoria";
  }
  if (text === "2" || text.includes("trocando ideias") || text.includes("conversar") || text.includes("conversando")) {
    return "conversa";
  }
  if (text === "3" || text.includes("flashcard")) {
    return "flashcards";
  }
  if (text === "4" || text.includes("memorex") || text.includes("resumo")) {
    return "memorex";
  }
  if (text === "5" || text.includes("treino") || text.includes("fáceis") || text.includes("faceis") || text.includes("básico") || text.includes("basico")) {
    return "treino";
  }
  if (text === "6" || text.includes("desafio") || text.includes("difíceis") || text.includes("dificeis")) {
    return "desafio";
  }
  if (text === "7" || text.includes("sos") || text.includes("me ajuda") || text.includes("ajuda")) {
    return "sos";
  }
  return "geral";
};

export default function ChatApp() {

  const [theme, setTheme] = useState<"light" | "dark">("dark");

  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const [messages, setMessages] = useState<Message[]>([]);

  const [input, setInput] = useState("");

  const [isTyping, setIsTyping] = useState(false);
  const [loadingTrack, setLoadingTrack] = useState<string>("geral");
  const [loadingMessageIndex, setLoadingMessageIndex] = useState<number>(0);

  useEffect(() => {
    if (!isTyping) {
      setLoadingMessageIndex(0);
      return;
    }
    const list = LOADING_MESSAGES[loadingTrack] || LOADING_MESSAGES.geral;
    const interval = setInterval(() => {
      setLoadingMessageIndex(prev => (prev + 1) % list.length);
    }, 2400);
    return () => clearInterval(interval);
  }, [isTyping, loadingTrack]);

  const [imagePreview, setImagePreview] = useState<string | null>(null);

  const [imageBase64, setImageBase64] = useState<string | null>(null);

  

  const [sessions, setSessions] = useState<Session[]>([]);

  const [currentSessionId, setCurrentSessionId] = useState<string | null>(null);

  const [editingSessionId, setEditingSessionId] = useState<string | null>(null);

  const [editTitle, setEditTitle] = useState("");



  const messagesEndRef = useRef<HTMLDivElement>(null);

  const skipBottomScrollRef = useRef<string | null>(null);

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

    if (skipBottomScrollRef.current) {

      const targetId = skipBottomScrollRef.current;

      skipBottomScrollRef.current = null;

      setTimeout(() => {

        const el = document.getElementById(`msg-${targetId}`);

        if (el) {

          el.scrollIntoView({ behavior: "smooth", block: "start" });

        }

      }, 120);

      return;

    }

    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });

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

    setIsTyping(true);
    setLoadingTrack(getTrackFromInput(textToSend));
    setLoadingMessageIndex(0);



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



      while (reader) {

        const { done, value } = await reader.read();

        if (done) break;

        

        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split("\n\n");

        buffer = lines.pop() || "";

        

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

                if (isFirstChunk) {

                  isFirstChunk = false;

                  setIsTyping(false); // Esconde a coruja com "..."

                  aiResponseText += data.chunk;

                  setMessages(prev => [...prev, { id: aiMsgId, role: "ai", text: aiResponseText }]);

                } else {

                  aiResponseText += data.chunk;

                  setMessages(prev => 

                    prev.map(msg => msg.id === aiMsgId ? { ...msg, text: aiResponseText } : msg)

                  );

                }

              }

            } catch (e) {

              console.error("Parse SSE error", e);

            }

          }

        }

      }

    if (aiResponseText.length > 350 && (aiResponseText.includes("###") || aiResponseText.includes("Bora ler") || aiResponseText.includes("Teoria"))) {

        skipBottomScrollRef.current = aiMsgId;

      }

    } catch (e: any) {

      const errorMsg = e.message.includes("logado") ? `⚠️ Ops! ${e.message}` : `⚠️ DEBUG ERROR: ${e.message}`;

      setMessages(prev => [...prev, { id: Date.now().toString(), role: "ai", text: errorMsg }]);

    } finally {

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
                      <div className="w-10 h-10 rounded-xl shrink-0 bg-[var(--accent-primary)] flex items-center justify-center shadow-md animate-pulse">
                        <img src="./owl-white.png" alt="Mob.me" className="w-6 h-6 object-contain" />
                      </div>
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
                          {(LOADING_MESSAGES[loadingTrack] || LOADING_MESSAGES.geral)[loadingMessageIndex % (LOADING_MESSAGES[loadingTrack] || LOADING_MESSAGES.geral).length]}
                        </span>
                      </div>
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

