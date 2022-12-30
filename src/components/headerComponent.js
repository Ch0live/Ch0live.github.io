class HeaderComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <nav>
          <ul id="nav">
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="../index.html">Splash Page</a>
            </li>
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="./blog.html">Home</a>
            </li>
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="./exampleBlogPost.html"><em>An Introduction to Markdown</em></a>
            </li>
          </ul>
        </nav>
      `;
    }
}

customElements.define("header-component", HeaderComponent);
