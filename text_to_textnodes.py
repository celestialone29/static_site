def text_to_textnodes(text):
    # Start with the basic text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split for bold text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Split for italic text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    # Split for code blocks
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Split for images
    nodes = split_nodes_image(nodes)
    
    # Split for links
    nodes = split_nodes_link(nodes)
    
    return nodes
import unittest
from markdown_splitter import text_to_textnodes  # Assuming this is where your function is

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_basic(self):
        text = "This is **bold** and *italic* text"
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_with_code(self):
        text = "This is a `code block` in the text"
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in the text", TextType.TEXT),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_with_image(self):
        text = "This is an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_nodes = [
            TextNode("This is an image ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_with_link(self):
        text = "Click on this [link](https://boot.dev)"
        expected_nodes = [
            TextNode("Click on this ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_mixed(self):
        text = "This is **bold** text with *italic* and `code block` and a [link](https://boot.dev) and ![image](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

if __name__ == "__main__":
    unittest.main()

