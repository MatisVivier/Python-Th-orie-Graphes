def pref(mot):  #fonction préfixe
    lst = []  #stock les préfixes
    for i in range(len(mot)+1):  #ajout du préfixe dans la liste (premier préfixe = 0)
        lst.append(mot[0:i]) 
    return lst

def suf(mot):  #fonction suffixe
    lst = []
    for i in range(len(mot)+1):
        lst.append(mot[i:len(mot)+1])  #suffixe obtenu en prenant les caractères de la chaine jusqu'à la fin de la chaine
    return lst

def fact(mot):  #fonction facteurs
    lst = []
    for i in range(len(mot)+1):  #boucle imbriquer de la chaine
        for j in range(len(mot)+1): #definit la fin de la chaine
            lst.append(mot[i:j])  
    lst = list(set(lst)) #elimination des doublons de la liste en la convertissant en un ensemble
    return lst

def miroir(mot):
    return mot[::-1]  #prend tout les caracteres de la chaine dans le sens inverse

def concatene(l1, l2):
    lst = []
    for m1 in l1:  
        for m2 in l2:  #boucle qui itére sur chaque élément m2 dans la liste l2
            lst.append(m1+m2)  #ajout de la concaténation de m1 et m2 à la liste lst
    lst = list(set(lst))  # elimination des doublons
    return lst

def puis(l1, puissance): 
    lst = l1[:]  #initialisser avec une copie de la liste l1 (permet de modifier l1 pendant son éxecution)
    lst2 = []
    for i in range(puissance-1): #boucle for qui itére sur les puissance de 1 à puissance -1  
        for m1 in l1:
            for m2 in lst:
                lst2.append(m1+m2)
        lst = list(set(lst2))
    return lst

def tousmots(l1, lim):  
    lst = l1[:]
    for i in range(lim): #de 0 à lim-1
        for j in lst:
            lst2 = [j]  #initialisation de lst2 avec j
            lst3 = concatene(lst, lst2) #concaténation de la lst avec lst2
            for k in lst3:  #boucle qui itére sur chaque élement de k dans lst3
                if len(k) <= lim:  #vérif que longueur de k est inférieur ou égale a lim
                    lst.append(k) 
    lst.append('')  #ajout d'une chaine vide à la fin de lst
    lst = list(set(lst))
    return lst

def defauto():  #permet de faire la saisie d'un automate
    #initialisation
    alphabet = []
    etat = []
    transitions = []
    ini = []
    f = []
    #demande à l'utilisateur
    nombre = int(input("Entrer le nombre de lettre de l'alphabet : "))
    for i in range(nombre):
        lettre = str(input("Lettre "+ str(i+1) + " : "))
        alphabet.append(lettre)
    nbEtat= int(input("Entrer le nombre d'états de l'automate: "))
    for i in range(nbEtat):
        etat.append(i)
    print("Nous allons à présent entrer les transitions \n")
    fin = 1
    while(fin != 0):
        transition = []
        depart = -1
        while (depart not in etat):
            depart = int(input("Entrer l'état de départ : "))
        transition.append(depart)
        trans = 0
        while (trans not in alphabet):
            trans = str(input("Entrer la lettre de transition : "))
        transition.append(trans)
        final = -1
        while(final not in etat):
            final = int(input("Entrer l'état de final : "))
        transition.append(final)
        fin = int(input("Entrer une autre transition ? 0 pour non, autre chiffre pour oui : "))
        transitions.append(transition)
    fin = 1
    while(fin != 0):
        initial = -1
        while(initial not in etat):
            initial = int(input("Entrer un état initial : "))
        ini.append(initial)
        fin = int(input("Entrer un autre état initial ? 0 pour non, autre chiffre pour oui : "))
    fin = 1
    while(fin != 0):
        final = -1
        while(final not in etat):
            final = int(input("Entrer un état final : "))
        f.append(final)
        fin = int(input("Entrer un autre état final ? 0 pour non, autre chiffre pour oui : "))
    auto ={"alphabet":alphabet,"etats": etat,
           "transitions":transitions,
           "I":ini,"F":f}
    return auto

