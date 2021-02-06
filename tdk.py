import sys
import json
#if you just get an error, try pip3 install --target=lib requests (be sure you have lib folder in your workflow)
from lib import requests

args = sys.argv[1]

def tdk(message) -> str:
    meanings = [i["anlamlarListe"][0]["anlam"] for i in requests.get(f"https://sozluk.gov.tr/gts?ara={message.lower().strip()}").json()]
    return ", ".join((meanings[0], meanings[1])) if len(meanings) >= 2 else meanings[0]
 
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
