import funciones

print('*****************************')
print('*       MUNDO LIBRO         *')
print('*****************************')

print('[1]- Mantenedor de categorias \n[2]- Reportes \n[3]- salir')
menu = int(input('selecccione una opcion: '))

match menu:
    case 1:
        print ('[1]- agregar categoria\n[2]- editar categoria\n[3]- buscar categoria\n[4]- eliminar categoria')
        categoria = int(input('seleccione que desea hacer: '))

        match categoria:
            case 1:
                nombreAdd= str(input('Que nombre desea agregar: '))
                funciones.agregarCategoria(nombreAdd)
            case 2:
                CategoriaDif = int(input('Que Id desea editar: '))
                NombreDif = str(input('que nombre desea colocar: '))
                funciones.editarCategoria(CategoriaDif, NombreDif)
            case 3:
                funciones.listarCategoria()
            case 4:
                CategoriaID = int(input('selccione la id que desea eliminar:'))
                funciones.eliminarCategoria(CategoriaID)