def lirelettre(t, e, a): 
    lst = []
    for depart, lettre, fin in t:  #boucle sur les transition de l'automate t, en récupérant pour chaque, le départ, la lettre et la fin
        if depart in e:  # verifie si l'etat de départ fait partie des états de e
            if lettre == a: #vérifie si la lette lue est égale à a
                lst.append(fin) #si les deux sont vraie, alors ajout de l'état d'arrivée de lst
    lst = list(set(lst))
    return lst

def liremot(T, E, m):
    lst = E  
    for lettre in m: #boucle sur les lettre du mot m, en utilisant lire lettre
        lst = lirelettre(T, lst, lettre)
    return lst

def accepte(auto, m):
    #recup des transitions de l'automate auto dans la variable ...
    T = auto['transitions']
    E = auto['I']
    F = auto['F']
    lst = liremot(T, E, m) #recup la liste des états ateints apres avoir lu le mot m
    for etat in lst:  #pour chaque etat apres avoir lu le mot m
        if etat in F:  #si etat est final
            return True
    return False

def langage_accepte(auto, n):
    lst = tousmots(auto["alphabet"], n)  #initialisation avec tous les mots possibles de longueur inf ou égale
    lst2 = []
    for mot in lst:
        if (accepte(auto, mot)):  #verif l'automate avec (accepte). si accepté, alors dans lst
            lst2.append(mot)
    return lst2

def deterministe(auto):
    if (len(auto["I"]) > 1): #verif si l'automate a plus d'un etat initial
        return False
    for etat in auto["etats"]:  #parcourt touts les état de l'automate, verifie si y'a plusieurs transitions possible avec meme lettre
        lst = []
        for depart, lettre, fin in auto["transitions"]: #verif si la transition partant de l'état correspond à la lettre déja présente dans lst
        #si oui, cela signifie qu'il y a plusieurs transitions possibles avec la meme lettre donc false
            if lettre == '':
                return False
            if depart == etat:
                if lettre in lst:
                    return False
                lst.append(lettre)
    return True

#Fonction permettant de définir si un état d'un automate est déterministe ou non
def deterministe_etat(auto, etat):
    lst = []
    for depart, lettre, fin in auto["transitions"]:
         if lettre == '':
             return False
         if depart == etat:
             if lettre in lst:
                 return False
             lst.append(lettre)
    return True

def determinise(auto):
    #On vérifie si l'automate est déjà déterministe ou non
    if deterministe(auto):
        return auto
    
    #on initialise les nouvelles valeurs de l'automate déterministe
    alphabet = auto["alphabet"]
    etats = auto["etats"]
    ini = auto["I"]
    f = auto["F"]
    transitions = []
    nouveau_etat = []
    
    #On parcourt tous les états de l'automate
    for etat in auto["etats"]:
        transition = []
        lst = []
        
        #On parcourt toutes les transitions
        for depart, lettre, fin in auto["transitions"]:
            if depart == etat:
                transition = []
                transition.append(depart)
                transition.append(lettre)
                
                #Si l'état actuel est déjà déterministe on ne touche à rien
                if (deterministe_etat(auto, etat)):
                    transition.append(fin)
                    transitions.append(transition)
                    
                #Sinon on met dans une liste les états qui vont former un nouvel état    
                else:
                    lst.append(fin)
                    
        #On finalise la nouvelle transition avec le nouvel état créée
        if (not deterministe_etat(auto, etat)):
            transition.append(lst)
            nouveau_etat.append(lst)
            etats.append(lst)
            transitions.append(transition)
            
    #On va ajouter les transitions des nouveaux états en les parcourant
    for etat1, etat2 in nouveau_etat:
        n_etat = [etat1, etat2]
        
        #On ajoute le nouvel état parmi l'état final si c'en est un
        for final in auto["F"]:
            if ((etat1 == final or etat2 == final)and n_etat not in f):
                f.append(n_etat)
                
        #On parcourt l'alphabet et on ajoute les transitions du nouvel automate
        for lettre in auto["alphabet"]:
            transition = []
            lst=[etat1]
            lst2=[etat2]
            t = lirelettre(auto["transitions"], lst, lettre)
            t2 = lirelettre(auto["transitions"], lst2, lettre)
            t3 = list(set(t+t2))
            if (len(t3) > 0):
                transition.append(n_etat)
                transition.append(lettre)
                transition.append(t3)
                transitions.append(transition)
    
    #On crée l'automate déterministe
    auto_det ={"alphabet":alphabet,"etats": etats,
           "transitions":transitions,
           "I":ini,"F":f}
    return auto_det

