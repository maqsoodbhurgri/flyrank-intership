class MemoryRepository:

    def __init__(self):
        self.items = []
        self.counter = 1

    def create_item(self, name):

        item = {
            "id": self.counter,
            "name": name
        }

        self.items.append(item)
        self.counter += 1

        return item

    def get_items(self):
        return self.items
