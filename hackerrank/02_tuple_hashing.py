if __name__ == '__main__':
    n = int(input())  # Lee el número de elementos en la tupla
    integer_list = tuple(map(int, input().split()))  # Lee los enteros y crea la tupla

    result = hash(integer_list)  # Calcula el hash de la tupla

    print(result)  # Imprime el resultado del hash
