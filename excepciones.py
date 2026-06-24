
# Excepciones 

class ClienteInvalidoError(Exception):
    """Error relacionado con datos inválidos del cliente."""
    pass


class ServicioNoDisponibleError(Exception):
    """Error relacionado con servicios no disponibles."""
    pass


class ReservaError(Exception):
    """Error relacionado con reservas."""
    pass


class CostoError(Exception):
    """Error relacionado con cálculos de costos."""
    pass