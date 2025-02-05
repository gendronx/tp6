from enum import Enum


class GameState(Enum):
    Not_Started = 0
    Round_Active = 1
    Round_Done = 2
    Game_Over = 3
