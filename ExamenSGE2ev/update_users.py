import json
import hashlib

with open('usuarios.json', 'r') as arch:
    users_data = json.load(arch)

numero = 12
identificador = format(id(numero), 'x')
print(identificador)

with open('secure-users.json', 'w')as arch:
    json.dump(users_data, arch)
    
for usuario in users_data:
    contraseña_act = 'SGE'
    hash_obj = hashlib.sha256()
    hash_obj.update(contraseña_act.encode('utf-8'))
    contraseña_hash = hash_obj.hexdigest()

print("Contraseña original: ",
    contraseña_act)
print("Contraseña hasheada: ",
      contraseña_hash)

