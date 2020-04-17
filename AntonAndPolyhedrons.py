n = int(input())
face = 0
for i in range(n):
    condition = input()
    if condition == "Tetrahedron":
        face += 4
    elif condition == "Cube":
        face += 6
    elif condition == "Octahedron":
        face += 8
    elif condition == "Dodecahedron":
        face += 12
    else:
        face += 20

print(face)
