from io import TextIOWrapper
import os
import re
from jinja2 import FileSystemLoader, Environment, Template

env = Environment(loader=FileSystemLoader("./templates"))


def write_to_file(path: str, html_file: str):
    with open(path + ".html", 'w') as file:
        file.write(html_file)


def get_template(name: str) -> Template:
    return env.get_template(f"{name}.j2")


def interpret_content(line: str) -> str:
    if line[0:2] == "# ":
        return get_template("block").render(type="h1", content=line[2:])
    if line[0:3] == "## ":
        return get_template("block").render(type="h2", content=line[3:])
    if line[0:4] == "### ":
        return get_template("block").render(type="h3", content=line[4:])
    if re.search("\!\[\[.*", line):
        return get_template("img").render(filename=line[3:-2])
    else:
        return get_template("block").render(type="p", content=line)


def interpret_md(md_file: TextIOWrapper) -> str:
    html_file_body = []
    for line in md_file.readlines():
        if re.search("^\s*$", line):
            continue
        html_file_body.append(interpret_content(line.strip()))
    return html_file_body


def generate_html_from_md(name: str, category: str):
    path = os.path.join(os.getcwd(), "blog-posts", category, name)
    md_file = open(path + ".md", "r")
    html_file_body = interpret_md(md_file)
    html_file = get_template("wrapper").render(body=html_file_body)
    write_to_file(path, html_file)
    print(f"written to path {path}")


if __name__ == "__main__":
    generate_html_from_md("charging-and-walking", "travel")
