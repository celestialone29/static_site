def create_block_node(block, block_type):
    """
    Creates an HTMLNode for a given markdown block.

    Parameters:
        block (str): The markdown block.
        block_type (str): The type of the block (e.g., "heading", "paragraph").

    Returns:
        HTMLNode: The HTML representation of the block.
    """
    if block_type == "heading":
        level = block.count("#")
        return HTMLNode(f"h{level}", children=text_to_children(block[level + 1:].strip()))
    if block_type == "paragraph":
        return HTMLNode("p", children=text_to_children(block))
    if block_type == "code":
        return HTMLNode("pre", children=[HTMLNode("code", text=block.strip("```"))])
    if block_type == "quote":
        return HTMLNode("blockquote", children=text_to_children(block.replace(">", "").strip()))
    if block_type == "unordered_list":
        items = [HTMLNode("li", children=text_to_children(item.strip()[2:])) for item in block.splitlines()]
        return HTMLNode("ul", children=items)
    if block_type == "ordered_list":
        items = [HTMLNode("li", children=text_to_children(item.split(". ", 1)[1])) for item in block.splitlines()]
        return HTMLNode("ol", children=items)
    return HTMLNode("p", children=text_to_children(block))  # Default to paragraph

