class EducamobHeader extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    const backUrl = this.getAttribute('back-url') || '#PORTAL_WIX';
    
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          position: sticky;
          top: 0;
          z-index: 1000;
        }
        
        header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 1rem 4%;
          background-color: transparent;
          transition: background-color 0.3s ease;
        }
        
        header.scrolled {
          background-color: var(--bg-card, #0a0a0a);
          border-bottom: 1px solid var(--border, rgba(255,255,255,0.08));
        }
        
        .logo {
          font-family: 'Inter', sans-serif;
          font-size: 1.5rem;
          font-weight: 800;
          color: var(--text, #ffffff);
          text-decoration: none;
          letter-spacing: -1px;
        }
        
        .logo span {
          color: #FF6A00;
        }
        
        .logo img {
          height: 40px;
          transform: scale(3.5);
          transform-origin: center;
          display: block;
          transition: transform 0.3s ease;
        }
        
        .logo:hover img {
          transform: scale(3.6);
        }
        
        .back-link {
          font-family: 'Inter', sans-serif;
          font-size: 0.9rem;
          color: var(--text-muted, #a3a3a3);
          text-decoration: none;
          display: flex;
          align-items: center;
          gap: 6px;
          transition: color 0.3s;
          font-weight: 600;
          flex: 1;
        }
        
        .back-link:hover {
          color: var(--text, #ffffff);
        }

        /* Theme Switch */
        .theme-switch-wrapper {
          display: flex;
          align-items: center;
          flex: 1;
          justify-content: flex-end;
        }
        .theme-switch {
          position: relative;
          display: inline-block;
          width: 52px;
          height: 28px;
        }
        .theme-switch input { opacity: 0; width: 0; height: 0; }
        .slider {
          position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
          background-color: #ffffff; border: 2px solid #1a1a1a; transition: .3s;
          border-radius: 30px; display: flex; align-items: center; justify-content: space-between;
          padding: 0 4px; overflow: hidden;
        }
        .slider:before {
          position: absolute; content: ""; height: 20px; width: 20px; left: 2px; bottom: 2px;
          background-color: #1a1a1a; transition: .3s; border-radius: 50%; z-index: 2;
        }
        input:checked + .slider { background-color: #1a1a1a; border: 2px solid #ffffff; }
        input:checked + .slider:before { transform: translateX(24px); background-color: #ffffff; }
        .slider-icon { font-size: 14px; z-index: 1; pointer-events: none; transition: opacity 0.3s; }
        .icon-sun { filter: brightness(0) invert(1); }
        .icon-moon { filter: brightness(0); }
        input:not(:checked) + .slider .icon-sun { opacity: 0; }
        input:checked + .slider .icon-moon { opacity: 0; }
      </style>
      
      <header id="main-header">
        <a href="${backUrl}" class="back-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
          Voltar ao Hub
        </a>
        <a href="${backUrl}" class="logo" style="display: flex; align-items: center; flex: 1; justify-content: center;">
          <img src="../../shared/assets/BASE-V1-cropped.png" alt="BASE">
        </a>
        
        <div class="theme-switch-wrapper" title="Alternar tema">
          <label class="theme-switch">
            <input type="checkbox" id="theme-toggle">
            <span class="slider">
              <span class="slider-icon icon-sun">☀️</span>
              <span class="slider-icon icon-moon">🌙</span>
            </span>
          </label>
        </div>
      </header>
    `;

    // Lógica do Theme Switch
    // Como a biblioteca antes era só escura, mantemos escuro como fallback se não houver preferência
    const themeToggle = this.shadowRoot.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('educamob_theme') || 'dark'; 
    
    // Injeta estilo no documento para evitar Flash
    if (currentTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      themeToggle.checked = true;
    } else {
      document.documentElement.removeAttribute('data-theme');
      themeToggle.checked = false;
    }

    themeToggle.addEventListener('change', (e) => {
      if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('educamob_theme', 'dark');
      } else {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('educamob_theme', 'light');
      }
    });

    window.addEventListener('scroll', () => {
      const header = this.shadowRoot.getElementById('main-header');
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
}

customElements.define('educamob-header', EducamobHeader);
