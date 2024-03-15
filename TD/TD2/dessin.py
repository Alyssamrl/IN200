import tkinter as tk
import random

canvas_largeur = 300
canvas_longueur = 300

color = "blue"
def choisircouleur():
    global color 
    color = input("Quelle couleur voulez-vous ?")

def cercle():
    x = random.randint(50, canvas_largeur-50)
    y = random.randint(50, canvas_longueur-50)
    canvas.create_oval(x-50, y+50, x+50, y-50, fill = "blue")

def carre():
    x = random.randint(50, canvas_largeur-50)
    y = random.randint(50, canvas_longueur-50)
    canvas.create_rectangle(x, y, x+100, y+100, fill = "red")

def croix():
    x = random.randint(50, canvas_largeur-50)
    y = random.randint(50, canvas_longueur-50)
    canvas.create_line(x-50, y, x+50, y, fill = "yellow", width = 25)
    canvas.create_line(x, y+50, x, y-50, fill = "yellow", width = 25)

fenetre = tk.Tk()
fenetre.title("Mon dessin")
canvas = tk.Canvas(fenetre, width = 300, height = 300, bg = "black")
canvas.grid(row = 1, rowspan = 3, column = 1)

boutton_couleur = tk.Button(fenetre, text = "Choisir une couleur", command = choisircouleur)
boutton_couleur.grid(row = 0, column = 1)
boutton_cercle = tk.Button(fenetre, text = "Cercle", command = cercle)
boutton_cercle.grid(row = 1, column = 0)
boutton_carre = tk.Button(fenetre, text = "Carré", command = carre)
boutton_carre.grid(row = 2, column = 0)
boutton_croix = tk.Button(fenetre, text = "Croix", command = croix)
boutton_croix.grid(row = 3, column = 0)

boutton_undo = tk.Button(fenetre, text = "Choisir une couleur")

objects = []
def demi_cercle():
    x = random.randint(50, canvas_largeur-50)
    y = random.randint(50, canvas_longueur-50)
    objects.append(canvas.create_oval(x-50, y+50, x+50, y-50, fill = "blue"))

def demi_rectangle():
    x = random.randint(50, canvas_largeur-50)
    y = random.randint(50, canvas_longueur-50)
    objects.append(canvas.create_rectangle(x, y, x+100, y+100, fill = "red"))







fenetre.mainloop()