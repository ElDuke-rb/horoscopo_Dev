import random
from fecha_es import fecha_esp

# Signos zodiacales:
signos = ["Aries ♈", "Tauro ♉", "Géminis ♊", "Cáncer ♋", "Leo ♌", "Virgo ♍",
    "Libra ♎", "Escorpio ♏", "Sagitario ♐", "Capricornio ♑", "Acuario ♒", "Piscis ♓"
]

# Elementos de programación:
tecnologias = [
     "JavaScript", "Python", "Ruby", "Rails", "Java", "CSS", "Git", "Docker",
    "React", "Node.js", "SQL", "API", "Linux", "Cobol", "Ensamblador"
]

Acciones_tech = [
    "hacer commit",
    "deployar en producción",
    "debuggear código",
    "actualizar dependencias",
    "pushear cambios",
    "refactorizar código",
    "hacer pull requests",
    "resolver conflictos de merge",
	"centrar un div",
    "instalar Arch Linux manualmente"
]

eventos_cosmicos = [
    "la luna en conjunción con GitHub",
    "Marte en tu repositorio",
    "Júpiter alineado con tu backend",
    "Saturno cruzando tu framework",
    "la Constelación del While Infinito",
    "el Solsticio de las Variables Sin Nombre",
    "Saturno sincronizado con tus pipelines",
    "Neptuno flotando en tu frontend"
]

consejos = [
    "haz backup de tu código",
    "revisa dos veces antes de hacer deploy",
    "es hora de aprender Python",
    "es momento de aprender Ruby",
    "documenta tu código, aunque sea con memes",
    "prueba tu código fuera de producción",
    "actualiza tus dependencias… pero con cuidado",
    "no hagas commits en viernes",
    "no ignores las advertencias del linter"
    "instala Arch Linux manualmente y díselo a todo mundo."
]

# Función para crear lista de los signos;
def lista_signos():
    for i in range(0, 12, 2):
        num1 = f"{i+1}. ==> ".ljust(3)
        columna1 = f"{num1} {signos[i]}".ljust(20)

        num2 = f"{i+2}. ==> ".ljust(3)
        columna2 = f"{num2} {signos[i+1]}"

        list_signos = print (f"{columna1} {columna2}")

    return list_signos

# Función que imprime un menú con todos los signos y capta la elección de usuario.
def menu_signos():
    print ("\n ---* ¿De qué signo eres? 🤔 +--- \n")
    lista_signos()
    num = int(input("\n Escribe el número: "))
    return num


def generar_horoscopo():
    signo = signos[menu_signos() - 1]
    tech = random.choice(tecnologias)
    accion = random.choice(Acciones_tech)
    evento = random.choice(eventos_cosmicos)
    consejo = random.choice(consejos)

    horoscopo = f"""

🌟 Horóscopo Dev para {signo} 🌟

- Con la llegada de {evento}, es momento de prestar atención a tus proyectos de {tech}.
- Hoy es {random.choice(['excelente', 'riesgoso', 'ideal', 'complicado'])} para {accion}.

Consejo del día: {consejo.capitalize()}.

Nivel de debugging requerido: {'🐛' * random.randint(1, 5)}
Compatibilidad con: {random.choice(tecnologias)}
"""
    return horoscopo

# Generar horóscopo para hoy
print("\n === 🔮 Horóscopo del Programador ===")
print(f"Hoy es: {fecha_esp()}")


print(generar_horoscopo())