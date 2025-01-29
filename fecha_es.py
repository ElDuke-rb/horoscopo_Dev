from datetime import datetime

def fecha_esp():

    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]

    dias_semana = [
        "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
    ]

    ahora = datetime.now()
    dia_semana = dias_semana[ahora.weekday()]
    mes = meses[ahora.month - 1]

    return f"{dia_semana.capitalize()} {ahora.day} de {mes} de {ahora.year}"