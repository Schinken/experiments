__author__ = 'schinken'

# Peg Game Solver
# description: https://en.wikipedia.org/wiki/Peg_solitaire
#
# Example Game:
#
#       1
#      2 3
#     4 5 6
#    7 8 9 a
#   b c d e f

possible_moves = [
    ('1','2','4'),('2','4','7'),('4','7','b'),('b','7','4'),('7','4','2'),('4','2','1'),
    ('1','3','6'),('3','6','a'),('6','a','f'),('f','a','6'),('a','6','3'),('6','3','1'),
    ('b','c','d'),('c','d','e'),('d','e','f'),('f','e','d'),('e','d','c'),('d','c','b'),
    ('3','5','8'),('5','8','c'),('c','8','5'),('8','5','3'),
    ('2','5','9'),('5','9','e'),('e','9','5'),('9','5','2'),
    ('7','8','9'),('8','9','a'),('a','9','8'),('9','8','7'),
    ('6','9','d'),('d','9','6'),
    ('4','8','d'),('d','8','4'),
    ('4','5','6'),('6','5','4')
]

def main():
    print "Do something"


if __name__ == "__main__":
    main()