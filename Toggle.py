counter = int(input())
for y in range(counter):
    N,K = input().split()
    string = list(input())
    N = int(N)
    K = int(K)
    y=0
    for x in range(N):
        if string[x] == "1" and y<K:
            y += 1
            string[x] = "0"
        elif string[x] == "0" and y<K:
            string[x] = "0"
    print("".join(string))