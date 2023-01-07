class HeaderComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <nav>
          <ul id="nav">
            <li>
              <a href="../index.html">Splash Page</a>
            </li>
            <li>
              <a href="./blog.html">Home</a>
            </li>
            <li>
              <a href="./blogPost.html"><em>An Introduction to Markdown</em></a>
            </li>
          </ul>
        </nav>
      `;
    }
}

customElements.define("header-component", HeaderComponent);
