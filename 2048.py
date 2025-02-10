# Auteur : Dylan Pinto Davide
# Names  : 2048.py
# Dates  : 10.02.2025

from tkinter import *
from random import choice, randint

window = Tk()
window.geometry("550x550")
window.title("2048")

x0 = 50
y0 = 90

# Définit la taille des cases en pixels
case_width = 100
case_height = 100
espacement = 10  # Espacement entre les cases

# Grille initiale du jeu avec des 0
numbers = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Liste des objets de case pour afficher les valeurs à l'écran
case = [[None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]]

# Couleurs pour chaque valeur
color = {
    0: "white",
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

# Fonction pour afficher les cases avec leurs valeurs à l'écran
def display_game():
    for line in range(len(case)):
        for col in range(len(case[line])):
            case[line][col].config(text=str(numbers[line][col]), bg=color[numbers[line][col]])


# Création des cases avec les couleurs appropriées
for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        case[line][col] = Label(window, text=str(numbers[line][col]), bg=color[numbers[line][col]], width=10, height=3, borderwidth=1, relief="solid", font=("arial", 15))
        case[line][col].place(x=x0 + (case_width + espacement) * col, y=y0 + (case_height + espacement) * line)



# Fonction pour ajouter une nouvelle tuile de 2 à un emplacement vide
def add_new_tile():#aide de chat gpt
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if numbers[i][j] == 0]
    if empty_tiles:
        i, j = choice(empty_tiles)  # Choisir un emplacement vide au hasard
        numbers[i][j] = 2  # Placer une tuile de valeur 2
    display_game()



def pack_4(a, b, c, d):
    nums = [a, b, c, d]

    # Compléter avec des zéros à la fin
    nums += [0] * (4 - len(nums))

    # Fusionner les cases égales
    for i in range(3):
        if nums[i] == nums[i + 1] and nums[i] != 0:
            nums[i] *= 2
            nums[i + 1] = 0
            break

    # Réorganiser les cases après la fusion (enlever les zéros restants)
    nums = [num for num in nums if num != 0]
    nums += [0] * (4 - len(nums))

    return nums[0], nums[1], nums[2], nums[3]



# Fonction pour déplacer et fusionner les cases d'une ligne vers la gauche
def move_left(event=None):
    global numbers

    # Appliquer la fonction pack4 à chaque ligne
    for i in range(4):
        numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3] = pack_4(numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3])

    # Ajouter une nouvelle tuile après un déplacement
    add_new_tile()

    display_game()



# Fonction pour déplacer et fusionner les cases d'une ligne vers la droite
def move_right(event=None):
    global numbers

    # Appliquer la fonction pack_4 à chaque ligne, après inversion
    for i in range(4):
        # Inverser la ligne pour que le mouvement soit de droite à gauche
        numbers[i] = numbers[i][::-1]
        numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3] = pack_4(numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3])
        # Réinverser la ligne après le déplacement
        numbers[i] = numbers[i][::-1]

    # Ajouter une nouvelle tuile après un déplacement
    add_new_tile()

    display_game()



# Fonction pour déplacer et fusionner les cases d'une colonne
def move_haut(event=None):
    global numbers

    # Appliquer la fonction pack_4 à chaque colonne
    for col in range(4):
        nums = [numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]]
        nums = pack_4(*nums)
        for i in range(4):
            numbers[i][col] = nums[i]

    add_new_tile()
    display_game()



# Fonction pour déplacer et fusionner les cases d'une colonne vers le bas
def move_bas(event=None):
    global numbers

    # Appliquer la fonction pack_4 à chaque colonne
    for col in range(4):
        nums = [numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]]
        nums = pack_4(*nums)
        for i in range(4):
            numbers[3-i][col] = nums[i]

    add_new_tile()
    display_game()

# Fonction des touches
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_haut)
window.bind("<Down>", move_bas)

#réinitialiser le jeu
def new_game():
    global numbers
    numbers = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    add_new_tile()
    add_new_tile()
    display_game()

# Ajouter deux tuiles de départ
new_game()

# Titre du jeu
frameTitre = LabelFrame(window)
frameTitre.pack(fill=X, padx=15)

frameBoutons = LabelFrame(window)
frameBoutons.pack(fill=X)

titre = Label(frameTitre, text="2048", bg="#DA70FA", font=("Arial", 20))
titre.pack(fill=X)

labelScore = Label(frameBoutons, text="score :", font=("Arial", 15))
labelScore.pack(side=LEFT, padx=80)

boutonNEW = Button(frameBoutons, text="NOUVEAU", command=new_game)
boutonNEW.pack(side=RIGHT, padx=80)

window.mainloop()
