from pathlib import Path

path = Path("hello_agains.txt")
contents = path.read_text().rstrip()
lines = contents.splitlines()

text_content = {}

for line_no, line in enumerate(lines, 1):
    text_content[line_no] = line


print("The dictionary of lines:")
print(text_content)
