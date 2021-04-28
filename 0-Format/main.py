
if __name__ == '__main__':
    print('hello world!')
    name = input('Type in your name: ')
    age = int(input('Type in your age: '))

    print('Name entered: {}, aged: {}'.format(name, age))

    tag = 'p'
    print('<{0}>{1}<{0}>'.format(tag, name))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
