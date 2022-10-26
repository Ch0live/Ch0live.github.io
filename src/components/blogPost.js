class BlogPost extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <div>
        <div class="font-medium text-3xl mb-2 text-gray-100">
          Sample injected blog post header
        </div>
        <body class="font-medium text-m mb-2 text-black break-after-auto text-center">
          Sample injected blog post body
        </body>
      </div>
    `;
  }
}

customElements.define('blog-post-component', BlogPost);