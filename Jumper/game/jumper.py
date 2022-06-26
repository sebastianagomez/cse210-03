class Jumper:

    def __init__(self):

        self._parachute = [" ___ ","/___\\", "\   /"," \ / ","  0  "," /|\ "," / \ "]
        self._wrong_hints = 0

    def update_parachute(self):

        self._wrong_hints = self._wrong_hints + 1

        self._parachute[self._wrong_hints - 1] = "     "

    def get_parachute(self):

        return self._parachute

    def reach_wrong_hint(self):

        return self._wrong_hints < 4