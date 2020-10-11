def hello_n(name:str, n:int):
    for i in range(n):
        print('Hello', name)

hello_n('Fyodor', 6)
hello_n('Petya', 2)
Fyodor = 'Fyodor', 5
hello_n(*Fyodor)


