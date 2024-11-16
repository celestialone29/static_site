class HTMLNode:
    def __init__(self, tag, children=None, text=None):
        """
        Represents a single HTML node.

        Parameters:
            tag (str): The HTML tag for the node.
            children (list): List of child nodes (HTMLNode instances).
            text (str): The text content of the node, if applicable.
        """
        self.tag = tag
        self.children = children if children is not None else []
        self.text = text

    def __str__(self):
        if self.text:
            return f"<{self.tag}>{self.text}</{self.tag}>"
        children_html = "".join(str(child) for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"
def markdown_to_html_node(markdown):
    """
    Converts a full markdown document into a single HTMLNode.

    Parameters:
        markdown (str): The full markdown document.

    Returns:
        HTMLNode: The root HTMLNode containing all child nodes.
    """
    blocks = markdown_to_blocks(markdown)  # Split into blocks
    parent_node = HTMLNode("div")  # Root node

    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = create_block_node(block, block_type)
        parent_node.children.append(block_node)

    return parent_node

