import requests as requests

from socket import gethostbyname, create_connection, error

onlineConnection = "false"

def conexion():

    tecla = "w"


    while tecla!="s" and tecla!="S":
        ciudad = input("Introduzca el nombre de una ciudad:")
        comprobarConexionInternet()
        if(onlineConnection == "false"):
            continue

        # Creamos un diccionario con los parámetros de la URL
        parametros = {"q": ciudad,
                      "units": "metric",
                      "APPID": "89b9fdb6f95944991fd97b6727d65c78"}

        print("\n")
        # Realizamos la petición, indicando la URL y los parámetros
        respuesta = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parametros)

        # Si la respuesta devuelve el código de estado 200, todo ha ido bien
        if respuesta.status_code == 200:
            # La respuesta json se convierte en un diccionario
            datos = respuesta.json()
            # Obtenemos descripción del tiempo del diccionario y la traducimos al español
            estadoTiempo = datos["weather"][0]["main"]

            if estadoTiempo == "Clear":
                imprimirDatos(datos, "Despejado")
            elif estadoTiempo == "Clouds":
                imprimirDatos(datos, "Nubes")
            elif estadoTiempo == "Mist":
                imprimirDatos(datos, "Niebla")
            elif estadoTiempo == "Rain":
                imprimirDatos(datos, "Lluvia")
            elif estadoTiempo == "Thunderstorm":
                imprimirDatos(datos, "Tormenta")
            elif estadoTiempo == "Snow":
                imprimirDatos(datos, "Nieve")
            else:
                imprimirDatos(datos, estadoTiempo)

        else:
            print("Lo sentimos, los datos para esa ciudad no se encuentran disponibles.")

        tecla=input("Pulse S si quiere salir del programa o cualquier otra tecla si desea continuar:\n")

def imprimirDatos(datos, descripcion):
    print("Estado del tiempo actual: ", descripcion)
    print("La temperatura actual es:", datos["main"]["temp"], "ºC")
    print("La sensación térmica es:", datos["main"]["feels_like"], "ºC")
    print("La temperatura mínima es:", datos["main"]["temp_min"], "ºC")
    print("La temperatura máxima es:", datos["main"]["temp_max"], "ºC")
    print("La presión es:", datos["main"]["pressure"], "hPa")
    print("La humedad es:", datos["main"]["humidity"], "% \n")


#Si no se pueden obtener los datos por falta de conexión a Internet, se informará al usuario de ello
def comprobarConexionInternet():
    global onlineConnection
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        onlineConnection = "true"
    except error:
        print("No se pueden comprobar los datos sin conexión a Internet")
        print("\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conexion()