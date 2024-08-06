import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

consumo1_ds = pd.read_csv("data/API_EG.USE.ELEC.KH.PC_DS2_es_csv_v2_834019.csv")

# Reemplazando los datos Null con N/A
consumo1_ds_filtered = consumo1_ds.fillna('N/A')
consumo1_ds_filtered.info()

column_rename_map = {
    "Country Name": "Pais",
    "Country Code": "Cod_Pais",
    "Indicator Name": "Unidad",
    "Indicator Code": "Cod_Unidad"
}
consumo1_ds_renombrado = consumo1_ds_filtered.rename(columns=column_rename_map)

consumo_paises = consumo1_ds_renombrado.iloc[:,4:68].sum(1) #Suma los valores de consumo de 1960 a 2023 de cada pais
consumo_paises_1 = consumo_paises.set_axis(consumo1_ds_renombrado.iloc[:,1])


df = consumo_paises_1.sort_values(ascending=False) #Organiza los paises de acuerdo a su consumo de mayor a menor
data_d =  consumo1_ds_renombrado.copy()
for pais in df[185:266].index:
    data_d = data_d.drop(data_d[data_d['Cod_Pais'] == pais].index)

print('____________________________________________________________')
ds = df.copy()
latino = pd.Index(['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'CRI', 'CUB', 'DOM', 'ECU', 'SLV', 'GTM', 'HTI', 'HND', 'MEX', 'NIC', 'PAN', 'PRY', 'PER', 'PRI', 'URY', 'VEN'])

ds = df.iloc[0:21].copy()
cont = 0
for pais in latino:
    ds.iloc[cont] = df[df.index == pais].copy()
    cont += 1

ds = ds.set_axis(latino)
ds = ds.sort_values(ascending=False)
print(ds)
