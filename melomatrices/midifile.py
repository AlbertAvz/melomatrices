import mido


class MidiFile(mido.MidiFile):
    def print_tracks(self, meta_only=False) -> None:
        print(f"{len(self.tracks)} tracks in {self.filename}")

        for number, track in enumerate(self.tracks):
            if not track.name:
                track.name = "Unnamed"
            print(f"Track {number + 1}: {track.name} ({len(track)} messages)")
