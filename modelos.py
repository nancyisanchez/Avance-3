# Sistema para registrar pacientes y consultar sus datos.
# Se aplican conceptos de:
# - Encapsulamiento
# - Herencia
# - Polimorfismo
# - Composición


# --------------------------------------------------
# CLASE AUXILIAR PARA COMPOSICIÓN
# --------------------------------------------------
class SignosVitales:

    def __init__(self, presion_arterial, frecuencia_cardiaca, temperatura):

        # Encapsulamiento
        self._presion_arterial = presion_arterial

        self.frecuencia_cardiaca = frecuencia_cardiaca
        self.temperatura = temperatura

    def get_presion_arterial(self):
        return self._presion_arterial

    def set_presion_arterial(self, nueva_presion):
        if nueva_presion != "":
            self._presion_arterial = nueva_presion
        else:
            print("Error: la presión arterial no puede estar vacía.")

    def obtener_resumen(self):
        return (
            f"Presión arterial: {self._presion_arterial} mmHg | "
            f"Frecuencia cardiaca: {self.frecuencia_cardiaca} bpm | "
            f"Temperatura: {self.temperatura} °C"
        )


# --------------------------------------------------
# CLASE BASE
# --------------------------------------------------
class Paciente:

    def __init__(self, nombre, edad, diagnostico, signos_vitales):

        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

        # Composición:
        # Un Paciente tiene un objeto SignosVitales
        self.signos_vitales = signos_vitales

    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")

    def mostrar_edad(self):
        print(f"Edad: {self.edad} años")

    def mostrar_diagnostico(self):
        print(f"Diagnóstico: {self.diagnostico}")

    def mostrar_signos_vitales(self):
        print(
            f"Signos Vitales: "
            f"{self.signos_vitales.obtener_resumen()}"
        )


# --------------------------------------------------
# SUBCLASE
# --------------------------------------------------
class PacienteHospitalizado(Paciente):

    def __init__(
        self,
        nombre,
        edad,
        diagnostico,
        signos_vitales,
        habitacion,
        dias_internado
    ):

        # Uso de super() y Herencia
        super().__init__(
            nombre,
            edad,
            diagnostico,
            signos_vitales
        )

        self.habitacion = habitacion
        self.dias_internado = dias_internado

    def mostrar_hospitalizacion(self):
        print(
            f"Habitación: {self.habitacion} | "
            f"Días internado: {self.dias_internado}"
        )

    # Polimorfismo
    def mostrar_diagnostico(self):
        print(
            f"Diagnóstico: {self.diagnostico} | "
            f"Habitación: {self.habitacion} | "
            f"Días internado: {self.dias_internado}"
        )
