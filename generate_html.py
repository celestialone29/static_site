import os

def generate_pages_recursive(content_dir, template_path, dest_dir):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Iterate through all items in the content directory
    for item in os.listdir(content_dir):
        item_path = os.path.join(content_dir, item)
        
        if os.path.isdir(item_path):
            # Recursively process subdirectories
            subfolder_dest = os.path.join(dest_dir, item)
            generate_pages_recursive(item_path, template_path, subfolder_dest)
        elif os.path.isfile(item_path) and item.endswith('.md'):
            # Read the raw content from the Markdown file
            with open(item_path, 'r') as f:
                raw_content = f.read()
            
            # Generate the output HTML file path
            html_filename = os.path.splitext(item)[0] + '.html'
            html_filepath = os.path.join(dest_dir, html_filename)
            
            # Read the HTML template
            with open(template_path, 'r') as template_file:
                template_content = template_file.read()
            
            # Replace the placeholder with the raw content
            html_page = template_content.replace('{{ content }}', raw_content)
            
            # Write the generated HTML page
            with open(html_filepath, 'w') as output_file:
                output_file.write(html_page)

def main():
    # Define paths
    content_dir = 'content'
    template_path = 'templates/template.html'
    dest_dir = 'public'
    
    # Generate the pages
    generate_pages_recursive(content_dir, template_path, dest_dir)

if __name__ == "__main__":
    main()

