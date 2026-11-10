# Sistema para registrar pacientes y consultar sus datos.
# Se aplican conceptos de:
# Encapsulamiento
# Herencia
# Polimorfismo
# Composición

# --------------------------------------------------
# CLASE AUXILIAR PARA COMPOSICIÓN
# --------------------------------------------------
class SignosVitales:

    def __init__(self, temperatura, frecuencia_cardiaca):
        self.temperatura = temperatura
        self.frecuencia_cardiaca = frecuencia_cardiaca

    def mostrar_signos(self):
        return (
            f"Temperatura: {self.temperatura} °C | "
            f"Frecuencia cardiaca: {self.frecuencia_cardiaca} lpm"
        )


# --------------------------------------------------
# CLASE BASE
# --------------------------------------------------
class Paciente:

    def __init__(self, nombre, edad, diagnostico,
                 presion_arterial, signos_vitales):

        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

        # Aplicación de Encapsulamiento
        self.__presion_arterial = presion_arterial

        # Composición
        self.signos_vitales = signos_vitales

    # Getter
    def get_presion_arterial(self):
        return self.__presion_arterial

    # Setter
    def set_presion_arterial(self, nueva_presion):
        if nueva_presion != "":
            self.__presion_arterial = nueva_presion
        else:
            print("Error: la presión arterial no puede estar vacía.")

    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")

    def mostrar_edad(self):
        print(f"Edad: {self.edad} años")

    def mostrar_diagnostico(self):
        print(f"Diagnóstico: {self.diagnostico}")

    def mostrar_presion_arterial(self):
        print(f"Presión arterial: {self.__presion_arterial} mmHg")

    # Uso de la composición
    def mostrar_signos_vitales(self):
        print(self.signos_vitales.mostrar_signos())


# --------------------------------------------------
# SUBCLASE
# --------------------------------------------------
class PacienteHospitalizado(Paciente):

    def __init__(
            self,
            nombre,
            edad,
            diagnostico,
            presion_arterial,
            signos_vitales,
            habitacion,
            dias_internado):

        # Herencia y super()
        super().__init__(
            nombre,
            edad,
            diagnostico,
            presion_arterial,
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
