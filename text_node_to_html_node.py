from htmlnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)  # Raw text with no tag
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)  # Bold text with <b> tag
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)  # Italic text with <i> tag
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)  # Code text with <code> tag
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("URL is required for a LINK TextType.")
        return LeafNode("a", text_node.text, {"href": text_node.url})  # Link with <a> tag
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.text:
            raise ValueError("URL and alt text are required for an IMAGE TextType.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})  # Image with <img> tag
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")

