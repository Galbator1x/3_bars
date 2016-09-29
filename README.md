3_bars
======

This script takes as input the coordinates and shows the biggest bar,
the smallest bar and closest bar.

Usage
-----

Download [list of bars](http://data.mos.ru/opendata/7710881420-bary).
Enter the path to the list of bars by first parameter
```
~$ python3 bars.py 'Бары.json'
Enter the coordinates
longitude:37.9
latitude:55.9
Biggest bar: ['Ночной клуб «Орфей»']
Smallest bar: ['БАР. СОКИ', 'Соки', 'Фреш-бар', 'Фито-бар', 'Бар в Деловом центре Яуза']
Closest bar: Бар «ЭПИЦЕНТР»
```

Requirements
------------

- Python >= 3.4
