def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    return quick_sort([i for i in lst if i < lst[0]]) + [lst[0]] + quick_sort([i for i in lst if i > lst[0]])
# List comprehension corresponds to std::copy_if
