import requests
def obter_categorias(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]   #Mostra as categorias no terminal 

def descobrir_locais(api_key, latitudeInicial, longitudeInicial, raio, tipos):
    url = "https://api.geoapify.com/v2/places"
    params = {
        'lat': latitudeInicial,
        'lon': longitudeInicial,
        'radius': raio,
        'categories': tipos,
        'apiKey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get('features', [])
    else:
        print(f"Erro na solicitação da API: {response.status_code}")
        return []
def informacao_local(locais):
    print("\nInformações dos Locais:")
    numLocal=0
    distTotal=0
    for local in locais:
        nome = local.get('properties', {}).get('name', 'Nome não disponível')
        if nome=='Nome não disponível':
            continue
        pais = local.get('properties', {}).get('country')
        localizacao = local.get('geometry', {}).get('coordinates', [])
        latitudeFinal, longitudeFinal = localizacao 
        distancia=local.get('properties',{}).get('distance')/1000 #metros para kilometros
        Morada = local.get('properties',{}).get('formatted') # (Informação extra-1)
        cidade = local.get('properties',{}).get('city')#(Informação extra-2)
        codigoPostal=local.get('properties',{}).get('postcode')#(Informação extra-3)
        numLocal+=1  #Estatisticas básicas-1
        if distancia is None:     #Estatisticas básicas-2
            continue
        else:
            distTotal += distancia
        print(f"\nNome: {nome}")
        print(f"Cidade : {cidade}")
        print(f"País: {pais}")
        print(f"Localização: Longitude {longitudeFinal}, Latitude {latitudeFinal}")
        print(f"Distância à localização de partida: {distancia} km")
        print(f"Morada : {Morada}")
        print(f"Código Postal: {codigoPostal}")
        print("\n Estatisticas básicas:")
        print(f"Numero total de locais sugeridos: {numLocal}" )
        print(f"Distância média : {distTotal/numLocal} km")
def main():
    api_key = '555e197603d0449f8c335d2fc48d6580'
    categorias_ficheiro = 'categories.txt'

    categorias = obter_categorias(categorias_ficheiro)
    print("Categorias disponíveis:", categorias)

    latitudeInicial= float(input("Digite a latitude do local de partida: "))
    longitudeInicial = float(input("Digite a longitude do local de partida: "))
    raio = float(input("Digite a distância máxima de viagem (em km): "))
    tipos_escolhidos = [tipo.strip() for tipo in input("Digite os tipos de locais desejados (separados por vírgula): ").split(',')]
    
    tipos_validos = [tipo.strip() for tipo in tipos_escolhidos if tipo.strip() in categorias]

    locais = descobrir_locais(api_key, latitudeInicial, longitudeInicial, raio, tipos_validos)
    
    informacao_local(locais) 

if __name__ == "__main__":
    main()
