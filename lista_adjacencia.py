grafo = {
    'V1': ['V2', 'V3', 'V6'],
    'V2': ['V1', 'V3', 'V4', 'V6', 'V7'],
    'V3': ['V1', 'V2'],
    'V4': ['V2', 'V5'],
    'V5': ['V4', 'V6', 'V8'],
    'V6': ['V1', 'V2', 'V5', 'V7'],
    'V7': ['V2', 'V6', 'V8'],
    'V8': ['V5', 'V7']
}


def inserir_vertice(v):
    if v == "":
        print("Nome de vertice invalido!")
    elif v in grafo:
        print("Vertice ja existe!")
    else:
        grafo[v] = []
        print("Vertice inserido!")


def inserir_aresta(v1, v2):
    if v1 not in grafo or v2 not in grafo:
        print("Vertice nao encontrado!")
    else:
        if v2 in grafo[v1]:
            print("Aresta ja existe!")
        else:
            grafo[v1].append(v2)

            if v1 not in grafo[v2]:
                grafo[v2].append(v1)

            print("Aresta inserida!")


def remover_vertice(v):
    if v not in grafo:
        print("Vertice nao encontrado!")
    else:
        for vertice in grafo:
            if v in grafo[vertice]:
                grafo[vertice].remove(v)

        del grafo[v]

        print("Vertice removido!")


def remover_aresta(v1, v2):
    if v1 not in grafo or v2 not in grafo:
        print("Vertice nao encontrado!")
    else:
        if v2 not in grafo[v1]:
            print("Aresta nao existe!")
        else:
            grafo[v1].remove(v2)

            if v1 in grafo[v2]:
                grafo[v2].remove(v1)

            print("Aresta removida!")


def calcular_grau():
    for vertice in grafo:
        grau = len(grafo[vertice])

        if vertice in grafo[vertice]:
            grau += 1

        print(vertice, ":", grau)


def listar_vizinhos_vertice(v):
    if v not in grafo:
        print("Vertice nao encontrado!")
    else:
        print("Vizinhos de", v, ":", grafo[v])


def verificar_aresta(v1, v2):
    if v1 not in grafo or v2 not in grafo:
        print("Vertice nao encontrado!")
    else:
        if v2 in grafo[v1]:
            print("Existe aresta!")
        else:
            print("Nao existe aresta!")


def verificar_percurso(percurso):
    possivel = True

    if len(percurso) == 0:
        possivel = False

    for v in percurso:
        if v not in grafo:
            possivel = False

    for i in range(len(percurso) - 1):
        v1 = percurso[i]
        v2 = percurso[i + 1]

        if v1 not in grafo or v2 not in grafo:
            possivel = False
            break

        if v2 not in grafo[v1]:
            possivel = False
            break

    if possivel:
        print("Percurso possivel!")
    else:
        print("Percurso impossivel!")


def mostrar_grafo():
    for vertice in grafo:
        print(vertice, ":", grafo[vertice])


def busca_em_largura(inicio):
    fila = [inicio]
    visitados = []

    while len(fila) > 0:
        vertice = fila.pop(0)
        visitados.append(vertice)
        vizinhos = grafo[vertice]

        for vizinho in vizinhos:
            if vizinho not in fila:
                if vizinho not in visitados:
                    fila.append(vizinho)

        print("Visitados:", visitados, "| Fila:", fila)

    return visitados


def menor_caminho(inicio, destino):
    fila = [
        {
            'vertice': inicio,
            'caminho': [inicio]
        }
    ]
    visitados = []

    while len(fila) > 0:
        item = fila.pop(0)
        vertice = item['vertice']
        caminho = item['caminho']

        if vertice == destino:
            return caminho

        visitados.append(vertice)
        vizinhos = grafo[vertice]

        for vizinho in vizinhos:
            esta_na_fila = False
            for item_fila in fila:
                if item_fila['vertice'] == vizinho:
                    esta_na_fila = True

            foi_visitado = vizinho in visitados

            if esta_na_fila == False and foi_visitado == False:
                fila.append({
                    'vertice': vizinho,
                    'caminho': caminho + [vizinho]
                })

    return []


while True:
    print("\n===== LISTA DE ADJACENCIA =====")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("3 - Inserir aresta")
    print("4 - Remover aresta")
    print("5 - Calcular grau dos vertices")
    print("6 - Verificar aresta")
    print("7 - Listar vizinhos")
    print("8 - Verificar percurso")
    print("9 - Mostrar grafo")
    print("10 - Busca em largura")
    print("11 - Menor caminho (busca em largura)")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        v = input("Digite o vertice: ").strip().upper()
        inserir_vertice(v)

    elif opcao == "2":
        v = input("Digite o vertice: ").strip().upper()
        remover_vertice(v)

    elif opcao == "3":
        v1 = input("Digite o primeiro vertice: ").strip().upper()
        v2 = input("Digite o segundo vertice: ").strip().upper()
        inserir_aresta(v1, v2)

    elif opcao == "4":
        v1 = input("Digite o primeiro vertice: ").strip().upper()
        v2 = input("Digite o segundo vertice: ").strip().upper()
        remover_aresta(v1, v2)

    elif opcao == "5":
        calcular_grau()

    elif opcao == "6":
        v1 = input("Digite o primeiro vertice: ").strip().upper()
        v2 = input("Digite o segundo vertice: ").strip().upper()
        verificar_aresta(v1, v2)

    elif opcao == "7":
        v = input("Digite o vertice: ").strip().upper()
        listar_vizinhos_vertice(v)

    elif opcao == "8":
        percurso = input("Digite o percurso separado por espaco: ")
        percurso = percurso.upper().split()
        verificar_percurso(percurso)

    elif opcao == "9":
        mostrar_grafo()

    elif opcao == "10":
        v = input("Digite o vertice inicial: ").strip().upper()
        if v not in grafo:
            print("Vertice nao encontrado!")
        else:
            visitados = busca_em_largura(v)
            print("Ordem de visita:", visitados)

    elif opcao == "11":
        v1 = input("Digite o vertice inicial: ").strip().upper()
        v2 = input("Digite o vertice destino: ").strip().upper()
        if v1 not in grafo or v2 not in grafo:
            print("Vertice nao encontrado!")
        else:
            caminho = menor_caminho(v1, v2)
            if caminho == []:
                print("Nao existe caminho!")
            else:
                print("Menor caminho:", caminho)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida!")

    input("\nPressione Enter para continuar...")
