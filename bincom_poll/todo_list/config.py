import psycopg2

conn = psycopg2.connect(
    database='bincom',
    user='peter',
    password='peterojo32'
)

cursor = conn.cursor()
