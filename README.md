# Algorithme de parcellisation


### Utilisation du binaire

`$ ./binaryName  filepath`

filepath : chemin du fichier de configuration du champ


### Output

Le binaire affiche sur la sortie standard une représentation du champ :
la liste des polygones du champ, avec pour chacun d’eux la liste des côtés ;
la liste des cellules du quadrillage généré, avec pour chacune d’elles les coordonnées du centre et des sommets, et le type.

Exemple :

`
Edges: [([7.0, 10.0], [11.0, 10.0]), ([11.0, 10.0], [11.0, 6.0]), ([11.0, 6.0], [9.0, 6.0]), ([9.0, 6.0], [9.0, 7.0]), ([9.0, 7.0], [7.0, 7.0]), ([7.0, 7.0], [7.0, 10.0])]

Cells:

Cell(center: (7.5, 6.5), vertices: [(7.0, 7.0), (8.0, 7.0), (8.0, 6.0), (7.0, 6.0)], type: COMPLETLY_OUTSIDE)

Cell(center: (7.5, 7.5), vertices: [(7.0, 8.0), (8.0, 8.0), (8.0, 7.0), (7.0, 7.0)], type: COMPLETLY_INSIDE)

Cell(center: (7.5, 8.5), vertices: [(7.0, 9.0), (8.0, 9.0), (8.0, 8.0), (7.0, 8.0)], type: COMPLETLY_INSIDE)

Cell(center: (7.5, 9.5), vertices: [(7.0, 10.0), (8.0, 10.0), (8.0, 9.0), (7.0, 9.0)], type: COMPLETLY_INSIDE)

[…]
`


### Contenu du fichier de configuration

Un champ est composé d’un ou plusieurs polygones. Il s’agit de la bordure extérieure (polygone parent) et des potentielles zones de non-vol (polygone enfant). Ainsi :
le polygone parent doit contenir tous les polygones enfants ;
un polygone enfant ne peut pas contenir d’autres polygones enfants ;
les bords des polygones (parent ou enfants) ne doivent pas être sécants ou confondus.

Un fichier de configuration est composé d’une ou plusieurs lignes.
Sur la première ligne, le polygone parent est défini.
Si des polygones enfants existent, ils sont définis sur les lignes suivantes (une ligne par polygone enfant).
La définition d’un polygone consiste en une liste des coordonnées de tous ses sommets successifs (c’est-à-dire que le sommet n+1 doit être lié au sommet n par une arête du polygone).

Exemple de fichier de configuration d’un champ contenant une zone de non-vol :

`
(0;0.2) (0;-1) (3;8.5) (0;4)

(2;3) (3;2.9) (2;4)
`


### Format des coordonnées
Une unité correspond à la dimension du plus petit côté de la prise de vue rectangulaire du drone.
Les coordonnées du champ sont basées sur ces unités.
Un cellule du quadrillage correspond à une unité.
