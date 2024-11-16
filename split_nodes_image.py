from enum import Enum

# Assuming these are imported
# from your project

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            images = extract_markdown_images(text)
            # Process images, splitting text around each image
            last_index = 0
            for alt_text, url in images:
                start = text.find(f"![{alt_text}]({url})", last_index)
                if start != -1:
                    # Append text before the image
                    if last_index < start:
                        new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))
                    # Append the image as a TextNode
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    # Update the last index after this image
                    last_index = start + len(f"![{alt_text}]({url})")
            # Append any remaining text after the last image
            if last_index < len(text):
                new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
        else:
            new_nodes.append(node)  # Copy non-text nodes as-is
    return new_nodes

