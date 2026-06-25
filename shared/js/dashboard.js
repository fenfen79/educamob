document.addEventListener('DOMContentLoaded', () => {
  const tbodyEstudos = document.getElementById('dashboard-estudos-tbody');
  const tbodyRevisoes = document.getElementById('dashboard-revisoes-tbody');
  const sectionEstudos = document.getElementById('section-estudos');
  const sectionRevisoes = document.getElementById('section-revisoes');
  const emptyState = document.getElementById('empty-state');
  
  const filterPeriod = document.getElementById('filter-period');
  const filterSubject = document.getElementById('filter-subject');
  const filterStatus = document.getElementById('filter-status');

  const quizzes = window.MOCK_QUIZZES || {};
  
  async function renderDashboard() {
    let hasEstudos = false;
    let hasRevisoes = false;
    
    let htmlEstudos = '';
    let htmlRevisoes = '';
    
    const now = Date.now();
    const periodValue = filterPeriod ? filterPeriod.value : 'all';
    const subjectValue = filterSubject ? filterSubject.value : 'all';
    const statusValue = filterStatus ? filterStatus.value : 'all';

    // Template premium para as "bolas" (Efeito Esfera 3D Glossy)
    const createBallIcon = (lightColor, darkColor, shadowColor) => `
      <div style="width:34px; height:34px; border-radius:50%; background: radial-gradient(circle at 10px 10px, ${lightColor}, ${darkColor}); box-shadow: 0 4px 10px ${shadowColor}, inset -3px -3px 6px rgba(0,0,0,0.25); flex-shrink:0;"></div>
    `;
    
    // Template premium para o andamento (Esfera Azul Elétrico com Relógio)
    const createClockIcon = () => `
      <div style="display:flex; align-items:center; justify-content:center; width:34px; height:34px; border-radius:50%; background: radial-gradient(circle at 10px 10px, #42a5f5, #0d47a1); box-shadow: 0 4px 10px rgba(13,71,161,0.5), inset -3px -3px 6px rgba(0,0,0,0.4); flex-shrink:0;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 3px rgba(255,255,255,0.6));">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
      </div>
    `;

    let allActivities = [];

    // --- BUSCA NA NUVEM (SUPABASE) ---
    if (window.supabaseClient) {
      const { data: { session } } = await window.supabaseClient.auth.getSession();
      if (session) {
        const { data: activities, error } = await window.supabaseClient
          .from('student_progress')
          .select('*')
          .order('created_at', { ascending: false });

        if (!error && activities && activities.length > 0) {
          activities.forEach(state => {
            allActivities.push({
              source: 'cloud',
              subject_id: state.subject_id,
              subject_name: state.subject_name,
              score: Number(state.score),
              total_questions: state.total_questions,
              activity_type: state.activity_type,
              created_at: state.created_at,
              timestamp: new Date(state.created_at).getTime(),
              currentQuestionIndex: state.total_questions, // na nuvem é sempre finalizado
              finished: true
            });
          });
        }
      }
    }

    // --- BUSCA LOCAL (ITENS EM ANDAMENTO E RASCUNHOS) ---
    Object.keys(quizzes).forEach(subjectId => {
      const revisaStateRaw = localStorage.getItem(`educamob_quiz_${subjectId}`);
      const spaStateRaw = localStorage.getItem(`educamob_spa_${subjectId}`);
      
      const localActivities = [];
      if (revisaStateRaw) localActivities.push(JSON.parse(revisaStateRaw));
      if (spaStateRaw) localActivities.push(JSON.parse(spaStateRaw));

      localActivities.forEach(state => {
        if (state.finished) return; // Se está finalizado local, logo estará na nuvem, ignora aqui pra não duplicar.
        
        allActivities.push({
          source: 'local',
          subject_id: subjectId,
          subject_name: quizzes[subjectId] ? quizzes[subjectId].title : 'Atividade',
          score: state.currentQuestionIndex > 0 ? (state.correctCount / state.currentQuestionIndex) * 100 : 0,
          total_questions: state.totalQuestions,
          activity_type: state.type ? state.type.toLowerCase() : 'quiz', // assume quiz se nulo
          created_at: state.timestamp ? new Date(state.timestamp).toISOString() : new Date().toISOString(),
          timestamp: state.timestamp || Date.now(),
          currentQuestionIndex: state.currentQuestionIndex,
          finished: false
        });
      });
    });

    // Ordenar todas as atividades do mais recente para o mais antigo
    allActivities.sort((a, b) => b.timestamp - a.timestamp);

    const seenSubjects = new Set(); // Guarda as matérias já processadas (para mostrar só a mais recente)

    allActivities.forEach(state => {
        // Ignora se já vimos a versão mais recente dessa matéria
        if (seenSubjects.has(state.subject_id)) return;
        seenSubjects.add(state.subject_id);

        const subject = quizzes[state.subject_id] || { 
          title: state.subject_name, 
          disciplina: 'Geral', 
          icon: '' 
        };
        
        // Aplicação de Filtros Matéria/Período
        if (subjectValue !== 'all' && subject.disciplina !== subjectValue && subject.title !== subjectValue) return;

        if (periodValue !== 'all' && state.timestamp) {
            const dateObj = new Date(state.timestamp);
            const diffDays = (now - dateObj.getTime()) / (1000 * 60 * 60 * 24);
            if (periodValue === 'today' && diffDays > 1) return;
            if (periodValue === '7days' && diffDays > 7) return;
            if (periodValue === '30days' && diffDays > 30) return;
        }

        let scoreHtml = '';
        let questionsHtml = `${state.currentQuestionIndex}/${state.total_questions}`;
        
        let statusCode = 'pending';
        let statusIcon = '';

        if (state.finished) {
          const score = state.score;
          scoreHtml = `<span class="score-text">${Math.round(score)}%</span>`;
          questionsHtml = `${state.total_questions}/${state.total_questions}`;

          if (score >= 75) {
            statusCode = 'green';
            statusIcon = createBallIcon('#81c784', '#2e7d32', 'rgba(46,125,50,0.4)');
          } else if (score >= 50) {
            statusCode = 'yellow';
            statusIcon = createBallIcon('#ffd54f', '#f57f17', 'rgba(245,127,23,0.4)');
          } else {
            statusCode = 'red';
            statusIcon = createBallIcon('#e57373', '#c62828', 'rgba(198,40,40,0.4)');
          }
        } else {
          statusCode = 'pending';
          statusIcon = createClockIcon();
          scoreHtml = `<span class="score-text" style="color: var(--text-muted)">
            ${Math.round(state.score)}% 
            <span style="font-size:0.65rem; font-weight:700; text-transform:uppercase; background-color: var(--text); color: var(--bg); padding: 4px 6px; border-radius: 4px; margin-left: 4px; display: inline-flex; align-items: center; justify-content: center; letter-spacing: 0.5px; line-height: 1;">Parcial</span>
          </span>`;
        }
        
        // Aplicação do Filtro de Status
        if (statusValue !== 'all' && statusValue !== statusCode) return;

        const isSPA = state.activity_type === 'spa';
        
        const dateObjLocal = new Date(state.timestamp);
        const dateStr = dateObjLocal.toLocaleDateString('pt-BR') + ' às ' + dateObjLocal.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
        
        const dateBadgeStyle = "font-size:0.7rem; font-weight:600; letter-spacing: 0.8px; background-color: var(--text); color: var(--bg); padding: 4px 8px; border-radius: 4px; display: inline-flex; align-items: center; justify-content: center; margin-top: 4px; line-height: 1;";
        const statusBadgeStyle = "font-size:0.65rem; font-weight:700; text-transform:uppercase; background-color: var(--text); color: var(--bg); padding: 4px 6px; border-radius: 4px; display: inline-flex; align-items: center; justify-content: center; margin-top: 4px; letter-spacing: 0.5px; line-height: 1;";
        
        const dataFormatada = `<span style="${dateBadgeStyle}">${dateStr}</span>`;
        const emAndamentoBadge = `<span style="${statusBadgeStyle}">Em andamento</span>`;
        
        const rowHtml = `
          <tr>
            <td data-label="Atividade">
              <div class="subject-info">
                <span class="subject-icon">${statusIcon}</span>
                <div>
                  <div class="subject-name">${subject.title}</div>
                  <div>${state.finished ? dataFormatada : emAndamentoBadge}</div>
                </div>
              </div>
            </td>
            <td data-label="Aproveitamento" style="text-align: center;">${scoreHtml}</td>
            <td data-label="Exercícios realizados" style="color: var(--text-muted); font-weight: 600; text-align: center;">${questionsHtml}</td>
          </tr>
        `;

        if (isSPA) {
          htmlEstudos += rowHtml;
          hasEstudos = true;
        } else {
          htmlRevisoes += rowHtml;
          hasRevisoes = true;
        }
    });

    if (hasEstudos) {
      tbodyEstudos.innerHTML = htmlEstudos;
      if(sectionEstudos) sectionEstudos.style.display = 'block';
    } else {
      if(sectionEstudos) sectionEstudos.style.display = 'none';
    }

    if (hasRevisoes) {
      tbodyRevisoes.innerHTML = htmlRevisoes;
      if(sectionRevisoes) sectionRevisoes.style.display = 'block';
    } else {
      if(sectionRevisoes) sectionRevisoes.style.display = 'none';
    }

    if (!hasEstudos && !hasRevisoes) {
      if(emptyState) emptyState.style.display = 'block';
    } else {
      if(emptyState) emptyState.style.display = 'none';
    }
  }

  if (filterPeriod) filterPeriod.addEventListener('change', renderDashboard);
  if (filterSubject) filterSubject.addEventListener('change', renderDashboard);
  if (filterStatus) filterStatus.addEventListener('change', renderDashboard);

  renderDashboard();
});
