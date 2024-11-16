class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have at least one child.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have at least one child.")
        
        # Generate HTML for each child recursively
        children_html = ''.join(child.to_html() for child in self.children)
        
        # Return the HTML output for the parent tag
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

