from interface.screen_controller import ScreenController
from interface.game_engine import GameEngine


class ScreenControllerImpl(ScreenController):
    pass


class GameEngineImpl(GameEngine):
    pass


if __name__ == '__main__':
    engine = GameEngineImpl()
    ScreenControllerImpl.clear_screen()
    ScreenControllerImpl.screen_output(engine.get_output(), engine.get_hint(), engine.get_guess())

    char_input = input("")
    while not engine.guess_character(char_input):
        ScreenControllerImpl.clear_screen()
        ScreenControllerImpl.screen_output(engine.get_output(), engine.get_hint(), engine.get_guess())
        char_input = input("")

    ScreenControllerImpl.clear_screen()
    ScreenControllerImpl.screen_output(engine.get_output(), engine.get_hint(), engine.get_guess())
