from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:

            if duracion <= 0:
                raise ReservaError(
                    "La duración debe ser mayor que cero."
                )

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"

        except Exception as e:

            raise ReservaError(
                "Error al crear la reserva."
            ) from e

    # CONFIRMAR

    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede confirmar una reserva cancelada."
            )

        self.estado = "Confirmada"

    # CANCELAR

    def cancelar(self):

        self.estado = "Cancelada"

    # PROCESAR

    def procesar(self):

        return (
            f"Reserva procesada para "
            f"{self.cliente.nombre}"
        )

    # MOSTRAR INFO

    def mostrar_reserva(self):

        return (
            f"\nCliente: {self.cliente.nombre}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDuración: {self.duracion}"
            f"\nEstado: {self.estado}"
        )