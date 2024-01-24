while True:
    
    N = input()
    length = 0
    
    if N == "0":
        break
        
    num_list = [int(x) for x in N]

    for i in range(len(num_list)):
        
        if num_list[i] == 1:
            length += 2
            
        elif num_list[i] == 0:
            length += 4
            
        else:
            length += 3
            
    length += (len(num_list) + 1)
            
    print(length)
