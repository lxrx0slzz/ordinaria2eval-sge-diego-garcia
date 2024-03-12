import json
import pandas as pd

with open('secure-users.json', 'r') as arch:
    reservas_data = json.load(arch)

df_reservas = pd.DataFrame(reservas_data)

with open('secure-users.json', 'r') as arch:
    users_data = json.load(arch)

df_reservas.to_excel('reservas.xlsx', index = False)