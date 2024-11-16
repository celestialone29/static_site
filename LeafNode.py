class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        # Enforce no children for LeafNode
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        # Return raw text if there's no tag
        if self.tag is None:
            return self.value
        # Otherwise, return as an HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

