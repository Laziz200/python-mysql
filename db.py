import pymysql.cursors

def create_books_table(cursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            published_year INT,
            genre VARCHAR(100),
            price DECIMAL(10, 2),
            available BOOLEAN
        );
    """)

def insert_book(cursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """
    cursor.execute("""
        INSERT INTO books (title, author, published_year, genre, price, available)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (title, author, published_year, genre, price, available))

def show_all_books(cursor):
    """
    Retrieve and display all books from the 'books' table.
    """
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    for book in books:
        print(book)

def search_books_by_author_or_genre(cursor, search_type, search_value):
    """
    Search for books by author or genre.
    """
    if search_type == "author":
        cursor.execute("SELECT * FROM books WHERE author LIKE %s;", ('%' + search_value + '%',))
    elif search_type == "genre":
        cursor.execute("SELECT * FROM books WHERE genre LIKE %s;", ('%' + search_value + '%',))
    else:
        print("Invalid search type. Please use 'author' or 'genre'.")
        return

    books = cursor.fetchall()
    for book in books:
        print(book)

def update_book_price(cursor, book_id, new_price):
    """
    Update the price of a specific book.
    """
    cursor.execute("UPDATE books SET price = %s WHERE id = %s;", (new_price, book_id))

def update_book_availability(cursor, book_id, available):
    """
    Update the availability of a specific book.
    """
    cursor.execute("UPDATE books SET available = %s WHERE id = %s;", (available, book_id))

def delete_book(cursor, book_id):
    """
    Delete a specific book from the 'books' table.
    """
    cursor.execute("DELETE FROM books WHERE id = %s;", (book_id,))

def sort_books_by_year(cursor, order="ASC"):
    """
    Retrieve books sorted by published year.
    """
    query = f"SELECT * FROM books ORDER BY published_year {order};"
    cursor.execute(query)
    books = cursor.fetchall()
    for book in books:
        print(book)

def count_books(cursor):
    """
    Count the total number of books in the 'books' table.
    """
    cursor.execute("SELECT COUNT(*) FROM books;")
    count = cursor.fetchone()[0]
    print(f"Total books: {count}")

def price_statistics(cursor):
    """
    Display min, max, and average price of books.
    """
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM books;")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"Min Price: {min_price}, Max Price: {max_price}, Avg Price: {avg_price:.2f}")

