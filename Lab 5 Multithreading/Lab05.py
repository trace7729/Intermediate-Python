import random
import sqlite3
from sqlite3 import Error
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
import operator
# Python II - Lab 5 - Annie Yen

people_db_file = "sqlite.db" # The name of the database file to use
max_people = 500 # Number of records to create

def read_file(file):
    '''
    Read-only access, return read file as delimited list
    Args:
        file: string
    Returns:
        name_list: list
    '''
    name_list = []
    with open(file, 'r') as filehandle:
        name_list.extend(line.rstrip() for line in filehandle.readlines())
    return name_list

def generate_people(count):
    '''
    Form list of tuples with each tuple represents one person
    (id, first name, last name)
    Args:
        count: number of tuples in a list
    Returns:
        output: list of tuples
    '''
    last_name = []
    first_name = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        first = [ executor.submit(read_file, 'FirstNames.txt')]
        last = [ executor.submit(read_file, 'LastNames.txt')]
        for future in as_completed(first):
            try:
                first_name=future.result()
            except Exception as exc:
                print(f'{exc!r}')
        for future in as_completed(last):
            try:
                last_name=future.result()
            except Exception as exc:
                print(f'{exc!r}') 
    output=list(
        tuple(x) for x in zip(
            (i for i in range(count+1)),
            (first_name[random.randint(0,len(first_name))] for i in range(count)),
            (last_name[random.randint(0,len(last_name))] for i in range(count))
        )
    )
    return output

def create_people_database(db_file, count):
    '''
    Create a SQLite database and insert names into items
    Args:
        db_file: name string of database to use
        count: integer number of records to insert
    '''
    conn = sqlite3.connect(db_file)
    with conn:
        sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people(
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL);"""
        cursor = conn.cursor()
        cursor.execute(sql_create_people_table)
        sql_truncate_people = "DELETE FROM people;"
        cursor.execute(sql_truncate_people)
        people = generate_people(count)
        sql_insert_person = "INSERT INTO people(id,first_name,last_name) VALUES(?,?,?);"
        for person in people:
            #print(person)
            cursor.execute(sql_insert_person, person)
            print(cursor.lastrowid)
        cursor.close()

class PersonDB():
    ''' Context manager class provides read access to database '''
    def __init__(self, db_file=''):
        ''' Store db_file parameter value '''
        self.db_file = db_file

    def __enter__(self):
        ''' Initiate connection to database '''
        self.conn = sqlite3.connect(self.db_file,check_same_thread=False)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        ''' Close database connection '''
        self.conn.close()

    def load_person(self, id):
        ''' Load record with given id '''
        sql = "SELECT * FROM people WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        result = (-1, '', '')
        if records is not None and len(records) > 0:
            result = records[0]
        cursor.close()
        return result


def test_PersonDB():
    ''' Test the load_person method of PersonDB '''
    with PersonDB(people_db_file) as db:
        print(db.load_person(10000))
        print(db.load_person(122))
        print(db.load_person(300))


def many_futures_as_complete():
    '''
    Load the people records, using ThreadPoolExecutor
    Returns:
        result_list: list of tuples (id, first name, last name)
    '''
    result_list = []
    with ThreadPoolExecutor(max_workers=10) as executor, PersonDB(people_db_file) as db:
        futures = [executor.submit(db.load_person, x) for x in range(max_people)]
        wait(futures, return_when=ALL_COMPLETED)
        for future in as_completed(futures):
            try:
                result_list.append(future.result())
            except Exception as err:
                print(f'{exc!r}')
    return result_list


def main():
    #people = generate_people(max_people)
    #print(people)
    #create_people_database(people_db_file, max_people)
    #test_PersonDB()
    #db = PersonDB(people_db_file)
    '''
    Sort the list of records in last name and first name order 
    '''
    output_list = []
    output_list.extend(many_futures_as_complete())
    output_list.sort(key=lambda x:(x[2], x[1]))
    for x in output_list: print(x)


if __name__ == '__main__':
    main()