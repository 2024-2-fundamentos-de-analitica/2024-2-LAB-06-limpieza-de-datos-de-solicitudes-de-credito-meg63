"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd

def pregunta_01():
    data= pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    
    #Limpiar la columna sexo
    # Ver los valores distintos que hay en sexo
    data["sexo"] = data["sexo"].str.lower()


    # Limpiar emprendimiento
    data["tipo_de_emprendimiento"] = data["tipo_de_emprendimiento"].str.lower()
    data["tipo_de_emprendimiento"] = data["tipo_de_emprendimiento"].str.strip()
    


    # Limpiar barrio
    data["barrio"] = data["barrio"].str.lower()
    data["barrio"] = data["barrio"].str.replace("_", " ")
    data["barrio"] = data["barrio"].str.replace("-", " ")
    #data["barrio"] = data["barrio"].str.replace(".", " ")
    #data["barrio"] = data["barrio"].str.strip()
 
    

    


    # Limpiar idea_negocio
    data["idea_negocio"] = data["idea_negocio"].str.lower()
    data["idea_negocio"] = data["idea_negocio"].str.replace("_", " ")
    data["idea_negocio"] = data["idea_negocio"].str.replace("-", " ")
    data["idea_negocio"] = data["idea_negocio"].str.strip()
    


    


    


    # Limpiar monto credito
    data["monto_del_credito"] = data["monto_del_credito"].str.strip()
    data["monto_del_credito"] = data["monto_del_credito"].str.replace("$","")
    data["monto_del_credito"] = data["monto_del_credito"].str.replace(",","")
    data["monto_del_credito"] = data["monto_del_credito"].str.replace(".00","")
    data["monto_del_credito"] = data["monto_del_credito"].astype(int)


    
   
   # Limpiar linea credito
    data["línea_credito"] = data["línea_credito"].str.lower()
    data["línea_credito"] = data["línea_credito"].str.strip()
    data["línea_credito"] = data["línea_credito"].str.replace("_", " ")
    data["línea_credito"] = data["línea_credito"].str.replace("-", " ")
    data["línea_credito"] = data["línea_credito"].str.strip()
   
 
    # Limpiar fecha
    data["fecha_de_beneficio"] = pd.to_datetime(
            data["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(pd.to_datetime(data["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    


    # Limpiar comuna
    data["comuna_ciudadano"] = data["comuna_ciudadano"].astype(int)
   

    data=data.drop_duplicates()
    data=data.dropna()
 


    data.to_csv("files/output/solicitudes_de_credito.csv", sep=";")
   
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
pregunta_01()