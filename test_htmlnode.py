import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Some text")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_attributes(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Sample", props={"class": "container"})
        expected_repr = "HTMLNode(tag='div', value='Sample', children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()

