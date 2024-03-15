import tkinter as tk

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    fenetre = tk.Tk()
    canvas = tk.Canvas(fenetre, width = 256, height = 256, bg = "black")
    for i in canvas:
        for j in canvas:
            canvas[i, j] = tk.Canvas(fenetre, bg = color)
    return canvas

draw_pixel(4, 4, "white")


fenetre = tk.Tk()
fenetre.title("tk")
canvas = tk.Canvas(fenetre, width = 256, height = 256, bg = "black")
canvas.grid(row = 0, rowspan = 3, column = 1)
boutton_aléatoire = tk.Button(fenetre, text = "Aléatoire")
boutton_aléatoire.grid(row = 0, column = 0)
boutton_degradegris = tk.Button(fenetre, text = "Dégradé gris")
boutton_degradegris.grid(row = 1, column = 0)
boutton_degrade2D = tk.Button(fenetre, text = "Dégradé 2D")
boutton_degrade2D.grid(row = 2, column = 0)

fenetre.mainloop()