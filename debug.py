from_path = "content/index.md"

def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown")

markdown_content = open(from_path, "r").read()
title = extract_title(markdown_content)
print("Markdown content:", markdown_content)

print(f"Extracted Title: {title}")

