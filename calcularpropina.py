def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

def dividir_cuenta(total_pagar, numero_personas):
    return total_pagar / numero_personas

# Ejemplo de uso
total_cuenta = float(input("Ingresa el total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))
numero_personas = int(input("Ingresa el número de personas que compartirán la cuenta: "))

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)
total_por_persona = dividir_cuenta(total_pagar, numero_personas)

print(f"Debes dejar una propina de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")
print(f"Cada persona debe pagar: ${total_por_persona:.2f}")