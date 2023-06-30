def split_and_join(line):
    # write your code here
    words = line.split(" ")
    # join the words with -
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)