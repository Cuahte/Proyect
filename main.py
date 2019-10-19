from Regs import Registro
import pandas as pd

registro = Registro("info_cuerna_agosto.xls", "cuernavaca", "2019", "agosto")

def df_to_csv(nombre, df):
    csv_nombre = nombre + ".csv"
    dfcsv = df
    dfcsv.to_csv(csv_nombre, index = None, header=True)
    
df_to_csv("ejercicio",registro.get_df_Ejercicio())
df_to_csv("tipoacto",registro.get_df_TipoActoJuridico())
df_to_csv("objetoacto",registro.get_df_ObjetoActoJuridico())
df_to_csv("sector",registro.get_df_SectorActoJurico())
df_to_csv("montoentregado",registro.get_df_MontoEntregado())
df_to_csv("montototal",registro.get_df_MontoAprovechado())
df_to_csv("convenios",registro.get_df_convenios())

