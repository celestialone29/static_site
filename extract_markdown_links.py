def extract_markdown_links(text):
    # Regular expression pattern to match [anchor text](URL)
    pattern = r"\[([^\]]+)\]\((https?://[^\s]+)\)"
    # Find all matches and return as a list of tuples
    return re.findall(pattern, text)

