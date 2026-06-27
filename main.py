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


# LISTAS DEL SISTEMA

clientes = []
servicios = []
reservas = []

# FUNCIÓN PARA REGISTRAR ERRORES Y EVENTOS

def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        archivo.write(
            f"[{fecha}] {mensaje}\n"
        )


print("\n======================================================")
print("      SISTEMA DE GESTIÓN DE CLIENTES Y RESERVAS")
print("======================================================\n")


# OPERACIÓN 1
# Registrar un cliente válido

print("OPERACIÓN 1 - Registrar cliente válido")

try:

    cliente1 = Cliente(
        "Leonardo Nieto",
        "Leonardo@gmail.com",
        "3111111111"
    )

    clientes.append(cliente1)

    print(cliente1)

except ClienteInvalidoError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 2
# Registrar cliente con nombre vacío

print("OPERACIÓN 2 - Cliente con nombre inválido")

try:

    cliente2 = Cliente(
        "",
        "correo@gmail.com",
        "3201234567"
    )

    clientes.append(cliente2)

except ClienteInvalidoError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 3
# Registrar cliente con correo inválido

print("OPERACIÓN 3 - Cliente con correo inválido")

try:

    cliente3 = Cliente(
        "Juan Pérez",
        "correo_invalido",
        "3201234567"
    )

    clientes.append(cliente3)

except ClienteInvalidoError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 4
# Registrar cliente con teléfono inválido

print("OPERACIÓN 4 - Cliente con teléfono inválido")

try:

    cliente4 = Cliente(
        "María Gómez",
        "maria@gmail.com",
        "ABC123"
    )

    clientes.append(cliente4)

except ClienteInvalidoError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 5
# Crear un servicio válido

print("OPERACIÓN 5 - Reserva de sala")

try:

    sala = ReservaSala(3)

    servicios.append(sala)

    print(sala.describir())

    print(
        f"Costo del servicio: "
        f"${sala.calcular_costo()}"
    )

except ServicioNoDisponibleError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 6
# Servicio inválido

print("OPERACIÓN 6 - Servicio con duración inválida")

try:

    sala_error = ReservaSala(-2)

    servicios.append(sala_error)

except ServicioNoDisponibleError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 7
# Crear un alquiler de equipo válido

print("OPERACIÓN 7 - Alquiler de equipo")

try:

    equipo = AlquilerEquipo(5)

    servicios.append(equipo)

    print(equipo.describir())

    print(
        f"Costo del servicio: "
        f"${equipo.calcular_costo()}"
    )

except ServicioNoDisponibleError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 8
# Crear una asesoría válida

print("OPERACIÓN 8 - Asesoría especializada")

try:

    asesoria = AsesoriaEspecializada(2)

    servicios.append(asesoria)

    print(asesoria.describir())

    print(
        f"Costo del servicio: "
        f"${asesoria.calcular_costo()}"
    )

except ServicioNoDisponibleError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")

# OPERACIÓN 9
# Crear una reserva válida

print("OPERACIÓN 9 - Crear reserva válida")

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    reservas.append(reserva1)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

except ReservaError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# OPERACIÓN 10
# Crear una reserva inválida

print("OPERACIÓN 10 - Reserva inválida")

try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -1
    )

    reservas.append(reserva2)

except ReservaError as e:

    print("ERROR:", e)
    registrar_log(e)


print("\n------------------------------------------------------")


# COSTO NORMAL

print("PRUEBA - COSTO NORMAL")

try:

    print(
        f"Costo normal: "
        f"${sala.calcular_costo()}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


print("\n------------------------------------------------------")


# COSTO CON DESCUENTO

print("PRUEBA - COSTO CON DESCUENTO")

try:

    print(
        f"Costo con descuento: "
        f"${sala.calcular_costo_final(descuento=10)}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


print("\n------------------------------------------------------")


# COSTO CON IMPUESTO

print("PRUEBA - COSTO CON IMPUESTO")

try:

    print(
        f"Costo con impuesto: "
        f"${sala.calcular_costo_final(impuesto=19)}"
    )

except CostoError as e:

    print(e)
    registrar_log(e)


print("\n------------------------------------------------------")


# TRY - EXCEPT - ELSE

print("PRUEBA TRY - EXCEPT - ELSE")

try:

    equipo2 = AlquilerEquipo(7)

    servicios.append(equipo2)

except Exception as e:

    print(e)

else:

    print(
        "El bloque ELSE se ejecutó correctamente."
    )


print("\n------------------------------------------------------")

# TRY - FINALLY

print("PRUEBA TRY - FINALLY")

try:

    asesoria2 = AsesoriaEspecializada(1)

    servicios.append(asesoria2)

finally:

    print(
        "El bloque FINALLY siempre se ejecuta."
    )


print("\n------------------------------------------------------")

# LISTAR CLIENTES

print("CLIENTES REGISTRADOS")

for cliente in clientes:

    print(cliente)


print("\n------------------------------------------------------")


# LISTAR SERVICIOS

print("SERVICIOS REGISTRADOS")

for servicio in servicios:

    print(servicio.nombre)


print("\n------------------------------------------------------")

# LISTAR RESERVAS

print("RESERVAS REGISTRADAS")

for reserva in reservas:

    print(reserva.mostrar_reserva())


print("\n------------------------------------------------------")

# RESUMEN FINAL

print("======================================================")
print("RESUMEN GENERAL DEL SISTEMA")
print("======================================================")

print(f"Clientes registrados : {len(clientes)}")
print(f"Servicios registrados: {len(servicios)}")
print(f"Reservas registradas : {len(reservas)}")


print("\n======================================================")
print("TODAS LAS PRUEBAS FUERON EJECUTADAS")
print("======================================================")