'''from random import choice
from main123 import *


class MainList:
    RANDOM_DICT = []
    DATA = [[('1rst, sg', '-mi', '-i'), ('1rst, du', '-vas', '-vahe'), ('1rst, pl', '-mas', '-mahe')],
            [('2nd, sg', '-si', '-se'), ('2nd, du', '-thas', '-ithe'), ('2nd, pl', '-tha', '-dhve')],
            [('3rd, sg', '-ti', '-te'), ('3rd, du', '-tas', '-ite'), ('3rd, pl', '-nti', '-nte')]]

    P_HINT = [['-mi', '-vas', '-mas'],
              ['-si', '-thas', '-tha'],
              ['-ti', '-tas', '-nti']]

    A_HINT = [['-i', '-vahe', '-mahe'],
              ['-se', '-ithe', '-dhve'],
              ['-te', '-ite', '-nte']]

    VERB_RES = ''
    RAND_DATA = ''

    def __call__(self, word):
        return self.add_data(word)

    def __str__(self) -> list:
        return f'{self.RANDOM_DICT}'

    def add_data(self, word: Verb) -> None:
        self.RANDOM_DICT.append(word)

    def random_data(self) -> tuple:
        all_data = [elem for item in MainList.DATA for elem in item]
        MainList.RAND_DATA = choice(all_data)
        return MainList.RAND_DATA

    def random_verb(self) -> tuple:
        res = choice(MainList.RANDOM_DICT)
        MainList.VERB_RES = (res.translation, res.conj)
        return MainList.VERB_RES

    def show_conjugation_hint(self) -> str:
        if self.VERB_RES[-1] == '-/P/-':
            return self.RAND_DATA[1]
        elif self.VERB_RES[-1] == '-/A/-':
            return self.RAND_DATA[-1]
        elif self.VERB_RES[-1] == '-/U/-':
            return f'{self.RAND_DATA[-1], self.RAND_DATA[-2]}'


if __name__ == '__main__':
    a = MainList()
    a1 = Verb('-/is./-', '-/iccha-/-', '-/хотіти, воліти/-', '-/U/-')
    a2 = Verb('-/likh/-', '-/likha/-', '-/писати/-', '-/P/-')
    a3 = Verb('-/khaad/-', '-/khaada/-', '-/їсти/-', '-/P/-')
    a4 = Verb('-/iiks./-', '-/iiks.a/-', '-/бачити, дивитись/-', '-/A/-')
    a5 = Verb('-/c,iks./-', '-/c,iks.a/-', '-/навчатись/-', '-/A/-')
    a(a1)
    a(a2)
    a(a3)
    a(a4)
    a(a5)
    # a.show_conjugation_hint
    # print('a.RANDOM_DICT', a.RANDOM_DICT)
    a.random_verb()
    a.random_data()
    print('a.VERB_RES', a.VERB_RES)
    print('a.RAND_DATA', a.RAND_DATA)
    print('a.show_conjugation_hint', a.show_conjugation_hint())



class Verb:
    def __init__(self, inf_value, pres_base, translation, conj):
        self.inf_value = inf_value
        self.pres_base = pres_base
        self.translation = translation
        self.conj = conj

    def __str__(self):
        return f'{self.inf_value} {self.pres_base} {self.translation} {self.conj}'


if __name__ == '__main__':
    print(Verb.__dict__)
    v = Verb('-/is./-', '-/iccha-/-', '-/хотіти, воліти/-', '-/U/-')
    print(v.inf_value)
    print(v)


from tkinter import *
root = Tk()
label = Label(root, text='LANGUAGE TRAINER')
label.pack()






root.mainloop()


'''
'''import tkinter as tk
from main_body import *
from random import choice


def get_random_word():
    return choice(['above', 'below', 'upper', 'under', 'after', 'hitherto'])


def get_random_num():
    return choice(range(10))


def get_random_symbol():
    return choice(['!', '@', '#', '$'])


def rule_cb():
    for entry in [ent1, ent2, ent3, ent4]:
        if cb_var.get() == 1:
            entry.config(state='normal', bg='white')
        else:
            entry.config(state='disabled')


win = tk.Tk()
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.config(background='Grey')
win.title('SANSCRIT LANGUAGE TRAINER')
win.geometry('1600x800')
# win.minsize(500, 300)
# win.maxsize(900, 700)
win.resizable(True, True)
label1 = tk.Label(win, text='RANDOM VERB',
                  font=('Dubai', 14, 'bold'),
                  bg='grey',
                  padx=10,
                  pady=30,
                  width=15,
                  height=1)
label2 = tk.Label(win, text='HINT TRANSLATION',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label3 = tk.Label(win, text='HINT CONJUGATION FORM',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label4 = tk.Label(win, text='infinitive form',
                  bg='grey', font=('Dubai', 12, 'bold'))
label5 = tk.Label(win, text='base', bg='grey', font=('Dubai', 12, 'bold'))
label6 = tk.Label(win, text='translation', bg='grey', font=('Dubai', 12, 'bold'))
label7 = tk.Label(win, text='conjugation type', bg='grey', font=('Dubai', 12, 'bold'))
label8 = tk.Label(win, text='Enter new data', bg='grey', font=('Dubai', 16, 'bold'))
btn2 = tk.Button(win, text='SAVE DATA', activebackground='yellow')
btn3 = tk.Button(win, text='translation hint', activebackground='yellow', anchor='e')
btn4 = tk.Button(win, text='conjugation hint', activebackground='yellow')
btn5 = tk.Button(win, text='GENERATE', activebackground='yellow', state='normal')
cb_var = tk.IntVar()
cb_var.set(0)
cb = tk.Checkbutton(win, text='insert data', bg='grey', activebackground='grey', variable=cb_var, onvalue=1,
                    offvalue=0, command=rule_cb)

cb.deselect()
ent1 = tk.Entry(win, state='disabled', bg='grey')  # HEREHEREHEREHERE
ent2 = tk.Entry(win, state='disabled')
ent3 = tk.Entry(win, state='disabled')
ent4 = tk.Entry(win, state='disabled')

mes = tk.Message(win, text=str(get_random_word()).upper(), bg='grey', font=('Dubai', 16, 'bold'), width=100)
mes1 = tk.Message(win, text=str(get_random_num()).upper(), bg='grey', font=('Dubai', 16, 'bold'), width=100)
mes2 = tk.Message(win, text=str(get_random_symbol()).upper(), bg='grey', font=('Dubai', 16, 'bold'), width=100)
label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=2, column=3)
label4.grid(row=5, column=1)
label5.grid(row=5, column=2)
label6.grid(row=5, column=3)
label7.grid(row=5, column=4)
label8.grid(row=4, column=1)
btn2.grid(row=12, column=1)
btn3.grid(row=1, column=5)
btn4.grid(row=3, column=5)
btn5.grid(row=12, column=5)
ent1.grid(row=6, column=1)
ent2.grid(row=6, column=2)
ent3.grid(row=6, column=3)
ent4.grid(row=6, column=4)
cb.grid(row=6, column=5)

mes.grid(row=1, column=1)
mes1.grid(row=1, column=3)
mes2.grid(row=3, column=3)

if __name__ == '__main__':
    win.mainloop()
    print(cb)
'''
'''import tkinter as tk
from main_body import *
from random import choice

a = MainList()
a.get_random_verb()
a.get_random_conj()


def get_random_verb(self):
    book = openpyxl.open('sample.xlsx', read_only=True)
    sheet = book.active
    res = choice([i for i in sheet.values])
    self.RAND_VERB_RES = res
    return res


def get_random_word():
    return choice(['above', 'below', 'upper', 'under', 'after', 'hitherto'])


def get_random_num():
    return choice(range(10))


def get_random_symbol():
    return choice(['!', '@', '#', '$'])


def rule_cb():
    for entry in [ent1, ent2, ent3, ent4]:
        if cb_var.get() == 1:
            entry.config(state='normal', bg='white')
        else:
            entry.config(state='disabled')


win = tk.Tk()
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.config(background='Grey')
win.title('SANSCRIT LANGUAGE TRAINER')
win.geometry('1600x800')
# win.minsize(500, 300)
# win.maxsize(900, 700)
win.resizable(True, True)
label1 = tk.Label(win, text='RANDOM VERB',
                  font=('Dubai', 14, 'bold'),
                  bg='grey',
                  padx=10,
                  pady=30,
                  width=15,
                  height=1)
label2 = tk.Label(win, text='HINT TRANSLATION',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label3 = tk.Label(win, text='HINT CONJUGATION FORM',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label4 = tk.Label(win, text='infinitive form',
                  bg='grey', font=('Dubai', 12, 'bold'))
label5 = tk.Label(win, text='base', bg='grey', font=('Dubai', 12, 'bold'))
label6 = tk.Label(win, text='translation', bg='grey', font=('Dubai', 12, 'bold'))
label7 = tk.Label(win, text='conjugation type', bg='grey', font=('Dubai', 12, 'bold'))
label8 = tk.Label(win, text='Enter new data', bg='grey', font=('Dubai', 16, 'bold'))
label9 = tk.Label(win, text='RANDOM CONJ', bg='grey', font=('Dubai', 16, 'bold'))
label10 = tk.Label(win, text=a.get_random_verb()[0], bg='grey', font=('Dubai', 16, 'bold'))
btn2 = tk.Button(win, text='SAVE DATA', activebackground='yellow', font=('Arial', 20, 'bold'))
btn3 = tk.Button(win, text='translation hint', activebackground='yellow', anchor='e', font=('Arial', 16, 'bold'))
btn4 = tk.Button(win, text='conjugation hint', activebackground='yellow', font=('Arial', 16, 'bold'))
btn5 = tk.Button(win, text='GENERATE', activebackground='yellow',
                 command=lambda: (
                     tk.Label(win, text=f'{a.get_random_verb()[0]}', bg=choice(['blue', 'grey', 'white', 'green']),
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=1)
                     ,
                     tk.Label(win, text=f'{a.get_random_conj()[0]}', bg=choice(['blue', 'grey', 'white', 'green']),width=20,
                              font=('Arial', 15, 'bold')).grid(row=4,
                                                               column=1),
                     tk.Label(win, text=f'{a.show_conjugation_hint()}', bg=choice(['blue', 'grey', 'white', 'green']),width=20,
                              font=('Arial', 15, 'bold')).grid(row=3,
                                                               column=3),tk.Label(win, text=f'{a.show_random_verb()[2:]}', bg=choice(['blue', 'grey', 'white', 'green']),width=20,
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=3)),
                 font=('Arial', 20, 'bold'))
cb_var = tk.IntVar()
cb_var.set(0)
cb = tk.Checkbutton(win, text='insert data', bg='grey', activebackground='grey', variable=cb_var, onvalue=1,
                    offvalue=0, command=rule_cb)

cb.deselect()
ent1 = tk.Entry(win, state='disabled', bg='grey')  # HEREHEREHEREHERE
ent2 = tk.Entry(win, state='disabled')
ent3 = tk.Entry(win, state='disabled')
ent4 = tk.Entry(win, state='disabled')

mes = tk.Label(win, text=f'{a.show_random_verb()[0]}', bg='grey', font=('Dubai', 16, 'bold'))
mes1 = tk.Label(win, text=f'{a.RAND_VERB_RES[2]}', bg='grey', font=('Dubai', 16, 'bold'))
mes2 = tk.Label(win, text=str(a.RAND_VERB_RES[3]), bg='grey', font=('Dubai', 16, 'bold'))
mes3 = tk.Label(win, text=str(a.get_random_conj()).split('\'')[1], bg='grey', font=('Dubai', 14, 'bold'))
label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=2, column=3)
label4.grid(row=5, column=1)
label5.grid(row=5, column=2)
label6.grid(row=5, column=3)
label7.grid(row=5, column=4)
label8.grid(row=4, column=4)
label9.grid(row=3, column=1)
label10.grid(row=10, column=10)
btn2.grid(row=12, column=1)
btn3.grid(row=1, column=5)
btn4.grid(row=3, column=5)
btn5.grid(row=12, column=5)
ent1.grid(row=6, column=1)
ent2.grid(row=6, column=2)
ent3.grid(row=6, column=3)
ent4.grid(row=6, column=4)
cb.grid(row=6, column=5)

mes.grid(row=1, column=1)
mes1.grid(row=1, column=3)
mes2.grid(row=3, column=3)
mes3.grid(row=4, column=1)

if __name__ == '__main__':
    win.mainloop()
    print(a.RAND_VERB_RES)
    print(a.RAND_CONJ_RES)
'''
'''import tkinter as tk
from main_body import *
from random import choice
from verb_body import *

a = MainList()
a.get_random_verb()
a.get_random_conj()


def get_random_verb(self):
    book = openpyxl.open('sample.xlsx', read_only=True)
    sheet = book.active
    res = choice([i for i in sheet.values])
    self.RAND_VERB_RES = res
    return res


def rule_cb():
    for entry in [ent1, ent2, ent3, ent4]:
        if cb_var.get() == 1:
            entry.config(state='normal', bg='white')
        else:
            entry.config(state='disabled')


def uncover_translation():
    if cb3_var.get() == 1:
        return 'black'
    else:
        return 'grey'

def uncover_conj():
    if cb4_var.get() == 1:
        return 'black'
    else:
        return 'grey'

win = tk.Tk()
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.config(background='Grey')
win.title('SANSCRIT LANGUAGE TRAINER')
win.geometry('1600x800')
# win.minsize(500, 300)
# win.maxsize(900, 700)
win.resizable(True, True)
ent1 = tk.Entry(win, state='disabled', bg='grey')  # HEREHEREHEREHERE
ent2 = tk.Entry(win, state='disabled')
ent3 = tk.Entry(win, state='disabled')
ent4 = tk.Entry(win, state='disabled')
label1 = tk.Label(win, text='RANDOM VERB',
                  font=('Dubai', 14, 'bold'),
                  bg='grey',
                  padx=10,
                  pady=30,
                  width=15,
                  height=1)
label2 = tk.Label(win, text='HINT TRANSLATION',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label3 = tk.Label(win, text='HINT CONJUGATION FORM',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label4 = tk.Label(win, text='infinitive form',
                  bg='grey', font=('Dubai', 12, 'bold'))
label5 = tk.Label(win, text='base', bg='grey', font=('Dubai', 12, 'bold'))
label6 = tk.Label(win, text='translation', bg='grey', font=('Dubai', 12, 'bold'))
label7 = tk.Label(win, text='conjugation type', bg='grey', font=('Dubai', 12, 'bold'))
label8 = tk.Label(win, text='Enter new data', bg='grey', font=('Dubai', 16, 'bold'))
label9 = tk.Label(win, text='RANDOM CONJ', bg='grey', font=('Dubai', 16, 'bold'))
btn2 = tk.Button(win, text='SAVE DATA', activebackground='yellow', font=(
    'Arial', 20, 'bold'),
                 command=a.add_data(ent1.get(), ent2.get(), ent3.get(), ent4.get()))
# btn3 = tk.Button(win, text='translation hint', activebackground='yellow', anchor='e', command=uncover_text,font=('Arial', 16, 'bold'))
cb3_var = tk.IntVar()
cb3 = tk.Checkbutton(win, text='translation hint', activebackground='yellow', anchor='e', command=uncover_translation,
                     font=('Arial', 16, 'bold'), bg='grey',variable=cb3_var, onvalue=1,offvalue=0)
cb3_var.set(0)
cb4_var = tk.IntVar()
cb4 = tk.Checkbutton(win, text='conjugation hint', font=('Arial', 16, 'bold'), bg='grey', variable=cb4_var, onvalue=1,
                     offvalue=0, command=uncover_conj)
cb4_var.set(0)
btn5 = tk.Button(win, text='GENERATE', activebackground='yellow',
                 command=lambda: (
                     tk.Label(win, text=f'{a.get_random_verb()[0]}'.strip(')('), bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=1)
                     ,
                     tk.Label(win, text=f'{a.get_random_conj()[0]}'.strip(')('), bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=4,
                                                               column=1),
                     tk.Label(win, fg=f'{uncover_conj()}'
                              , text=f'{a.show_conjugation_hint()}'.strip(')('), bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=3,
                                                               column=3),
                     tk.Label(win, text=f'{a.show_random_verb()[2:]}'.strip(')('), bg='grey', fg=f'{uncover_translation()}',width=20,
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=3)),
                 font=('Arial', 20, 'bold'))
cb_var = tk.IntVar()
cb_var.set(0)
cb = tk.Checkbutton(win, text='insert data', bg='grey', activebackground='grey', variable=cb_var, onvalue=1,
                    offvalue=0, command=rule_cb)

cb.deselect()

mes = tk.Label(win, text=f'{a.show_random_verb()[0]}', bg='grey', font=('Dubai', 16, 'bold'))
mes1 = tk.Label(win, text=f'{a.RAND_VERB_RES[2]}', bg='grey', font=('Dubai', 16, 'bold'))
mes2 = tk.Label(win, text=str(a.RAND_VERB_RES[3]), bg='grey', font=('Dubai', 16, 'bold'))
mes3 = tk.Label(win, text=str(a.get_random_conj()).split('\'')[1], bg='grey', font=('Dubai', 14, 'bold'))
label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=2, column=3)
label4.grid(row=5, column=1)
label5.grid(row=5, column=2)
label6.grid(row=5, column=3)
label7.grid(row=5, column=4)
label8.grid(row=4, column=4)
label9.grid(row=3, column=1)
btn2.grid(row=12, column=1)
cb3.grid(row=1, column=5)
cb4.grid(row=3, column=5)
btn5.grid(row=12, column=5)
ent1.grid(row=6, column=1)
ent2.grid(row=6, column=2)
ent3.grid(row=6, column=3)
ent4.grid(row=6, column=4)
cb.grid(row=6, column=5)

mes.grid(row=1, column=1)
mes1.grid(row=1, column=3)
mes2.grid(row=3, column=3)
mes3.grid(row=4, column=1)

if __name__ == '__main__':
    win.mainloop()
'''
"""tk.Label(win, fg=f'{uncover_conj()}'
                              , text=f'{a.show_conjugation_hint()}'.strip('()'), bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=3,
                                                               column=3),
                     tk.Label(win, text=f'{a.RAND_VERB_RES[-2]}', bg='grey', fg=f'{uncover_translation()}',
                              width=20,
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=3)),"""3



