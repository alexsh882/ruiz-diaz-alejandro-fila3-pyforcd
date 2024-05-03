

LISTA = [1,1,2,2,2,2,2,2,2,2,3,4,4,5,6,6,7];

def eliminar_duplicados(lista: list) -> list:
    """
    Función que recibe una lista y retorna la misma lista sin valores
    duplicados (si los hubiere), manteniendo el orden original.
    """
    return list(set(lista))

print(eliminar_duplicados(LISTA))