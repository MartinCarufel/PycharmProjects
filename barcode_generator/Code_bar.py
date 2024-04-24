import tkinter
from io import BytesIO
from barcode.codex import Code128
from barcode.writer import SVGWriter
from barcode.writer import ImageWriter, BaseWriter
from PIL import Image, ImageTk
from tkinter import *
from datetime import date


# b = Code128("2024-05-18", writer=ImageWriter())
# img = b.render()
# im = Image.open(img, )
# im.show()



render_opt = {"font_size":4,
              "module_width":0.12,
              "module_height":4,
              "text_distance":2}
# ImageWriter.set_options({"font_size":6},)

with open("codebar_file.svg", 'wb') as f:
    pass
    # bar = Code128("2024-05-18").write(f)
    # bar = Code128("2024-05-18", writer=ImageWriter).write(f)

# following create a file
with open("this_file.png", "wb") as f:
    Code128(date.today().strftime("%Y-%m-%d"), writer=ImageWriter()).write(f)

    # This line create Pillow type image "img"
img = Code128(date.today().strftime("%Y-%m-%d"), writer=ImageWriter()).render(writer_options=render_opt)
# Save the rendered image
img.save("img.png")

root = Tk()

# set the app geometry as per image size get by the property size of the pillow object and format
# it in text to pass to the tkinter geometry property
root.geometry("{}x{}".format(img.size[0], img.size[1]))

# Generate Tk image
label_img = ImageTk.PhotoImage(img)
label1 = tkinter.Label(image=label_img)
label1.pack()
# img.show()

root.mainloop()
