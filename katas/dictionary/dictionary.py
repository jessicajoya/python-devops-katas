class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word: str, definition: str) -> None:
        key = word.lower()
        self.entries[key] = definition

    def look(self, word: str) -> str:
        key = word.lower()
        if key in self.entries:
            return self.entries[key]
        return f"Can't find entry for {word}"
