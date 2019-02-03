from abc import abstractmethod, ABCMeta


class GameType(metaclass=ABCMeta):
    game_type_name = None
    game_type_id = None

    @abstractmethod
    def run_parser(self, game_type_name, game_type_id):
        pass
