from abc import ABC, abstractmethod
from excepciones import (
    ServicioNoDisponibleError,
    CostoError
)


# CLASE ABSTRACTA

class Servicio(ABC):

    def __init__(self, nombre):

        if not nombre.strip():
            raise ServicioNoDisponibleError(
                "El servicio debe tener un nombre."
            )

        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    # Método con parámetros opcionales
    def calcular_costo_final(
        self,
        descuento=0,
        impuesto=0
    ):

        costo = self.calcular_costo()

        if descuento < 0:
            raise CostoError(
                "El descuento no puede ser negativo."
            )

        costo -= costo * (descuento / 100)
        costo += costo * (impuesto / 100)

        return round(costo, 2)


# RESERVA DE SALA

class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ServicioNoDisponibleError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas

    def calcular_costo(self):

        return self.horas * 50000

    def describir(self):

        return (
            f"Sala reservada durante "
            f"{self.horas} horas."
        )


# ALQUILER DE EQUIPO

class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipo")

        if dias <= 0:
            raise ServicioNoDisponibleError(
                "Los días deben ser mayores que cero."
            )

        self.dias = dias

    def calcular_costo(self):

        return self.dias * 30000

    def describir(self):

        return (
            f"Equipo alquilado durante "
            f"{self.dias} días."
        )


# ASESORÍA ESPECIALIZADA


class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):

        super().__init__("Asesoría Especializada")

        if horas <= 0:
            raise ServicioNoDisponibleError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas

    def calcular_costo(self):

        return self.horas * 80000

    def describir(self):

        return (
            f"Asesoría especializada durante "
            f"{self.horas} horas."
        )