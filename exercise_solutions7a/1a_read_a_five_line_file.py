from pathlib import Path

print("--- Reading in the entire file:")
path = Path("content_five_lines.txt")
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line_no, line in enumerate(lines, 1):
    print(f"{line_no}: {line}")
