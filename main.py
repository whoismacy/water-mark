"A Simple word watermark for Images"
from tkinter import Canvas, Entry, Tk, PhotoImage, Label, Button, messagebox
from PIL import Image, ImageFont, ImageDraw


def extract_name(file_path):
    """return name of the image_file"""
    return list(filter(lambda x: '.' in x, file_path.split("/")))[0].\
        split('.')[0]


def process_image():
    """function that gets called once the process button is clicked
    it adds the watermark to the image."""
    file_path = fp_input.get()
    wm_content = watermark_e.get().upper()

    if file_path:
        if wm_content:
            try:
                with Image.open(file_path).convert("RGBA") as base:
                    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.tt\
f", 60)
                    d = ImageDraw.Draw(txt)
                    d.text((10, 10), wm_content, font=fnt, fill=(12, 255,
                                                                 23, 90))
                    out = Image.alpha_composite(base, txt)
                    out.save(f"{extract_name(file_path)}.png")
            except (FileNotFoundError, ValueError,  TypeError,
                    IsADirectoryError):
                messagebox.showerror(title="Invalid File Path", message="Prov\
ide correct absolute path")
        else:
            messagebox.showerror(title="Empty Watermark", message="Watermark M\
essage cannot be empty !!")
    else:
        messagebox.showerror(title="Empty File Path", message="File Path cann\
ot be empty !!")


window = Tk()
window.title("Image add WaterMark")
window.minsize(height=600, width=600)
window.config(padx=100, pady=100)

FONT = ("Courier", 20, "bold")

# Orange-cup creating the photo image
orange_cup = PhotoImage(file="orange_cup.png")

# Creating the image canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=orange_cup)
canvas.grid(column=1, row=0)

# file path label
fp_label = Label(text="File path: ", font=FONT)
fp_label.grid(column=0, row=1)

# file path input
fp_input = Entry(width=35)
fp_input.grid(column=1, row=1, columnspan=1)
fp_input.focus()

# watermark text
watermark = Label(text="Text to add to Image: ", font=FONT)
watermark.grid(column=0, row=2)

# watermark entry
watermark_e = Entry(width=35)
watermark_e.grid(column=1, row=2, columnspan=1)

# file path button
fp_submit = Button(text="Process", command=process_image)
fp_submit.grid(column=2, row=2)


def quit_prog():
    "quits from the program"
    window.quit()


# exit from the program
exit_button = Button(text="Exit", command=quit_prog, width=50)
exit_button.grid(column=0, row=3, columnspan=3)

# Keep the window open
window.mainloop()
