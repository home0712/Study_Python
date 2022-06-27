if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # result
    result = []
    
    # i + j + k != n
    
    # All permutations
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k) != n:
                    result.append([i, j, k]) # able to add a list as an element
    
    print(result)
    
