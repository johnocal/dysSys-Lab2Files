from datatype.enums import DartMultiplier

class Dart:
    def __init__(self, multiplier, segment):
        self.multiplier = multiplier
        self.segment = segment

    def get_score(self):
        return self.multiplier * self.segment

    def to_string(self):
        segment = None
        if self.segment is 25:
            segment = "BULL"
        if self.segment is 0:
            return "MISS"
        return DartMultiplier(self.multiplier).name + "-" + str(self.segment) if segment is None else segment

class Visit:
    def __init__(self):
        self.darts = []

    def __init__(self, darts):
        self.darts = []
        self.add_darts(darts)

    def add_dart(self, dart):
        self.darts.append(Dart(dart[0], dart[1]))

    def add_darts(self, darts):
        for dart in darts:
            self.add_dart(dart)

    def remove_trailing_darts(self, index):
        del self.darts[index:]

    def get_total(self):
        total = 0
        for dart in self.darts:
            total += dart.get_score()
        return total

    def to_string(self):
        output = ""
        for dart in self.darts:
            output += dart.to_string() + " "
        return output

    