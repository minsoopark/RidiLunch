# -*- coding: utf-8 -*-

from rullet import rullet
import random, codecs, os, sys

menus = '화로사랑|야끼도리센|도원|백암순대국밥|피플일레븐|제주도새기|아비꼬|연부대찌개|썬데이반점|취홍|고슴도치|대치동불고기|새마을식당|버거킹|고운님|본디마을|아라섬|뜰에서화로구이'

# k: 한식 j: 일식 c: 중식 a: 양식
sort = 'k|j|c|k|a|k|j|k|c|c|k|k|k|a|k|k|j|k'

# f: 먼 m: 보통 n: 가까운
distance = 'm|n|m|m|n|n|f|m|m|n|f|m|f|n|n|n|n|n'

def lunch(param=[]):
    arr = open_menus()
    
    if len(param) > 0:
        args = ['', param]
    else:
        args = sys.argv
    
    choice = process_args(args)
    
    if not choice:
        return

    if is_recently_eaten(choice):
        lunch()
        return

    print choice
    add_recently_eaten(choice)


def open_menus():
    data = menus.decode('utf-8').strip()
    return data.split('|')


def open_sorts():
    data = sort.decode('utf-8').strip()
    return data.split('|')


def open_distances():
    data = distance.decode('utf-8').strip()
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


def process_args(args):
    arr = open_menus()
    darr = open_distances()
    sarr = open_sorts()
    
    results = []
    if len(args) >= 2:
        f_arg = args[1]
        if f_arg.startswith('-d'):
            for idx, d in enumerate(darr):
                if d == f_arg[2:]:
                    results.append(arr[idx])
        elif f_arg.startswith('-s'):
            for idx, s in enumerate(sarr):
                if s == f_arg[2:]:
                    results.append(arr[idx])
    else:
        results = arr
        
    if len(results) == 0:
        print_help()
        return None
    
    choice = rullet.run(results)
    return choice


def print_help():
    print ''
    print '<< Options Help >>'
    print u'-d : 거리별 추첨 (f: 먼, m: 보통, n: 가까운)'
    print u'-s : 종류별 추첨 (k: 한식, c: 중식, j: 일식, a:양식)'
    print ''


if __name__ == '__main__':
    lunch()
