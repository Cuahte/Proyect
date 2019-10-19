import pandas as pd
#from pandas import ExcelFile
xls=pd.read_excel('Ayuntamiento de Amacuzac.xls', skiprows=5)
#print(xls.columns)
values = xls['ID'].values

#print(values)
columnas = ['ID', ' Ejercicio', ' Fecha de Inicio Del Periodo Que Se Informa']
df_seleccionados = xls[columnas]
#print(df_seleccionados)

#ejerc=xls[" Ejercicio"]
fech_inic=xls[" Fecha de Inicio Del Periodo Que Se Informa"]
print(identif)
#print(ejerc)
print(fech_inic)
"""
print(xls.sheet_names)
#print("test")
info=xls.parse('Informacion')
print(info)


identificador= info['Ejercicio']
print(ID)"""