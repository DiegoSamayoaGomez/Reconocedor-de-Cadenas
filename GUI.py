from tkinter import *
from automata.fa.dfa import DFA
from DFA import arranca
from PIL import Image, ImageTk

#Función para botones sin programar
def btn_clicked():
    print("Botón 2")

#Envío de entrada de texto a DFA    
def enviarDFA():
    canvas.itemconfig(Canv, text="\t"+arranca(entry1.get()))

def abrirIMGNFA():
    global my_image2
    text_box.config(state='normal')
    text_box.delete('1.0', END)
    text_box.config(state='disabled')
    my_image2 = PhotoImage(file=f"NFAIMG.png")
    text_box.image_create(END, image=my_image2)
    
def abrirIMGDFA():
    global my_image
    text_box.config(state='normal')
    text_box.delete('1.0', END)
    text_box.config(state='disabled')
    my_image = PhotoImage(file=f"DFAImg.png")
    text_box.image_create(END, image=my_image)

def abrirIMGMinDFA():
    global my_image
    text_box.config(state='normal')
    text_box.delete('1.0', END)
    text_box.config(state='disabled')
    my_image = PhotoImage(file=f"MinDFA.png")
    text_box.image_create(END, image=my_image)
   
def nuevo():   
    text_box.config(state='normal')
    text_box.delete('1.0', END)
    entry1.delete(0,END)
    text_box.config(state='disabled')

#Función que abre ventana de Información
def informacionGUI():
    ventanaInformacion = Toplevel()
    ventanaInformacion.title("Información")
    ventanaInformacion.geometry("700x400")  
    c=Canvas(ventanaInformacion,
    bg="#ffffff",
    height=700,
    width=400)
    filename=PhotoImage(file = f"background_1.png")
    background_label=Label(ventanaInformacion,image=filename)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    ventanaInformacion.resizable(False, False)
    ventanaInformacion.mainloop()

#Inicio de interfaz 2
window = Tk()
window.title("Reconocedor de cadenas")

#Dimensiones de ventana
window.geometry("880x550")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 550,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    440.0, 87.0,
    image=background_img)

#Mostrar aceptación o rechazo de cadena de prueba
Canv = canvas.create_text(
    350.0, 160.5,
    text = "",
    fill = "#000000",
    font = ("Roboto", int(14.0)))

#TextBox 1
entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    362.0, 121.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)   

entry0.place(
    x = 14, y = 109,
    width = 696,
    height = 23)
regex = "((0|1|2|3|4|5|6|7|8|9)|(0|1|2|3|4|5|6|7|8|9)+)|((Cv|CV)|(Vc|VC)|((Cv|CV)(cv|Cv|cV|CV)+))|((Vc|VC)(vc|Vc|vC|VC)+)"
entry0.insert(0, regex)
entry0.configure(state=DISABLED)

#TextBox - Ingreso de cadena de pruebas
entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    362.0, 195.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 14, y = 183,
    width = 696,
    height = 23)

#Salida de Texto

#----------------
message ='''Bienvenido

Seleccione una opción para comenzar:
1.Puede ingresar su cadena de prueba en el apartado de "Cadena de prueba" y compruebe
su resultado.
2.El botón "?" le ayudará a encontrar información adicional.
3.El botón "AFND" mostrará el autómata AFND con transiciones vacías gráficamente.
4.El botón "AFD-Reducido" mostrará el autómata AFD reducido (Método del árbol) gráficamente.
5.El botón "AFD" mostrará el autómata AFND (algoritmo de Thompson) gráficamente.

Gracias y saludos
'''

text_box = Text(
    window,
    height=12,
    width=40
)
text_box.insert('end', message)

text_box.pack(expand=True)
text_box.config(state='disabled')
text_box.place(
   x = 16, y = 269,
   width = 840,
   height = 270)

#Botón Comprobar
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = enviarDFA,
    relief = "flat")

b0.place(
    x = 741, y = 134,
    width = 121,
    height = 49)

#Botón AFND
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = abrirIMGNFA,
    relief = "flat")

b1.place(
    x = 14, y = 220,
    width = 115,
    height = 32)

#Botón AFND-Reducido
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = abrirIMGMinDFA,
    relief = "flat")

b2.place(
    x = 147, y = 220,
    width = 115,
    height = 32)

#Botón para información
img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = informacionGUI,
    relief = "flat")

b3.place(
    x = 811, y = 17,
    width = 45,
    height = 45)

#Botón para DFA
img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = abrirIMGDFA,
    relief = "flat")

b4.place(
    x = 280, y = 220,
    width = 115,
    height = 32)

#Botón Nuevo
img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = nuevo,
    relief = "flat")

b5.place(
    x = 413, y = 220,
    width = 115,
    height = 32)

#Permitir maximizar pantalla
window.resizable(False, False)

#Fin de Interfaz
window.mainloop()