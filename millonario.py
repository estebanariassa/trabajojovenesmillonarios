import random

# Generar preguntas y respuestas aleatorias
import random

# Generar preguntas y respuestas aleatorias
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de España?",
        "opciones": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
        "respuesta_correcta": "Madrid"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Tierra", "Júpiter", "Marte", "Saturno"],
        "respuesta_correcta": "Júpiter"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Pacífico", "Atlántico", "Índico", "Ártico"],
        "respuesta_correcta": "Pacífico"
    },
    {
        "pregunta": "¿Cuál es el animal más rápido del mundo?",
        "opciones": ["Guepardo", "León", "Águila", "Tortuga"],
        "respuesta_correcta": "Guepardo"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"],
        "respuesta_correcta": "Nilo"
    },
    {
        "pregunta": "¿Cuál es el país más poblado del mundo?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el monte más alto del mundo?",
        "opciones": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
        "respuesta_correcta": "Everest"
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado en el mundo?",
        "opciones": ["Español", "Mandarín", "Inglés", "Hindi"],
        "respuesta_correcta": "Mandarín"
    },
    {
        "pregunta": "¿Cuál es el país con más ciudades del mundo?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más países en su frontera?",
        "opciones": ["Alemania", "Rusia", "China", "Afganistán"],
        "respuesta_correcta": "Rusia"
    },
    {
        "pregunta": "¿Cuál es el país con más lagos?",
        "opciones": ["Canadá", "Estados Unidos", "Alemania", "Brasil"],
        "respuesta_correcta": "Canadá"
    },
    {
        "pregunta": "¿Cuál es el país con más islas?",
        "opciones": ["Grecia", "Japón", "Canadá", "Estados Unidos"],
        "respuesta_correcta": "Japón"
    },
    {
        "pregunta": "¿Cuál es el país con más volcanes activos?",
        "opciones": ["Indonesia", "Islandia", "Italia", "Japón"],
        "respuesta_correcta": "Indonesia"
    },
    {
        "pregunta": "¿Cuál es el país con más parques nacionales?",
        "opciones": ["Estados Unidos", "Canadá", "Australia", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más estados?",
        "opciones": ["Estados Unidos", "Canadá", "India", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más habitantes?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más ciudades?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más islas?",
        "opciones": ["Grecia", "Japón", "Canadá", "Estados Unidos"],
        "respuesta_correcta": "Japón"
    },
    {
        "pregunta": "¿Cuál es el país con más volcanes activos?",
        "opciones": ["Indonesia", "Islandia", "Italia", "Japón"],
        "respuesta_correcta": "Indonesia"
    },
    {
        "pregunta": "¿Cuál es el país con más parques nacionales?",
        "opciones": ["Estados Unidos", "Canadá", "Australia", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más estados?",
        "opciones": ["Estados Unidos", "Canadá", "India", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más habitantes?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más ciudades?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más islas?",
        "opciones": ["Grecia", "Japón", "Canadá", "Estados Unidos"],
        "respuesta_correcta": "Japón"
    },
    {
        "pregunta": "¿Cuál es el país con más volcanes activos?",
        "opciones": ["Indonesia", "Islandia", "Italia", "Japón"],
        "respuesta_correcta": "Indonesia"
    },
    {
        "pregunta": "¿Cuál es el país con más parques nacionales?",
        "opciones": ["Estados Unidos", "Canadá", "Australia", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más estados?",
        "opciones": ["Estados Unidos", "Canadá", "India", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más habitantes?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más ciudades?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más islas?",
        "opciones": ["Grecia", "Japón", "Canadá", "Estados Unidos"],
        "respuesta_correcta": "Japón"
    },
    {
        "pregunta": "¿Cuál es el país con más volcanes activos?",
        "opciones": ["Indonesia", "Islandia", "Italia", "Japón"],
        "respuesta_correcta": "Indonesia"
    },
    {
        "pregunta": "¿Cuál es el país con más parques nacionales?",
        "opciones": ["Estados Unidos", "Canadá", "Australia", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más estados?",
        "opciones": ["Estados Unidos", "Canadá", "India", "Brasil"],
        "respuesta_correcta": "Estados Unidos"
    },
    {
        "pregunta": "¿Cuál es el país con más habitantes?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más ciudades?",
        "opciones": ["China", "India", "Estados Unidos", "Brasil"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el país con más islas?",
        "opciones": ["Grecia", "Japón", "Canadá", "Estados Unidos"],
        "respuesta_correcta": "Japón"
    },
]

# Generar respuestas aleatorias para cada pregunta
for pregunta in preguntas:
    opciones_aleatorias = pregunta["opciones"][:]
    random.shuffle(opciones_aleatorias)
    pregunta["opciones"] = opciones_aleatorias
ayudas = {
    "50/50": "Elimina dos opciones incorrectas.",
    "Cambio": "Cambia la pregunta.",
    "Salir": "Retirarse del juego."
}

reglas = """
¡Bienvenido al Quien Quiere Ser Millonario!
Las reglas son las siguientes:
- Tienes 10 estaciones para responder preguntas.
- Puedes usar las siguientes ayudas: 50/50, Cambio, Salir.
- Si decides usar una ayuda, no podrás usarla de nuevo.
- En las estaciones 5 y 7, puedes decidir retirarte del juego.
- Si decides retirarte, llevarás el puntaje acumulado.
- El puntaje se incrementa siguiendo la serie de Fibonacci.
"""

def generar_serie_fibonacci(n):
    serie = [1, 2]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie

# Generar la serie de Fibonacci para 10 estaciones
serie_fibonacci = generar_serie_fibonacci(10)

# Generar la serie de Fibonacci para 10 estaciones
serie_fibonacci = generar_serie_fibonacci(10)


def hacer_pregunta(pregunta, ayudas_usadas, estacion):
    print(f"Estación {estacion}: {pregunta['pregunta']}")
    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")

    # Opción para usar una ayuda
    print("Ayudas disponibles:")
    for ayuda, descripcion in ayudas.items():
        if ayuda not in ayudas_usadas:
            print(f"{ayuda}: {descripcion}")

    respuesta_usuario = input("Elige una opción o una ayuda: ")

    # Verificar si el usuario eligió una ayuda
    if respuesta_usuario in ayudas:
        if respuesta_usuario == "50/50":
            # Implementar la lógica para la ayuda "50/50"
            print("Has usado la ayuda 50/50. Ahora tienes dos opciones incorrectas eliminadas.")
            # Eliminar dos opciones incorrectas
            opciones_incorrectas = [opcion for opcion in pregunta["opciones"] if
                                    opcion != pregunta["respuesta_correcta"]]
            incorrectas_a_eliminar = random.sample(opciones_incorrectas, 2)
            for incorrecta in incorrectas_a_eliminar:
                pregunta["opciones"].remove(incorrecta)
            ayudas_usadas.add(respuesta_usuario)
            return hacer_pregunta(pregunta, ayudas_usadas,
                                  estacion)  # Vuelve a hacer la pregunta con las opciones actualizadas
        elif respuesta_usuario == "Cambio":
            print("Has usado la ayuda Cambio. Cambiando de pregunta.")
            ayudas_usadas.add(respuesta_usuario)
            # Seleccionar una nueva pregunta y volver a hacer la pregunta actual
            nueva_pregunta = random.choice(preguntas)
            preguntas.remove(nueva_pregunta)
            return hacer_pregunta(nueva_pregunta, ayudas_usadas,
                                  estacion)  # Vuelve a hacer la pregunta con la nueva pregunta
        elif respuesta_usuario == "Salir":
            return False  # El jugador decide retirarse
        else:
            print("Ayuda no implementada.")
            return hacer_pregunta(pregunta, ayudas_usadas, estacion)  # Vuelve a hacer la pregunta sin cambios

    # Verificar si la respuesta del usuario es correcta
    if pregunta["opciones"][int(respuesta_usuario) - 1] == pregunta["respuesta_correcta"]:
        print("¡Correcto!")
        return True
    else:
        print("Incorrecto.")
        return False


def jugar():
    print("Ingresa el nombre del jugador:")
    nombre_jugador = input()
    print(f"¡Bienvenido, {nombre_jugador}!")
    print(reglas)
    print("Ayudas disponibles:")
    for ayuda, descripcion in ayudas.items():
        print(f"{ayuda}: {descripcion}")

    puntaje = 0
    ayudas_usadas = set()
    for estacion in range(1, 11):
        if estacion in [5, 7] and input("¿Quieres retirarte? (s/n): ").lower() == "s":
            print("Has decidido retirarte. Tu puntaje final es:", puntaje)
            return
        pregunta = random.choice(preguntas)
        preguntas.remove(pregunta)  # Asegurarse de que la pregunta no se repita
        if hacer_pregunta(pregunta, ayudas_usadas, estacion):
            puntaje += serie_fibonacci[estacion - 1]
            print(f"Tu puntaje actual es: {puntaje}")
        else:
            print("El juego ha terminado. Tu puntaje final es:", puntaje)
            return


# Iniciar el juego
jugar()
