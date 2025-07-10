#Autor Felipe Cortes
#005D_D
inventario = {}
inventario['Rotulado'] = {
    '8475HD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10],
                  '2175HD': [327990,4], 
                  'JjfFHD': [424990,1],
                  'fgdxFHD': [664990,21], 
                  '123FHD': [290890,32], 
                  '342FHD': [444990,7],
                  'GF75HD': [749990,2], 
                  'UWU131HD': [349990,1], 
                  'FS1230HD': [249990,0],
                 }


def menu():
    print('*** MENU PRINCIPAL ***\n'
            '1. Stock marca.\n'
            '2. Búsqueda por RAM y precio.\n'
            '3. Eliminar producto.\n'
            '4. Salir.')

def BuscarMarca():
    global inventario
    contador = 0
    marca = input('Ingrese la marca:  ').capitalize()
    encontrado = False
    for rotulado,brand in inventario["Rotulado"].items():
        if marca in brand:
            encontrado = True
            break
    if encontrado:
        marca_filtrada = {
            codigo: datos for codigo,datos in inventario["Rotulado"].items()
            if datos[0].title()== marca
        }
    else:
        return print(f'La marca {marca} no esta en el diccionario')
        

    if marca_filtrada:
        print(f'Mostrando marcas {marca}')
        for codigo,datos in marca_filtrada.items():
            
            contador = contador + 1 
    
    if marca == 'Hp':
        contador = contador//contador
        contador = contador * stock['8475HD'][1] + contador * stock['fgdxFHD'][1]
    elif marca == 'Acer':
        contador = contador//contador
        contador = contador * contador * stock['2175HD'][1] + contador * stock['123FHD'][1]+ contador * stock['342FHD'][1]
    elif marca == 'Asus':
        contador = contador//contador
        contador = contador * contador * stock['JjfFHD'][1] + contador * stock['GF75HD'][1]
    elif marca == 'Dell':
        contador = contador//contador
        contador = contador * contador * stock['UWU131HD'][1]
    else:
        print('Marca no encontrada')
    print(f'La cantidad de stock de {marca} es {contador}')

def Eliminar():
    modelo_a_eliminar = input("Ingresa el modelo a eliminar: ")
    valor_eliminado = inventario['Rotulado'].pop(modelo_a_eliminar)
    if valor_eliminado is not None:
        print(f"Se eliminó el modelo '{modelo_a_eliminar}' y sus valores: {valor_eliminado}.")
        print(f'aqui el nuevo diccionario con el valor eliminado \n{inventario}')
    else:
        print(f"El modelo '{modelo_a_eliminar}' no existe.")
    
def Busqueda():
    try:    
        ram_minima = int(input('Ingresa la ram minima: ' ))
        ram_maxima = int(input('Ingresa la ram maxima: ' ))
        precio = int(input('ingresa el precio maximo: '))
        if inventario['Rotulado']['8475HD'][1] >= ram_minima and inventario['Rotulado']['8475HD'][1] <= ram_maxima and stock['8475HD'][0] < precio:
            print(inventario['Rotulado']['8475HD'])
        if inventario['Rotulado']['2175HD'][1] >= ram_minima and inventario['Rotulado']['2175HD'][1] <= ram_maxima and stock['2175HD'][0] < precio:
            print(inventario['Rotulado']['2175HD'])
        if inventario['Rotulado']['JjfFHD'][1] >= ram_minima and inventario['Rotulado']['JjfFHD'][1] <= ram_maxima and stock['JjfFHD'][0] < precio:
            print(inventario['Rotulado']['JjfFHD'])
        if inventario['Rotulado']['fgdxFHD'][1] >= ram_minima and inventario['Rotulado']['fgdxFHD'][1] <= ram_maxima and stock['fgdxFHD'][0] < precio:
            print(inventario['Rotulado']['fgdxFHD'])
        if inventario['Rotulado']['GF75HD'][1] >= ram_minima and inventario['Rotulado']['GF75HD'][1] <= ram_maxima and stock['GF75HD'][0] < precio:
            print(inventario['Rotulado']['GF75HD'])
        if inventario['Rotulado']['123FHD'][1] >= ram_minima and inventario['Rotulado']['123FHD'][1] <= ram_maxima and stock['123FHD'][0] < precio:
            print(inventario['Rotulado']['123FHD'])
        if inventario['Rotulado']['342FHD'][1] >= ram_minima and inventario['Rotulado']['342FHD'][1] <= ram_maxima and stock['342FHD'][0] < precio:
            print(inventario['Rotulado']['342FHD'])
        if inventario['Rotulado']['UWU131HD'][1] >= ram_minima and inventario['Rotulado']['UWU131HD'][1] <= ram_maxima and stock['UWU131HD'][0] < precio:
            print(inventario['Rotulado']['UWU131HD'])
    except ValueError:
        print('Debes ingresar numeros enteros')

menu()
opcion = input('')

while opcion != '4':
    if opcion == '1':
        BuscarMarca()
        menu()
        opcion = input('')
    elif opcion == '2':
        Busqueda()
        menu()
        opcion = input('')
    elif opcion == '3':
        Eliminar()
        menu()
        opcion = input('')
    else:
        print('Opcion no valida')
        menu()
        opcion = input('')

