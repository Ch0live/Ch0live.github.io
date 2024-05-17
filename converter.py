import os
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader("./templates"))


def get_template(name: str):
    return env.get_template(f"{name}.j2")


def interpret_md(line: str):
    return f"<p> hello! Here's your line: {line} </p>"


def generate_html_from_md(name: str, category: str):
    path = os.path.join(os.getcwd(), "blog-posts", category, f"{name}.md")
    md_file = open(path, "r")
   
    html_file_body = []
    for line in md_file.readlines():
        html_file_body.append(interpret_md(line))

    temp = get_template("wrapper").render(body=html_file_body)
    print(temp)


if __name__ == "__main__":
    generate_html_from_md("charging-and-walking", "travel")
