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


class EnemyRule(InferenceRule):
    def getqueries(self):
        partner_enemy = [('?person', 'enemy', '?enemy'),
                        ('?rel', 'with', '?person'),
                        ('?rel', 'with', '?partner')]
        print("fdg: ", partner_enemy)
        return [partner_enemy]

    def _maketriples(self, person, enemy, rel, partner):
        return [(partner, 'enemy', enemy)]
