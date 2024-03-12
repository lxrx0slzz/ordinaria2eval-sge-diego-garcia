import json

import pandas as pd

with open('secure-users.json', 'r') as arch:
    user_data = json.load(arch)

df = pd.DataFrame(user_data)

df.to_excel('usuarios.xlsx' , index = False)