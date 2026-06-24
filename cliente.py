from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, correo, telefono):

        self.validar_nombre(nombre)
        self.validar_correo(correo)
        self.validar_telefono(telefono)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # VALIDACIONES

    def validar_nombre(self, nombre):

        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre nunca debe estar vacío."
            )

    def validar_correo(self, correo):

        if "@" not in correo:
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )

    def validar_telefono(self, telefono):

        if not telefono.isdigit():
            raise ClienteInvalidoError(
                "El teléfono debe contener únicamente números."
            )

        if len(telefono) < 10:
            raise ClienteInvalidoError(
                "El teléfono debe tener mínimo 10 dígitos."
            )

    # PROPERTIES

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # MÉTODOS

    def mostrar_datos(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):

        return self.mostrar_datos()