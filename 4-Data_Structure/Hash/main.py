from dictionary import Dictionary

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dic = Dictionary()
    dic.insert('i', 1)
    dic.insert('ii', 2)
    dic.insert('iii', 3)
    dic.insert('iv', 4)
    dic.insert('v', 5)
    dic.insert('vi', 6)
    dic.insert('vi', 7)
    dic.insert('vii', 8)
    dic.insert('ix', 9)
    dic.insert('x', 10)
    print(dic.collisions)
    print(dic.table)