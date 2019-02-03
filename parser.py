import re
import models

def parse_line(line):
    re_competentie = re.compile(r'^Competentie ([0-9]+) - (.+)')
    re_deelcompetentie = re.compile(r'^Deelcompetentie ([0-9]+\.[0-9]+) - (.+)')
    re_leerplandoel = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+) (.+)')

    match = re_competentie.match(line)
    if match:
        c = models.Competentie()
        c.nummer = match.group(1).strip()
        c.omschrijving = match.group(2).strip()
        return c
        
    match = re_deelcompetentie.match(line)
    if match:
        d = models.Deelcompetentie()
        d.nummer = match.group(1).strip()
        d.omschrijving = match.group(2).strip()
        d.competentie = d.nummer.split('.')[0]
        return d
        
    match = re_leerplandoel.match(line)
    if match:
        l = models.Leerplandoel()
        l.nummer = match.group(1).strip()
        l.omschrijving = match.group(2).strip()
        l.competentie = l.nummer.split('.')[0]
        l.deelcompetentie = l.nummer.split('.')[1]
        return l
    
    return None


def parse_leerplandoelentekst():
    leerplanonderdelen = []
    
    with open('leerplandoelen_text.txt', 'r') as f:
        for line in f:
            r = parse_line(line)
            if r:
                leerplanonderdelen.append(r)

    return leerplanonderdelen
