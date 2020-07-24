import mysql.connector

db = mysql.connector.connect(
        user='root', password='******',
        host='127.0.0.1', port=3306,
        database='sensye',)

q = "INSERT INTO mushrooms (cap_shape,cap_colour,odor,gill_size,gill_colour,stalk_colour_above_ring,veil_colour,ring_type,spore_print_colour,population,habitat,latitude,longtidue, time)VALUES('p','s','t','c','n','s','w','p','k','s','u',46.4504,62.4556,'2:24:56 pm')"
c = db.cursor()
c.execute(q)
db.commit()