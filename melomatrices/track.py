from typing import Tuple, List
import numpy
from note import Note


class Track:
    def __init__(self,
                 track_number: int,
                 name: str,
                 title: str,
                 midi_numbers: Tuple[int, ...],
                 notes: List[Note]
                 ):

        self.track_number = track_number
        self.name = name
        self.title = title
        self.midi_numbers = midi_numbers
        self.notes = notes
        self.max_transition = 0

    def calc_std(self) -> numpy.ndarray:
        return numpy.std(self.midi_numbers)

    def calc_transitions(self) -> None:
        for note in self.notes:
            note.add_transitions(self.midi_numbers)

    def calc_frequencies(self) -> None:
        for note in self.notes:
            note.hz()

    def calc_max_transition(self) -> None:
        self.max_transition = max([max(note.transitions.values()) for note in self.notes if note.transitions])

    def numbers_list(self) -> List[int]:
        return [note.number for note in self.notes]

    def frequencies_list(self) -> List[int]:
        return [note.sound_frequency for note in self.notes]

    def __repr__(self):
        return f"{self.track_number}: {self.title} ({self.name}), " \
               f"{len(self.midi_numbers)} notes ({len(self.notes)} unique)"