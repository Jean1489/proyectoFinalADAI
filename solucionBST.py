import time

class TreeNode:
    def __init__(self, escena):
        self.escena = escena
        self.left = None
        self.right = None

def insert(root, escena):
    if root is None:
        return TreeNode(escena)
    
    grandeza_total1 = sum(grandezas[animales.index(animal)] for animal in root.escena)
    grandeza_total2 = sum(grandezas[animales.index(animal)] for animal in escena)

    if grandeza_total2 < grandeza_total1 or (grandeza_total2 == grandeza_total1 and escena < root.escena):
        root.left = insert(root.left, escena)
    else:
        root.right = insert(root.right, escena)
    
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.escena)
        inorder_traversal(root.right)

def espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes):
    animales_grandezas = list(zip(animales, grandezas))
    bst = None

    # Insertar las escenas de apertura en el BST
    for escena in apertura:
        bst = insert(bst, escena)

    # Insertar las escenas de partes en el BST
    for parte in partes:
        for escena in parte:
            bst = insert(bst, escena)

    # Realizar un recorrido inorder para obtener el orden final de las escenas
    escenas_ordenadas = []
    def inorder_append(root):
        nonlocal escenas_ordenadas
        if root:
            inorder_append(root.left)
            escenas_ordenadas.append(root.escena)
            inorder_append(root.right)
    
    inorder_append(bst)

    # Encontrar el animal que participa en más escenas
    participacion_animales = {}
    for escena in escenas_ordenadas:
        for animal in escena:
            if animal in participacion_animales:
                participacion_animales[animal] += 1
            else:
                participacion_animales[animal] = 1

    max_participacion = max(participacion_animales.values())
    animales_max_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == max_participacion]

    # Encontrar el animal que participa en menos escenas
    min_participacion = min(participacion_animales.values())
    animales_min_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == min_participacion]
    
    # Calcular el promedio de las grandezas de todas las escenas
    suma_total_grandezas = sum(grandezas)
    promedio_grandezas = suma_total_grandezas / (m * k)

    # Imprimir la información obtenida
    print("El orden en el que se debe presentar el espectáculo es:")
    for i, escena in enumerate(escenas_ordenadas, start=1):
        print("escena{} =".format(i), escena)
    print("El animal que participó en más escenas dentro del espectáculo fue", animales_max_participacion, "con", max_participacion, "escenas.")
    print("El animal que participó en menos escenas dentro del espectáculo fue", animales_min_participacion, "con", min_participacion, "escenas.")
    print("La escena de menor grandeza total fue la escena", escenas_ordenadas[0])
    print("La escena de mayor grandeza total fue la escena", escenas_ordenadas[-1])
    print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandezas)

# Función para medir el tiempo de ejecución de espectaculo_zoologico
def medir_tiempo_espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes):
    inicio = time.time()
    espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes)
    fin = time.time()
    tiempo_total = fin - inicio
    print("La función espectaculo_zoologico se ejecutó en", tiempo_total, "segundos")

# Ejemplo de uso
n = 6
m = 3
k = 2
animales = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]
apertura = [["gato", "ciempies", "libelula"], ["ciempies", "tapir", "gato"], ["tapir", "perro", "gato"], ["tapir", "nutria", "perro"]]
partes = [[["ciempies", "tapir", "gato"], ["tapir", "nutria", "perro"]], [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]]

medir_tiempo_espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes)
