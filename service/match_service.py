from abc import ABC, abstractmethod

class MatchManager(ABC):
    def __init__(self):
        self.match = None

    def set_match(self, match):
        self.match = match
        self.post_init() #initialise whatever is specific
                        # to the match type

    def end_match(self):
        self.match.active = False

    @abstractmethod
    def post_init(self):
    #Primitive operation. You have to override me.
    #Im a placeholder
        pass

class MatchVisitTemplate(ABC):
    def process_visit(self, player_index, visit):
        """
        returns result (0 meaning game goes on, >0 meaning
        a dart finished the game), response (info messages)
        Skeleton of operation to perform. Dont override me.

        The template method defines a skeleton of an algoritym in
        an operation and defers some steps to subclasses.
        """
        status, message = self.validate_visit(player_index, visit)
        if status is False:
            return -1, message

        #result stores which, if any, of the darts closed out the game
        result = self.check_winning_condition(player_index, visit)
        self.record_statistics(player_index, visit, result)

    #Note this violates the seperation of concerns principle
    #(we are mixing presnetation logic in with
    # service/business logic - we should refactor,
    #especially if we move to a GUI front end
        return result, self.format_summary(player_index, visit)

    @abstractmethod
    def validate_visit(self, player_index, visit):
        #primitive operation, override, placeholder
        pass

    @abstractmethod
    def check_winning_condition(self, player_index, visit):
        #primitive operation, override, placeholder
        pass

    @abstractmethod
    def record_statistics(self, player_index, visit, result):
        #primitive operation, override, placeholder
        pass

    @abstractmethod
    def format_summary(self, player_index, visit):
        #primitive operation, override, placeholder
        pass