import re

from tika import parser


def factor(a, b, c):
    for i in range(-100, 100):
        for j in range(-100, 100):
            if i*j == c and i+j == b or i * j == a * c and i + j == b:
                return i, j


def factor_readable(a, b, c):
    for i in range(-30, 30):
        for j in range(-30, 30):
            if i*j == c and i+j == b:
                if i > 0 and j > 0:
                    return "(x+"+str(i)+")(x+"+str(j)+")"
                elif i > 0 and j < 0:
                    return "(x+"+str(i)+")(x"+str(j)+")"
                elif i < 0 and j > 0:
                    return "(x"+str(i)+")(x+"+str(j)+")"
                else:
                    return "(x"+str(i)+")(x"+str(j)+")"
    return "Not Factorable!"


def solve_by_factor(a, b, c):
    for i in range(-30, 30):
        for j in range(-30, 30):
            if i*j == c and i+j == b:
                return "X="+str(i*-1)+" or X="+str(j*-1)


def read_pdf_to_string(file_name):
    return parser.from_file(file_name)['content']

# regex should find all quadratics and return them so they can be parsed

def get_all_equations(text):
    regex = r"(?:(-?\d*x\^2\+?-?\d*x\+?-?\d*|x\^2\+?-?\d*x\+?(\d*))|(-?\d*x\^2|x\^2)|(-?\d*x\^2\+?-?\d*|x\^2\+?-?\d*))|(-?\d*x\^2\+?-?\d*x|x\^2\+?-?\d*x)|(\(x\+?-?\d*\)\^2\+?-?\d*)|(-?\d*\(x\+?-?\d*\)\^2(\+?-?\d*))|(-?\d*\(x\+?-?\d*\)\^2)|(\(x\+?-?\d*\)\^2)"
    unfiltered = re.findall(regex, text)
    return [j for i in unfiltered for j in i if len(j) != 0]

# Deprecated
def quadFinder(text):
    # WIP regex
    regex = r"(?:(?:(-?\d)*x\^2(?:\+|-)(-?\d)*x(?:\+|-)(-?\d)*|x\^2(?:\+|-)(-?\d)*x(?:\+|-)(\d*))|(?:(-?\d)*x\^2|x\^2)|(?:(-?\d)*x\^2(?:\+|-)(-?\d)*|x\^2(?:\+|-)(-?\d)*))|(?:(-?\d)*x\^2(?:\+|-)(-?\d)*x|x\^2(?:\+|-)(-?\d)*x)|(?:\(x(?:\+|-)(-?\d)*\)\^2((?:\+|-)(-?\d)*))|(?:(-?\d)*\(x(?:\+|-)(-?\d)*\)\^2((?:\+|-)(-?\d)*))|(?:(-?\d)*\(x(?:\+|-)(-?\d)*\)\^2)|(?: \(x(?:\+|-)(-?\d)*\)\^2)"
    unfiltered_matches = re.findall(regex, text)
    filtered_matches = []
    for i in unfiltered_matches:
        for j in i:
            if len(i) == 0:
                continue
            else:
                filtered_matches += j
    return [float(i) for i in filtered_matches]


def main(text):
    data = quadFinder(text)
    print(factor_readable(data[0], data[1], data[2]))


if __name__ == "__main__":
    main("2x^2+3x+2")
