def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            links = extract_markdown_links(text)
            # Process links, splitting text around each link
            last_index = 0
            for anchor_text, url in links:
                start = text.find(f"[{anchor_text}]({url})", last_index)
                if start != -1:
                    # Append text before the link
                    if last_index < start:
                        new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))
                    # Append the link as a TextNode
                    new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
                    # Update the last index after this link
                    last_index = start + len(f"[{anchor_text}]({url})")
            # Append any remaining text after the last link
            if last_index < len(text):
                new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
        else:
            new_nodes.append(node)  # Copy non-text nodes as-is
    return new_nodes

