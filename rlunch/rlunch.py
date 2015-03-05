# -*- coding: utf-8 -*-

from rullet import rullet
import random, codecs, os, sys
import click


class Menu:
    def __init__(self, name, distance, sort):
        self.name = name
        self.distance = distance
        self.sort = sort

menus = []
menus.append(Menu(u'화로사랑', 'm', 'k'))
menus.append(Menu(u'야끼도리센', 'n', 'j'))
menus.append(Menu(u'도원', 'm', 'c'))
menus.append(Menu(u'백암순대국밥', 'm', 'k'))
menus.append(Menu(u'피플일레븐', 'n', 'w'))
menus.append(Menu(u'제주도새기', 'n', 'k'))
menus.append(Menu(u'아비꼬', 'f', 'j'))
menus.append(Menu(u'연부대찌개', 'm', 'k'))
menus.append(Menu(u'썬데이반점', 'm', 'c'))
menus.append(Menu(u'취홍', 'n', 'c'))
menus.append(Menu(u'고슴도치', 'f', 'k'))
menus.append(Menu(u'대치동불고기', 'm', 'k'))
menus.append(Menu(u'새마을식당', 'f', 'k'))
menus.append(Menu(u'버거킹', 'n', 'w'))
menus.append(Menu(u'고운님', 'n', 'k'))
menus.append(Menu(u'본디마을', 'n', 'k'))
menus.append(Menu(u'아라섬', 'n', 'j'))
menus.append(Menu(u'뜰에서화로구이', 'n', 'k'))
menus.append(Menu(u'김밥천국', 'n', 'k'))
menus.append(Menu(u'스모키살룬', 'n', 'w'))

distance_options = ('f', 'm', 'n')
sort_options = ('k', 'c', 'j', 'w')


@click.command()
@click.option('-d', '--distance', type=click.Choice(distance_options), help=u'f:먼 m:보통 n:가까운')
@click.option('-s', '--sort', type=click.Choice(sort_options), help=u'k:한식 c:중식 j:일식 w:양식')
def lunch(distance, sort):
    while True:
        choice = rullet.run(menus)

        if is_recently_eaten(choice.name):
            continue
        if distance is not None and choice.distance != distance:
            continue
        if sort is not None and choice.sort != sort:
            continue

        break

    print choice.name
    add_recently_eaten(choice.name)


def is_recently_eaten(choice):
    if not os.path.exists('logs'):
        f = open('logs', 'w')
        f.close()

    f = open('logs', 'r')
    data = f.read().strip()
    arr = data.split('|')

    f.close()
    
    for str in arr:
        if choice == str.decode('utf-8').strip():
            return True

    return False


def add_recently_eaten(choice):
    f = codecs.open('logs', 'r', encoding='utf-8')
    data = f.read().strip()
    arr = data.split('|')

    if ''.decode('utf-8') in arr:
        arr.remove('')

    f.close()
    
    f = open('logs', 'w')
    arr.append(choice)

    if len(arr) >= 4:
        arr = arr[1:4]

    f.write('|'.join(arr).encode('utf-8').strip())
    f.close()


if __name__ == '__main__':
    lunch()
