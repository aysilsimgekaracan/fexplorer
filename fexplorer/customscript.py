import psycopg2
import datetime
from fexplorer.db_info import DATABASE, USER, PASSWORD

def addFile(option):
    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD)
    
    today = datetime.datetime.now()
    date_time = today.strftime("%Y-%m-%d, %H:%M:%S")
    
    query = "INSERT INTO fexplorer.files (file_name, path, extension, detail, date_added) VALUES ('{name}', '{path}', '{type}', '{fileDetails}', '{date_time}');".format(**option, date_time=date_time)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def customScript(option):
    addFile(option)