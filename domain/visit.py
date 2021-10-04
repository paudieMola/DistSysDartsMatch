from datatype.enums import DartMultiplier

class Dart:
    def __init__(self, multiplier, segment):
        self.multiplier = multiplier
        """
        see datatype.enums DartType: optionally create this as a
        property and validate
        """
        self.segment = segment # 1 to 20, 0 for miss /  double-bull
        # /single-bull

    def get_score(self):
        return self.multiplier * self.segment

    def to_string(self)
        segment = None
        if self.segment is 25:
            segment = "BULL"
        if self.segment is 0:
            return "MISS"
        return DartMultiplier(self.multiplier).name + "-" + str(self.segment) if segment is None else segment

class Visit:
    def __init__(self):
        self.darts = []