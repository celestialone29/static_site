from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # Only process nodes of TextType.TEXT that contain the delimiter
        if node.text_type == TextType.TEXT and delimiter in node.text:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:  # Even index: regular text
                    if part:  # Avoid adding empty strings
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Odd index: text within delimiter
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)  # Add nodes without delimiter as is
    
    return new_nodes

