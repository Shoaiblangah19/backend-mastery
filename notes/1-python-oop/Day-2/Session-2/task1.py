'''
### ⚡ Micro Task 1 (~7 min)

```
Create a class `Playlist`:
  - __init__ takes playlist_name (str)
  - stores songs as empty list internally

  - add_song(title: str, artist: str, duration_seconds: int)
      → stores song as dict in the list
  
  - total_duration() → returns total seconds (no parameters needed)
  
  - longest_song() → returns the title of longest song

Test:
  p = Playlist("Road Trip")
  p.add_song("Bohemian Rhapsody", "Queen", 354)
  p.add_song("Stairway to Heaven", "Led Zeppelin", 482)
  p.add_song("Hotel California", "Eagles", 391)

  p.total_duration()  → 1227
  p.longest_song()    → "Stairway to Heaven"

Decide yourself: which things are parameters, which are self attributes.
Time: 7 minutes.
'''

class Playlist:
    def __init__(self,playlist_name:str):
        self.playlist_name:str = playlist_name
        self.duration:int = 0

        self.songs: list[dict]=[]
    
    def add_song(self,title:str,artist:str,duration_seconds:int)->None:
        self.songs.append({
            "title":title,
            "artist":artist,
            "duration_seconds":duration_seconds
        })
        self.duration += duration_seconds
    def total_duration(self)->int:
        return self.duration
    def longest_song(self)->str:
        longest={
            "title":"",
            "duration_seconds":0
        }
        for song in self.songs:
            if song["duration_seconds"]>=longest["duration_seconds"]:
                longest["title"]=song["title"]
                longest["duration_seconds"]=song["duration_seconds"]
        
        return longest["title"]

p = Playlist("Road Trip")
p.add_song("Bohemian Rhapsody", "Queen", 354)
p.add_song("Stairway to Heaven", "Led Zeppelin", 482)
p.add_song("Hotel California", "Eagles", 391)

print(p.total_duration()) #→ 1227
print(p.longest_song())   #→ "Stairway to Heaven"

if __name__ == "__main__":

    # Test 1: Basic initialization
    try:
        p = Playlist("My Playlist")
        assert p.playlist_name == "My Playlist"
        assert p.songs == []
        assert p.duration == 0
        print("Test 1 passed: Initialization works correctly")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: Adding a single song
    try:
        p = Playlist("Test")
        p.add_song("Song A", "Artist A", 200)
        assert len(p.songs) == 1
        assert p.songs[0]["title"] == "Song A"
        assert p.songs[0]["artist"] == "Artist A"
        assert p.songs[0]["duration_seconds"] == 200
        print("Test 2 passed: Single song added correctly")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: Total duration with provided test data
    try:
        p = Playlist("Road Trip")
        p.add_song("Bohemian Rhapsody", "Queen", 354)
        p.add_song("Stairway to Heaven", "Led Zeppelin", 482)
        p.add_song("Hotel California", "Eagles", 391)
        assert p.total_duration() == 1227, f"Expected 1227, got {p.total_duration()}"
        print("Test 3 passed: Total duration is 1227")
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: Longest song with provided test data
    try:
        p = Playlist("Road Trip")
        p.add_song("Bohemian Rhapsody", "Queen", 354)
        p.add_song("Stairway to Heaven", "Led Zeppelin", 482)
        p.add_song("Hotel California", "Eagles", 391)
        assert p.longest_song() == "Stairway to Heaven", f"Expected 'Stairway to Heaven', got '{p.longest_song()}'"
        print("Test 4 passed: Longest song is 'Stairway to Heaven'")
    except Exception as e:
        print(f"Test 4 failed: {e}")

    # Test 5: Empty playlist - total_duration
    try:
        p = Playlist("Empty")
        assert p.total_duration() == 0
        print("Test 5 passed: Empty playlist duration is 0")
    except Exception as e:
        print(f"Test 5 failed: {e}")

    # Test 6: Empty playlist - longest_song returns empty string
    try:
        p = Playlist("Empty")
        result = p.longest_song()
        assert result == "", f"Expected empty string, got '{result}'"
        print("Test 6 passed: Empty playlist longest song returns empty string")
    except Exception as e:
        print(f"Test 6 failed: {e}")

    # Test 7: Single song is both total and longest
    try:
        p = Playlist("Solo")
        p.add_song("Only Song", "Solo Artist", 300)
        assert p.total_duration() == 300
        assert p.longest_song() == "Only Song"
        print("Test 7 passed: Single song handles both methods correctly")
    except Exception as e:
        print(f"Test 7 failed: {e}")

    # Test 8: Two songs with EQUAL duration - longest_song picks last one (due to >=)
    try:
        p = Playlist("Tied")
        p.add_song("First", "A", 300)
        p.add_song("Second", "B", 300)
        result = p.longest_song()
        # Your code uses >=, so "Second" overwrites "First"
        assert result == "Second", f"Expected 'Second', got '{result}'"
        print("Test 8 passed: Equal duration returns last added song")
    except Exception as e:
        print(f"Test 8 failed: {e}")

    # Test 9: Duration accumulates correctly across multiple adds
    try:
        p = Playlist("Accumulate")
        p.add_song("A", "X", 100)
        assert p.total_duration() == 100
        p.add_song("B", "Y", 200)
        assert p.total_duration() == 300
        p.add_song("C", "Z", 150)
        assert p.total_duration() == 450
        print("Test 9 passed: Duration accumulates correctly")
    except Exception as e:
        print(f"Test 9 failed: {e}")

    print("\nAll tests completed!")