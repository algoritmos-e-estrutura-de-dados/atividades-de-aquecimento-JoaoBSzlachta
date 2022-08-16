nome = str(input())
salarioFixo = float(input())
totalVendas = float(input())

salarioComBonus = float((totalVendas * 0.15) + salarioFixo)

print(f"TOTAL = {round(salarioComBonus, 2)} ")