
# signup
def dbsignup(cursor,name,password):
    cursor.execute("INSERT INTO users values('{}','{}',CURRENT_DATE())".format(name,password))

#login
def dbsignin(cursor,name,password):
    cursor.execute("SELECT password from users WHERE username='{}'".format(name))
    row = cursor.fetchone()
    if row is None:
        return False
    checkpassword=row[0]
    if password==checkpassword:
        return True
    else:
        return False

def dbview(cursor,name):
    cursor.execute("DROP VIEW IF EXISTS {}".format(name))
    cursor.execute('''CREATE VIEW {} AS
                    SELECT username, book_name,chapters,chapters_read,rating AS sno
                    FROM books_read WHERE username="{}"'''.format(name,name))
    cursor.execute("SELECT * FROM {}".format(name))
    rows=cursor.fetchall()
    return rows

def dboutofstock(cursor,name,book_name):
    cursor.execute("SELECT count(*) FROM books_read where book_name='{}'".format(book_name))
    stock=cursor.fetchone()
    return stock[0]

def dbaddbook(cursor,name,book_name,chapters,chapters_read,rating):
    cursor.execute("INSERT INTO books_read values('{}','{}',{},{},{})".format(name,book_name,chapters,chapters_read,rating))

def dbgetrank(cursor,name):
    cursor.execute("SELECT COUNT(username) FROM books_read WHERE username='{}'".format(name))
    count=cursor.fetchone()
    return count[0]