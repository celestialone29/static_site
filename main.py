import os
import shutil
import markdown_parser

# Function to copy static files (like images, CSS, etc.)
def copy_static_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # We assume that static files have extensions like .jpg, .png, .css, .js
            if file.endswith(('.jpg', '.png', '.gif', '.css', '.js')):
                src_path = os.path.join(root, file)
                # Get the relative path of the file from the src_dir
                relative_path = os.path.relpath(src_path, src_dir)
                dest_path = os.path.join(dest_dir, relative_path)
                
                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Copy the static file
                shutil.copy(src_path, dest_path)

# Function to generate HTML pages from markdown files
def generate_page(content_path, template_path, dest_path):
    # Read markdown content
    with open(content_path, 'r') as file:
        markdown_content = file.read()

    # Convert markdown to HTML using markdown_parser
    html_content = markdown_parser.parse(markdown_content)

    # Read the template
    with open(template_path, 'r') as template_file:
        template = template_file.read()

    # Replace content in template
    page_content = template.replace("{{ content }}", html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final HTML
    with open(dest_path, 'w') as dest_file:
        dest_file.write(page_content)

# Recursive function to generate HTML pages from all markdown files
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                markdown_file_path = os.path.join(root, file)
                # Assume here you generate output HTML path, e.g.
                output_html_path = os.path.join(dest_dir_path, root.replace(dir_path_content, ''), file.replace('.md', '.html'))
                  
                print(f"Processing Markdown: {markdown_file_path}")
                print(f"Generating HTML: {output_html_path}")

                # Add your html generation logic here
                # For example, reading markdown, using template, and writing to output

                relative_output_path = os.path.join(dest_dir_path, os.path.relpath(root, dir_path_content), file.replace('.md', '.html'))
                generate_page(markdown_file_path, template_path, relative_output_path)

# Main function to generate the site
def main():
    # Clean the public directory before generating
    if os.path.exists("public"):
        shutil.rmtree("public")

    # Generate pages from markdown files
    generate_pages_recursive("content", "templates/templates/template.html", "public")

    # Copy static files from static folder
    if os.path.exists("static"):
        copy_static_files("static", "public")


if __name__ == "__main__":
    main()

