
from tkinter import *
def add():
    a=x1.get()
    b=x2.get()
    c=t1.get("1.0",'end-1c')
    p=open("C:/FaceRecognitionAttendance/untitled/studentdetails/"+a+b+".txt","w")
    p.write(c)
    p.close()
    print("A")

root=Tk()
l1=Label(text="Select Branch")
l1.pack()
l1=["CSE","IT"]
x1=StringVar()
c1=OptionMenu(root,x1,*l1)
c1.pack()
l2=Label(text="Select Semester")
l2.pack()
l2=["1","2","3","4","5","6","7","8"]
x2=StringVar()
c2=OptionMenu(root,x2,*l2)
c2.pack()
l3=Label(text="Assignment")
l3.pack()
t1=Text(height=20)
t1.pack()
b1=Button(text="SAVE",command=add)
b1.pack()
mainloop()
