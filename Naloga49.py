def matrika(matrika):
    for y in range(0,len(matrika),1):
        for x in range(0,len(matrika[y]),1):
            print(matrika[y][x], end=" ")
            print()


def matrika2(matrika, st):
    for y in range(0,len(matrika),1):
        for x in range(0,len(matrika[y]),1):
            matrika[y][x]=matrika[y][x]*st
    return matrika

m= matrika2([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], 8)

matrika(m)