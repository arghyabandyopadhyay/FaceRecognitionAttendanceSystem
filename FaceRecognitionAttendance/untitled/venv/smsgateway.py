import twilio
import twilio.rest
from tkinter import *
from twilio.rest import Client
import pandas as pd




def add():
    a=x1.get()
    b=x2.get()
    c=t1.get("1.0",'end-1c')
    print(a,b,c)
    print(type(b))
    #p=open("C:/Project7thsem/untitled/studentdetails/"+a+b+".txt","w")
    #p.write(c)
    #p.close()
    df = pd.read_csv("C:/FaceRecognitionAttendance/untitled/StudentDetails/StudentDetails.csv")
    Id=0;
    while TRUE:
        Id = Id + 1;
        aa = df.loc[df['ID'] == Id][df['Branch'] == a]['Name'].values
        bb = df.loc[df['ID'] == Id][df['Branch'] == a]['Branch'].values
        cc = df.loc[df['ID'] == Id][df['Branch'] == a]['Sem'].values
        dd = df.loc[df['ID'] == Id][df['Branch'] == a]['Mobile'].values
        #twillo client key, refer to twillo website
        client = Client("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        test1 = df.loc[df['ID'] == Id]['ID'].values
        try:
            int(test1)
        except TypeError:
            break
        try:
            test = aa[0]
        except IndexError:
            continue


        if str(int(cc[0])) == b:
            mobileno="+91"+str(int(dd[0]))
            client.messages.create(to=mobileno,
                                   from_="+12014935178",
                                   body="Hello,"+str(aa[0])+" of branch "+str(bb[0])+" semester= "+str(cc[0])+"   "+c)




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
l3=Label(text="Message to be sent")
l3.pack()
t1=Text(height=20)
t1.pack()
b1=Button(text="Send Message",command=add)
b1.pack()
mainloop()