def renommage(auto):
    #initialisation
    etats = auto["etats"]
    ini = auto["I"]
    f = auto["F"]
    transitions = auto["transitions"]
    modif = {}
    for i in range(len(etats)): #si un etat posse un nom different de son indice (0 et nbr d'état) on l'ajoute dans le dico modif avec comme clé le nom dé létat et son indice
        if (etats[i] != i):  #modif du nom des etats en utilisant les indices
            modif[str(etats[i])] = i
            etats[i] = i
    for i, (depart, lettre, fin) in enumerate(transitions): #parcourt les transitions de l'automate. 
        if str(depart) in modif.keys():
            depart = modif[str(depart)]
        if str(fin) in modif.keys():
            fin = modif[str(fin)]
        transitions[i] = (depart, lettre, fin)
    for j, initial in enumerate(ini):  #parcourt les états initiaux et si un état a été modifié on met a jour la liste des états initiaux
        if str(initial) in modif.keys():
            ini[j] = modif[str(initial)]
    for k, final in enumerate(f):  #parcourt tous les états finaux et si un état a été modifié on met à jour la liste des états finaux
        if str(final) in modif.keys():
            f[k] = modif[str(final)]
    auto_ren ={"alphabet":auto["alphabet"],"etats": etats,
           "transitions":transitions,
           "I":ini,"F":f}  #création d'un nouvel automate avec les composant modifié
    return auto_ren

def complet(auto):
    for etat in auto["etats"]:  #parcourt tous les états de l'automate
        switch = False  #init a false et sera modifier à true si une transition sortant est trouvée a partir de cet état
        for depart, lettre, fin in auto["transitions"]:
            if depart == etat:
                switch = True
                break
        if not switch:  #verifie si switch est restée a false pour l'état en question. Si c'est le cas, il n'est pas complet et donc retourne false
            return False

    for etat in auto["etats"]:  #parcourt à nouveau les états de l'automate
        for lettre in auto["alphabet"]:  
            if not lirelettre(auto["transitions"], [etat], lettre):  #verif s'il existe une transition sortant. Si pas trouvé, il n'est pas complet et return false
                return False

    return True  #si toutes les verif passent, il est bien complet


def complete(auto):
    if complet(auto):  #verif si l'automate entrée est deja complet
        return auto
    #initialisation
    etats = auto["etats"][:]
    ini = auto["I"]
    f = auto["F"]
    transitions = auto["transitions"][:]
    nouveau_etat = len(etats)  #création d'un nouvel etat qui n'appartient pas déjà à la liste d'états de l'automate en entrée
    while nouveau_etat in etats:
        nouveau_etat += 1
    etats.append(nouveau_etat)
    
    #verif pour chaque état de l'automate en entrée si il y a une transition sortante
    #si ce n'est pas le cas, on ajoute une transition pour chaque lettre de l'alphabet de l'état courant vers le nouvel état crée (nouveau_etat)
    for etat in etats:
        switch = False
        for depart, lettre, fin in transitions:
            if depart == etat:
                switch = True
                break
        if not switch:
            for lettre in auto["alphabet"]:
                transition = []
                transition.append(etat)
                transition.append(lettre)
                transition.append(nouveau_etat)
                transitions.append(transition)

    #verif pour chaque etat si il y a une transition sortant
    #si ce n'est pas le cas on ajoute une transition depuis l'état courant vers le nouvel état crée pour chaque lettre manquante
    for etat in etats:
        for lettre in auto["alphabet"]:
            if not lirelettre(transitions, [etat], lettre):
                transition = []
                transition.append(etat)
                transition.append(lettre)
                transition.append(nouveau_etat)
                transitions.append(transition)
    
    #création nouvel automate complet avec les listes modifiée
    auto_comp ={"alphabet":auto["alphabet"],"etats": etats,
           "transitions":transitions,
           "I":ini,"F":f}
    return auto_comp

