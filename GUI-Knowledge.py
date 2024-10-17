from tkinter import *
from tkinter import ttk  #ธีมของ TK
from tkinter import messagebox

GUI = Tk() #สร้างหน้าต่าง หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อหน้าต่าง
GUI.geometry('500x400') #ขนาดหน้าต่าง

L1 = Label (GUI,text='โปรแกรทบันทึกความรู้',font=('Angsana New',30), fg ='green')
L1.place(x=30,y=30)

#B1 = ttk.Button(GUI,text='เงินมีอยู่เท่าไร (B1)') #สร้างปุ่ม จากธีม TK
#B1.pack(ipadx=20,ipady=20) #จัดตำแหน่งให้ปุ่มอยู่ บน กลาง (ขนาดปุ่ม)

###########

def Button2():
    text = 'มีแค่ 30 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
    #messagebox.showwarning('เงินในบัญชี',text)

FB1 = LabelFrame(GUI,text='การเงิน')
FB1.place (x=100,y=100)         
B2 = ttk.Button(FB1,text='เงินมีอยู่เท่าไร (B2)',command=Button2)
B2.pack(ipadx=5,ipady=5,padx=5,pady=5)

############

#B2 = Button(GUI,text='เงินมีอยู่เท่าไร') #สร้างปุ่ม
#B2.pack() #จัดตำแหน่งให้ปุ่มอยู่ บน กลาง




GUI.mainloop()
