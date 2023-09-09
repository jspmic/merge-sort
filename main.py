import sys
from random import randint

def merge(l1:list[int], l2:list[int]) -> list[int]:
    result = []
    while l1!=[] and l2!=[]:
        if l1[0]<=l2[0]:
            result.append(l1[0])
            l1.pop(0)
        else:
            result.append(l2[0])
            l2.pop(0)
    if l1!=[]: result+=l1
    if l2!=[]: result+=l2
    return result

def merge_sort(lst:list[int]) -> list[int]:
    if len(lst)==1: return lst
    else:
        m = len(lst)//2
        return merge(merge_sort(lst[:m]),merge_sort(lst[m:]))

if __name__=='__main__':
    l1 = [randint(0,100) for i in range(50)] #You can change 50 to n(a positive integer)
    l2 = [randint(0,100) for i in range(40)]
    print(f"\nList 1(initial): {l1}\n\nList 1(sorted): {merge_sort(l1)}")
    print("\n-------------")
    print(f"\nList 2(initial): {l2}\n\nList 2(sorted): {merge_sort(l2)}")
    sys.exit(0)

