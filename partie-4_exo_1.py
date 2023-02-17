lines = [" _ ",["|","_","|"],["|","_","|"]]

for line in lines:
    print(line)
    
build = {
    "1" : [0, (1,-1), (2, -1)],
    "2" : [1, (1, 1), (1, 2), (2, 0), (2,1)]
}


def segments(n):
    string_number = str(n)
    for i in range(len(string_number)):
        for j in range(len(build[string_number[i]])):
            if (j == 0) and build[string_number[i]][j] == 1:
                print(lines[0])
            elif (j == 0) and build[string_number[i]][j] == 0:
                continue
            for coord in build[string_number[i]][j]:
                print(coord)



segments(2)