from tkinter import *
from PIL import Image

master = Tk()


def openfile():
    v = StringVar()
    filename = filedialog.askopenfilename()
    lt = Label(master,textvariable=v).grid(row=0,column=3)
    v.set(filename)
    return filename


    
variable = StringVar()
variable.set(".jpg")


l1 = Label(master ,text="路径").grid(row=0,column=0)
Button(master,text="打开文件",command=openfile).grid(row=0, column=1)


l2 = Label(master,text="选择图片格式").grid(row=1,column=0)
w = OptionMenu(master,variable,".jpg",".png",".gif",".bmp")
w.grid(row=1,column=1)

l3 = Label(master,text="图片尺寸").grid(row=2,column=0)
lw = Label(master,text="宽").grid(row=2,column=1)
ew = Entry(master)
ew.grid(row=2,column=2)
lh = Label(master,text="高").grid(row=2,column=3)
eh = Entry(master)
eh.grid(row=2,column=4)

l4 = Label(master,text="保存路径").grid(row=3,column=0)

def savefile():
    filename = openfile()
    im = Image.open(filename)
    file = filename.split('.')
    file = file[0]+variable.get()
    width = int(ew.get())
    height = int(eh.get())
    out = im.resize((width,height),Image.ANTIALIAS)
    out.save(file,variable.get()[1:])
    return True
    
btn = Button(master,text="ok",command=savefile).grid(row=4,column=0)
mainloop()



