mi_lista_semana = [
    ['arroz','frijoles','lentejas'],
    ['atun','sardina','sopa'],
    ['agua','jugo','gaseosa'], 
]

#print(mi_lista_semana [1])


producto_buscado = mi_lista_semana [1][1]
print('producto extraido:', producto_buscado)

print('bebida extraida :', mi_lista_semana[2][0])

#El jugo se agoto , pondresmos te

mi_lista_semana[2][1] = "te"
print("fila de bebidas actualizada:" , mi_lista_semana)


#///////////////////////////////////////////////////////

#recorrer una matriz
# for fila in range(mi_lista_semana): #no esta funcionando
#     for elemnto in fila:
#         print(elemnto)

