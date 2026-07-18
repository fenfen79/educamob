// Banco de Dados Simulado de Quizzes
window.MOCK_QUIZZES = {
  "matematica_8_monomios": {
    title: "Monômios e Polinômios",
    icon: "",
    thumbnail: "content/fundamental-2/8-ano/matematica/cap-10-monomios-polinomios/hero_colorido.png",
    nivel: "Fundamental 2",
    serie: "8º Ano",
    disciplina: "Matemática",
    tags: ["álgebra", "monômios", "polinômios", "expressões"],
    questions: [
      // --- NÍVEL MODERADO ---
      {
        id: 1,
        text: "O que caracteriza dois monômios como sendo 'semelhantes'?",
        options: ["Possuírem o mesmo coeficiente numérico.", "Possuírem a mesma parte literal (letras e expoentes iguais).", "Possuírem o mesmo grau absoluto.", "Ambos serem positivos."],
        correctIndex: 1,
        resolution: "Para que dois monômios sejam semelhantes, a sua parte literal deve ser estritamente igual. Isso permite que eles sejam somados ou subtraídos diretamente."
      },
      {
        id: 2,
        text: "Qual é o grau absoluto do monômio 4x²y³?",
        options: ["Grau 2", "Grau 3", "Grau 4", "Grau 5"],
        correctIndex: 3,
        resolution: "O grau absoluto de um monômio com mais de uma variável é dado pela soma dos expoentes das suas variáveis. Somando 2 + 3, temos Grau 5."
      },
      {
        id: 3,
        text: "Qual é o resultado simplificado da soma: 7xy - 2xy + 4xy?",
        options: ["9xy", "9x³y³", "13xy", "5xy"],
        correctIndex: 0,
        resolution: "Como todos os monômios são semelhantes, nós apenas operamos os coeficientes: 7 - 2 + 4 = 9. Mantendo a parte literal, o resultado é 9xy."
      },
      {
        id: 4,
        text: "O que obtemos ao realizar o produto: (3a²b) * (-2ab³)?",
        options: ["-6a²b³", "6a³b⁴", "-6a³b⁴", "-6ab²"],
        correctIndex: 2,
        resolution: "Multiplicam-se os coeficientes numéricos (3 * -2 = -6) e, para as letras, soma-se os expoentes: a² * a¹ = a³, e b¹ * b³ = b⁴. Logo, -6a³b⁴."
      },
      {
        id: 5,
        text: "Qual o resultado da divisão: (15x⁵y³) ÷ (3x²y)?",
        options: ["5x³y²", "12x³y²", "5x⁷y⁴", "5xy"],
        correctIndex: 0,
        resolution: "Dividem-se os coeficientes numéricos (15 ÷ 3 = 5). Nas variáveis, subtraem-se os expoentes das bases iguais: x^(5-2) = x³ e y^(3-1) = y². Resultado: 5x³y²."
      },
      // --- NÍVEL DIFÍCIL ---
      {
        id: 6,
        text: "Efetue a operação com polinômios: (2x² - 3x + 1) - (x² + 4x - 5)",
        options: ["x² + x - 4", "x² - 7x + 6", "3x² + x - 4", "x² - 7x - 4"],
        correctIndex: 1,
        resolution: "O sinal de menos inverte os sinais do segundo polinômio: -x² - 4x + 5. Agrupando: (2x² - x²) + (-3x - 4x) + (1 + 5) = x² - 7x + 6."
      },
      {
        id: 7,
        text: "Aplicando os produtos notáveis, qual o desenvolvimento de (x + 3)²?",
        options: ["x² + 9", "x² + 3x + 9", "x² + 6x + 9", "2x + 6"],
        correctIndex: 2,
        resolution: "O quadrado da soma é igual ao quadrado do primeiro, mais duas vezes o primeiro pelo segundo, mais o quadrado do segundo: x² + 2*x*3 + 3² = x² + 6x + 9."
      },
      {
        id: 8,
        text: "O polinômio P(x) = (a - 2)x³ + x² + 1 tem o grau exato 2. Qual deve ser o valor de 'a'?",
        options: ["a = 1", "a = 2", "a = -2", "a = 0"],
        correctIndex: 1,
        resolution: "Para que o grau seja exatamente 2, o termo em x³ deve desaparecer (seu coeficiente deve ser zero). Portanto, a - 2 = 0, o que nos dá a = 2."
      },
      {
        id: 9,
        text: "Calcule a divisão do polinômio (6x⁴ - 9x³ + 3x²) pelo monômio (3x²):",
        options: ["2x² - 3x + 1", "2x² - 3x", "3x² - 6x + 1", "2x² + 3x - 1"],
        correctIndex: 0,
        resolution: "Dividimos cada termo do polinômio pelo monômio isoladamente: (6x⁴/3x²) = 2x²; (-9x³/3x²) = -3x; (3x²/3x²) = 1. Resultado: 2x² - 3x + 1."
      },
      {
        id: 10,
        text: "Simplifique a expressão equivalente à área de um retângulo com lados (x + y) e (x - y):",
        options: ["x² + y²", "x² - y²", "x² - 2xy + y²", "2x - 2y"],
        correctIndex: 1,
        resolution: "Esse é o produto notável da 'soma pela diferença'. Ao realizar a distributiva, os termos centrais se anulam (xy - xy = 0), restando a diferença de quadrados: x² - y²."
      }
    ]
  }
};


