class Album:
    def __init__(self, title, artist, quantity, id = None):
        self.title = title
        self.artist = artist
        self.quantity = quantity
        self.id = id

    def stock_level(self):
        if self.quantity <= 5:
            return "Low"
        if self.quantity <= 10:
            return "Medium"
        return "High"
