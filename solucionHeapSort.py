import time

class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza

    def __str__(self):
        return f"{self.nombre} ({self.grandeza})"


class Escena:
    def __init__(self, animales):
        self.animales = self.ordenar_animales_heapsort(animales)
        self.grandeza_total = sum(animal.grandeza for animal in self.animales)
        self.max_grandeza_individual = max(animal.grandeza for animal in self.animales)

    def __str__(self):
        return ", ".join(str(animal) for animal in self.animales)

    def ordenar_animales_heapsort(self, animales):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left].grandeza > arr[largest].grandeza:
                largest = left

            if right < n and arr[right].grandeza > arr[largest].grandeza:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(animales)

        for i in range(n // 2 - 1, -1, -1):
            heapify(animales, n, i)

        for i in range(n - 1, 0, -1):
            animales[i], animales[0] = animales[0], animales[i]
            heapify(animales, i, 0)

        return animales


class Espectaculo:
    def __init__(self, n, m, k, animales, apertura, partes):
        self.n = n
        self.m = m
        self.k = k
        self.animales = animales
        self.apertura = [Escena([animal for animal in escena]) for escena in apertura]
        self.partes = [
            [Escena([animal for animal in partida]) for partida in parte] for parte in partes
        ]

    def ordenar_escenas_heapsort(self, escenas):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left].grandeza_total > arr[largest].grandeza_total:
                largest = left

            if right < n and arr[right].grandeza_total > arr[largest].grandeza_total:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(escenas)

        for i in range(n // 2 - 1, -1, -1):
            heapify(escenas, n, i)

        for i in range(n - 1, 0, -1):
            escenas[i], escenas[0] = escenas[0], escenas[i]
            heapify(escenas, i, 0)

        return escenas

    def mostrar_escenas(self, escenas):
        for escena in escenas:
            print(escena)

    def ejecutar_espectaculo(self):
        apertura_ordenada = self.ordenar_escenas_heapsort(self.apertura)
        partes_ordenadas = [self.ordenar_escenas_heapsort(parte) for parte in self.partes]

        print("Apertura:")
        self.mostrar_escenas(apertura_ordenada)
        print()

        for i, parte in enumerate(partes_ordenadas, 1):
            print(f"Parte {i}:")
            self.mostrar_escenas(parte)
            print()

        todas_las_escenas_ordenadas = apertura_ordenada + sum(partes_ordenadas, [])
        animales_escenas = [
            animal for escena in todas_las_escenas_ordenadas for animal in escena.animales
        ]

        animales_participantes = set(animales_escenas)
        animales_contador = {
            animal: animales_escenas.count(animal) for animal in animales_participantes
        }

        animal_mas_participante = max(animales_contador, key=animales_contador.get)
        max_participacion = animales_contador[animal_mas_participante]

        animales_menos_participantes = [
            animal
            for animal, count in animales_contador.items()
            if count == min(animales_contador.values())
        ]
        min_participacion = animales_contador[animales_menos_participantes[0]]

        escena_menor_grandeza_total = min(
            todas_las_escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )
        escena_mayor_grandeza_total = max(
            todas_las_escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )

        promedio_grandezas = sum(animal.grandeza for animal in animales_escenas) / len(
            animales_escenas
        )

        print("\nResultados:")
        print(
            f"El animal que participó en más escenas dentro del espectáculo fue {animal_mas_participante.nombre} que participó en {max_participacion} escenas."
        )
        print(
            f"El animal que menos participó en escenas dentro del espectáculo fueron {', '.join(animal.nombre for animal in animales_menos_participantes)} quienes participaron cada uno en {min_participacion} escenas."
        )
        print(
            f"La escena de menor grandeza total fue la escena {escena_menor_grandeza_total}."
        )
        print(
            f"La escena de mayor grandeza total fue la escena {escena_mayor_grandeza_total}."
        )
        print(
            f"El promedio de grandeza de todo el espectáculo fue de {promedio_grandezas:.2f}."
        )

    def medir_tiempo(self):
        inicio = time.time()
        self.ejecutar_espectaculo()
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos.")


# Ejemplo de uso
n = 9
m = 4
k = 3

animales_dict = {
    "Capibara": Animal("Capibara", 1),
    "Loro": Animal("Loro", 2),
    "Caimán": Animal("Caimán", 3),
    "Boa": Animal("Boa", 4),
    "Cocodrilo": Animal("Cocodrilo", 5),
    "Cebra": Animal("Cebra", 6),
    "Pantera negra": Animal("Pantera negra", 7),
    "Tigre": Animal("Tigre", 8),
    "León": Animal("León", 9),
}

capibara = animales_dict["Capibara"]
loro = animales_dict["Loro"]
caiman = animales_dict["Caimán"]
boa = animales_dict["Boa"]
cocodrilo = animales_dict["Cocodrilo"]
cebra = animales_dict["Cebra"]
pantera = animales_dict["Pantera negra"]
tigre = animales_dict["Tigre"]
leon = animales_dict["León"]

apertura = [
    [caiman, capibara, loro],
    [boa, caiman, capibara],
    [cocodrilo, capibara, loro],
    [pantera, cocodrilo, loro],
    [tigre, loro, capibara],
    [leon, caiman, loro],
    [leon, cocodrilo, boa],
    [leon, pantera, cebra],
    [tigre, cebra, pantera],
]

partes = [
    [[caiman, capibara, loro], [tigre, loro, capibara], [tigre, cebra, pantera]],
    [[pantera, cocodrilo, loro], [leon, pantera, cebra], [cocodrilo, capibara, loro]],
    [[boa, caiman, capibara], [leon, caiman, loro], [leon, cocodrilo, boa]],
]

espectaculo = Espectaculo(n, m, k, animales_dict, apertura, partes)

# Ejecución del espectáculo
espectaculo.medir_tiempo()

