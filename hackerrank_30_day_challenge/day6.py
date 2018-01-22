T = int(input()) 

for j in range (0, T): 
    S = str(input())
    even = ""
    odd = ""
    for i in range(0,len(S)):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]
    answer = even + " " + odd
    print(answer)
