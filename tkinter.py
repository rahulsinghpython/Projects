import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainwindow = tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry("640x480+8+400") #using it to shift pixels at the end


label = tkinter.Label(mainwindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainwindow, relief="raised", borderwidth=1)
canvas.pack(side="left", fill= tkinter.Y) # make it fill the whole left side
# canvas.pack(side="left", fill= tkinter.X, expand=True) #lets say it doesnt cover


leftframe = tkinter.Frame(mainwindow)
leftframe.pack(side='left', anchor='n', fill= tkinter.Y, expand=False)

rightframe = tkinter.Frame(mainwindow)
rightframe.pack(side='right', anchor='n', fill= tkinter.Y, expand=True)


button1 = tkinter.Button(rightframe, text="button1")
button2 = tkinter.Button(rightframe, text="button2")
button3 = tkinter.Button(rightframe, text="button3")
button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='n')





mainwindow.mainloop() # let tk take over the loop


