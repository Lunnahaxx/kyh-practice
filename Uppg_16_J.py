#import pathlib

#p = pathlib.Path("Uppg_16_fil.log")

#content = p.read_text()



def case():

    dokument = "Uppg_16_fil.log"
    important = []
    keep_phrases = ["BEAR", "X-RAY"]

    with open(dokument) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        for phrase in keep_phrases:
            if keep_phrases in line:
                important.append(line)
                break

    print(*important, sep="\n")


if __name__ == 'main':
    case()