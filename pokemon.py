
import Users\maxil\OneDrive\Documents\spécial\Pokémon Judgement Desolation\Pokémon DD\commun\objets script/learnables.py

# création d'un objet Calamous
class Calamous:
    #définition de son type et de si c'est un pokémon
    pokemon = True
    type_ = "Water"
    # définition de ses talents et de son genre (qui seront random)
    abilities = "Multicule" or "Glissade" or "Protéen"
    gender = "M" or "F"
    # création de ses niveaux
    levels = 1
    exp = 0
    needexp = 30
    lootexp = 10
    difupgexp = 3
    # création de la possibilité de monter de niveau
    if adverse = 0:
        exp = exp + lootexp * difupgexp
        if levels = 1 and exp = needexp:
            levels = 2
            needexp = 70
            exp = 0
    if adverse = 0:
        exp = exp + lootexp * difupgexp
        if exp = needexp:
            levels = levels + 1
            needexp = needexp * 2
            exp = 0
    
    # définition de ses stats
    hp = 50
    atq = 35
    df = 40
    spa = 60
    spd = 30
    spe = 60
    pre = 1
    esc = 1

    # définition de l'apparence et des capacités qu'il pourra apprendre
    appearence = ('C:\Users\maxil\OneDrive\Documents\spécial\Pokémon Judgement Desolation\Pokémon DD\commun/assets\personnages\Poké-avant/Pouposorusse')
    learnables = 

    # définition de valeurs plus cachées
    happiness = 0

    # création de la possibilité de monter certaines d'entre elles
    if adverse = 0:
        happiness = happiness + 0.1
    
    # description du pokédex
    desc = "Ce pokémon ne peut pas vivre hors de l'eau : sa peau sèche dès qu'elle est déshydratée trop longtemps"