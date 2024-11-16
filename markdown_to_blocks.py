def markdown_to_blocks(markdown):
    """
    Splits a raw Markdown string into block-level Markdown elements.
    
    Parameters:
        markdown (str): The raw Markdown string.
        
    Returns:
        list: A list of Markdown block strings.
    """
    # Split by double newlines to separate blocks
    blocks = markdown.split("\n\n")
    # Strip whitespace and remove empty blocks
    return [block.strip() for block in blocks if block.strip()]

