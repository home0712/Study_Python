## tuple: unable to add a value after declare a tuple
# tuple을 새로 생성하여 append 해줌
# tuple + tuple 은 가능

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = ()
    for elem in integer_list:
        new_t = (elem,)
        t = t + new_t

    print(hash(t))
