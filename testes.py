test1 = ['a', 'b']
test2 = ["1", "2", "a"]


def run(teste):
    lista = [i for i in teste if i.isnumeric()]
    print(lista)


run(test1)

