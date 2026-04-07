print("Bievenido a la tienda")
nombre_producto = input("ingrese el nombre del producto:")
precio_producto = float(input("ingrese el precio del producto:"))
cantidad_producto = int(input("ingrese la cantidad del producto:"))


valor1 = precio_producto*cantidad_producto
tax = float(0.15)
impuesto = valor1*tax
Total = valor1+impuesto

print("informacion de la factura ")
print("nombre del producto:", nombre_producto)
print("precio del producto:", precio_producto)
print("cantidad del producto:", cantidad_producto)
print("subtotal",valor1)
print("impuesto",impuesto)
print("Total",Total)

