import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("Select * from dummy;")
    for row in cursor:
        print(f'row={row}')
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'Insert into dummy(a,b) values(?,?);',
        (1234, 'hello')
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update dummy set b = ? where a = ?;',
        ("ByeBye", 1234)
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from dummy where a > 5 ;'
    )
    conn.commit()
    read(conn)


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-4PDJOMHL;"
    "Database=Testdb;"
    "Trusted_Connection=yes"
)

read(conn)
create(conn)
update(conn)
delete(conn)