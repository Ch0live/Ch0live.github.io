class HeaderComponent extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `<header>
        <nav>
          <ul id="nav">
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="../index.html">Splash Page</a>
            </li>
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="./blog.html">Blog</a>
            </li>
            <li>
              <a class="text-grey-500 hover:text-black font-medium " href="./exampleBlogPost.html"><em>An Introduction to Markdown</em></a>
            </li>
          </ul>
        </nav>
      </header>`;
    }
}

customElements.define("header-component", HeaderComponent);
