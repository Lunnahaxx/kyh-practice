"2.0.Uppg_29 "
"Task info"
"""
Bygg ett Pythonprogram som genererar en random life quote med random getbild!

Hur? Jo genom att utgå ifrån bifogad fil, och byta ut "QUOTE_TEXT" mot 
get-citat som ni hittar i följande API:
   https://api.adviceslip.com/advice

Gör bara ett GET-request mot det så får ni random life advice!

HTML-fil att utgå ifrån bifogas som "uppgift29_template".html. 
Spara den i er kyh-practice.

Programmet ska alltså skapa en ny fil "goat_quote.html" där QUOTE_TEXT ersatts av ett nytt quote, 
och starta "goat_quote.html" i webbläsaren.

Tips: ni kommer behöva använda requests, webbrowser, och inbyggda replace() 
funktionen i string. Diskutera gärna igenom allt ni behöver göra först!
"""
"-------------------------"
"Koden 2.0.Uppg_29 "
"Lösningen"
import webbrowser
import requests
from pathlib import Path

r = requests.get("https://api.adviceslip.com/advice")
#r.text

print(r.json())


#p = Path('uppgift29_template.html')


#webbrowser.open(str(p))




#s = "Hejsan Banarne!"

#s2 = s.replace("Hej", "Däj")

#print(s2)















"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"




"-------------------------"
"-------------------------"
