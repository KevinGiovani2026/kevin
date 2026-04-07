#ambito global
nombre_publico = "kevin"

def informacion_privada(nombre_publico):
    #ambito local
    nombre_privado = "Giovani"
    Apellido_privad =  "Ajxup"

    print(f"Mi nombre completo es: {nombre_privado} {Apellido_privad}")
    #print(f"mi nombre publico es: {nombre_publico}" )
    print(f"(local) mi nombre publico es:{nombre_publico}")

    nombre_publico = "Carlos"

    return nombre_publico

    #nombre = "kevin"
nombre_publico = informacion_privada(nombre_publico)

print(f'(global) Mi nombre  publico es:{nombre_publico}')