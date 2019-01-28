from abc import abstractmethod, ABCMeta


class GameType(metaclass=ABCMeta):
    gametype_name = None
    gametype_id = None

    @abstractmethod
    def find(self, gametype_name, gametype_id):
        pass
