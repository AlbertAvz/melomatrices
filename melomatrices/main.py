from argparser import path
from midifile import MidiFile
from melomatrix import MeloMatrix

midi = MidiFile(path)
midi.print_tracks()

track_number = int(input("Track number: "))
track_title = input("Track title: ")
title = input("Matrix title: ")

matrix = MeloMatrix(title)
matrix.create_track(midi, track_number, track_title)

matrix.track.calc_transitions()
matrix.track.calc_max_transition()
matrix.track.calc_frequencies()

matrix.create_plot()
matrix.draw()
matrix.labels()

matrix.save_plot()
