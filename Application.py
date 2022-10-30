from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
list=[]
gst=[]
gross=[]
def add():
    j=access()
    a=open("sales.txt","a")
    z=open("inventory.txt","a")
    data=Lb.get(ACTIVE)
    if data=='Pencil          5/-':
        b=qnt.get()
        if (b)>=j["Pencil"]:
            messagebox.showinfo("Oops","Not enough stock")
        else:
            tb.insert(END,'\nPencil\t5/- x %d'%(b))
            list.append(5*qnt.get())
            gst.append(0.18*5*b)
            gross.append(5*qnt.get()+0.18*5*b)
            a.write("Pencil"+"\n")
            a.write(str(qnt.get())+"\n")
            z.write('Pencil'+"\n")
            z.write(str(-b)+"\n")

    elif data=='Eraser          10/-':
        b=qnt.get()
        if (b)>=j["Eraser"]:
            messagebox.showinfo("Oops","Not enough stock")
        else:   
            tb.insert(END,'\nEraser\t10/- x %d'%(qnt.get()))
            list.append(10*qnt.get())
            gst.append(0.18*10*b)
            gross.append(10*qnt.get()+0.18*10*b)
            a.write("Eraser"+"\n")
            a.write(str(qnt.get())+"\n")
            z.write('Eraser'+"\n")
            z.write(str(-b)+"\n")
        
    elif data=='Sharpener     15/-':
        b=qnt.get()
        if (b)>=j["Sharpener"]:
            messagebox.showinfo("Oops","Not enough stock")
        else:
            tb.insert(END,'\nSharpener\t15/- x %d'%(qnt.get()))
            list.append(15*qnt.get())
            gross.append(15*qnt.get()+0.18*15*b)
            gst.append(0.18*15*b)
            a.write("Sharpener"+"\n")
            a.write(str(qnt.get())+"\n")
            z.write('Sharpener'+"\n")
            z.write(str(-b)+"\n")
            
    elif data=='Ruler             10/-':
        b=qnt.get()
        if (b)>=j["Ruler"]:
            messagebox.showinfo("Oops","Not enough stock")
        else:
            tb.insert(END,'\nRuler\t10/- x %d'%(qnt.get()))
            list.append(10*qnt.get())
            gross.append(10*qnt.get()+0.18*10*b)
            gst.append(0.18*10*b)
            a.write("Ruler"+"\n")
            a.write(str(qnt.get())+"\n")
            z.write('Ruler'+"\n")
            z.write(str(-b)+"\n")
    elif data=='Glue             20/-':
        b=qnt.get()
        if (b)>=j["Glue"]:
            messagebox.showinfo("Oops","Not enough stock")
        else:
            tb.insert(END,'\nGlue\t20/- x %d'%(qnt.get()))
            list.append(20*qnt.get())
            gst.append(0.18*20*b)
            gross.append(20*qnt.get()+0.18*20*b)
            a.write("Glue"+"\n")
            a.write(str(qnt.get())+"\n")
            z.write('Glue'+"\n")
            z.write(str(-b)+"\n")

def total():
    messagebox.showinfo("Hello %s"%(nameinfo.get()),"Amount to be paid: Rs. %d/-"%(sum(list)))
    messagebox.showinfo("Hello %s"%(nameinfo.get()),"GST applied: Rs. %d/-"%(sum(gst)))
    messagebox.showinfo("Hello %s"%(nameinfo.get()),"Total Amount to be paid: Rs. %d/-"%(sum(gross)))
    

def clr():
    tb.delete(1.0,END)
    list.clear()
    
f=Tk()
f.title("Billing")

nameinfo=StringVar()
data=IntVar()
qnt=IntVar()


name=Label(f,text='Name :')
e1=Entry(f,width=15,bd=3,textvariable=nameinfo)


prod=Label(f,text='Products :',bd=3)
Lb=Listbox(f,height=7,width=15,bd=3)
Lb.insert(0,'Items          Price\n')
Lb.insert(1,'Pencil          5/-')
Lb.insert(2,'Eraser          10/-')
Lb.insert(3,'Sharpener     15/-')
Lb.insert (4,'Ruler             10/-')
Lb.insert (5,'Glue             20/-')

