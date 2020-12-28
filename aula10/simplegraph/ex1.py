from simplegraph import *
from inferencerule import *


# menu
def menu():
    print("* Celebrities *")
    print("----------------------------------------------------")
    print("1. Infer all known people from Winona Ryder")
    print("2. List all known people from Winona Ryder")
    print("3. Save all triples from Winona Ryder's known people")
    print("----------------------------------------------------")
    print("0. End")
    return int(input("Opção: "))


def f1():
    print('Infer all known people from Winona Ryder')
    er = KnownRule()
    print(er)
    _graph.applyinference(er)
    print('Done-->')


def f2():
    print('List all known people from Winona Ryder')
    lista = _graph.query([('Winona Ryder', 'knows', '?person')])
    for a in lista:
        print("Winona Ryder knows %s" % (a['person']))


def f3():
    print("Save all triples from Winona Ryder's known people")
    _graph.savetriples("winona.csv", ('Winona Ryder', 'knows', None))
    print('Saved-->')


def run(op):
    _funcs[op - 1]()


# inicio do modulo
if __name__ == "__main__":
    _funcs = (f1, f2, f3)
    _graph = SimpleGraph()

    _graph.load('celebrities.csv')
    _graph.printAllTriples()

    while True:
        op = menu()
        if op == 0:
            break
        run(op)
