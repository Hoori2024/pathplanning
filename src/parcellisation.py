import sys


def displayUsageAndExit(exitCode):
    print(f"USAGE: {sys.argv[0]} parcellisation.py filepath")
    exit(exitCode)


def parseInputFile(filepath):
    """
        (0; 0.2) (0; -1) (3.8; 5) (0; 4)
        (2; 3) (3; 2.9) (2; 4)
        cette fonction parse le fichier d'entrée et retourne un tableau de coordonnées
    """
    # TODO:
    # - check if every polygon has at least 3 vertices
    # - vérifier qu'un polygone n'ait pas plusieurs sommets confondus
    # - vérifier que les polygones enfants soient tous dans le polygone parent
    # - vérifier qu'un polygone enfant ne soit pas dans un autre polyone enfant
    
    vertices_polygon = []
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        for i in lines:
            stockVertice = []
            line = i.replace("(", "").replace(" ","").replace("\n", "")
            for j in line.split(")"):
                if j != "":
                    stockVertice.append([float(j.split(";")[0]), float(j.split(";")[1])])
            vertices_polygon.append(stockVertice)
    except FileNotFoundError:
        print("File not found")
        exit(84)
    print(vertices_polygon)
    #vertices_polygon_list:list(tuple) = [(float(vertices_polygon[i]), float(vertices_polygon[i+1])) for i in range(1, len(vertices_polygon), 2)]
    #print(f"vertices list {vertices_polygon_list}")
    for line in lines[1:]:
        print(line)
            
            
    


def displayResult():
    ...


def isPointInPolygon():
    ...


def getShiftedCenterCoords():
    ...


def main():
    parseInputFile(sys.argv[1])
    if len(sys.argv) <= 1:
        displayUsageAndExit(84)
    if '-h' in sys.argv or '--help' in sys.argv:
        displayUsageAndExit(0)

    
    



if __name__ == "__main__":
    main()
