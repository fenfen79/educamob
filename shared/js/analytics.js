window.EducamobAnalytics = {
  registrarAcesso: function(itemId) {
    let acessos = JSON.parse(localStorage.getItem('edm_acessos') || '[]');
    acessos.push({
      id: itemId,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('edm_acessos', JSON.stringify(acessos));
  },

  registrarQuiz: function(itemId, acertos, total) {
    let quizzes = JSON.parse(localStorage.getItem('edm_quizzes') || '[]');
    quizzes.push({
      id: itemId,
      acertos: acertos,
      total: total,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('edm_quizzes', JSON.stringify(quizzes));
  },

  getDesempenhoSemanal: function() {
    // Retorna mock simples para estrutura, filtrando os últimos 7 dias na implementação real
    const acessos = JSON.parse(localStorage.getItem('edm_acessos') || '[]');
    const quizzes = JSON.parse(localStorage.getItem('edm_quizzes') || '[]');
    
    let totalAcertos = 0;
    let totalQuestoes = 0;
    
    quizzes.forEach(q => {
      totalAcertos += q.acertos;
      totalQuestoes += q.total;
    });
    
    const mediaAcertos = totalQuestoes > 0 ? Math.round((totalAcertos / totalQuestoes) * 100) : 0;
    
    return {
      totalAcessos: acessos.length,
      totalQuizzes: quizzes.length,
      mediaAcertos: mediaAcertos,
      porDisciplina: [
        { disciplina: 'Matemática', acertos: totalAcertos, total: totalQuestoes }
      ]
    };
  },

  getAtividadeRecente: function(limit = 10) {
    const acessos = JSON.parse(localStorage.getItem('edm_acessos') || '[]');
    return acessos.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp)).slice(0, limit);
  }
};
