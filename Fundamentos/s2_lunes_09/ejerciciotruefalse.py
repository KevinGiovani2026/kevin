edad= int(input("cual es su edad:"))
vip = input("¿es usted un cliente vip")
ingresa = (edad == 18) and (vip == "si") 
#regla1 Puede entrar si es mayor de 18 anios
print(f"puede ingresar a la sala exclusiva  {ingresa}") 