from typing import Dict, Tuple, List


class Note:
    def __init__(self, number: int):
        self.number = number
        self.sound_frequency: int = 0
        self.transitions: Dict[int, int] = {}

    def hz(self) -> None:
        self.sound_frequency = int(440 * (2 ** ((self.number - 69) / 12)))

    def add_transitions(self, midi_numbers: Tuple) -> None:
        for index, number in enumerate(midi_numbers[:-1]):
            if number == self.number:
                if midi_numbers[index + 1] not in self.transitions:
                    self.transitions[midi_numbers[index + 1]] = 1
                else:
                    self.transitions[midi_numbers[index + 1]] += 1

    def circle_params(self) -> List[Tuple]:
        return [(pair_number, self.number, value)
                for pair_number, value in self.transitions.items()]

    def __repr__(self):
        return f"{self.number} ({self.sound_frequency} Hz) " \
               f"{self.transitions}"
