def first_repeating(lst):
    symbol_dct = {}
    for symb in lst:
        if symb not in symbol_dct:
            symbol_dct[symb] = 1
        else:
            symbol_dct[symb] += 1

        if symbol_dct[symb] == 2:
            return symb


def first_repeating_v2(lst):
    """ Можно было создать список, но он занимает больше памяти """
    symbol_str = ''
    for symb in lst:
        if str(symb) in symbol_str:
            return symb
        symbol_str += str(symb)


def first_repeating_v3(lst):
    """ Самый оптимальный вариант """
    for i, symb in enumerate(lst):
        if symb in lst[:i]:
            return symb


print(first_repeating(['a', 'b', 'c', 'k', 'b', 'd', 'b']))
print(first_repeating_v2(['a', 'b', 'c', 'k', 'b', 'd', 'b']))
print(first_repeating_v3(['a', 'b', 'c', 'k', 'b', 'd', 'b']))
print(first_repeating(['a', 'b', 2, 'c', 'k', 'd', 3, 2]))
print(first_repeating_v2(['a', 'b', 2, 'c', 'k', 'd', 3, 2]))
print(first_repeating_v3(['a', 'b', 2, 'c', 'k', 'd', 3, 2]))
