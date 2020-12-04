# -*- coding: utf-8 -*-

# main.py

from simplegraph import SimpleGraph


# menu
def menu():
    print("*** MENU ***")
    print("1. Listar Triplos")
    print("2. Filtrar Triplos")
    print("3. Pesquisar Triplos")
    print("---------------------")
    print("4. Carregar Grafo")
    print("5. Guardar Grafo")
    print("6. Fundir Grafos")
    print("---------------------")
    print("7. Inserir Novo Triplo")
    print("8. Remover Triplo")
    print("---------------------")
    print("9. lista filmes")
    print("10. Realizador by filme")
    print("11. Atores by filme")
    print("12. Filmes by director")
    print("13. Filmes by actor")
    print("14. Atores by director e em que filmes")
    print("0. Sair")
    print("---------------------")
    return int(input("Opcao: "))


def listgraph():
    print("Listar Triplos")
    _graph.printAllTriples()


def filtergraph():
    print("Filtrar Triplos")
    sub = input("Sujeito: ")
    if len(sub) == 0: sub = None
    pred = input("Predicado: ")
    if len(pred) == 0: pred = None
    obj = input("Objeto: ")
    if len(obj) == 0: obj = None
    t = _graph.triples(sub, pred, obj)
    SimpleGraph.printTriples(t)


def search():
    print("Nomes dos realizadores de filmes.")
    lista = _graph.query([('?film', 'directed_by', '?real'),
                          ('?real', 'name', '?realname')
                          ])
    conj = set()
    for a in lista:
        conj.add(a['realname'])
    for a in sorted(conj):
        print(a)


def loadgraph():
    print("Carregar Grafo")
    # _graph.load(input("Nome do ficheiro: "))
    _graph.load('movies.csv')
    _graph2.load('movies.org.csv')  # tem mais dados


def storegraph():
    print("Guarda Grafo")
    _graph.save(input("Nome do ficheiro: "))


def mergegraphs():
    print("Fusao de Grafos")
    g = SimpleGraph()
    g.load(input("Nome do ficheiro: "))
    for sub, pred, obj in g.triples(None, None, None):
        _graph.add(sub, pred, obj)


def inserttriple():
    print("Inserir triplo")
    sub = input("Sujeito: ")
    pred = input("Predicado: ")
    obj = input("Objeto: ")
    _graph.add(sub, pred, obj)


def removetriple():
    print("Remover triplo")
    sub = input("Sujeito: ")
    if len(sub) == 0: sub = None
    pred = input("Predicado: ")
    if len(pred) == 0: pred = None
    obj = input("Objeto: ")
    if len(obj) == 0: obj = None
    _graph.remove(sub, pred, obj)


def film_list():
    # lista de todos os filmes
    lista = _graph.query([('?film', 'directed_by', '?real'),
                          ('?film', 'name', '?film_name')
                          ])
    conj = set()
    for a in lista:
        conj.add(a['film_name'])

    for a in sorted(conj):
        print(a)


def get_realizador(film="Yes"):
    # realizador de um dado filme
    r = _graph2.query([('?film', 'name', film),
                       ('?film', 'directed_by', '?real'),
                       ('?real', 'name', '?real_name')
                       ])
    print(r[0]['real_name'])


def get_atores(film="Yes"):
    # realizador de um dado filme
    lista = _graph2.query([('?film', 'name', film),
                           ('?film', 'starring', '?real'),
                           ('?real', 'name', '?real_name')
                           ])
    conj = set()
    for a in lista:
        conj.add(a['real_name'])

    for a in sorted(conj):
        print(a)


def films_by_director(d="Sally Potter"):
    # filmes dado um realizador
    lista = _graph2.query([('?d_id', 'name', d),
                           ('?film', 'directed_by', '?d_id'),
                           ('?film', 'name', '?film_name')
                           ])
    conj = set()
    for a in lista:
        conj.add(a['film_name'])

    for a in sorted(conj):
        print(a)


def films_by_actor(a="Joan Allen"):
    # filmes dado um actor
    lista = _graph2.query([('?d_id', 'name', a),
                           ('?film', 'starring', '?d_id'),
                           ('?film', 'name', '?film_name')
                           ])
    conj = set()
    for a in lista:
        conj.add(a['film_name'])

    for a in sorted(conj):
        print(a)


def actors_by_director(d="Sally Potter"):
    # todo
    # Lista de atores orientados por um dado realizador e em que filmes

    result = _graph2.query([('?d_id', 'name', d),
                            ('?film', 'directed_by', '?d_id'),
                            ('?film', 'name', '?film_name'),
                            ('?film', 'starring', '?a_id'),
                            ('?a_id', 'name', 'a_name')
                            ])
    # conj = set()
    # for a in result:
    #     conj.add(a['film_name'])
    print(result)

    # for a in sorted(conj):
    #     print(a)


def run(op):
    _funcs[op - 1]()


# inicio do modulo
if __name__ == "__main__":
    _funcs = (listgraph, filtergraph, search, loadgraph, storegraph, mergegraphs, inserttriple, removetriple,
              film_list, get_realizador, get_atores, films_by_director, films_by_actor, actors_by_director)
    _graph = SimpleGraph()
    _graph2 = SimpleGraph()

    loadgraph()
    while (True):
        op = menu()
        if op == 0:
            break
        run(op)
