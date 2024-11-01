def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('the smiths', 'strangeways, here we come')
print(album)

album = make_album('hue and cry', 'remote')
print(album)

album = make_album('prefab sprout', 'steve mcqueen')
print(album)
