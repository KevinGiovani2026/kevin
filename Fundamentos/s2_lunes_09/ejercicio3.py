print("Bienvenidos a la tienda")

#datos del clinente
cliente_vip = True
articulos_comprados = 6
dia_semana = "lunes"

#regla1: descuento mayorista si compra mas de 5 articulos y es VIP
aplica_mayorista = (articulos_comprados > 5) and (cliente_vip == True)
print(f"¿Aplica descuento mayorista? {aplica_mayorista}")

#regla 2: descuentos especiales de lunes si es lunes o es vip
descuento = (dia_semana == "lunes") or (cliente_vip == true)
print(f"¿Aplica descuento especial {descuento}")

#regla 3: verificar que la tienda no este cerrada
tienda_cerrada = False
podemos_vender = not tienda_cerrada
print (f'¿podemos vender? {podemos_vender}')
