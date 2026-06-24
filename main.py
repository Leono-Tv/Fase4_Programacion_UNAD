from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError,
    CostoError
)

from datetime import datetime


# LOGS

def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        fecha = datetime.now()

        archivo.write(
            f"[{fecha}] {mensaje}\n"
        )


print("\n===================================")
print("SISTEMA DE GESTIÓN SOFTWARE FJ")
print("===================================\n")


# ==========================================
# OPERACIÓN 1
# Cliente válido
# ==========================================

try:

    cliente1 = Cliente(
        "Leonardo Nieto",
        "Leonardo@gmail.com",
        "3111111111"
    )

    print(cliente1)

except ClienteInvalidoError as e:

    print(e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 2
# Cliente inválido
# ==========================================

try:

    cliente2 = Cliente(
        "",
        "correo@gmail.com",
        "3111111111"
    )

except ClienteInvalidoError as e:

    print("\nERROR:", e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 3
# Correo inválido
# ==========================================

try:

    cliente3 = Cliente(
        "Juan",
        "correo_invalido",
        "3111111111"
    )

except ClienteInvalidoError as e:

    print("\nERROR:", e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 4
# Servicio válido
# ==========================================

try:

    sala = ReservaSala(3)

    print("\n" + sala.describir())

except ServicioNoDisponibleError as e:

    print(e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 5
# Servicio inválido
# ==========================================

try:

    sala_error = ReservaSala(-2)

except ServicioNoDisponibleError as e:

    print("\nERROR:", e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 6
# Reserva válida
# ==========================================

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    reserva1.confirmar()

    print(
        "\n" +
        reserva1.mostrar_reserva()
    )

except ReservaError as e:

    print(e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 7
# Reserva inválida
# ==========================================

try:

    reserva_error = Reserva(
        cliente1,
        sala,
        -1
    )

except ReservaError as e:

    print("\nERROR:", e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 8
# Costo normal
# ==========================================

try:

    print(
        f"\nCosto normal: "
        f"${sala.calcular_costo()}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 9
# Costo con descuento
# ==========================================

try:

    print(
        f"Costo con descuento: "
        f"${sala.calcular_costo_final(descuento=10)}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


# ==========================================
# OPERACIÓN 10
# Costo con impuesto
# ==========================================

try:

    print(
        f"Costo con impuesto: "
        f"${sala.calcular_costo_final(impuesto=19)}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


# ==========================================
# TRY - EXCEPT - ELSE
# ==========================================

try:

    equipo = AlquilerEquipo(5)

except Exception as e:

    print(e)

else:

    print(
        "\nELSE ejecutado correctamente."
    )


# ==========================================
# TRY - FINALLY
# ==========================================

try:

    asesoria = AsesoriaEspecializada(2)

finally:

    print(
        "\nFINALLY ejecutado."
    )


print("\n===================================")
print("FIN DE LAS PRUEBAS")
print("===================================\n")