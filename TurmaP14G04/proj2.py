import requests


def inputs_atracoes():
    localizacao = input("introduza a sua latitude e longitude separados por uma virgula: ")
    raio_de_distancia = input("introduza distancia que quer percorrer em kms: ")
    tipos_de_atracoes = input("introduza os tipos de atrações que quer visitar separados por virgulas (sem espaços): ")
    num_atracoes = input("quantas atrações de cada categoria quer ver? ")
    return localizacao, raio_de_distancia, tipos_de_atracoes, num_atracoes

def tratamento_de_inputs(localizacao, raio_de_distancia,tipos_de_atracoes):
    try:
        latitude,longitude = map(float, localizacao.split(','))
        raio_de_distancia = float(raio_de_distancia) * 1000  #converte para metros para ser depois usado na api
        return longitude, latitude, raio_de_distancia, tipos_de_atracoes
    except ValueError:
        print('Erro: os valores introduzidos não são válidos')
        return None, None, None, None

def atracoes(longitude, latitude, raio_de_distancia, tipos_de_atracoes, num_atracoes):
    tipos_de_atracoes = tipos_de_atracoes.split(',')
    lista_atracoes = []  #lista onde vão ser armazenados os dicionarios das atrações
    for tipo in tipos_de_atracoes:
       

        url = f"https://api.geoapify.com/v2/places?categories={tipo}&filter=circle:{latitude},{longitude},{raio_de_distancia}&bias=proximity:{latitude},{longitude}&limit={num_atracoes}&apiKey=1bd1479b4015483b98cd7bb025cd7e50"
        resp = requests.get(url)

        if resp.status_code != 200:
            print(f"Erro: O request de api falhou com o erro: {resp.status_code}")
            return resp.status_code

        data = resp.json()
        features = data.get('features', [])

        for feature in features:
            #cria um novo dicionario para cada feature
            dict_atracoes = {}
            properties = feature.get('properties', {})

            dict_atracoes["Nome:"] = properties.get('name', 'não encontrado')
            dict_atracoes["Tipo:"] = properties.get('categories', 'não encontrado')
            dict_atracoes["Morada:"] = properties.get('formatted', 'não encontrado')
            dict_atracoes["Pais:"] = properties.get('country', 'não encontrado')
            dict_atracoes["Distrito:"] = properties.get('district', 'não encontrado')
            dict_atracoes["Cidade:"] = properties.get('city', 'não encontrado')
            dict_atracoes["Vila:"] = properties.get('village', 'não encontrado')
            dict_atracoes["Rua:"] = properties.get('street', 'não encontrado')
            dict_atracoes["Numero da porta:"] = properties.get('housenumber', 'não encontrado')
            dict_atracoes["Codigo postal:"] = properties.get('postcode', 'não encontrado')
            dict_atracoes["Latitude:"] = properties.get('lat', 'não encontrado')
            dict_atracoes["Longitude:"] = properties.get('lon', 'não encontrado')
            dict_atracoes["Distancia:"] = str(properties.get('distance', 'não encontrado')) + " metros"

            #adição dos dicionarios à lista
            lista_atracoes.append(dict_atracoes)

    return lista_atracoes

def escolha_filtro(lista_atracoes):
    print("como quer ordenar as atrações que vai observar?")
    print("1-ordem alfabética")
    print("2-ordem alfabética inversa")
    print("3-menor distancia")
    print("4-maior distancia")

    filtro = input("introduza aqui a sua escolha: ")
    print("\n")
    if filtro in ("1","2","3","4"):
        filtro_atracoes(filtro,lista_atracoes)
    else:
        print("escolha inválida")
        escolha_filtro(lista_atracoes)

def filtro_atracoes(filtro,lista_atracoes):
    if filtro == "1":
        sorted_atracoes = sorted(lista_atracoes, key=lambda x: x['Tipo:'][0] if isinstance(x['Tipo:'], list) else x['Tipo:']) #ordenação por ordem alfabetica
        for dict_atracoes in sorted_atracoes:
            for key, value in dict_atracoes.items():
                print(f"{key} {value}")
            print("\n")
    elif filtro == "2":
        sorted_atracoes = sorted(lista_atracoes, key=lambda x: x['Tipo:'][0] if isinstance(x['Tipo:'], list) else x['Tipo:'], reverse=True) #ordenação por ordem alfabetica invertida
        for dict_atracoes in sorted_atracoes:
            for key, value in dict_atracoes.items():
                print(f"{key} {value}")
            print("\n")
    elif filtro == "3":
        sorted_atracoes = sorted(lista_atracoes, key=lambda x: float(x['Distancia:'].split()[0])) #ordenação por distancia crescente
        for dict_atracoes in sorted_atracoes:
            for key, value in dict_atracoes.items():
                print(f"{key} {value}")
            print("\n")
    elif filtro == "4":
        sorted_atracoes = sorted(lista_atracoes, key=lambda x: float(x['Distancia:'].split()[0]), reverse=True) #ordenação por distancia decrescente
        for dict_atracoes in sorted_atracoes:
            for key, value in dict_atracoes.items():
                print(f"{key} {value}")
            print("\n")

def metereologia(latitude,longitude):
    interesse = input("tem interesse em ver a metereologia atual da localização escolhida? ")
    if interesse == 'sim' or interesse == 'Sim' or interesse == 's':
        urlm = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=1a8a7d59e22decf84cc0905849862665&units=metric&lang=pt"
        resp1 = requests.get(urlm)
        if resp1.status_code != 200:
                print(f"Erro: O request de api falhou com o erro: {resp1.status_code}, não vai ser possível apresentar a metereologia")
                return
        data1 = resp1.json()
        cidade = data1['name']
        descricao = data1['weather'][0]['description']
        temp = data1['main']['temp_max']
        sensacao = data1['main']['feels_like']

        print(f"em {cidade} está {descricao} com uma temperatura de {temp}ºC e uma sensação térmica de {sensacao}ºC")

def main():
    localizacao, raio_de_distancia, tipos_de_atracoes, num_atracoes = inputs_atracoes()
    longitude, latitude, raio_de_distancia, tipos_de_atracoes = tratamento_de_inputs(localizacao, raio_de_distancia, tipos_de_atracoes)

    if longitude is not None:
        lista_atracoes = atracoes(latitude, longitude, raio_de_distancia, tipos_de_atracoes,num_atracoes)
        escolha_filtro(lista_atracoes)
        metereologia(latitude,longitude)

if __name__ == "__main__":
    main()