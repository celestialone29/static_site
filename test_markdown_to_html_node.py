def test_markdown_to_html_node():
    markdown = """# Heading 1

This is a **bold** paragraph with *italic* text.


> Quote block

* Item 1
* Item 2

1. Ordered item 1
2. Ordered item 2"""

    html_node = markdown_to_html_node(markdown)
    assert str(html_node) == (
        "<div>"
        "<h1>Heading 1</h1>"
        "<p>This is a <b>bold</b> paragraph with <i>italic</i> text.</p>"
        "<pre><code>Code block</code></pre>"
        "<blockquote>Quote block</blockquote>"
        "<ul><li>Item 1</li><li>Item 2</li></ul>"
        "<ol><li>Ordered item 1</li><li>Ordered item 2</li></ol>"
        "</div>"
    )
    print("All tests passed!")

# Run the tests
test_markdown_to_html_node()

