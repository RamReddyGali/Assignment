import mysql.connector
USER='root'
PASSWORD='******'
HOST='127.0.0.1'
PORT='3306'
DATABASE='sensye'
TABLE='mushrooms'

db = mysql.connector.connect(
        user=USER, password=PASSWORD,
        host=HOST, port=PORT,
        database=DATABASE,)

q = f'''CREATE TABLE IF NOT EXISTS {DATABASE}.{TABLE}(
cap_shape varchar(20),
cap_colour varchar(20),
odor varchar(20),
gill_size varchar(20),
gill_colour varchar(20),
stalk_colour_above_ring varchar(20),
veil_colour varchar(20),
ring_type varchar(20),
spore_print_colour varchar(20),
population varchar(20),
habitat varchar(20),
latitude double,
longtidue double,
time varchar (32)
)'''
c = db.cursor()
c.execute(q)
db.commit()