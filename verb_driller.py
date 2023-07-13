import tkinter as tk
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
win.geometry('1200x600+60+10')
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


label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=2, column=3)
label4.grid(row=5, column=1)
label5.grid(row=5, column=2)
label6.grid(row=5, column=3)
label7.grid(row=5, column=4)
label8.grid(row=4, column=4)
btn2.grid(row=12, column=1)

btn5.grid(row=12, column=5)
ent1.grid(row=6, column=1)
ent2.grid(row=6, column=2)
ent3.grid(row=6, column=3)
ent4.grid(row=6, column=4)
cb.grid(row=6, column=5)



if __name__ == '__main__':
    win.mainloop()

