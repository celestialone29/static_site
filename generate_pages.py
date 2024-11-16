import markdown
import os

# Function to generate HTML pages recursively
def generate_pages_recursive(content_dir, template_path, dest_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Loop through all files and directories in the content directory
    for item in os.listdir(content_dir):
        item_path = os.path.join(content_dir, item)
        
        if os.path.isdir(item_path):
            # If it's a directory, recurse into it
            subfolder_dest = os.path.join(dest_dir, item)
            generate_pages_recursive(item_path, template_path, subfolder_dest)
            
        elif os.path.isfile(item_path) and item.endswith('.md'):
            # If it's a markdown file, convert it to HTML
            with open(item_path, 'r') as md_file:
                content = md_file.read()
            
            # Convert the markdown content to HTML using the correct extensions
            html_content = markdown.markdown(
                content,
                extensions=['fenced_code', 'codehilite']
            )
            
            # Generate the HTML filename
            html_filename = os.path.splitext(item)[0] + '.html'
            html_filepath = os.path.join(dest_dir, html_filename)
            
            # Read the template and replace the {{ content }} placeholder
            with open(template_path, 'r') as template_file:
                template_content = template_file.read()
                html_page = template_content.replace('{{ content }}', html_content)
            
            # Write the generated HTML page to the destination folder
            with open(html_filepath, 'w') as output_file:
                output_file.write(html_page)
            print(f"Generated: {html_filepath}")

# Main function to start the process
def main():
    # Define paths for the content, template, and destination
    content_dir = 'content'
    template_path = 'templates/template.html'
    dest_dir = 'public'
    
    # Call the recursive page generation function
    generate_pages_recursive(content_dir, template_path, dest_dir)

if __name__ == "__main__":
    main()

