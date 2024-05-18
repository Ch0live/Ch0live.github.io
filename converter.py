import os
import re
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
        return get_template("block").render(type="h1", content=line[2:])
    if line[0:3] == "## ":
        return get_template("block").render(type="h2", content=line[3:])
    if line[0:4] == "### ":
        return get_template("block").render(type="h3", content=line[4:])
    if re.search("\!\[\[.*", line):
        return get_template("img").render(filename=line[3:-3])
    else:
        return get_template("block").render(type="p", content=line)


def generate_html_from_md(name: str, category: str):
    path = os.path.join(os.getcwd(), "blog-posts", category, name)
    md_file = open(path + ".md", "r")
   
    html_file_body = []
    for line in md_file.readlines():
        html_file_body.append(interpret_md(line))

    html_file = get_template("wrapper").render(body=html_file_body)
    with open(path + ".html", 'w') as file:
        file.write(html_file)
    print(f"written to path {path}")


if __name__ == "__main__":
    generate_html_from_md("charging-and-walking", "travel")
