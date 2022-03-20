import sqlite3 as sl


def addtodb(id, name, victim_count, famous_for, moniker, age_at_arrest):
    con = sl.connect('serial_killer.db')
    with con:

        try:
            con.execute("""
                CREATE TABLE KILLERS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    victimcount INTEGER,
                    famousfor TEXT,
                    moniker TEXT,
                    ageatarrest INTEGER
                );
            """)
        except:
            pass

        sql = 'INSERT INTO KILLERS (id, name, victimcount, famousfor, moniker, ageatarrest) values(?, ?, ' \
            '?,?,?,?) '

    data = [
        (id, name, victim_count, famous_for, moniker, age_at_arrest)
    ]
    try:
        with con:
            con.executemany(sql, data)
    except Exception as e:
        print(e)


def add_queries():
    print("Before adding please look at sampleserialkillers.txt for an idea on the basic structure.")
    id = input("Please provide an id for the serial killer (in integers): ")
    name = input("Please provide the name: ")
    victim_count = input("Please provide the victim count (in integers): ")
    famous_for = input("Please provide the details on the signature of the serial killer: ")
    moniker = input("Please provide the moniker of the serial killer: ")
    age_at_arrest = input("Please provide the age of the serial killer at his arrest (in integers): ")
    addtodb(id, name,victim_count,famous_for,moniker,age_at_arrest)

add_queries()