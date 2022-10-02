codProd1 = int(input())
qtdProd1 = int(input())
priceProd1 = float(input())

codProd2 = int(input())
qtdProd2 = int(input())
priceProd2 = float(input())

valorPagar = float((qtdProd1 * priceProd1) + (qtdProd2 * priceProd2))
print (f"VALOR A PAGAR: R$ {round(valorPagar, 2)}")