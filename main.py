import sys
import heapq
import gc
# input = sys.stdin
input_string = input()
# input_string = 'beep boop beer!'
# input_string = 'abacabad'
# input_string = 'aa'


class Site:
    def __init__(self, weight, first_el, second_el):
        self.weight = weight
        self.first_el = first_el
        self.second_el = second_el
        self.parent = None

    def __repr__(self):
        return f"{self.weight}({self.first_el}:{self.second_el})"

    def __eq__(self, other):
        return self.weight == other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight


def get_path(branch: Site, parent: Site, res: str):

    if parent is None:
        return res

    if id(parent.first_el) == id(branch):
        res = '0'
    elif id(parent.second_el) == id(branch):
        res = '1'
    if isinstance(parent, Site):
        result = get_path(parent, parent.parent, '')
        res += result
        return res
    else:
        return res


def get_fric(input_string: str):

    input_set = set(input_string)
    d_sort = [(Site(input_string.count(x), x, '')) for x in input_set]
    heapq.heapify(d_sort)

    for i in range(len(d_sort)-1):
        first_el = heapq.heappop(d_sort)
        second_el = heapq.heappop(d_sort)
        new_el = Site(first_el.weight+second_el.weight, first_el, second_el)
        first_el.parent = new_el
        second_el.parent = new_el

        heapq.heappush(d_sort, new_el)
    return d_sort


d_sort = get_fric(input_string)
sites = [obj for obj in gc.get_objects() if isinstance(obj, Site) and (isinstance(obj.first_el, str))]
symbol_codes = {}
for sym in sites:
    symbol_codes[sym.first_el] = get_path(sym, sym.parent, '')[::-1]
    if symbol_codes[sym.first_el] == '':
        symbol_codes[sym.first_el] = '0'
code_string = ''
for sym in input_string:
    code_string += symbol_codes[sym]

print(len(set(input_string)), len(code_string))
for kv in symbol_codes.items():
    print(kv[0]+':', kv[1])
print(code_string)
