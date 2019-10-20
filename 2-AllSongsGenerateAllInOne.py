import glob
import json
jsonfiles = []
desiredFilename = "somefile.txt"

with open(desiredFilename, 'a', encoding='utf-8') as the_file:
    for file in glob.glob("*.json"):
        jsonfiles.append(file)
        with open(file) as json_file:
            data = json.load(json_file)
            for p in data['songs']:
                the_file.write(p['lyrics'])
