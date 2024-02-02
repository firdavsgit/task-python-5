list = [0,0,-10]

i = 0
result = 0
def find_vektor(lst, index, result):
    while index < len(lst):
        x = list[index]
        result += x**2
        index += 1

    return int(result ** 0.5)


print(find_vektor(list, i, result))



