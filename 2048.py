from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("2048")

x0 = 25
y0 = 100

# Définit la taille des cases en pixels
case_width = 80
case_height = 80
espacement = 10  # Espacement entre les cases

numbers = [[2, 4, 8, 16],
           [32, 64, 128, 256],
           [512, 1024, 2048, 512]]

case = [[None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]]


# Création des cases avec espacement
for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        case[line][col] = Label(window, text=numbers[line][col], width=10, height=3, borderwidth=1, relief="solid",
                            font=("arial", 15), bg="red")
        case[line][col].place(x=x0 + (case_width + espacement) * col, y=y0 + (case_height + espacement) * line)









# Titre du jeu
frameTitre = Frame(window)
frameTitre.pack(fill=X, padx=15)

titre = Label(frameTitre, text="2048", font=("Arial", 20))
titre.pack(fill=X)

window.mainloop()
