from mysql import connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Athulya@30",
                database="book_db"
            )
            return self.connection

        except Exception as e:
            print(e)
            return None

class LibraryManager(DbConnect):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "select * from book_details"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            # print(records)
            return (records)
        except Exception as e:
            # print(e)
            return []

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into book_details (book_name, author_name,  price, type, published_year) values(%s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("New book added successfully.......")
        except Exception as e:
            print(e)



# library_instance = LibraryManager()

# library_instance.post(book_name="The Alchemist", author_name="Paulo Coelho", price=350, type="Fiction", published_year=1988)
# library_instance.post(book_name="The Secret", author_name="Rhonde Byrne", price=219, type="Self-Help", published_year=2006)
# library_instance.post(book_name="Rich Dad Poor Dad", author_name="Robert Kiyosaki", price=317, type="Finance",  published_year=1987)

# library_instance.get()