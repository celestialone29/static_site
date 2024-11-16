def test_block_to_block_type():
    # Test headings
    assert block_to_block_type("# Heading") == "heading"
    assert block_to_block_type("### Subheading") == "heading"
    assert block_to_block_type("###### Small heading") == "heading"

    # Test code blocks
    assert block_to_block_type("```\ncode block\n```") == "code"

    # Test quote blocks
    assert block_to_block_type("> Quote line 1\n> Quote line 2") == "quote"

    # Test unordered lists
    assert block_to_block_type("* Item 1\n* Item 2") == "unordered_list"
    assert block_to_block_type("- Item 1\n- Item 2") == "unordered_list"

    # Test ordered lists
    assert block_to_block_type("1. First item\n2. Second item") == "ordered_list"

    # Test paragraphs
    assert block_to_block_type("This is a regular paragraph.") == "paragraph"

    # Edge cases
    assert block_to_block_type("##Invalid heading") == "paragraph"  # No space after ##
    assert block_to_block_type("1. First item\n3. Third item") == "paragraph"  # Incorrect numbering in ordered list

    print("All tests passed!")

# Run the tests
test_block_to_block_type()

