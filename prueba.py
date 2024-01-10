lista = ['manzana','pera','fresa']
lista2 = ['mango','uva','durazno']
listas = lista + lista2
lista_index = [(index, item) for index, item in enumerate(listas)]
print(lista_index)