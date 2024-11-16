import re

def extract_markdown_images(text):
    # Regular expression pattern to match ![alt text](URL)
    pattern = r"!\[([^\]]+)\]\((https?://[^\s]+)\)"
    # Find all matches and return as a list of tuples
    return re.findall(pattern, text)

