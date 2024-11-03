from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

print("Show the newlines in string contents:")
print(repr(contents))

lines = contents.splitlines()
print()
for line_no, line in enumerate(lines, 1):
    print(f"{line_no}: {repr(line)}")
