from tkinter import *

informacionTK = Tk()

informacionTK.title("Información")
informacionTK.geometry("700x400")
informacionTK.configure(bg = "#ffffff")
canvas = Canvas(
    informacionTK,
    bg = "#ffffff",
    height = 400,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_1.png")
background = canvas.create_image(
    350.0, 188.0,
    image=background_img)

informacionTK.resizable(False, False)
informacionTK.mainloop()