'''import tkinter as tk
from main_body import *
from random import choice
from verb_body import *
from database_body import *
from tkinter import ttk

a = MainList()
db = DataBase()


def rule_cb():
    for entry in [ent1, ent2, ent3, ent4]:
        if cb_var.get() == 1:
            entry.config(state='normal', bg='white')
        else:
            entry.config(state='disabled')


# def uncover_translation():
#     if cb3_var.get() == 1:
#         return 'black'
#     else:
#         return 'grey'


# def uncover_conj():
#     if cb4_var.get() == 1:
#         return 'black'
#     else:
#         return 'grey'


def add_data():
    with sq.connect('verb_base.db') as con:
        cur = con.cursor()
        if all(map(lambda x: bool(x), [ent1, ent2, ent3, ent4])):
            cur.execute(f"""INSERT INTO verb_base VALUES (
            '{ent1.get()}', '{ent2.get()}', '{ent3.get()}', '{ent4.get()}')""")
            for i in [ent1, ent2, ent3, ent4]:
                i.delete(0, 'end')
        con.commit()


win = tk.Tk()
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.config(background='Grey')
win.title('SANSCRIT LANGUAGE TRAINER')
win.geometry('1600x800')
# win.minsize(500, 300)
# win.maxsize(900, 700)
win.resizable(True, True)
ent1 = tk.Entry(win, state='disabled')  # HEREHEREHEREHERE
ent2 = tk.Entry(win, state='disabled')
ent3 = tk.Entry(win, state='disabled')
ent4 = tk.Entry(win, state='disabled')
label1 = tk.Label(win, text='RANDOM VERB',
                  font=('Dubai', 14, 'bold'),
                  bg='grey',
                  padx=10,
                  pady=30,
                  width=15,
                  height=1)
label2 = tk.Label(win, text='HINT TRANSLATION',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label3 = tk.Label(win, text='HINT CONJUGATION FORM',
                  bg='grey',
                  font=('Dubai', 14, 'bold'))
label4 = tk.Label(win, text='infinitive form',
                  bg='grey', font=('Dubai', 12, 'bold'))
label5 = tk.Label(win, text='base', bg='grey', font=('Dubai', 12, 'bold'))
label6 = tk.Label(win, text='translation', bg='grey', font=('Dubai', 12, 'bold'))
label7 = tk.Label(win, text='conjugation type', bg='grey', font=('Dubai', 12, 'bold'))
label8 = tk.Label(win, text='Enter new data', bg='grey', font=('Dubai', 16, 'bold'))
label9 = tk.Label(win, text='RANDOM CONJ', bg='grey', font=('Dubai', 16, 'bold'))
combo1 = ttk.Combobox(win, values=a.RAND_VERB_RES)
combo1.grid(column=3, row=1)
btn2 = tk.Button(win, text='SAVE DATA', activebackground='yellow', font=(
    'Arial', 20, 'bold'),
                 command=add_data)
# cb3_var = tk.IntVar()
# cb3 = tk.Checkbutton(win, text='translation hint', activebackground='yellow', anchor='e', command=uncover_translation,
#                      font=('Arial', 16, 'bold'), bg='grey', variable=cb3_var, onvalue=1, offvalue=0)
# cb3_var.set(0)
# cb4_var = tk.IntVar()
# cb4 = tk.Checkbutton(win, text='conjugation hint', font=('Arial', 16, 'bold'), bg='grey', variable=cb4_var, onvalue=1,
#                      offvalue=0, command=uncover_conj)
# cb4_var.set(0)
btn5 = tk.Button(win, text='GENERATE', activebackground='yellow',
                 command=lambda: (
                     tk.Label(win, text=f'{a.get_random_verb()[0]}', bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=1,
                                                               column=1)
                     ,
                     tk.Label(win, text=f'{a.get_random_conj()[0]}', bg='grey', width=20,
                              font=('Arial', 15, 'bold')).grid(row=4,
                                                               column=1), ttk.Combobox(win, values=f'{a.show_conjugation_hint()}', width=20,
                                                                                       font=('Arial', 15, 'bold')).grid(
                         row=3,
                         column=3),
                     ttk.Combobox(win, values=f'{a.RAND_VERB_RES[-2]}',
                                  width=20,
                                  font=('Arial', 15, 'bold')).grid(row=1,
                                                                   column=3)), font=('Arial', 20, 'bold'))
cb_var = tk.IntVar()
cb_var.set(0)
cb = tk.Checkbutton(win, text='insert data', bg='grey', activebackground='grey', variable=cb_var, onvalue=1,
                    offvalue=0, command=rule_cb)

cb.deselect()

# mes = tk.Label(win, text=f'{a.get_random_verb()[0]}123', bg='grey', font=('Dubai', 16, 'bold'))
# mes1 = tk.Label(win, text=f'{a.get_random_verb()[1]}456', bg='grey', font=('Dubai', 16, 'bold'))
# mes2 = tk.Label(win, text=str(a.get_random_verb()[2]), bg='grey', font=('Dubai', 16, 'bold'))
# mes3 = tk.Label(win, text=str(a.get_random_conj()).split('\'')[1], bg='grey', font=('Dubai', 14, 'bold'))
label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=2, column=3)
label4.grid(row=5, column=1)
label5.grid(row=5, column=2)
label6.grid(row=5, column=3)
label7.grid(row=5, column=4)
label8.grid(row=4, column=4)
# label9.grid(row=3, column=1)
btn2.grid(row=12, column=1)
# cb3.grid(row=1, column=5)
# cb4.grid(row=3, column=5)
btn5.grid(row=12, column=5)
ent1.grid(row=6, column=1)
ent2.grid(row=6, column=2)
ent3.grid(row=6, column=3)
ent4.grid(row=6, column=4)
cb.grid(row=6, column=5)

# mes.grid(row=1, column=1)
# mes1.grid(row=1, column=3)
# mes2.grid(row=3, column=3)
# mes3.grid(row=4, column=1)

if __name__ == '__main__':
    win.mainloop()
    # v = Verb('1', '2', '3', '4')
    # a.add_data(v)
    print(a.get_random_verb())
'''