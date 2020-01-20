import sqlite3
from tkinter import *
from tkinter import messagebox

from bs4 import BeautifulSoup

conn = sqlite3.connect("medicos.db")


def indexar():
    try:
        conn.execute("""DROP TABLE IF EXISTS RESPUESTA""")
        conn.execute("""DROP TABLE IF EXISTS TEMA""")
        conn.execute('''create table RESPUESTA(
                    id            integer  not null primary key,
                    fechaHora     datetime not null,
                    texto         text     not null,
                    temaOrigen_id integer  not null
                        references TEMA
                            deferrable initially deferred
                );''')

        conn.execute('''
                    create table TEMA(
            id              integer not null primary key,
            titulo          text    not null,
            numRespuestas   integer not null,
            ultimaRespuesta date,
            category        text    not null
        );''')

        messagebox.showinfo("Éxito", "Se ha indexado con éxito")
    except:
        messagebox.showerror("Error", "Se ha producido un error al indexar")


def getElement(text, tag, clase):
    soup = BeautifulSoup(text, "html.parser")
    return soup.find_all(tag, class_=clase)


def getElementNoClass(text, tag):
    soup = BeautifulSoup(text, "html.parser")
    return soup.find_all(tag)



def listadoNoticias():
    try:
        temas = conn.execute('''SELECT * FROM TEMA WHERE TEMA.CATEGORY = 'Noticia' ''')
    except:
        messagebox.showerror("Error", "Se ha intentado buscar noticias sin haber indexado antes.")
    if (temas.rowcount == -1):
        messagebox.showwarning("Warning",
                               "Actualmente no existen artículos para listar. Dele a indexar noticias y artículos antes de hacer click sobre buscar")
    else:
        mensaje = "Se ha completado la instrucción de forma correcta, guardando " + str(temas.rowcount) + " temas"
        messagebox.showinfo("Éxito", mensaje)

    return temas


def listadoArticulos():
    try:
        temas = conn.execute('''SELECT * FROM TEMA WHERE TEMA.CATEGORY = 'Articulo' ''')
    except:
        messagebox.showerror("Error", "Se ha intentado buscar noticias sin haber indexado antes.")
    if (temas.rowcount == -1):
        messagebox.showwarning("Warning",
                               "Actualmente no existen artículos para listar. Dele a indexar noticias y artículos antes de hacer click sobre buscar")
    else:
        mensaje = "Se ha completado la instrucción de forma correcta, guardando " + str(temas.rowcount) + " temas"
        messagebox.showinfo("Éxito", mensaje)

    return temas


def ventana():
    root = Tk()
    menubar = Menu(root)
    firstMenu = Menu(menubar, tearoff=0)
    firstMenu.add_command(label="Indexar", command=indexar)
    firstMenu.add_separator()
    firstMenu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Inicio", menu=firstMenu)

    articlesMenu = Menu(menubar, tearoff=0)
    articlesMenu.add_command(label="Listado de noticias", command=listadoNoticias)
    articlesMenu.add_command(label="Listado de artículos", command=listadoArticulos)
    menubar.add_cascade(label="Listar", menu=articlesMenu)

    root.config(menu=menubar)
    root.mainloop()


if __name__ == '__main__':
    ventana()
