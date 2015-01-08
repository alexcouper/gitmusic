from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note

STARTING_RANGE = "C C' E E, G G' C, E' G, C'' E,, G'' C,, E'' G,, C''' E,,, G''' C,,,, E'''' G,,,, C'''' E,,,, G'''' C,,,, E'''' G,,,,".split(' ')
TRANSPOSITION = 0
TRANSPOSITION_INCREASE = 0
MAPPING = {}
TIME = 0
DURATION = 0.25
# Mapping from person to index

def get_note(person):
    try:
        index = MAPPING[person]
    except KeyError:
        index = len(MAPPING)
        MAPPING[person] = index
    n = Note(STARTING_RANGE[index], dur=DURATION).transposition(TRANSPOSITION)
    return n

def get_chord(row):
    global TRANSPOSITION
    if not row:
        return
    people = list(set(row.split(' ')))
    if row and len(people) == 1:

        TRANSPOSITION += TRANSPOSITION_INCREASE
        if TRANSPOSITION > 0:
            TRANSPOSITION = TRANSPOSITION % 30
    notes = []
    for person in people:
        notes.append(get_note(person))
    chord = NoteSeq(notes)
    return chord

def main(content):
    """
    Turn content into a song.
    """
    midi = Midi(1, tempo=200)

    global TIME
    lines = content.splitlines()
    for row in lines:

        chord = get_chord(row.split('<>')[-1].strip())
        if chord:
            for note in chord:
                midi.midi_data.addNote(0, 0, note.midi_number,
                                       TIME, note.dur, note.volume)
        TIME += DURATION*2
    midi.write("live.mid")


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    content = file(filename, 'r').read()
    main(content)
