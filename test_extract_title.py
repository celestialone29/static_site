import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#   Title With Spaces  "), "Title With Spaces")
    
    def test_extract_title_no_h1(self):
        with self.assertRaises(ValueError):
            extract_title("## Subheading\nContent without an H1 header")
    
    def test_extract_title_multiple_h1(self):
        self.assertEqual(extract_title("# First Title\n# Second Title"), "First Title")

if __name__ == "__main__":
    unittest.main()

