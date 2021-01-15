from tkinter import *
from tkinter.ttk import Treeview

sos = ['110','120']
root = Tk()
root.title('小林智能基金计算工具V1.0.1')
root.geometry('560x360')
text = Text(root)
text.place(rely=0,relheight=1)

text.insert(END,'CESHISHUJU %s'%sos)
root.mainloop()