import psycopg2

conn = psycopg2.connect("dbname = dvdrental user = postgress password = vin4798 host= localhost")

cur = conn.cursor()

cur.execute("SELECT first_name FROM customer")
rows= cur.fetchall()
rows
