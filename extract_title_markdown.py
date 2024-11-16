def extract_title(markdown):
    """
    Extracts the H1 title from the markdown content.

    Parameters:
        markdown (str): The markdown content.

    Returns:
        str: The extracted title.

    Raises:
        ValueError: If no H1 title is found.
    """
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in the markdown file.")

