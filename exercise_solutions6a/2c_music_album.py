def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if num_songs:
        album_dict["num_songs"] = num_songs
    return album_dict


album = make_album("the smiths", "strangeways, here we come")
print(album)

album = make_album("hue and cry", "remote")
print(album)

album = make_album("prefab sprout", "steve mcqueen")
print(album)

album = make_album("the blue nile", "a walk across the rooftops", num_songs=12)
print(album)
