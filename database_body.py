import sqlite3 as sq
from random import choice

# from verb_body import *

class Verb:
    def __init__(self, inf_value, pres_base, translation, conj):
        self.inf_value = inf_value
        self.pres_base = pres_base
        self.translation = translation
        self.conj = conj

    def __str__(self):
        return f'{self.inf_value} {self.pres_base} {self.translation} {self.conj}'


class DataBase():

    def __init__(self):
        self.create_database()

    def create_database(self):
        with sq.connect('verb_base.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS verb_base (
            inf_value TEXT NOT NULL,
            pres_base TEXT NOT NULL,
            translation TEXT NOT NULL,
            conj TEXT NOT NULL
            )""")

    # def add_data(self, verb: 'Verb'):
    #     with sq.connect('verb_base.db') as con:
    #         cur = con.cursor()
    #         cur.execute(f"""INSERT INTO verb_base VALUES (
    #         '{verb.inf_value}', '{verb.pres_base}', '{verb.translation}', '{verb.conj}')""")
    #         con.commit()
    #
    # def get_random_verb(self):
    #     with sq.connect('verb_base.db') as con:
    #         cur = con.cursor()
    #         res = cur.execute("""SELECT * FROM verb_base""")
    #         con.commit()
    #     # for i in res:
    #     #     print(i)
    #     return choice([*res])




# if __name__ == '__main__':
#     db = DataBase()
    # v = Verb('is.', 'iccha-', 'хотіти, воліти', 'U')
    # db.add_data(v)
    # v2 = Verb('likh', 'likcha-', 'писати', 'P')
    # db.add_data(v2)
    # v3 = Verb('khaad', 'khaada-', 'їсти', 'P')
    # db.add_data(v3)
    # v4 = Verb('c,iks.', 'c,iks.a', 'навчатися', 'A')
    # db.add_data(v4)
    # v5 = Verb('gam', 'gaccha-', 'ходити, бродити', 'P')
    # db.add_data(v5)
    # v6 = Verb('vas', 'vasa-', 'жити, мешкати', 'U')
    # db.add_data(v6)
    # print(db.get_random_verb())