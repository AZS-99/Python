
import merge
from bubble import bubble_sort

if __name__ == '__main__':
    lst = [10, 9, 5, 11]
    lst2 = merge.merge_sort(lst)

    lst3 = bubble_sort(lst)
    print(lst2)
    print(lst3)

