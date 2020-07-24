from csv import DictReader
import json
import mysql.connector

USER='root'
PASSWORD='******'
HOST='127.0.0.1'
PORT='3306'
DATABASE='sensye'
TABLE='mushrooms'

class Etl:
    def __init__(self, path, trans_file_name):
        self.path = path
        self.trans_file_name = trans_file_name
        self.out_dict = {}

    def convert_trans_file(self, file_name):
        file_path = f"{self.path}/{file_name}"
        with open(file_path, "r") as file:
            for row in file.readlines():
                row_dict = {}
                values = row.split(".")
                serial_key, serial_value = values
                attr_key, attr_val = serial_value.split(":")
                pair_dict = {}
                for pairs in attr_val.split(","):
                    x, y = pairs.split("=")
                    x_strp = x.rstrip("\n").strip()
                    y_strp = y.rstrip("\n").strip()
                    x_enc = f"{x_strp}"
                    y_enc = f"{y_strp}"
                    pair_dict[y_enc] = x_enc
                serial_key_enc = f"{serial_key.strip()}"
                row_dict[serial_key_enc] = pair_dict
                self.out_dict.update(row_dict)
            return self.out_dict

    def write_out_trans_file(self, content):
        o_file_path = f"{self.path}/{self.trans_file_name}"
        with open(o_file_path, "w") as w_file:
            json.dump(content, w_file)

    def translate_values(self, dict_object, col_name, row_value):
        trans_value = dict_object[col_name].get(row_value,'Null')
        return trans_value

    def read_trans_dict_file(self):
        file_path = f'{self.path}/{self.trans_file_name}'
        with open(file_path, 'r') as tfile:
            json_dict = json.load(tfile)
            return json_dict

    def load_mysql_table(self):
        file_path=f'{self.path}/insert_stmt.txt'
        db = mysql.connector.connect(
            user=USER, password=PASSWORD,
            host=HOST, port=PORT,
            database=DATABASE,)
        cur=db.cursor()

        with open(file_path, 'r') as read_file:
            for lines in read_file.readlines():
                cur.execute(lines)
        db.commit()

    def create_insert_statement(self, db_name, table_name, trans_row):
        string_row = ','.join("'"+item+"'" for item in trans_row)
        return f'insert into {db_name}.{table_name} values( {string_row})'




####################MAIN CODE####################
DB_NAME='sensye'
TABLE_NAME='mushrooms'


#creation of trans file
new_etl = Etl("/Users/ramgali/PycharmProjects/Pydemo/Sensye/data", "trans_dict.json")
out_dict = new_etl.convert_trans_file("trns-file.txt")
new_etl.write_out_trans_file(out_dict)


#reading data file
dict_object = new_etl.read_trans_dict_file()
d_file_path = f'{new_etl.path}/agaricus-lepiota.csv'
with open(f'{new_etl.path}/insert_stmt.txt', 'w') as w_file:
    with open(d_file_path, 'r') as file:
        csv_file_buffer = DictReader(file, delimiter=',')
        field_names = csv_file_buffer.fieldnames
        for row in csv_file_buffer:
            final_row = []
            for col_name in field_names:
                if col_name not in ('lat', 'lon', 'Time'):
                    trans_col = new_etl.translate_values(dict_object, col_name, row[col_name])
                    final_row.append(trans_col)
            for o_col_name in ['lat', 'lon', 'Time']:
                final_row.append(row[o_col_name])
            insert_stmnt=new_etl.create_insert_statement(DB_NAME, TABLE_NAME, final_row)
            w_file.write(f'{insert_stmnt}\n')




#connecting to database

new_etl.load_mysql_table()

