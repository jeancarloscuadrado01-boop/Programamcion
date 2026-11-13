"""Escenarios de simulación del sistema de gestión de Software FJ."""

from exceptions.excepciones_personalizadas import DatoInvalidoError, ReservaError
from models.cliente import Cliente
from models.reserva import Reserva
from models.servicio_asesoria import AsesoriaEspecializada
from models.servicio_equipos import AlquilerEquipos
from models.servicio_salas import ReservaSalas
from utils.logger import logger


def crear_cliente(documento="1023456", nombre="Carlos Pérez",
                  correo="carlos@mail.com", telefono="3001234567"):
    return Cliente(documento, nombre, correo, telefono)


# Escenarios válidos

def reserva_sala():
    sala = ReservaSalas("S01", "Sala Ejecutiva", 50.0, 10)
    reserva = Reserva("RES-001", crear_cliente(), sala, 3)
    reserva.confirmar()
    reserva.procesar()


def alquiler_equipo():
    cliente = crear_cliente("1023457", "María Rodríguez", "maria@mail.com", "3009876543")
    equipo = AlquilerEquipos("E01", "Laptop Core i7", 30.0, "SN-9988")
    reserva = Reserva("RES-002", cliente, equipo, 5)
    reserva.confirmar()
    reserva.procesar()


def asesoria_especializada():
    cliente = crear_cliente("1023459", "Lucía Torres", "lucia@mail.com", "3005554433")
    asesoria = AsesoriaEspecializada("A01", "Consultoría Cloud", 120.0, "Arquitectura")
    reserva = Reserva("RES-003", cliente, asesoria, 2)
    reserva.confirmar()
    reserva.procesar()


def cancelar_reserva():
    equipo = AlquilerEquipos("E02", "Proyector Laser", 45.0, "SN-1122")
    reserva = Reserva("RES-004", crear_cliente(), equipo, 2)
    reserva.confirmar()
    reserva.cancelar()


def costos_por_servicio():
    servicios = [
        ReservaSalas("S02", "Sala Juntas", 40.0, 6),
        AlquilerEquipos("E03", "Cámara 4K", 25.0, "SN-3344"),
        AsesoriaEspecializada("A02", "Asesoría Datos", 100.0, "Analítica"),
    ]
    for servicio in servicios:
        print(f"   {type(servicio).__name__}: {servicio.calcular_costo(2)}")


# Escenarios inválidos

def documento_invalido():
    crear_cliente(documento="ABC1234")


def correo_invalido():
    crear_cliente(correo="carlosmail.com")


def nombre_vacio():
    crear_cliente(nombre="")


def telefono_invalido():
    crear_cliente(telefono="12ab")


def horas_negativas():
    sala = ReservaSalas("S03", "Sala Mini", 20.0, 4)
    Reserva("RES-005", crear_cliente(), sala, -4)


def procesar_sin_confirmar():
    sala = ReservaSalas("S04", "Sala Auxiliar", 30.0, 5)
    Reserva("RES-006", crear_cliente(), sala, 1).procesar()


def cancelar_dos_veces():
    sala = ReservaSalas("S05", "Sala Taller", 30.0, 5)
    reserva = Reserva("RES-007", crear_cliente(), sala, 1)
    reserva.cancelar()
    reserva.cancelar()


# Cada escenario: (descripción, función, excepción esperada o None)
ESCENARIOS = [
    ("Reserva de sala confirmada y procesada", reserva_sala, None),
    ("Alquiler de equipo", alquiler_equipo, None),
    ("Asesoría especializada", asesoria_especializada, None),
    ("Cancelación de una reserva", cancelar_reserva, None),
    ("Cálculo de costos por tipo de servicio", costos_por_servicio, None),
    ("Documento con letras", documento_invalido, DatoInvalidoError),
    ("Correo sin arroba", correo_invalido, DatoInvalidoError),
    ("Nombre vacío", nombre_vacio, DatoInvalidoError),
    ("Teléfono inválido", telefono_invalido, DatoInvalidoError),
    ("Horas negativas", horas_negativas, ReservaError),
    ("Procesar sin confirmar", procesar_sin_confirmar, ReservaError),
    ("Cancelar dos veces", cancelar_dos_veces, ReservaError),
]


def ejecutar_simulaciones():
    logger.info("Inicio de simulaciones")
    print("SIMULACIONES - SOFTWARE FJ")
    print("-" * 50)

    exitosas = controladas = fallidas = 0

    for numero, (descripcion, escenario, esperada) in enumerate(ESCENARIOS, start=1):
        print(f"\n[{numero}/{len(ESCENARIOS)}] {descripcion}")
        try:
            escenario()
        except Exception as error:
            if esperada is not None and isinstance(error, esperada):
                controladas += 1
                print(f"   Error controlado: {error}")
                logger.warning("Escenario %d (%s): %s", numero, descripcion, error)
            else:
                fallidas += 1
                print(f"   Error inesperado: {type(error).__name__}: {error}")
                logger.exception("Escenario %d (%s) falló", numero, descripcion)
        else:
            if esperada is None:
                exitosas += 1
                print("   Correcto")
                logger.info("Escenario %d (%s) exitoso", numero, descripcion)
            else:
                fallidas += 1
                print(f"   No se lanzó la excepción esperada ({esperada.__name__})")
                logger.error("Escenario %d (%s): no lanzó %s",
                             numero, descripcion, esperada.__name__)
        finally:
            logger.info("Escenario %d finalizado", numero)

    print("\n" + "=" * 50)
    print(f"Exitosas: {exitosas} | Errores controlados: {controladas} | Fallidas: {fallidas}")
    print("Detalle completo en logs/app.log")
    logger.info("Fin de simulaciones")
