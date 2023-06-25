if __name__ == '__main__':
    N = int(input())  # Read the initial size of the list
    my_list = []

    for _ in range(N):
        command, *args = input().split()  # Read each command and its arguments (if any)

        if command == 'insert':
            i, e = map(int, args)
            my_list.insert(i, e)
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            e = int(args[0])
            my_list.remove(e)
        elif command == 'append':
            e = int(args[0])
            my_list.append(e)
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
