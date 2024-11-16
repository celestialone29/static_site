def block_to_block_type(block):
    """
    Determines the type of a Markdown block.

    Parameters:
        block (str): A single block of Markdown text.

    Returns:
        str: The type of the block (e.g., "heading", "paragraph", etc.).
    """
    # Check for heading
    if block.startswith("# "):
        return "heading"
    if block.startswith("## "):
        return "heading"
    if block.startswith("### "):
        return "heading"
    if block.startswith("#### "):
        return "heading"
    if block.startswith("##### "):
        return "heading"
    if block.startswith("###### "):
        return "heading"
   

