# Dictionnaire ordonne

class DictOrdonne:
    def __init__(self, dictionnaire={}, **KeyValues) :
        self._cles = []
        self._valeurs = []

        if type(dictionnaire) not in (dict, DictOrdonne):
            raise TypeError( \
                'le type attendu est un dictionnaire (usuel ou ordonne)')
        for cle in dictionnaire:
            self[cle] = dictionnaire[cle]

        for cle in KeyValues:
            self[cle] = KeyValues[cle]
    
    def __repr__(self) :
        """Représentation de notre objet. C'est cette chaîne qui
sera affichée
quand on saisit directement le dictionnaire dans l'interpréteur, ou en
utilisant la fonction 'repr'."""
        chaine = '{'
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine +=', '
            else:
                premier_passage = False
            chaine+= repr(cle)+':'+repr(valeur)
        chaine +='}'
        return chaine
    
    def __str__(self):
        """Fonction appelée quand on souhaite afficher le
dictionnaire grâce
à la fonction 'print' ou le convertir en chaîne grâce au constructeur
'str'. On redirige sur __repr__"""
        return repr(self)
    
    def __len__(self):      #lorsqu'on met un nom entre underscore
        #cela en fat une conction appelable. len(dicOrdonne)
        """Renvoie la taille du dictionnaire"""
        return len(self._cles)
    
    def __contains__(self, cle):
        """Renvoie True si la clé est dans la liste des clés, False
sinon"""
        return cle in self._cles
    
    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, 
        une exception KeyError sinon"""
        if cle not in self._cles:
            raise KeyError(\
                'La cle {0} ne se trouve pas dans le dictionnaire'.format(\
                cle))
        else:
            indice = self._cles.index(cle)
            return self._valeurs[indice]
    
    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une
clé
présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
à la fin du dictionnaire"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur 
        else:
            self._cles.append(cle), self._valeurs.append(valeur)
    
    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self._cles:
            raise KeyError(\
                "La cle {0} ne se trouve pas dans le dictionnaire".format(cle))
        else:
            indice = self._cles.index(cle)
            self._cles.remove(cle)
            self._valeurs.pop(indice)
    
    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur
des clés"""
        return iter(self._cles)
    
    def __add__(self, autre_dict):
        """On renvoie un nouveau dictionnaire contenant les deux
dictionnaires mis bout à bout (d'abord self puis autre_objet)"""
        if autre_dict is not type(self):
            raise TypeError(\
                "Impossible de concatener {0} et {1}".format(\
                    type(self), type(autre_dict)))
        else:
            nouveau = DictOrdonne()
            for cle, valeur in self.items():
                nouveau[cle] = valeur

            for cle, valeur in autre_dict.items():
                nouveau[cle] = valeur
            return nouveau
        
    def items(self):
        """Renvoie un générateur contenant les couples (cle,
valeur)"""
        for i, cle in enumerate(self._cles):
            valeur = self._valeurs[i]
            yield(cle, valeur)
    
    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self._cles)
    def keys(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self._valeurs)
    
    def reverse(self):
        """Inversion du dictionnaire"""
        # On crée deux listes vides qui contiendront le nouvel ordre des clés
# et valeurs
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            cles.insert(0,cle)
            valeurs.insert(0,valeur)
        self._cles = cles
        self._valeurs = valeurs
    
    def sort(self):
        """Méthode permettant de trier le dictionnaire en fonction
de ses clés"""
        cles_triees = sorted(self._cles)
        valeurs = []
        for cle in cles_triees:
            valeur = self[cle]
            valeurs.append(valeur)
        self._cles = cles_triees
        self._valeurs = valeurs





        

    




    


        
