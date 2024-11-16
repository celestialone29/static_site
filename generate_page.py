import os
import re

def convert_to_html_tags(content):
    # Replace Markdown headings with HTML equivalents
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    return content
print("Converted Content:", content)


def generate_page(src_path, template_path, dest_path):
    # Read the template
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    
    # Read and process the markdown content
    with open(src_path, 'r') as file:
        content = file.read()
        # Extract title from the markdown file
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Untitled"
        content = convert_to_html_tags(content)

    # Replace placeholders in the template
    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # Write the output to the destination path
    with open(dest_path, 'w') as output_file:
        output_file.write(page_content)

def generate_pages_recursive(content_dir, template_path, public_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, content_dir)
                dest_path = os.path.join(public_dir, os.path.splitext(rel_path)[0] + ".html")
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(src_path, template_path, dest_path)

def main():
    content_dir = "content"
    template_path = "templates/template.html"
    public_dir = "public"
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()