def inventory():
    a=Toplevel(f)
    a.title("Inventory")
    b4=Button(a, text="ok",width=12, bd=3,command=a.withdraw )
    b=Entry(a,width=15,bd=3)
    c=Entry(a,width=15,bd=3)
    l1=Label(a,text="Name of Item",bd=3)
    m1=Label(a,text="Quantity",bd=3)
    def nexts():
        l.append(b.get()+"\n")
        l.append(c.get()+"\n")
        m=open("inventory.txt","a+")
        for j in range(0,len(l)):
            m.write(l[j])
        m.close()
        b.delete(0,END)
        c.delete(0,END)
    b5=Button(a, text="next",width=12,bd=3, command=nexts )
    l=[]
    b.grid(row=1,column=1,padx=5,pady=5)
    l1.grid(row=1,column=0,padx=5,pady=5)
    m1.grid(row=2,column=0,padx=5,pady=5)
    c.grid(row=2,column=1,padx=5,pady=5)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
def graph():
            q=graph1()
            plt.title("Share of sales in terms of quantity")
            plt.pie(q.values(),labels=q.keys(),autopct='%1.1f%%')
            plt.show()
quan=Label(f,text='Quantity :')
e2=Entry(f,width=15,bd=3,textvariable=qnt)


b1=Button(f,text='Add Items',width=12,bd=3,command=add)
tb=Text(f,height=5,width=20,bd=3)
b3=Button(f,text='Clear Items',width=12,bd=3,command=clr)
scrollb = Scrollbar( command=tb.yview)
tb['yscrollcommand'] = scrollb.set

b2=Button(f,text='Total',width=12,bd=3,command=total)
b6=Button(f, text="inventory",width=12,bd=3, command=inventory )
b7=Button(f,text="Sales graph",width=12,bd=3 ,command=graph)

name.grid(row=0,column=0,padx=5,pady=5)
e1.grid(row=0,column=1,padx=5,pady=5)
prod.grid(row=1,column=0,padx=5,pady=5)
Lb.grid(row=1,column=1,padx=5,pady=5)
quan.grid(row=2,column=0,padx=5,pady=5)
e2.grid(row=2,column=1,padx=5,pady=5)
b1.grid(row=3,column=1,padx=5,pady=5)
tb.grid(row=4,columnspan=2,padx=5,pady=5)
b3.grid(row=5,column=0,padx=5,pady=5)
b2.grid(row=5,column=1,padx=5,pady=5)
b6.grid(row=6,column=0,padx=5,pady=5)
b7.grid(row=6,column=1,padx=5,pady=5)
scrollb.grid(row=4, column=2, sticky='nsew')


def duplicate(l):
        l1=[]
        for i in l:
                if i not in l1:
                        l1.append(i)
        return l1
    
def access():
    l=[]
    m=[]
    f=[]
    k=[]
    a=open("inventory.txt","r")
    b=a.readlines()
    for i in range(0,len(b)):
        b[i]=b[i].rstrip('\n')
    for i in range(0,len(b)):
        if i%2==0:
                l.append(b[i])
        else:
                m.append(b[i])
    for i in range(len(l)):
        c=l[i]
        d=0
        for j in range(len(l)):
            if l[j]==c:
                d=d+int(m[j])
                l[j].replace("!","l[j]")
            else:
                continue
        k.append(d)
        f.append(c)
        f1=duplicate(f)
        k2=duplicate(k)
    j=dict()
    for i in range(len(f)):
        j[f[i]]=k[i]
    print(j)
    return j
def terminate():
    print("ok")
def graph1():
    l=[]
    m=[]
    f=[]
    k=[]
    a=open("sales.txt","r")
    b=a.readlines()
    for i in range(0,len(b)):
        b[i]=b[i].rstrip('\n')
    for i in range(0,len(b)):
        if i%2==0:
                l.append(b[i])
        else:
                m.append(b[i])
    for i in range(len(l)):
        c=l[i]
        d=0
        for j in range(len(l)):
            if l[j]==c:
                d=d+int(m[j])
                l[j].replace("!","l[j]")
            else:
                continue
        k.append(d)
        f.append(c)
        f1=duplicate(f)
        k2=duplicate(k)
    j=dict()
    for i in range(len(f)):
        j[f[i]]=k[i]
    print(j)
    return j

f.mainloop()
