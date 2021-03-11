from tkinter import *
import csv
import random

root=Tk()
root.title("kockice")

label=Label(root, text="Dice roller")
label.grid(row=0, column=0, columnspan=5)

e1=Entry(root, width=10)
e2=Entry(root, width=10)
e3=Entry(root, width=10)
e4=Entry(root, width=10)
e5=Entry(root, width=10)

e1.grid(row=1, column=0)
e2.grid(row=1, column=1)
e3.grid(row=1, column=2)
e4.grid(row=1, column=3)
e5.grid(row=1, column=4)

count=1

def roll1():
    r=random.randint(1, 6)
    s=str(r)
    e1.delete(0, END)
    e1.insert(0, s)

def roll2():
    r=random.randint(1, 6)
    s=str(r)
    e2.delete(0, END)
    e2.insert(0, s)

def roll3():
    r=random.randint(1, 6)
    s=str(r)
    e3.delete(0, END)
    e3.insert(0, s)

def roll4():
    r=random.randint(1, 6)
    s=str(r)
    e4.delete(0, END)
    e4.insert(0, s)

def roll5():
    r=random.randint(1, 6)
    s=str(r)
    e5.delete(0, END)
    e5.insert(0, s)

def save():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    f=e5.get()

    
      
    with open('kockice.csv', mode='a') as csv_file:
        kockice_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    

        kockice_writer.writerow([count, a, b, c, d, f])
    csv_file.close()
    
def clicked():
    
    global count

    count=count+1
  

def roll_all():
    roll1()
    roll2()
    roll3()
    roll4()
    roll5()
    save()
    clicked()

button1=Button(root, text="Roll", command=roll_all, padx=146)
button1.grid(row=2, column=0, columnspan=5)

root.mainloop()
    
    
    


    
    
    


    

