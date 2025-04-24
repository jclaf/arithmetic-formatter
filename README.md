# arithmetic-formatter

- **Cette algorithme formate jusqu’à 5 opérations d’addition ou de soustraction en colonnes, façon “cahier d’école”.**
- **Il vérifie la validité des entrées et affiche (optionnellement) les résultats.**
- **Idéal pour générer des exercices de calcul ou pour afficher proprement des opérations.**

---

## Description du Code

### 1. Fonction `arithmetic_arranger`

#### **Paramètres**
- `problems` : Liste de chaînes représentant des opérations à deux opérandes, ex. `["32 + 698", "3801 - 2"]`.
- `show_answers` (optionnel) : Booléen, si `True` affiche aussi les résultats.

---

### 2. **Vérification des entrées**

```python
if len(problems) > 5:
    return 'Error: Too many problems.'
else:
    for i in problems:
        cp = i.split()
        if not cp[0].isnumeric() or not cp[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        if len(cp[0]) > 4 or len(cp[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if cp[1] != '+' and cp[1] != '-':
            return "Error: Operator must be '+' or '-'."
```
- **Nombre d'opérations** : Maximum 5, sinon erreur.
- **Chiffres** : Les opérandes doivent être des nombres entiers positifs.
- **Taille** : Pas plus de 4 chiffres par nombre.
- **Opérateur** : Doit être `+` ou `-`.

---

### 3. **Formatage des opérations**

```python
for index, i in enumerate(problems):
    cp = i.split()
    space = '    ' if index < len(problems) - 1 else ''
    line1 += cp[0].rjust(max(len(cp[0]), len(cp[2])) + 2) + space
    line2 += cp[1] + ' ' + cp[2].rjust(max(len(cp[0]), len(cp[2]))) + space
    line3 += '-' * (max(len(cp[0]), len(cp[2])) + 2) + space
    if show_answers:
        if cp[1] == '+':
            line4 += str(int(cp[0]) + int(cp[2])).rjust(max(len(cp[0]), len(cp[2])) + 2) + space
        else:
            line4 += str(int(cp[0]) - int(cp[2])).rjust(max(len(cp[0]), len(cp[2])) + 2) + space
        final_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        final_problems = line1 + '\n' + line2 + '\n' + line3
```

- **Pour chaque opération** :
    - **Espacement** : 4 espaces entre chaque opération (sauf la dernière).
    - **Ligne 1** : Premier opérande, aligné à droite.
    - **Ligne 2** : Opérateur + deuxième opérande, aligné à droite.
    - **Ligne 3** : Ligne de tirets (autant que la largeur de l'opération).
    - **Ligne 4** (si demandé) : Résultat, aligné à droite.

---

### 4. **Retour du résultat**

- Les lignes sont assemblées avec des sauts de ligne pour former un affichage en colonnes, comme sur une feuille d’exercice.
- Si `show_answers` est `True`, la ligne des résultats est ajoutée.

---

### 5. **Exemples d’utilisation**

```python
if __name__ == "__main__":
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["24 + 8215", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
```

**Exemple de sortie :**
```
  3801      123
-    2    +  49
------    ------
```
Ou avec réponses :
```
    3      988
+ 855    +  40
-----    -----
  858     1028
```

---

## Algorithme Utilisé

### **Formatage et validation d’opérations arithmétiques**

- **Validation** : Vérifie la conformité des entrées (nombre, format, opérateur).
- **Calcul** : Effectue l’opération si demandé.
- **Formatage** : Utilise `rjust` pour aligner les nombres à droite et crée des lignes de tirets pour séparer l’opération du résultat.
- **Assemblage** : Construit l’affichage ligne par ligne, avec des espaces pour séparer les opérations.

---
