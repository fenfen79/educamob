class EducamobFooter extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    const year = new Date().getFullYear();
    
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          margin-top: auto;
          width: 100%;
        }
        
        footer {
          padding: 2rem 4%;
          text-align: center;
          border-top: 1px solid rgba(255,255,255,0.08);
          font-family: 'Inter', sans-serif;
        }
        
        p {
          color: #a3a3a3;
          font-size: 0.85rem;
          font-weight: 600;
          letter-spacing: 0.5px;
          margin: 0;
        }
        
        span {
          color: #FF6A00;
        }
      </style>
      
      <footer>
        <p>© ${year} educa<span>mob</span> — Escola é onde você aprende.</p>
      </footer>
    `;
  }
}

customElements.define('educamob-footer', EducamobFooter);
