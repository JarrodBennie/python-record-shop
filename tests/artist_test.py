import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def test_artist_name_is_set(self):
        artist = Artist("AC/DC")
        self.assertEqual("AC/DC", artist.name)

    def test_artist_name_changed(self):
        artist = Artist("AC/DC")
        artist.name = "Iron Maiden"
        self.assertEqual("Iron Maiden", artist.name)

if __name__ == '__main__':
    unittest.main()