def complement(auto):
    # Compléter l'automate
    auto_comp = complete(auto)
    
    # Inverser les états acceptants et non acceptants
    etats = auto_comp["etats"]
    ini = auto_comp["I"]
    f = []
    for etat in etats:
        if etat not in auto_comp["F"]:
            f.append(etat)
    
    # Créer le nouvel automate
    auto_comp = {"alphabet": auto_comp["alphabet"],
                 "etats": etats,
                 "transitions": auto_comp["transitions"],
                 "I": ini,
                 "F": f}
    
    return auto_comp


def inter(auto1, auto2):
    # Vérification des automates d'entrée
    if (not deterministe(auto1) or not deterministe(auto2)):
        raise ValueError("Les automates doivent être déterministes")
    if (auto1["alphabet"] != auto2["alphabet"]):
        raise ValueError("Les automates doivent avoir le même alphabet")
    
    # Initialisation des variables
    alphabet = auto1["alphabet"][:]
    etats = []
    transitions = []
    f = []
    ini = [(auto1["I"][0], auto2["I"][0])]
    
    # Création de l'ensemble des nouveaux états
    for etat1 in auto1["etats"]:
        for etat2 in auto2["etats"]:
            etat = (etat1, etat2)
            if etat1 in auto1["F"] and etat2 in auto2["F"]:
                f.append(etat)
    
    # Création des nouvelles transitions
    for depart, lettre, fin in auto1["transitions"]:
        for depart2, lettre2, fin2 in auto2["transitions"]:
            if lettre == lettre2:
                transition = []
                transition.append((depart, depart2))
                transition.append(lettre)
                transition.append((fin, fin2))
                if transition not in transitions:
                    transitions.append(transition)
                    if ((depart, depart2) not in etats and (fin, fin2) not in etats):
                        etats.append((depart, depart2))
                        etats.append((fin, fin2))
    
    auto_res = {
        "alphabet": alphabet,
        "etats": etats,
        "transitions": transitions,
        "I": ini,
        "F": f
    }
    
    return auto_res


def difference(auto1, auto2):
    # Compléter les automates
    comp1 = complete(auto1)
    comp2 = complete(auto2)
    compl_auto2 = complement(comp2)

    # Calcul de l'intersection entre auto1 et compl_auto2
    inter_auto = inter(comp1, compl_auto2)

    auto_res = {
        "alphabet": inter_auto["alphabet"],
        "etats": list(set(inter_auto["etats"])),
        "transitions": inter_auto["transitions"],
        "I": [inter_auto["I"]],
        "F": inter_auto["F"]
    }

    return auto_res

#fonction qui détermine si un automate est accessible
def accessible(auto):
    # Initialisation des états accessibles
    accessibles = [auto['I'][0]]
    for i in range(2):
        for etat in auto["etats"]:
            if etat not in accessibles:
                for depart, lettre, fin in auto["transitions"]:
                    for access in accessibles:
                        if (depart == access and fin == etat and fin not in accessibles):
                            accessibles.append(fin)
        
    # Vérification si tous les états sont accessibles
    for etat in auto['etats']:
        if etat not in accessibles:
            return False
    return True

#fonction qui détermine si un automate est coaccessible
def coaccessible(auto):
    # Initialisation des états coaccessibles
    coaccessibles = []
    for final in auto['F']:
        coaccessibles.append(final)
    
    for etat in auto["etats"]:
        for lettre in auto["alphabet"]:
            lst = lirelettre(auto["transitions"], [etat], lettre)
            for coaccess in coaccessibles:
                if coaccess in lst:
                    if (etat not in coaccessibles):
                        coaccessibles.append(etat)             
        
    # Vérification si tous les états sont coaccessibles
    for etat in auto['etats']:
        if etat not in coaccessibles:
            return False
    return True

