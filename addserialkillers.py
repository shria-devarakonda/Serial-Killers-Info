import sqlite3 as sl


def add_to_db(name, victim_count, famous_for, moniker, age_at_arrest):
    con = sl.connect('serial_killer.db')
    with con:

        try:
            con.execute("""
                CREATE TABLE KILLERS (
                    name TEXT,
                    victimcount INTEGER,
                    famousfor TEXT,
                    moniker TEXT,
                    ageatarrest INTEGER
                );
            """)
        except:
            pass

        sql = 'INSERT INTO KILLERS (name, victimcount, famousfor, moniker, ageatarrest) values(?, ?, ' \
            '?,?,?) '

    data = [
        (name, victim_count, famous_for, moniker, age_at_arrest)
    ]
    try:
        with con:
            con.executemany(sql, data)
    except Exception as e:
        print(e)


def add_queries():
    print("Before adding please look at sampleserialkillers.txt for an idea on the basic structure.")
    con = sl.connect('serial_killer.db')
    cursor = con.cursor()
    name = input("Please provide the name: ")
    victim_count = input("Please provide the victim count (in integers): ")
    famous_for = input("Please provide the details on the signature of the serial killer: ")
    moniker = input("Please provide the moniker of the serial killer: ")
    age_at_arrest = input("Please provide the age of the serial killer at his arrest (in integers): ")
    add_to_db(name,victim_count,famous_for,moniker,age_at_arrest)
    print("Database updated successfully!")


def names():
    sk_name = []
    con = sl.connect('serial_killer.db')
    data = con.execute("SELECT name FROM KILLERS")
    for row in data:
        sk_name.append(row)
    import re
    a = re.sub("]*\\[*\\(*\\)*'*", '', str(sk_name))
    c = re.sub("(,)", '|', a)
    return c


def delete_row():
    print("Deleting a row:\n")
    print(names()[:-1])
    conn = sl.connect('serial_killer.db')
    name = input("Please provide the name of the killer (exactly as given), that you wish to remove "
                 "from the database: ")
    with conn:
        try:
            conn.execute(f'DELETE FROM KILLERS WHERE name like "{name}";')
            print("Please check if updated, if the list still contains the name, the record has not been removed:")
            print(names()[:-1])
        except:
            print("Delete Failed, did you give the exact name?")
            raise Exception


def init():
    query = input("Would you like to add or delete? type add if youd like to add and delete if youd like to delete.\n")
    if "add" in query:
        add_queries()
    else:
        delete_row()

init()