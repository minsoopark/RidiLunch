# -*- coding: utf-8 -*-

import random, codecs, os

menus = '화로사랑|야끼도리센|도원|백암순대국밥|피플일레븐|제주도새기|아비꼬|연부대찌개|썬데이반점|취홍|고슴도치|대치동불고기|새마을식당|버거킹'

def lunch():
    arr = open_menus()
    choice = arr[(int) (random.random() * len(arr))]

    if is_recently_eaten(choice):
        lunch()
        return

    print choice
    add_recently_eaten(choice)


def open_menus():
    data = menus.decode('utf-8').strip()
    return data.split('|')


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
