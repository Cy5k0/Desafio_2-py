#resp: variable que acepta la respuesta a ingresar datos nuevamente
#W : corresponde al peso de la persona en Kg.
#H: corresponde a la altura en metros.
#IMC: EL valor del IMC, en [Kg/m2]

#tupla con los rangos de valores
#valor minimo se asumió como 0 y el maximo como indeterminado
rangos_imc = [
    (0, 18.5, "Bajo Peso"),        # Para valores menores a 18.5
    (18.5, 25, "Adecuado"),           # Para el rango [18.5, 25)
    (25, 30, "Sobrepeso"),            # Para el rango [25, 30)
    (30, 35, "Obesidad Grado I"),     # Para el rango [30, 35)
    (35, 40, "Obesidad Grado II"),    # Para el rango [35, 40)
    (40, None, "Obesidad Grado III")  # Para valores mayores a 40
]



