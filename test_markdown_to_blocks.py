def test_markdown_to_blocks():
    # Test case 1: Simple Markdown input
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    expected_output = [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    ]
    assert markdown_to_blocks(markdown) == expected_output

    # Test case 2: Excessive newlines
    markdown = """# Heading with excessive newlines


This is a paragraph.


* List item 1


* List item 2"""
    expected_output = [
        "# Heading with excessive newlines",
        "This is a paragraph.",
        "* List item 1\n\n* List item 2"
    ]
    assert markdown_to_blocks(markdown) == expected_output

    # Test case 3: Empty input
    markdown = ""
    expected_output = []
    assert markdown_to_blocks(markdown) == expected_output

    # Test case 4: Only whitespace input
    markdown = "   \n\n   \n"
    expected_output = []
    assert markdown_to_blocks(markdown) == expected_output

    print("All tests passed!")

# Run the tests
test_markdown_to_blocks()

