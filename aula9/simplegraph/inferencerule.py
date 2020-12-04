# -*- coding: utf-8 -*-

# inferencerule.py


class InferenceRule:
    """
    Implementa a regra base para as inferencias
    """

    def getqueries(self):
        return None  # tive de substituir return []

    def maketriples(self, binding):
        return self._maketriples(**binding)
