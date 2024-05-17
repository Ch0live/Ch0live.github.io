import os


def interpret_md(line: str):
    return f"<p> hello! Here's your line: {line} </p>"


def generate_html_from_md(name: str, category: str):

    path = os.path.join(os.getcwd(), "blog-posts", category, f"{name}.md")
    md_file = open(path, "r")
   
    html_file_body = []
    for line in md_file.readlines():
        html_file_body.append(interpret_md(line))


if __name__ == "__main__":
    generate_html_from_md("charging-and-walking", "travel")