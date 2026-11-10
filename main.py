
from modelos import SignosVitales, Paciente, PacienteHospitalizado


# Instanciación de objetos de Composición (SignosVitales)
signos_p1 = SignosVitales("110/70", 72, 36.5)
signos_p2 = SignosVitales("140/90", 85, 37.0)
signos_p3 = SignosVitales("120/80", 78, 36.8)


# Instanciación de Pacientes integrando la Composición
paciente1 = Paciente(
    "Graciela",
    60,
    "Hepatitis",
    signos_p1
)

paciente2 = PacienteHospitalizado(
    "Alejandro",
    47,
    "Hipertensión",
    signos_p2,
    "201A",
    5
)

paciente3 = PacienteHospitalizado(
    "Monserrat",
    46,
    "Diabetes",
    signos_p3,
    "305B",
    3
)


# PRUEBAS DE EJECUCIÓN

print("PACIENTE 1")
paciente1.mostrar_nombre()
paciente1.mostrar_edad()
paciente1.mostrar_diagnostico()
paciente1.mostrar_signos_vitales()

print("PACIENTE 2")
paciente2.mostrar_nombre()
paciente2.mostrar_edad()
paciente2.mostrar_diagnostico()
paciente2.mostrar_signos_vitales()
paciente2.mostrar_hospitalizacion()

print("PACIENTE 3")
paciente3.mostrar_nombre()
paciente3.mostrar_edad()
paciente3.mostrar_diagnostico()
paciente3.mostrar_signos_vitales()
paciente3.mostrar_hospitalizacion()

print("DEMOSTRACIÓN DE ENCAPSULAMIENTO")

print(
    f"Presión original: "
    f"{paciente1.signos_vitales.get_presion_arterial()}"
)

paciente1.signos_vitales.set_presion_arterial("115/75")

print("Presión actualizada:")
paciente1.mostrar_signos_vitales()
