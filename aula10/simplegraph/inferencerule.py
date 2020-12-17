# -*- coding: utf-8 -*-

# inferencerule.py


class InferenceRule:
    """
    Implementa a regra base para as inefrencias
    """
    def getqueries(self):
        return None # tive de substituir return []

    def maketriples(self,binding):
        return self._maketriples(**binding)


class KnownRule(InferenceRule):
    def getqueries(self):
        qs = [("Winona Ryder", "starred_in", "?film"),
              ('?person', 'starred_in', '?film')]
        return qs

    def _maketriples(self, film, person):
        return [('Winona Ryder', 'knows', person)]