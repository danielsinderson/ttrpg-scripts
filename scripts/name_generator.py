"""

"""

import tracery, sys
from tracery.modifiers import base_english


rules = {
    "name_1": "#start1.capitalize##end1#",
    "start1": ["ab", "al", "am", "an", "ba", "bal", "tir", "tra", "ne", "ty", "dor"],
    "end1": ["lion", "ren", "rel", "tor", "lor", "lan", "kan", "kar"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)


def create_names(n: int) -> list:
    return [grammar.flatten("#name_1#") for i in range(n)]


def main():
    print(sys.argv)
    num: int = 1
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        print(num)
    names = create_names(num)
    print(names)


if __name__ == "__main__":
    main()