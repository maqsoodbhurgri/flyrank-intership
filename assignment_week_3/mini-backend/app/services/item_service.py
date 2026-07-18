from app.repositories.postgres_repository import PostgresRepository


class ItemService:

    def __init__(self):
        self.repo = PostgresRepository()

    def create_item(self, name):
        return self.repo.create_item(name)

    def get_items(self):
        return self.repo.get_items()
