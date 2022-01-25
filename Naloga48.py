def matrika(matrika):
    for y in range(len(matrika)):
        for x in range(len(matrika[y])):
            print(matrika[y][x], end=" ")
        print()

prikaz = ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrika(prikaz)

