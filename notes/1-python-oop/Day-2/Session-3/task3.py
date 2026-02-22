'''
### ⚡ Micro Task 3 (5 min)

Create a `Playlist` class with:
- name: str
- songs: list of dicts (each has "title": str, "artist": str, "duration": int)

Write an `add_song` method that accepts either:
- A single dict (one song)
- A list of dicts (multiple songs)

Use `isinstance` to handle both cases in one method. Add proper type hints for the parameter using `|` (union).

Test with single song addition and bulk addition. Verify both work.
'''

class Playlist:
    def __init__(self,name:str):
        self.name:str = name

        self.songs:list[dict[str,str|int]] = []
    def add_song(self,song: dict[str,str|int] | list[dict[str,str|int]])->None:
        if isinstance(song,dict):
            self.songs.append(song)
        else:
            for s in song:
                self.songs.append(s)
if __name__ == "__main__":

    # Test 1: Basic initialization — WILL FAIL
    try:
        p = Playlist("My Playlist")
        print(f"Songs attribute exists: {hasattr(p, 'songs')}")
        print(f"Songs value: {p.songs}")
        print("Test 1 passed")
    except AttributeError as e:
        print(f"Test 1 FAILED: {e}")

    # Test 2: Add single song — WILL FAIL
    try:
        p = Playlist("Rock")
        p.add_song({"title": "Thunder", "artist": "AC/DC", "duration": 293})
        assert len(p.songs) == 1
        print("Test 2 passed")
    except AttributeError as e:
        print(f"Test 2 FAILED: {e}")

    # Test 3: Add multiple songs — WILL FAIL
    try:
        p = Playlist("Mixed")
        songs = [
            {"title": "A", "artist": "X", "duration": 200},
            {"title": "B", "artist": "Y", "duration": 300}
        ]
        p.add_song(songs)
        assert len(p.songs) == 2
        print("Test 3 passed")
    except AttributeError as e:
        print(f"Test 3 FAILED: {e}")