'''
 * Nombre: API.py
 * Programadora: Fernanda Esquivel (feresq.gt@gmail.com)
 * Lenguaje: Python
 * Recursos: VSCode, Swagger UI
 * Descripción: Programa que crea una API REST con endpoints para obtener data del archivo "polizas_clean.csv".
 * Historial de Modificaciones: 
    - Creación: 31.07.2025
    - Última modificación: 31.07.2025
'''

from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import pandas as pd

#Nombre del API
app = FastAPI(title="BSE Technical Test API REST")

#Cargar los datos limpios
df = pd.read_csv("data/polizas_clean.csv")

#Normalizar columnas (por si acaso)
df.columns = df.columns.str.strip().str.lower()

#Eliminar espacios extra en la columna sac
df["sac"] = df["sac"].astype(str).str.strip()

#Creación de endpoints
#GET /importaciones
@app.get("/importaciones")
def listImportaciones(skip: int = 0, limit: int = 10): #paginación
    data = df.iloc[skip:skip+limit].to_dict(orient="records") #devolver importaciones
    return {"total": len(df), "resultados": data}

#GET /importaciones/{correlativo}
@app.get("/importaciones/correlativo/{correlativo}")
#Función para obtener un registro por su correlativo
def getByCorrelativo(correlativo: int):
    row = df[df["correlativo"] == correlativo]
    if row.empty: #si no está el registro, se lanza un mensaje
        raise HTTPException(status_code=404, detail="Poliza no encontrada")
    return row.iloc[0].to_dict()

#GET /importaciones/{sac}
@app.get("/importaciones/sac/{sac}")
#Función para obtener un(os) registro(s) por su sac
def getBysac(sac: str, skip: int = 0, limit: int = 10):
    subset = df[df["sac"] == sac]
    data = subset.iloc[skip:skip+limit].to_dict(orient="records") #devolver todos los registros que coincidan
    return {"total": len(subset), "resultados": data}

#GET /estadisticas/por-pais
@app.get("/estadisticas/por-pais")
#Función para obtener registros por país
def sumarizeByPais():
    resumen = (
        df.groupby("pais")["valor_cif_uds"] #agrupar por país
        .sum() #sumar el valor del cif en dólares
        .reset_index()
        .rename(columns={"valor_cif_uds": "total_valor_cif_usd"}) #mostrar en una nueva columna
        .sort_values("total_valor_cif_usd", ascending=False)
    )
    return resumen.to_dict(orient="records")

#GET /estadisticas/por-aduana
@app.get("/estadisticas/por-aduana")
#Función para obtener registros por aduana
def sumarizeByAduana():
    resumen = (
        df.groupby("aduana")["valor_cif_uds"] #Agrupar por aduana
        .sum() #sumar el valor del cif en dólares
        .reset_index()
        .rename(columns={"valor_cif_uds": "total_valor_cif_usd"}) #mostrar en una nueva columna
        .sort_values("total_valor_cif_usd", ascending=False)
    )
    return resumen.to_dict(orient="records")