class QuizEngine {
  constructor(subjectId) {
    this.subjectId = subjectId;
    this.quizData = window.MOCK_QUIZZES[subjectId];
    this.storageKey = `educamob_quiz_${subjectId}`;
    
    this.state = {
      currentQuestionIndex: 0,
      correctCount: 0,
      answers: [], 
      finished: false,
      totalQuestions: this.quizData ? this.quizData.questions.length : 0
    };
  }

  loadState() {
    const saved = localStorage.getItem(this.storageKey);
    if (saved) {
      this.state = JSON.parse(saved);
    }
  }

  saveState() {
    this.state.timestamp = Date.now();
    // Infere o tipo baseado na URL (se tiver 'revisa', é revisa, senão é spa)
    this.state.type = window.location.pathname.includes('revisa') ? 'revisa' : 'spa';
    localStorage.setItem(this.storageKey, JSON.stringify(this.state));

    // Lógica Cloud: Salva no Supabase se o quiz terminou!
    if (this.state.finished) {
      this.saveToSupabase();
    }
  }

  async saveToSupabase() {
    if (!window.supabaseClient) {
      console.warn("Supabase Client não inicializado.");
      return;
    }
    
    try {
      const { data: { session } } = await window.supabaseClient.auth.getSession();
      if (!session) {
        console.warn("Usuário deslogado. Falha ao salvar nota na nuvem.");
        return;
      }
      
      const score = this.state.totalQuestions > 0 ? (this.state.correctCount / this.state.totalQuestions) * 100 : 0;
      
      const { error } = await window.supabaseClient.from('student_progress').insert([
        {
          user_id: session.user.id,
          subject_id: this.subjectId,
          subject_name: this.quizData.title || this.subjectId,
          score: score,
          total_questions: this.state.totalQuestions,
          activity_type: this.state.type,
          objeto: this.quizData.objeto || this.subjectId
        }
      ]);

      if (error) {
        console.error("Erro ao salvar nota no Supabase:", error);
      } else {
        console.log("🚀 Nota gravada com sucesso na Nuvem Educamob!");
        // Opcional: apaga do localStorage após salvar com sucesso na nuvem
        localStorage.removeItem(this.storageKey);
      }
    } catch (err) {
      console.error("Erro na requisição ao Supabase:", err);
    }
  }

  reset() {
    this.state = {
      currentQuestionIndex: 0,
      correctCount: 0,
      answers: [],
      finished: false,
      totalQuestions: this.quizData.questions.length
    };
    this.saveState();
  }

  getCurrentQuestion() {
    return this.quizData.questions[this.state.currentQuestionIndex];
  }

  answerQuestion(selectedIndex) {
    if (this.state.finished) return null;

    const question = this.getCurrentQuestion();
    const isCorrect = selectedIndex === question.correctIndex;
    
    if (isCorrect) {
      this.state.correctCount++;
    }

    this.state.answers.push({
      questionId: question.id,
      selectedOptionIndex: selectedIndex,
      isCorrect: isCorrect
    });

    this.saveState();
    return { isCorrect, resolution: question.resolution, correctIndex: question.correctIndex };
  }

  nextQuestion() {
    if (this.state.currentQuestionIndex < this.state.totalQuestions - 1) {
      this.state.currentQuestionIndex++;
      this.saveState();
      return true;
    } else {
      this.state.finished = true;
      this.saveState();
      return false;
    }
  }

  getProgress() {
    return {
      current: this.state.currentQuestionIndex + 1,
      total: this.state.totalQuestions,
      percent: Math.round(((this.state.currentQuestionIndex) / this.state.totalQuestions) * 100)
    };
  }
}

window.QuizEngine = QuizEngine;
