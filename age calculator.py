from tkinter import *
from datetime import  date


root = Tk()

root.title('Age Calculator')
root.geometry('800x600+200+100')
root.resizable(False,False)
root.configure(bg = 'gray')
image_icon = PhotoImage(file ='Age calculator  .png')
age_calculator = Label(root, image = image_icon,bg = 'gray')

age_calculator.place(x=250, y=15)

def calculate():
    today = date.today()
    birthday = date (int(entery_year.get()),int(entery_month.get()),int(entery_day.get()))
    age = today.year - birthday.year - ((today.month,today.day) < (birthday.month,birthday.day))
    Label(text = f'{enteryName.get()} your age is {age} years old',font= 'arial 15 italic',bg = 'gray',fg = 'green').place(x=250,y = 450)


label_name = Label(root,text = 'Name',font = 'arial 23',bg = 'gray')
label_name.place(x= 100, y = 250)
label_name = Label(root,text = 'Year',font = 'arial 23',bg = 'gray')
label_name.place(x= 100, y = 300)
label_name = Label(root,text = 'Month',font = 'arial 23',bg = 'gray')
label_name.place(x= 100, y = 350)
label_name = Label(root,text = 'Day',font = 'arial 23',bg = 'gray')
label_name.place(x= 100, y = 400)

enteryName = StringVar()
enteryYear = StringVar()
enteryMonth= StringVar()
enteryDay = StringVar()

entery_name = Entry(root,textvariable = enteryName,font='arial 15',fg = 'black',border = 3)
entery_name.place(x=250, y = 250)
entery_year = Entry(root,textvariable = enteryYear,font='arial 15',fg = 'black',border = 3)
entery_year.place(x=250, y = 300)
entery_month = Entry(root,textvariable = enteryMonth,font='arial 15',fg = 'black',border = 3)
entery_month.place(x=250, y = 350)
entery_day = Entry(root,textvariable = enteryDay,font='arial 15',fg = 'black',border = 3)
entery_day.place(x=250, y = 400)

button = Button(root,text = 'Calculate Age',fg = 'gray',bg = 'black',activebackground = 'black',font = 'arial 15 bold',width = 13,command = calculate)
button.place(x = 300,y = 500)


root.mainloop()