import os
import psycopg


DATABASE_URL = os.getenv("DATABASE_URL")


class PostgresRepository:

    def get_connection(self):
        return psycopg.connect(DATABASE_URL)

    def create_item(self, name):

        with self.get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute(
                    """
                    INSERT INTO items(name)
                    VALUES(%s)
                    RETURNING id,name
                    """,
                    (name,)
                )

                row = cur.fetchone()

                return {
                    "id": row[0],
                    "name": row[1]
                }

    def get_items(self):

        with self.get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute(
                    "SELECT id,name FROM items"
                )

                rows = cur.fetchall()

                return [
                    {
                        "id": row[0],
                        "name": row[1]
                    }
                    for row in rows
                ]
