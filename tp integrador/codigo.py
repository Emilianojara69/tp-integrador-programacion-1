# Lista de pacientes con nombre, DNI y prioridad (1-5, donde 5 es máxima urgencia)
pacientes = [
    {"nombre": "Ana Gómez", "dni": 30123123, "prioridad": 3},
    {"nombre": "Carlos Ruiz", "dni": 29500123, "prioridad": 5},
    {"nombre": "Lucía Díaz", "dni": 33100222, "prioridad": 1},
    {"nombre": "Marcos Ledesma", "dni": 31200123, "prioridad": 4},
    {"nombre": "Fernanda Luna", "dni": 30765432, "prioridad": 2}
]

# Ordenamiento por prioridad (de mayor a menor) - Bubble Sort adaptado
def ordenar_por_prioridad(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["prioridad"] < lista[j + 1]["prioridad"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ordenamiento por DNI (para búsqueda binaria)
def ordenar_por_dni(lista):
    lista.sort(key=lambda x: x["dni"])

# Búsqueda binaria por DNI en una lista ordenada
def busqueda_binaria_dni(lista, dni_buscado):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["dni"] == dni_buscado:
            return lista[medio]
        elif lista[medio]["dni"] < dni_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# # 🧪 PRUEBA 1: Ordenar por prioridad y mostrar resultado
# print("📌 Lista de pacientes ordenada por prioridad (mayor a menor):")
# ordenar_por_prioridad(pacientes)
# for paciente in pacientes:
#     print(f"{paciente['nombre']} - DNI: {paciente['dni']} - Prioridad: {paciente['prioridad']}")

# 🧪 PRUEBA 2: Ordenar por DNI y buscar uno específico
print("\n🔎 Búsqueda binaria por DNI:")
ordenar_por_dni(pacientes)
dni_buscado = 12345678
resultado = busqueda_binaria_dni(pacientes, dni_buscado)

if resultado:
    print(f"✅ Paciente encontrado: {resultado['nombre']} - DNI: {resultado['dni']} - Prioridad: {resultado['prioridad']}")
else:
    print("❌ Paciente no encontrado.")


