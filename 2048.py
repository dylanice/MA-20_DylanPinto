"""
name: 21048.py
auteur: dylan pinto davide
date: 27.01.2025
"""



from cProfile import label
from tkinter import *
from tkinter import Label

window = Tk()
window.geometry("550x550")
window.title("2048")

x0 = 50
y0 = 90

# Définit la taille des cases en pixels
case_width = 100
case_height = 100
espacement = 10  # Espacement entre les cases

numbers = [[2, 4, 8, 16],
           [32, 64, 128, 256],
           [512, 1024, 2048, 512],
            [0, 0, 0, 0]]

#numbers = [[2, 0, 0, 0],
           #[0, 0, 2, 0],
           #[0, 0, 0, 0],
            #[0, 0, 0, 0]]



case = [[None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]]

color = {
    0:"white",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#8C4E03",
    256: "#0FC2C0",
    512: "#2A8C82",
    1024: "#4CA4FF",
    2048: "#EDC22E"
}


def display_game():
    for line in range(len(case)):
        for cole in range(len(case[line])):
            case[line][cole].config(case,
                                     text=numbers[line][cole],
                                     bg=color[numbers[line][cole]]
                                     )
    return

# Création des cases avec espacement
for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        case[line][col] = Label(window, text=numbers[line][col], bg=color[numbers[line][col]], width=10, height=3, borderwidth=1, relief="solid", font=("arial", 15))
        case[line][col].place(x=x0 + (case_width + espacement) * col, y=y0 + (case_height + espacement) * line)


# Titre du jeu
frameTitre = LabelFrame(window)
frameTitre.pack(fill=X, padx=15,)

frameBoutons=LabelFrame(window)
frameBoutons.pack(fill=X,)

titre = Label(frameTitre, text="2048",bg="#DA70FA", font=("Arial", 20))
titre.pack(fill=X)

labelScore=Label(frameBoutons, text="score :", font=("Arial", 15))
labelScore.pack(side=LEFT,padx=80)

boutonNEW=Button(frameBoutons,text="NOUVEAU")
boutonNEW.pack(side=RIGHT,padx=80)


window.mainloop()
