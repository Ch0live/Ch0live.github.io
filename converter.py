import os
import logging

# A script to convert my markdown files into html

article_name = "kicking-this-all-off"
article_type = "travel"
path_to_article_md_file = os.path.join(os.getcwd(), "blog-posts", article_type, article_name + ".md")

article_md_file = open(path_to_article_md_file, "r")
article_html_body = ""

# Create article from md file
for line in article_md_file:
    if (line[0:1] == "# "):
        article_html_body.append(
            # load h1.j2 template
        )
    elif (line[0:2] == "## "):
        article_html_body.append(
            # load h2.j2 template
        )
    elif (line[0:3] == "### "):
        article_html_body.append(
            # load h3.j2 template
        )
    elif (line[0:2] == "!["):
        article_html_body.append(
            # load img.j2 template
        )
    elif (regex("[a-z][A-Z][1-9]", line[0])):
        # TODO: scan line for "[]()" links
        article_html_body.append(
            # load p.j2 template
        )
    else:
        logging.info(f"\nError: Unable to scan line\n{line}")
    
    # Append newline between each element
    article_html_file.append("")

# Wrap article with required HTML tags
# jinga_templates.load(article_html_file_wrapper, body=article_html_file)

# Write article to html file
# open(f"{article_name}.html")
