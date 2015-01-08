# -*- coding: utf-8 -*-
# Written by Holmar Sigmundsson

import codecs

from collections import defaultdict
from datetime import datetime, timedelta
from dateutil import parser

author_mapping = {
    'Alex Couper': 'AC',
    'Alexander Kamyanskiy': 'AK',
    'Alexander Litvin': 'AL',
    'Andri Janusson': 'AJ',
    'AslaugEir': 'AE',
    'Axel \xc3\x96rn': 'AO',
    'Axel \xc3\x96rn Sigur\xc3\xb0sson': 'AO',
    'Carles': 'CB',
    'Carles Barrobe\xcc\x81s': 'CB',
    'Carles Barrob\xc3\xa9s i Meix': 'CB',
    'Hei\xc3\xb0ar \xc3\x9e\xc3\xb3r\xc3\xb0arson': 'HT',
    'Helgi Moller': 'HM',
    'Helgi M\xc3\xb6ller': 'HM',
    'Hlynur Sigur\xc3\xbe\xc3\xb3rsson': 'HS',
    'H\xc3\xb3lmar Sigmundsson': 'HD',
    'Jon Ingi Sveinbjornsson': 'JI',
    'Kristjan Oddsson': 'KO',
    'Kristj\xc3\xa1n Oddsson': 'KO',
    'Krystian Sikora': 'KS',
    'Roman Konoval': 'RK',
    'Sigurdur Fannar Vilhelmsson': 'SF',
    'Sigurdur Runar Helgason': 'SR',
    'Sigur\xc3\xb0ur Fannar Vilhelmsson': 'SF',
    'Sk\xc3\xbali Arnlaugsson': 'SA',
    'Steinar Hugi': 'SH',
    'Steinar Hugi Sigur\xc3\xb0arson': 'SH',
    'alexander-litvin': 'AL',
    'aslaug': 'AE',
    'hlysig': 'HS',
    'jonarnarazazo': 'JA',
    'kuxi': 'H',
    'nellib': 'NB',
}



date_sections = {}
# Create sections for every 6hr period in the year
shit_date = parser.parse('2014/01/01 06:00')
crap_date = parser.parse('2015/01/01 00:00')
while shit_date < crap_date:
    date_sections[shit_date.strftime('%Y/%m/%d %H:%M')] = []
    shit_date = shit_date + timedelta(hours=6)


def main(git_log_filepath):
    with codecs.open(git_log_filepath) as f:
        for line in f.readlines()[::-1]:
            date, author = line.strip().split(';')
            date_p = parser.parse(date)
            hour = int(date_p.strftime('%H'))
            hour_section = hour - (hour % 6)
            formatted_date = date_p.strftime('%Y/%m/%d')
            shit = parser.parse('{0} {1}:00'.format(formatted_date, hour_section))
            if shit.year == 2013: continue
            date_sections[shit.strftime('%Y/%m/%d %H:%M')].append(author_mapping[author])


    for ds in sorted(date_sections.keys()):
        print ds, '<>', ' '.join(date_sections[ds])

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
