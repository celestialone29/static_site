class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
                f"children={self.children!r}, props={self.props!r})")
markdown_content = open(from_path, "r").read()
html_node = markdown_to_html_node(markdown_content)
html_content = html_node.to_html()
print(f"Converted HTML Content:\n{html_content}")
<h1>Tolkien Fan Club</h1>
<p><b>I like Tolkien</b>. Read my <a href="/majesty">first post here</a>...</p>

