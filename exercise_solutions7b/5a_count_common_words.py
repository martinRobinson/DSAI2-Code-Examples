from pathlib import Path

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filenames = ['alice_in_wonderland.txt', 'moby_dick.txt', 'little_women.txt']

search_term = 'whale'
for filename in filenames:
    count_common_words(filename, search_term)
