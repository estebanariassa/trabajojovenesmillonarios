


import random


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
        "pregunta": "¿Cuál es el libro más vendido de la historia?",
        "opciones": ["La biblia", "Don Quijote de la mancha", "Cien años de soledad", "el principito"],
        "respuesta_correcta": "La biblia"
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
        "pregunta": "¿Cuál es el deporte más practicado del mundo?",
        "opciones": ["Natacion", "Futbol", "Baloncesto", "Golf"],
        "respuesta_correcta": "Natacion"
    },
    {
        "pregunta": "¿Quién es el autor de el Quijote?",
        "opciones": ["Miguel de Cervantes", "Shakespeare", "Gabriel Garcia", "Mario Benedetti"],
        "respuesta_correcta": "Miguel de Cervantes"
    },
    {
        "pregunta": "¿Cuál fue la primera película de Disney?",
        "opciones": ["Blancanieves", "Mickey Mouse", "La cenicienta", "Cars"],
        "respuesta_correcta": "Blancanieves"
    },
    {
        "pregunta": "¿En qué lugar se usó la primera bomba atómica en combate?",
        "opciones": ["Hawai", "Tokio", "Hiroshima", "Roma"],
        "respuesta_correcta": "Hiroshima"
    },
    {
        "pregunta": "¿Con cuántos países comparte Colombia fronteras terrestres?",
        "opciones": ["5", "7", "4", "3"],
        "respuesta_correcta": "5"
    },
    {
        "pregunta": "¿Cuándo ganó la selección colombiana la Copa América de Fútbol?",
        "opciones": ["2001", "1997", "2011", "2007"],
        "respuesta_correcta": "2001"
    },
    {
        "pregunta": "¿Cuál es el área del arte protagonista en los premios Grammy?",
        "opciones": ["musica", "audivisuales", "peliculas", "ciencia"],
        "respuesta_correcta": "musica"
    },
    {
        "pregunta": "¿Qué día es la fiesta nacional de Estados Unidos?",
        "opciones": ["4 de julio", "20 de julio", "7 de agosto", "1 de enero"],
        "respuesta_correcta": "4 de julio"
    },
    {
        "pregunta": "¿cual es la cancion mas escuchada de spotify?",
        "opciones": ["blinding lights", "dakiti", "circles", "yo me porto bonito"],
        "respuesta_correcta": "blinding lights"
    },
    {
        "pregunta": "¿Cuál es el animal nacional de Australia?",
        "opciones": ["Canguro rojo", "condor de los andes", "aguila calva", "koala"],
        "respuesta_correcta": "Canguro rojo"
    },
    {
        "pregunta": "¿En que año se hundio el titanic?",
        "opciones": ["1997", "1913", "1912", "2011"],
        "respuesta_correcta": "1912"
    },
    {
        "pregunta": "¿Cual es la pelicula mas taquillera de la historia?",
        "opciones": ["2012", "Titanic", "Avengers Endgame", "Avatar"],
        "respuesta_correcta": "Avatar"
    },
    {
        "pregunta": "¿En qué año se estrenó la película Titanic?",
        "opciones": ["1997", "2012", "1913", "2000"],
        "respuesta_correcta": "1997"
    },
    {
        "pregunta": "¿En que año sucedio la catastrofe de chernobyl?",
        "opciones": ["2000", "1990", "2011", "1986"],
        "respuesta_correcta": "1986"
    },
    {
        "pregunta": "¿En que año sucedio la toma al palacio de justicia?",
        "opciones": ["1986", "1985", "2001", "1997"],
        "respuesta_correcta": "1985"
    },
    {
        "pregunta": "¿En que año tumbaron las torres gemelas?",
        "opciones": ["2005", "1998", "2010", "2001"],
        "respuesta_correcta": "2001"
    },
    {
        "pregunta": "¿Cuál es el álbum musical más vendido en la historia?",
        "opciones": ["Un verano sin ti", "the dark side of the moon", "X100Pre", "Thriller"],
        "respuesta_correcta": "Thriller"
    },
    {
        "pregunta": "¿Cuál es la videoconsola más vendida en la historia?",
        "opciones": ["Nintendo 64", "XboX360", "PS4", "PS2"],
        "respuesta_correcta": "PS2"
    },
    {
        "pregunta": "Cual es el album mas escuchado de spotify",
        "opciones": ["Starboy", "After Hours", "Un verano sin ti", "hollywood bleeding"],
        "respuesta_correcta": "Un verano sin ti"
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


for pregunta in preguntas:
    opciones_aleatorias = pregunta["opciones"][:]
    random.shuffle(opciones_aleatorias)
    pregunta["opciones"] = opciones_aleatorias
ayudas = {
    "50/50": "Elimina dos opciones incorrectas.",
    "Cambio": "Cambia la pregunta.",

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
    if n <= 0:
        return 0
    elif n==1:
        return 1
    else:
        a,b = 1, 1
        for _ in range (n-1):
            a,b = b, a+b
            return b
    return serie

# Generar la serie de Fibonacci para 10 estaciones



def hacer_pregunta(pregunta, ayudas_usadas, estacion):
    print(f"Estación {estacion}: {pregunta['pregunta']}")
    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")


    print("Ayudas disponibles:")
    for ayuda, descripcion in ayudas.items():
        if ayuda not in ayudas_usadas:
            print(f"{ayuda}: {descripcion}")

    respuesta_usuario = input("Elige una opción o una ayuda: ")


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
                                  estacion)
        elif respuesta_usuario == "Cambio":
            print("Has usado la ayuda Cambio. Cambiando de pregunta.")
            ayudas_usadas.add(respuesta_usuario)

            nueva_pregunta = random.choice(preguntas)
            preguntas.remove(nueva_pregunta)
            return hacer_pregunta(nueva_pregunta, ayudas_usadas, estacion)
        elif respuesta_usuario == "Salir":
            return False
        else:
            print("Ayuda no implementada.")
            return hacer_pregunta(pregunta, ayudas_usadas, estacion)


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
        preguntas.remove(pregunta)
        if hacer_pregunta(pregunta, ayudas_usadas, estacion):
            puntaje += generar_serie_fibonacci(estacion - 1)
            print(f"Tu puntaje actual es: {puntaje}")
        else:
            print("El juego ha terminado. Tu puntaje final es:", puntaje)
            return


jugar()