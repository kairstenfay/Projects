n = int(input())

my_dict = {}
for i in range(0, n): 
    arr = [arr_temp for arr_temp in input().strip().split(' ')]
    my_dict[arr[0]] = arr[1]

while True:
    try:
        q = str(input())
        if q in my_dict: 
            print(q + "=" + my_dict[q])
        else:
            print("Not found") 
    except EOFError:
        break

# could also try readLines() to count number of inputs 
