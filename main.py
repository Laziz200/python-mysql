import pymysql.cursors
connection = pymysql.connect(
    user='root',
    password='LAZIZ',
    database='company_db'
)

cursor = connection.cursor()

create_books_table(cursor)

insert_book(cursor, "Atomic Habits", "James Clear", 2018, "Self-help", 15.99, True)

connection.commit()

show_all_books(cursor)

cursor.close()
connection.close()

