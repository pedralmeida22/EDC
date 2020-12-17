from simplegraph import SimpleGraph
from inferencerule import *


def infer_enemies():
    print("Infer enemies")
    infer = EnemyRule()
    _graph.applyinference(infer)
    print("Done-->")


def show_enemies(celeb):
    print("List enemies")
    query = _graph.query([(celeb, 'enemy', '?p2')])
    for a in query:
        print(celeb + " enemy --> " + a['p2'])


if __name__ == "__main__":
    _graph = SimpleGraph()

    _graph.load('celebrities.csv')

    _graph.printAllTriples()
    print('----------------')

    infer_enemies()
    show_enemies("Jay-Z")
