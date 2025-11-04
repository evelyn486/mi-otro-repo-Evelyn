x = float(input("Ingresa el precio de el articulo: "))
S = (x + 500)* 25
if S>50000:
    DE = S * 0.25
else:
    DE = S * 0.15
PF = S - DE
print(f"El precio final es de: ", PF)
print(f"El descuento aplicado es de: ", DE)
# Evelyn Martinez Vazquez Grupo_201