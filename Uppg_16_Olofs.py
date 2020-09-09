from pathlib import Path

def run():
    for line in Path('Uppg_16_fil.log').read_text().splitlines():
        if 'BEAR' in line or 'X-RAY' in line:
            print(line)

    dokument = "Uppg_16_fil.log"
    important = []
    keep_phrases = ["BEAR", "X-RAY"]
    lines = Path(dokument).read_text().splitlines()


if __name__ == '__main__':
    run()