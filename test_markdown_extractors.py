import unittest
from markdown_extractors import extract_markdown_images, extract_markdown_links  # Assuming these are saved in a file named markdown_extractors.py

class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images_basic(self):
        text = "Here is an image ![alt text](https://example.com/image.png)"
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_multiple(self):
        text = "First image ![first](https://example.com/first.png) and second image ![second](https://example.com/second.png)"
        expected = [
            ("first", "https://example.com/first.png"),
            ("second", "https://example.com/second.png")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_images(self):
        text = "This text has no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_basic(self):
        text = "Here is a [link to example](https://example.com)"
        expected = [("link to example", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_multiple(self):
        text = "Here are links [first](https://example.com/first) and [second](https://example.com/second)"
        expected = [
            ("first", "https://example.com/first"),
            ("second", "https://example.com/second")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_links(self):
        text = "This text has no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_and_links(self):
        text = "Image ![image](https://example.com/image.png) and [link](https://example.com)"
        images_expected = [("image", "https://example.com/image.png")]
        links_expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_images(text), images_expected)
        self.assertEqual(extract_markdown_links(text), links_expected)

if __name__ == "__main__":
    unittest.main()

