import urllib, json;
import webbrowser
import time
src = "en"
out = "da"

f = open("/Users/anikaitsingh/Desktop/translator/languages.txt").readlines()
for i in range(len(f)):
    string = f[i].strip()
    beg = string.find(">", 1, len(string) - 1) + 1
    end = string.find("<", 1, len(string) - 1)
    word = string[beg:end]
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + src + "&tl=" + out + "&dt=t&q=" +  urllib.quote_plus(word);
    webbrowser.open_new_tab(url)
    time.sleep(1)
