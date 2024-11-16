import os

def test_file_access():
    # Paths to test
    markdown_test_path = 'content/majesty/index.md'
    html_test_path = 'public/majesty/index.html'

    try:
        # Reading the markdown file
        with open(markdown_test_path, 'r') as f:
            print("Successfully read the markdown file!")
        
        # Writing a test HTML file
        os.makedirs(os.path.dirname(html_test_path), exist_ok=True)
        with open(html_test_path, 'w') as f:
            f.write("<html><body>Test HTML content</body></html>")
            print("Successfully wrote an HTML file!")
    
    except Exception as e:
        print("An error occurred:", e)

test_file_access()
