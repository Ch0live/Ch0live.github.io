import os
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader("./templates"))


def write_to_file(name: str, body: str):
    f = open(f"{name}.html", "a")
    f.write(body)
    f.close()


def get_template(name: str):
    return env.get_template(f"{name}.j2")


def interpret_md(line: str):
    if line[0:2] == "# ":
        return get_template("h1").render(line[2:])
    else:
        return "<p> placeholder </p>"


def generate_html_from_md(name: str, category: str):
    path = os.path.join(os.getcwd(), "blog-posts", category, f"{name}.md")
    md_file = open(path, "r")
   
    html_file_body = []
    for line in md_file.readlines():
        html_file_body.append(interpret_md(line))

    html_file = get_template("wrapper").render(body=html_file_body)
    write_to_file(name, html_file)


if __name__ == "__main__":
    generate_html_from_md("charging-and-walking", "travel")
