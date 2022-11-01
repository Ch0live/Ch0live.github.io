class BlogPost extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
    <script src="https://cdn.jsdelivr.net/npm/showdown/dist/showdown.min.js"></script>
    <div id="mycontent"></div>
    <script>

      var converter = new showdown.Converter();
      var md = '[**Showdown**](http://www.showdownjs.com) Example code\n';
      var html = converter.makeHtml(md);
      document.querySelector('#mycontent').innerHTML = html;

    </script>
    `;
  }
}

customElements.define('blog-post-component', BlogPost);