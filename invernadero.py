# Definición de variables (nombres corregidos)
gallinas = 100
nivel_del_tanque_de_agua = 1500  # en litros
concentrado_de_gallinas = 640000  # en gramos
consumo_de_alimento_por_gallina = 100  # gramos
consumo_de_agua_por_gallina = 0.2  # litros
huevos_por_gallina_diarios = 0.65
popo_por_gallina_diarios = 120  # gramos

# Función para calcular los gastos diarios
def calcular_gastos(gallinas, consumo_de_agua_por_gallina, consumo_de_alimento_por_gallina):
    return gallinas * consumo_de_agua_por_gallina, gallinas * consumo_de_alimento_por_gallina

# Función para calcular los recursos restantes (devuelve números ahora)
def calcular_recursos_restantes(gallinas, concentrado_de_gallinas, nivel_del_tanque_de_agua, consumo_de_alimento_por_gallina, consumo_de_agua_por_gallina):
    consumo_total_diario = gallinas * consumo_de_alimento_por_gallina
    consumo_total_agua_diario = gallinas * consumo_de_agua_por_gallina
    concentrado_de_gallinas_restante = concentrado_de_gallinas - consumo_total_diario  # gramos
    agua_restante = nivel_del_tanque_de_agua - consumo_total_agua_diario  # litros
    return concentrado_de_gallinas_restante, agua_restante

# Función para calcular la producción
def calcular_produccion(gallinas, huevos_por_gallina_diarios, popo_por_gallina_diarios):
    return gallinas * huevos_por_gallina_diarios, gallinas * popo_por_gallina_diarios

# Inicialización de variables
concentrado_restante, agua_restante = calcular_recursos_restantes(
    gallinas, concentrado_de_gallinas, nivel_del_tanque_de_agua, 
    consumo_de_alimento_por_gallina, consumo_de_agua_por_gallina
)

# Simulación de 10 días
for dia in range(1, 61):
    print(f"\n📅 Día {dia}")

    # Calcular consumo diario
    consumo_agua, consumo_comida = calcular_gastos(
        gallinas, consumo_de_agua_por_gallina, consumo_de_alimento_por_gallina
    )

    # Verificar si hay recursos suficientes
    if agua_restante < consumo_agua or concentrado_restante < consumo_comida:
        print("❌ No hay recursos suficientes. Producción en 0.")
        huevos, popo = 0, 0
    else:
        agua_restante -= consumo_agua
        concentrado_restante -= consumo_comida
        huevos, popo = calcular_produccion(
            gallinas, huevos_por_gallina_diarios, popo_por_gallina_diarios
        )
        print(f"✅ Huevos: {huevos:.2f} | Popó: {popo:.2f} g")

    print(f"💧 Agua restante: {agua_restante:.2f} L")
    print(f"🍽️ Concentrado restante: {concentrado_restante:.2f} g")

    if agua_restante < consumo_agua or concentrado_restante < consumo_comida:
        print("⚠️ Advertencia: Recurso insuficiente para el siguiente día.")