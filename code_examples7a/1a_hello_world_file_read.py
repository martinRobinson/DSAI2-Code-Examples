from pathlib import Path

path = Path("hello_world.txt")
contents = path.read_text()
print(contents)