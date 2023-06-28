if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = tuple(integer_list)
    result = hash(integer_list)  # Calcula elhas hde la tupla
    print(result)  # Imprime el resultado del hash
