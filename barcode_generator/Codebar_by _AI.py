import tkinter as tk
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
from barcode.codex import Code128


def generate_barcode():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Generate barcode

    code128 = barcode.codex.Code128(current_date, writer=ImageWriter())
    # barcode_image = code128(current_date, writer=ImageWriter())

    # Save barcode image
    # barcode_image.save('barcode')
    code128.save('barcode')

    # Display barcode image in Tkinter window
    image = tk.PhotoImage(file='barcode.png')
    label = tk.Label(root, image=image)
    label.image = image
    label.pack()


# Create a Tkinter window
root = tk.Tk()
root.title("Date Barcode")

# Generate and display barcode
generate_barcode()

# Start the Tkinter event loop
root.mainloop()