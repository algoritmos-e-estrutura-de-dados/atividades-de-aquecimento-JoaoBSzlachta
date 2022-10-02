a = float(input())
b = float(input())
c = float(input())

triangulo = float((a * c) / 2)
circulo = float(3.14159 * (c**2))
trapezio = float(((a+b) * c) / 2)
quadrado = float(b**2)
retangulo = float(a * b)

print(f"TRIANGULO: {round(triangulo, 3)} \nCIRCULO: {round(circulo, 3)}")
print(f"TRAPEZIO: {round(trapezio, 3)} \nQUADRADO: {round(quadrado, 3)}")
print(f"RETANGULO: {round(retangulo, 3)}")