import json
path = "/Users/anikaitsingh/Desktop/translator/danish/"
file_in = "/Users/anikaitsingh/Desktop/translator/languages.txt"
file_out = "/Users/anikaitsingh/Desktop/translator/languages_danish.txt"

f = open(file_in).readlines()
out = open(file_out, "w+")
for i in range(len(f)):
    with open(path + str(i+1) + ".json") as x:
        data = json.load(x)[0][0][0].encode('utf-8')
    string = f[i].strip()
    beg = string.find(">", 1, len(string) - 1) + 1
    end = string.find("<", 1, len(string) - 1)
    string = string[:beg] + data + string[end:]
    print string
    out.write(string + "\n")
