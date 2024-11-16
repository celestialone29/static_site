import unittest
from markdown_splitter import split_nodes_image, split_nodes_link  # Assuming these functions are saved in markdown_splitter.py

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_link_basic(self):
        node = TextNode("Check out [Google](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Check out ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode("Here are [Google](https://www.google.com) and [GitHub](https://github.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Here are ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("GitHub", TextType.LINK, "https://github.com")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_image_basic(self):
        node = TextNode("Look at this image ![Alt text](https://example.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Look at this image ", TextType.TEXT),
            TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode("Images: ![First](https://example.com/first.png) and ![Second](https://example.com/second.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Images: ", TextType.TEXT),
            TextNode("First", TextType.IMAGE, "https://example.com/first.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Second", TextType.IMAGE, "https://example.com/second.png")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_mixed(self):
        node = TextNode("Here is a link [GitHub](https://github.com) and an image ![Logo](https://example.com/logo.png)", TextType.TEXT)
        link_nodes = split_nodes_link([node])
        image_nodes = split_nodes_image(link_nodes)
        expected = [
            TextNode("Here is a link ", TextType.TEXT),
            TextNode("GitHub", TextType.LINK, "https://github.com"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("Logo", TextType.IMAGE, "https://example.com/logo.png")
        ]
        self.assertEqual(image_nodes, expected)

if __name__ == "__main__":
    unittest.main()

