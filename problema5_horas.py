# =============================================================================
# Autor: Jean Carlos Redondo Cuadrado
# Curso: Fundamentos de Programación - Código: 213022
# Universidad Nacional Abierta y a Distancia - UNAD
# Fase 5 - Evaluación Final POA
# Problema 5: Horas trabajadas semanales - Clasificación de jornada laboral
# =============================================================================


# --- CONSTANTE DEL UMBRAL DE HORAS ESTÁNDAR ---

UMBRAL_HORAS = 40   # Umbral de horas semanales para considerar sobretiempo


# --- DEFINICIÓN DE LA FUNCIÓN DE CÁLCULO Y CLASIFICACIÓN ---

def calcular_horas_y_clasificar(horas_semana):
    """
    Función que suma las horas trabajadas de lunes a viernes y clasifica
    la jornada del recurso según si supera el umbral establecido.
    Parámetros:
        horas_semana (list): Lista con las horas trabajadas cada día [Lun, Mar, Mie, Jue, Vie].
    Retorna:
        tuple: (total_horas: int/float, clasificacion: str)
    """
    total_horas = 0     # Acumulador de horas inicializado en cero

    # Se recorre cada valor de horas diarias con un ciclo for
    for horas_dia in horas_semana:
        total_horas += horas_dia    # Se suma cada día al acumulador

    # Se evalúa si el total supera el umbral de 40 horas semanales
    if total_horas > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"       # Superó las horas estándar
    else:
        clasificacion = "Horario Estándar"  # Está dentro del límite normal

    # Se retorna la tupla con el total de horas y la clasificación obtenida
    return total_horas, clasificacion


# --- DATOS INICIALES: MATRIZ DE HORAS TRABAJADAS ---

# Cada fila tiene el formato: [Nombre_Recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo = [
    ["Juan Pérez",      9, 8, 10, 9, 8],    # Total esperado: 44h (Sobretiempo)
    ["María López",     8, 8,  8, 8, 8],    # Total esperado: 40h (Estándar)
    ["Carlos Torres",   7, 6,  9, 8, 7],    # Total esperado: 37h (Estándar)
    ["Ana Martínez",   10, 9, 10, 9, 10],   # Total esperado: 48h (Sobretiempo)
]

# Los días de la semana (para encabezados de la tabla)
dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie"]


# --- PRESENTACIÓN DEL REPORTE DE HORAS ---

# Se imprime el encabezado del reporte
print("=" * 70)
print("       REPORTE DE HORAS TRABAJADAS - EQUIPO SEMANAL")
print(f"       Umbral de horas estándar: {UMBRAL_HORAS} horas/semana")
print("=" * 70)

# Se imprime la cabecera de la tabla con los días de la semana
encabezado_dias = "  ".join(f"{d:>4}" for d in dias_semana)   # Formatea los días
print(f"{'Recurso':<18} {encabezado_dias}  {'Total':>6}  {'Clasificación'}")
print("-" * 70)

# Se recorre cada recurso (persona) del equipo con un ciclo for
for recurso in equipo:
    nombre       = recurso[0]     # Se extrae el nombre del recurso (columna 0)
    horas_diarias = recurso[1:]   # Se extraen las horas de lunes a viernes (columnas 1-5)

    # Se llama a la función para calcular total y clasificación
    total, clasificacion = calcular_horas_y_clasificar(horas_diarias)

    # Se formatea la fila de horas diarias para imprimir alineadas
    fila_horas = "  ".join(f"{h:>4}" for h in horas_diarias)

    # Se determina el símbolo de alerta si hay sobretiempo
    alerta = " ⚠" if clasificacion == "Sobretiempo" else "  "

    # Se imprime la fila completa del recurso con todos sus datos
    print(f"{nombre:<18} {fila_horas}  {total:>6}h  {clasificacion}{alerta}")

# --- RESUMEN ESTADÍSTICO DEL EQUIPO ---
print("=" * 70)
print("\n  RESUMEN ESTADÍSTICO DEL EQUIPO:")
print("-" * 40)

# Se calculan estadísticas generales recorriendo el equipo nuevamente
total_general = 0        # Suma total de horas de todo el equipo
en_sobretiempo = 0       # Contador de personas en sobretiempo

for recurso in equipo:
    nombre        = recurso[0]
    horas_diarias = recurso[1:]

    # Se llama nuevamente a la función para obtener datos de cada recurso
    total, clasificacion = calcular_horas_y_clasificar(horas_diarias)

    total_general += total    # Se acumula el total general

    # Se cuenta si este recurso está en sobretiempo
    if clasificacion == "Sobretiempo":
        en_sobretiempo += 1

# Se calcula el promedio de horas por persona
promedio = total_general / len(equipo)

# Se imprime el resumen con los datos estadísticos calculados
print(f"  Total de horas del equipo : {total_general}h")
print(f"  Promedio por persona      : {promedio:.1f}h")
print(f"  Personas en sobretiempo   : {en_sobretiempo} de {len(equipo)}")
print("-" * 40)
print("Informe generado por: Jean Carlos Redondo Cuadrado")
print("=" * 70)
