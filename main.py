from tkinter import *
import pyqrcode
# PIL allows for QR Code to be saved as png
from PIL import ImageTk, Image

# Generate QR Code
def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(175,400,window=image_label)

# Create Window
root = Tk()

canvas = Canvas(root,width=350,height=600)
canvas.pack()

app_label = Label(root,text="QR Code Generator",fg='blue',font=("Arial",20))
canvas.create_window(175,50,window=app_label)

# Name Label + Entry
name_label = Label(root,text="Link Name")
canvas.create_window(175,100,window=name_label)
name_entry = Entry(root)
canvas.create_window(175,120,window=name_entry)

# Link Label + Entry
link_label = Label(root,text="Link")
canvas.create_window(175,140,window=link_label)
link_entry = Entry(root)
canvas.create_window(175,160,window=link_entry)

# Generate Button
button = Button(text="Generate QR Code",command=generate)
canvas.create_window(175,200,window=button)

root.mainloop()