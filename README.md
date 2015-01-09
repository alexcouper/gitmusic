# gitmusic
Lightning talk fodder: turn the repo into a (rather awful) piece of music


## Installation

```
 $ pip install -r requirements.txt
```

## Usage

### get_git_data.py

Usage:
```
    python get_git_data.py <filename> > create_midi_input.txt
```

filename should contain content in the following format::

  Date; author

eg
```
    Fri Jan 3 16:07:02 2014;Alex Couper
    Fri Jan 3 15:10:48 2014;Alex Couper
```

To create a file in this form, you can use the git command:
```
    git log --after=2013-12-31 --until=2015-01-01 --format='%ad;%an' --date=local > get_git_data_input.txt
```






### create_midi.py

Usage:
```
    python create_midi.py <filename>
```
filename should contain content in the following format::

        Ignored Content <> space delimited items

eg:
```
    2014/01/02 06:00 <> HM SF AC
    2014/01/02 12:00 <> SA AC NB NB HS HM HM RK AC
    2014/01/02 18:00 <>
    2014/01/03 00:00 <> HS
```
Each item in the space delimited items is assigned a note.
All notes for a line are played together.
If a line occurs where only one item exists, the level that the notes are
transposed is increased by ``TRANSPOSITION_INCREASE``.

A midi file is written to ``live.mid``.

A example midi file generated from this can be found in ``examples``.
