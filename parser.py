import re

def parse_line(line):
    re_competentie = re.compile(r'^Competentie ([0-9]+) - (.+)')
    re_deelcompetentie = re.compile(r'^Deelcompetentie ([0-9]+\.[0-9]+) - (.+)')
    re_leerplandoel = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+) (.+)')

    match = re_competentie.match(line)
    if match:
        print("C")
        print(match.group(1, 2))

    match = re_deelcompetentie.match(line)
    if match:
        print("  D")
        print(match.group(1, 2))

    match = re_leerplandoel.match(line)
    if match:
        print("    L")
        print(match.group(1, 2))


if __name__ == '__main__':
    print("hello")
    with open('leerplandoelen_text.txt', 'r') as f:
        for line in f:
            parse_line(line)