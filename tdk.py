import sys
import json
from lib import requests

args = sys.argv[1]

def tdk(message) -> str:
    search_message = message.lower().strip()
    r = requests.get(f"https://sozluk.gov.tr/gts?ara={search_message}")
    r_content = r.json()
    
    meanings = [i["anlamlarListe"][0]["anlam"] for i in r_content]

    if len(meanings) >= 2:
        return ", ".join((meanings[0], meanings[1]))
        
    else:
        return meanings[0]
meaning = tdk(args)

try:
    title = ""
    for i in meaning:
        title += i
        meaning = meaning[meaning.index(i) + 1:]
        if len(title) >= 50:
            break

    subtext = meaning
    
except Exception as e:
    title = f"için sözlük.gov.tr'de ki sonuçlar:"
    subtext = meaning
result ={
    "items":
        [
            {
                "type": "text",
                "title": title,
                "subtitle": "".join(meaning).strip(),
                "arg": meaning
            }
        ]
}

finalResult = json.dumps(result)

print(finalResult)
