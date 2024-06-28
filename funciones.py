import json



def listarCategoria():
    with open('biblioteca.json', mode='r')as lecturaJson:
        leerjson = json.load(lecturaJson)

    print ('lista de categorias')
    for i in leerjson['Categoria']:
        print(i)

def agregarCategoria(nombreAdd=str):
    with open('biblioteca.json', mode='r')as lecturaJson:
        leerjson = json.load(lecturaJson)

        DiccionarioAdd = {
            'CategoriaID': len(leerjson['Categoria'])+1,
            'Nombre' : nombreAdd,
        }

        leerjson['Categoria'].append(DiccionarioAdd)

        with open('biblioteca.json', mode='w')as escrituraJson:
            json.dump(leerjson,escrituraJson,indent=4)
            print (f'Agregar Autor, Ejecutado correctamente.\n{DiccionarioAdd}')

def editarCategoria(CategoriaDIF=int, nombreDIF=str):
    with open('biblioteca.json', mode='r')as lecturaJson:
        leerjson = json.load(lecturaJson)
    contador=0
    for Categoria in leerjson['Categoria']:
        if Categoria['CategoriaID'] == CategoriaDIF:
            break
        contador += 1
    leerjson['Categoria'][contador]['Nombre'] = nombreDIF

    with open ('biblioteca.json', mode='w')as escrituraJson:
        json.dump(leerjson,escrituraJson,indent=4)
        print (f'EditarProducto, ejecutado correctamente.\n{leerjson['Categoria'][contador]}')

def eliminarCategoria(CategoriaID=int):
    with open('biblioteca.json', mode='r')as lecturaJson:
        leerjson= json.load(lecturaJson)

        contador = 0
        for Categoria in leerjson['CategoriaID']:
            if Categoria['CategoriaID'] == CategoriaID:
                break
            contador += 1

    with open('biblioteca.json', mode='w')as escrituraJson:
        json.dump(leerjson,escrituraJson,indent=4)




