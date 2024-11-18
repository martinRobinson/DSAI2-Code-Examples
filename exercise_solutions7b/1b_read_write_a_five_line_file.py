from pathlib import Path

print("--- Reading in the entire file:")
path = Path("content_five_lines.txt")
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
new_content = ""
lines = contents.splitlines()
for line_no, line in enumerate(lines, 1):
    print(f"{line_no}: {line}")
    new_content += f"{line_no}: {line}\n"

new_path = Path("content_five_lines_numbered.txt")
new_path.write_text(new_content)
