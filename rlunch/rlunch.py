# -*- coding: utf-8 -*-

import codecs
import os

import click
from rullet import rullet


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
@click.option('-d', '--distance',
              type=click.Choice(distance_options), help=u'f:먼 m:보통 n:가까운')
@click.option('-s', '--sort',
              type=click.Choice(sort_options), help=u'k:한식 c:중식 j:일식 w:양식')
def lunch(distance, sort):
    while True:
        choice = rullet.run(menus)

        if is_recently_eaten(choice.name):
            continue
        if distance and choice.distance != distance:
            continue
        if sort and choice.sort != sort:
            continue

        break

    print choice.name

    add_recently_eaten(choice.name)


def is_recently_eaten(choice):
    eaten_menus = get_eaten_menus()

    for menu in eaten_menus:
        if choice == menu.strip():
            return True

    return False


def add_recently_eaten(choice):
    eaten_menus = get_eaten_menus()
    eaten_menus.append(choice)

    remove_file()

    if len(eaten_menus) > 3:
        eaten_menus = eaten_menus[-3:]

    with codecs.open('logs', 'w+', encoding='utf-8') as f:
        f.write('|'.join(eaten_menus))


def get_eaten_menus():
    eaten_menus = []
    if not os.path.exists('logs'):
        open('logs', 'a').close()

    with codecs.open('logs', 'r', encoding='utf-8') as f:
        data = f.read().strip()
        eaten_menus = data.split('|')

    return eaten_menus


def remove_file():
    os.remove("logs")

if __name__ == '__main__':
    lunch()
