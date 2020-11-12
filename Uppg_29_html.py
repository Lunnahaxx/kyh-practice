"Uppg_29 "
"Task info"
"""
Bygg ett Pythonprogram som genererar en random life quote med random getbild!

Hur? Jo genom att utgå ifrån bifogad fil, och byta ut "QUOTE_TEXT" mot 
get-citat som ni hittar i följande API:
   https://api.adviceslip.com/advice

29.1 Gör bara ett GET-request mot det så får ni random life advice!

HTML-fil att utgå ifrån bifogas som "uppgift29_template".html. 
Spara den i er kyh-practice.

Programmet ska alltså skapa en ny fil "goat_quote.html" där QUOTE_TEXT ersatts av ett nytt quote, 
och starta "goat_quote.html" i webbläsaren.

Tips: ni kommer behöva använda requests, webbrowser, och inbyggda replace() 
funktionen i string. Diskutera gärna igenom allt ni behöver göra först!
"""
"-------------------------"
"Uppg_29 "
"Lösningen"
#import webbrowser
import requests
from pathlib import Path

r = requests.get("https://api.adviceslip.com/advice")
json_dict = r.json() #laddar api'n som en rå json fil, där r betyder read
dict_1 = json_dict["slip"] #öppnar dictionaryt där slip är key till ett inre dictionary
value_quote = dict_1["advice"] #key'n advide öppnar valuet som är quote'n, "value_quote"

content = Path("uppgift29_template.html").read_text() #variablen content anger vägen till
# html templaten, som med .read_text inläses
value = content.replace("QUOTE_TEXT", value_quote) #här ersätter säger man att i content skall
# man replace'a "QUOTE_TEXT" med value_quote,som hämtas från dict'et ovan. Den nya replaceade value
# variabeln läses sedan in i p.write_text där den "skrivs in"
p = Path("goat_q.html") #man anger p och vad man skall skapa. goat_q.html görs redo för att skapad som en ny fil
p.write_text(value, encoding='utf8') #här skapas den nya filen av python med innehållet man ger den i value,
# alltså en html sida som heter goat_q.html där man bytt ut ordet "QUOTE_TEXT" till ett random life advice hämtat
# från api'ovan, r.

print("Rå json, slipgrejen: ", dict_1)
print("Key'n 'advice' öppnar : valuet som vi döpt til variabeln 'value_quote' som är: ", value_quote)




#print(advice)
#print(r.json())

#p = Path('uppgift29_template.html')
#webbrowser.open(str(p))

#s = "QUOTE_TEXT"
#s2 = s.replace("QUOTE_TEXT", "r")

#s = "Hejsan Banarne!"

#s2 = s.replace("Hej", "Däj")

#print(s2)


"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"




"-------------------------"
"-------------------------"
