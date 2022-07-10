import tkinter
from tkinter import *
from tkinter import messagebox

import  main as pc


root=Tk()
root.title("Phone Contact")


def Buttom1():

    win=Toplevel(root)
    win.title("Search for a Phone")
    win.geometry("438x128")
    lb1=Label(win,text="Enter The number:")
    lb1.grid(row=1)
    inputfile=Entry(win,width=50)
    inputfile.grid(row=1,column=1)
    buttom6=Button(win,text="Done",width=10,padx=10,pady=10,command=lambda : DoneBt(inputfile,win))
    buttom6.grid(row=3,column=3)
    buttom6.place(relx=0.5, rely=0.5, anchor=CENTER)




def DoneBt(inputfile,win):
    phone_num=inputfile.get()
    if len(phone_num) != 10 :
        messagebox.showerror("Error", "This is invalid number")
    elif pc.getName(phone_num) is None:
        messagebox.showerror("Sorry", "the number is not found\n ")
    else:
        messagebox.showinfo("Name",f"The name of this Number is {pc.getName(phone_num)}")
        win.withdraw()



def Buttom2():
    win = Toplevel(root)
    win.title("Add Contact")
    win.geometry("438x128")
    lb2=Label(win,text="Enter the name:")
    lb2.grid(row=1)
    inputfile1 = Entry(win, width=25)
    inputfile1.grid(row=1, column=1)
    lb1 = Label(win, text="Enter The number:")
    lb1.grid(row=2)
    inputfile2=Entry(win, width=25)
    inputfile2.grid(row=2, column=1)
    buttom6 = Button(win, text="Done", width=10, padx=10, pady=5,command=lambda: Donebt2(inputfile1,inputfile2,win))
    buttom6.grid(row=3, column=3)
    buttom6.place(relx=0.5, rely=0.5, anchor=CENTER)


def Donebt2(name,num,win):
    name=name.get()
    phone=num.get()
    if pc.getName(phone) is None and len(phone) == 10:
        pc.AddContact(phone,name)
        messagebox.showinfo("Contact Add","You add the contact")
        win.withdraw()
    elif pc.getName(phone) is not None:
        messagebox.showerror("Error","The phone number is already in your contact")
    else:
        messagebox.showerror("Error","Please write the number correctly (10 digits)")




def Buttom3():
    win = Toplevel(root)
    win.title("Phone Contact")
    win.geometry("438x128")
    Lb1 = Listbox(win,width=438,height=128)
    number=1
    for num, names in pc.phone_contact.items():
        Lb1.insert(number,f"name: {names} Phone Number: {num}\n")
        Lb1.grid(row=number)
        number=number+1
    buttom9 = Button(win, text="Done", width=10, padx=10, pady=5, command=win.withdraw)





def Buttom4():
    win = Toplevel(root)
    win.title("Search for a Contact")
    win.geometry("438x128")
    lb1 = Label(win, text="Enter The name:")
    lb1.grid(row=1)
    inputfile = Entry(win, width=50)
    inputfile.grid(row=1, column=1)
    buttom6 = Button(win, text="Done", width=10, padx=10, pady=10, command=lambda: DoneBt2(inputfile,win))
    buttom6.grid(row=3, column=3)
    buttom6.place(relx=0.5, rely=0.5, anchor=CENTER)


def  DoneBt2(name,win):
    name=name.get()
    found = False
    for key, value in pc.phone_contact.items():
        if name.lower() == value.lower():
            messagebox.showinfo("Done",f"name:{value} phone:{key}")
            found = True
            win.withdraw()


    if found is False:
        messagebox.showerror("Error","the contact is not found ")


def exit():
    root.quit()

    # myFrame = Frame(win,width=438,height=128)
    # myFrame.grid(row=1)
    # for num, names in pc.phone_contact.items():
    #     Label(myFrame,text="\n").grid(row=1)
    #     Label(myFrame, text=f"name: {names} Phone Number: {num}\n").grid(row=1)






buttom1=Button(root,text="Search for a name by Phone",width=20,padx=10,pady=10,command=Buttom1)
buttom2=Button(root,text="Add Contact",width=20,padx=10,pady=10,command=Buttom2)
buttom3=Button(root,text="Display your Phone Contact",width=20,padx=10,pady=10,command=Buttom3)
buttom4=Button(root,text="Search for contact ",width=20,padx=10,pady=10,command=Buttom4)
buttom5=Button(root,text="Exit",width=20,padx=10,pady=10,command=exit)






buttom1.grid(row=0,column =1)
buttom2.grid(row=0,column =2)
buttom3.grid(row=0,column =3)
buttom4.grid(row=0,column =4)
buttom5.grid(column = 0, row = 1, columnspan = 10,sticky="nesw")






root.mainloop()
