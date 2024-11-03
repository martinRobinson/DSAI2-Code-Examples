from pathlib import Path

path = Path("hello_agains.txt")
contents = path.read_text().rstrip()
print(f"The type of contents is {type(contents)}")
print("Normal print of the string:")
print(contents)
print("The raw form of the string:")
raw_string = repr(contents)
print(raw_string)
