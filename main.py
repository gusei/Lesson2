import  tkinter as tk

win=tk.Tk()
win.title('Address Entry Form')

from_form=tk.Frame(relief=tk.SUNKEN,borderwidth=3)
from_form.pack()
labels=[
    'Имя',"фамилия:",'Адрес1','Адрес2','Город','Регион','Почтовый индекс','Страна',]
# Цикл для списка ярлыков полей.
for idx,text in enumerate(labels):
    label=tk.Label(master=from_form,text=text)
    entry=tk.Entry(master=from_form,width=50)
    label.grid(row=idx,column=0,sticky='e')
    entry.grid(row=idx,column=1)

win.mainloop()