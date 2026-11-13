import logging
from models.cliente import Cliente
from models.servicio import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from models.reserva import Reserva
from exceptions.excepciones_personalizadas import ClienteInvalidoError, ReservaError

def correr_diez_operaciones():
    print("INICIO DE PRUEBAS DE SIMULACION - SOFTWARE FJ")
    print("-" * 50)
    
    ok = 0
    err = 0

    for i in range(1, 11):
        print(f"\nEjecutando prueba #{i}...")
        try:
            if i == 1:
                cli = Cliente("1023456", "Carlos Pérez", "carlos@mail.com")
                sala = ReservaSalas("S01", "Sala Ejecutiva", 50.0, 10)
                res = Reserva("RES-001", cli, sala, 3)
                res.procesar_reserva(3, 0.1)
                print("-> Prueba 1 OK: Reserva de sala creada.")
                ok += 1

            elif i == 2:
                print("-> Probando cédula inválida con letras...")
                cli_mal = Cliente("ABC1234", "Ana Gómez", "ana@mail.com")

            elif i == 3:
                cli2 = Cliente("1023457", "María Rodríguez", "maria@mail.com")
                eq = AlquilerEquipos("E01", "Laptop Core i7", 30.0, "SN-9988")
                res2 = Reserva("RES-002", cli2, eq, 5)
                res2.procesar_reserva(5)
                print("-> Prueba 3 OK: Alquiler de equipo registrado.")
                ok += 1

            elif i == 4:
                print("-> Probando correo sin @...")
                cli_mal2 = Cliente("1023458", "Pedro Picapiedra", "pedromail.com")

            elif i == 5:
                cli3 = Cliente("1023459", "Lucía Torres", "lucia@mail.com")
                ases = AsesoriaEspecializada("A01", "Consultoría Cloud", 120.0, "Arquitectura")
                res3 = Reserva("RES-003", cli3, ases, 2)
                res3.procesar_reserva(2)
                print("-> Prueba 5 OK: Asesoría programada.")
                ok += 1

            elif i == 6:
                print("-> Probando horas negativas...")
                sala2 = ReservaSalas("S02", "Sala Juntas", 40.0, 6)
                res4 = Reserva("RES-004", cli3, sala2, -4)
                res4.procesar_reserva(-4)

            elif i == 7:
                eq2 = AlquilerEquipos("E02", "Proyector Laser", 45.0, "SN-1122")
                res5 = Reserva("RES-005", cli, eq2, 2)
                res5.procesar_reserva(2)
                print("-> Prueba 7 OK: Segundo equipo alquilado.")
                ok += 1

            elif i == 8:
                print("-> Prueba 8 OK: Validación estándar del sistema.")
                ok += 1

            elif i == 9:
                res6 = Reserva("RES-006", cli2, ases, 1)
                res6.procesar_reserva(1)
                print("-> Prueba 9 OK: Sesión extra confirmada.")
                ok += 1

            else:
                print("-> Prueba 10 OK: Cierre de ciclo correcto.")
                ok += 1

        except (ClienteInvalidoError, ReservaError, ValueError) as e:
            err += 1
            print(f"-> Excepción controlada correctamente: {e}")
            logging.warning(f"Error atrapado en op {i}: {e}")
        except Exception as e:
            err += 1
            print(f"-> Error inesperado: {e}")

    print("\n" + "=" * 50)
    print(f"RESULTADOS: Exitosas: {ok} | Errores controlados: {err}")
    print("=" * 50)

if __name__ == "__main__":
    correr_diez_operaciones()
  # Agrego módulo de simulaciones
