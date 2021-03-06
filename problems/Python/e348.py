''' Many numbers can be expressed as the sum of a square and a cube. Some of
them in more than one way. Find the sum of the five smallest such palindromic
numbers '''

from itertools import count
from collections import defaultdict
from euler import get_palindromes

def main():
    ''' Driver function '''
    end = int(9e8)
    palindromes = get_palindromes(0, end)
    cubes = cube_list(end)
    valid = add_cube_square(cubes, palindromes, end)
    print(sum(valid))

def add_cube_square(cubes, palindromes, end):
    ''' Add a square to every cube in 'cubes' and check if the result is in
    'palindromes'. Increment base of 'square' ('n') until it exceeds 'end'. The
    base of 'square' ('n') starts at 2. Keeps track of how many different ways
    each palindrome can be expressed as the sum of a cube and a square. Returns
    a sorted list of all palindromes that can be expressed in exactly four
    different ways '''
    n = 2
    square = 4
    valid = defaultdict(int)
    max_palin = max(palindromes)
    while square < end:
        square = n**2
        for cube in cubes:
            check = cube + square
            if check > max_palin:
                break
            if check in palindromes:
                valid[check] += 1
        n += 1
    return sorted(pal for pal, num in valid.items() if num == 4)

def cube_list(end):
    ''' Return list of cubes in the interval [8, 'end'] '''
    n = 2
    cube = 8
    cubes = []
    while cube <= end:
        cube = n**3
        cubes.append(cube)
        n += 1
    return cubes

if __name__ == "__main__":
    main()