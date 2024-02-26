import requests
import csv
from datetime import datetime

def obtener_datos_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos de la API")
        return None

def guardar_en_csv(datos, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'time', 'temperature', 'wind_speed'])
        timestamp = datos['current']['time']
        date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M").date()
        time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M").time()
        writer.writerow([date, time, datos['current']['temperature_2m'], datos['current']['wind_speed_10m']])
    print(f"Datos guardados exitosamente en {filename}")

def main():
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=40.4165&longitude=-3.7026&current=temperature_2m,wind_speed_10m"
    datos = obtener_datos_api(api_url)
    if datos:
        guardar_en_csv(datos, 'datos_clima.csv')

if __name__ == "__main__":
    main()
