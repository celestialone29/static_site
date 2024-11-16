def text_to_children(text):
    """
    Converts a block of text with inline markdown to child HTMLNode objects.

    Parameters:
        text (str): The raw text with inline markdown.

    Returns:
        list: A list of HTMLNode objects.
    """
    # For simplicity, we handle basic inline markdown here.
    children = []
    while "**" in text or "*" in text:
        if "**" in text:
            start = text.index("**")
            end = text.index("**", start + 2)
            if start > 0:
                children.append(HTMLNode("span", text=text[:start]))
            children.append(HTMLNode("b", text=text[start + 2:end]))
            text = text[end + 2:]
        elif "*" in text:
            start = text.index("*")
            end = text.index("*", start + 1)
            if start > 0:
                children.append(HTMLNode("span", text=text[:start]))
            children.append(HTMLNode("i", text=text[start + 1:end]))
            text = text[end + 1:]
    if text:
        children.append(HTMLNode("span", text=text))
    return children

