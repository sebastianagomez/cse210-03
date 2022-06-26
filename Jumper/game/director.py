from game.jumper import Jumper
from game.puzzle_word import PuzzleWord
from game.terminal_service import TerminalService

class Director:

    def __init__(self):
        
        self._jumper = Jumper()
        self._puzzle_word = PuzzleWord()
        self._terminal_service = TerminalService()
        self._is_playing = True

    def start_game(self):
        
        self._puzzle_word.random_word()
        self._terminal_service.draw(self._jumper.get_parachute())

        while(self._is_playing):

            if self._puzzle_word.correct_word_hint() or not self._jumper.reach_wrong_hint():
                self._is_playing = False

            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):

        inp_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._puzzle_word.last_hint_correct(inp_letter)

    def _do_updates(self):

        if (not self._puzzle_word.get_last_hint()):
            self._jumper.update_parachute()

        if self._puzzle_word.correct_word_hint() or not self._jumper.reach_wrong_hint():
            self._is_playing = False

    def _do_outputs(self):
        
        self._terminal_service.write_text(self._puzzle_word.get_word_displayed())
        self._terminal_service.draw(self._jumper.get_parachute())