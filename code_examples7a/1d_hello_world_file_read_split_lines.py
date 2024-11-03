from pathlib import Path

path = Path("hello_agains.txt")
contents = path.read_text().rstrip()
lines = contents.splitlines()

for line_no, line in enumerate(lines, 1):
    print(f"{line_no}: {line}")

print("The list of lines:")
print(repr(lines))
