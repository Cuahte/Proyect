import pandas as pd
class Registro:
    def __init__(self, registro_file, municipio, ano, mes):
        self.municipio = municipio
        self.ano = ano
        self.mes = mes
        self.basename = municipio + '_' + ano + '_' + mes 
        self.registro_excel = pd.read_excel(registro_file, skiprows = 5, shetname = 'Informacion')
        self.columnas = [' Ejercicio',\
        ' Tipo de Acto Jurídico (catálogo)',\
        ' Objeto de La Realización Del Acto Jurídico',\
        ' Sector Al Cual Se Otorgó El Acto Jurídico (catálogo)',\
        ' Monto Total O Beneficio, Servicio Y/o Recurso Público Aprovechado',\
        ' Monto Entregado, Bien, Servicio Y/o Recurso Público Aprovechado Al Periodo Que Se Informa',\
        ' Se Realizaron Convenios Modificatorios (catálogo)']
    #df de cantidad de ejercicios realizados
    def get_df_Ejercicio(self):
        values_counts = self.registro_excel[' Ejercicio'].value_counts(dropna = True, sort = True)
        df = values_counts.rename_axis('año').reset_index(name="cantidad")
        return df

    #df de cantidad de tipos de actos juridicos
    def get_df_TipoActoJuridico(self):
        values_counts = self.registro_excel[' Tipo de Acto Jurídico (catálogo)'].value_counts(dropna = True, sort = True)
        df = values_counts.rename_axis('tipo de acto juridico').reset_index(name="cantidad")
        return df

    def get_df_ObjetoActoJuridico(self):
        values_counts = self.registro_excel[' Objeto de La Realización Del Acto Jurídico'].value_counts(dropna = True, sort = True)
        df = values_counts.rename_axis('objeto de acto juridico').reset_index(name="cantidad")
        return df

    #df de cantidad de tipos de sectores
    def get_df_SectorActoJurico(self):
        values_counts = self.registro_excel[' Sector Al Cual Se Otorgó El Acto Jurídico (catálogo)'].value_counts(dropna = True, sort = True)
        df = values_counts.rename_axis('sector').reset_index(name="cantidad")
        return df

    #df de monto bene
    def get_df_MontoAprovechado(self):
        prom_value = self.registro_excel[' Monto Total O Beneficio, Servicio Y/o Recurso Público Aprovechado'].mean()
        data = [[self.mes, prom_value]]
        df = pd.DataFrame(data, columns = ['mes', 'monto'])
        return df

    def get_df_MontoEntregado(self):
        prom_value = self.registro_excel[' Monto Entregado, Bien, Servicio Y/o Recurso Público Aprovechado Al Periodo Que Se Informa'].mean()
        data = [[self.mes, prom_value]]
        df = pd.DataFrame(data, columns = ['mes', 'monto'])
        return df

    #df de convenios modificados
    def get_df_convenios(self):
        values_counts = self.registro_excel[' Se Realizaron Convenios Modificatorios (catálogo)'].value_counts(dropna = True, sort = True)
        df = values_counts.rename_axis('modificiacion convenio').reset_index(name="cantidad")
        return df

    #def base_name_csv(self):
    #    return csv_nombre = self.basename + '.csv'