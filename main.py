import json
from estree.parser import parse


def main():
    with open('filmbox.json', 'r') as f:
        ast = json.load(f)
    print(parse(ast))


if __name__ == '__main__':
    main()
