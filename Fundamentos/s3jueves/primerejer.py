cliente = { "nombre":"kevin", "edad":28, "ciudad" : "Guatemala"}
print (cliente["nombre"])
print(cliente["edad"])
print (cliente["ciudad"])

cliente["ciudad"] = "Nashville"
#------------------------------
#si vendi un arroz voy a actualizar

cliente["edad"] = cliente["edad"] + 1 
print(cliente)