#fonction qui détermine si un automate est émondé
def émondé(auto):
    if (accessible(auto) and coaccessible(auto)):
        return True
    return False

#fonction qui effectue l'algorithme de Moore en séparant les différents états
def separe_min(auto):
    if (not complet(auto) or not deterministe(auto)):
        raise ValueError("L'automate doit être déterministe et complet")
        
    #on initialise les listes et un dictionnaire
    separe = []
    first = []
    sec = []
    dico = {}
    
    #On sépare dans la liste separe les états terminaux des autres
    for etat in auto["etats"]:
        if etat in auto["F"]:
            first.append(etat)
        else:
            sec.append(etat)
    separe.append(first)
    separe.append(sec)
    
    #On ajoute dans un dictionnaire : les clé sont les états et les valeurs sont les états qu'ils transitionnent
    for etat in auto["etats"]:
        lst = []
        for depart, lettre, fin in auto["transitions"]:
            if depart == etat:
                lst.append(fin)
        dico[etat] = lst
    
    #On sépare les états avec l'algorithme de Moore (on effectue 10 fois la boucle pour être sûr)
    for x in range(10):
        for i in range(len(separe)):
            suppr = []
            for j in range(len(separe[i])-1):
                for y in range(2):
                    for liste in separe:
                        if dico[separe[i][j]][y] in liste:
                            if dico[separe[i][j+1]][y] not in liste:
                                lst = [separe[i][j]]
                                suppr.append(separe[i][j])
                                if (lst not in separe):
                                    separe.append(lst)
            suppr = list(set(suppr))
            for etat in suppr:
                separe[i].remove(etat)
                
    return separe

def minimise(auto):
    etats = separe_min(auto) 
    ini = []
    f = []
    transitions = []
    for initial in auto["I"]:  #parcourt tous les état initiaux de auto
        for etat in etats:
            if initial in etat:  #si etat init appartient a etat, alors on ajout etat a la liste "ini"
                ini.append(etat) 
    for final in auto["F"]: #parcourt tous les états finaux de auto
        for etat in etats:
            if final in etat:  #si etat final appartient à la classe etat, alors on ajoute etat a f
                if (etat not in f):
                    f.append(etat)
    for depart, lettre, fin in auto["transitions"]:
        for etat in etats:
            lst = []
            if depart in etat:  #si depart appartient a etat, alors etat dans lst
                lst.append(etat)
                lst.append(lettre)
                for etat2 in etats:
                    if (fin in etat2): #si etat fin appartient a etat2, alors etat2 dans lst
                        lst.append(etat2)
                if (lst not in transitions): #si lst n'est pas dans transitions, on l'y ajoute
                    transitions.append(lst)
    auto_min = {  #création automate en utilisant les listes
        "alphabet": auto["alphabet"],
        "etats": etats,
        "transitions": transitions,
        "I": ini,
        "F": f
    }
    
    return auto_min


if __name__ == '__main__':
    L1=['aa','ab','ba','bb']
    L2=['a', 'b', '']
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
"transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    auto1 ={"alphabet":['a','b'],"etats": [0,1],
"transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto2={"alphabet":['a','b'],"etats": [0,1],
"transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto3 ={"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}
    auto4 ={"alphabet":['a','b'],"etats": [0,1,2,],
"transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}
    auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
"transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
"I":[0],"F":[0,1]}
    auto7 ={"alphabet":['a','b'],"etats": [1,2,3,4,5,6],
"transitions":[[1,'a',5],[1,'b',4],[2,'a',6],[2,'b',6],[3,'b',3],[3,'a',6],
               [4,'a',2],[4,'b',1],[5,'a',2],[5,'b',3],[6,'b',6],[6,'a',3]],
"I":[1],"F":[1,2,3,6]}
    auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],
[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],
"I":[0],"F":[0,1,2,5]}

    

    print(renommage(minimise(auto6)))


   



