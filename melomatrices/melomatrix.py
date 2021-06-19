from matplotlib import font_manager as fm
from matplotlib import patches as patch
from matplotlib import pyplot as plot

from note import Note
from track import Track


class MeloMatrix:
    def __init__(self, title):
        self.axes = None
        self.track = None
        self.title = title
        self.font = fm.FontProperties(fname='../font/Raleway-ExtraLight.ttf')

    def create_track(self, midi, track_number, track_title) -> None:
        midi_numbers, notes = [], []

        for message in midi.tracks[track_number - 1]:
            if message.type == "note_on" and message.velocity != 0:
                midi_numbers.append(message.note)

        for midi_number in sorted(set(midi_numbers)):
            notes.append(Note(midi_number))

        self.track = Track(track_number, midi.tracks[track_number - 1].name, track_title, tuple(midi_numbers), notes)

    def draw(self) -> None:
        for note in self.track.notes:
            for params in note.circle_params():
                x, y, radius = params

                circle = patch.Circle(
                    (x, y),
                    radius=radius / (self.track.max_transition * 2),
                    color='white')

                self.axes.add_patch(circle)

    def labels(self) -> None:
        numbers = self.track.numbers_list()
        frequencies = self.track.frequencies_list()

        self.axes.set_xticks(numbers)
        self.axes.set_yticks(numbers)
        self.axes.set_xticklabels(frequencies, rotation=45)
        self.axes.set_yticklabels(frequencies)

        self.axes.set_title(self.track.title, fontsize=22, fontproperties=self.font)

        self.axes.text(
            0.02, 0.97,
            f'Standard Deviation: {round(self.track.calc_std(), 2)}',
            transform=self.axes.transAxes
        )

    def create_plot(self, size=10) -> None:
        plot.style.use('dark_background')
        plot.figure(figsize=(size, size))
        plot.suptitle(self.title, fontsize=30, fontproperties=self.font)
        plot.grid(True, linestyle='-', linewidth=0.05)
        plot.xlabel('Frequency (Hz)')

        self.axes = plot.subplot()

    def save_plot(self) -> None:
        self.axes.autoscale_view()
        plot.savefig(f'../plots/{self.title} | {self.track.title}.png')
