import webbrowser

from pathlib import Path


p = Path('test.html')

webbrowser.open(str(p))

s = "Hejsan Banarne!"

s2 = s.replace("Hej", "Däj")

print(s2)