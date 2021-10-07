"""Just put in to get matches running"""
from service.match_service import MatchVisitTemplate, MatchManager


class T01Match(MatchManager, MatchVisitTemplate):
    def __init__(self):
        super().__init__()

class T01MatchBuilder:
    def __init__(self):
        pass

    def __call__(self):
        return T01Match()