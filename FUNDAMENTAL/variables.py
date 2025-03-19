sueldoInicial = 500
sueldoAnual = 0
for mes in range(12):
    sueldoDelMes = sueldoInicial + mes * 5
    sueldoAnual += sueldoDelMes
    mes = 1
    print(f"El sueldo del mes {mes + 1} es: {sueldoDelMes}")

print(f"En todo el año, gané: {sueldoAnual}")