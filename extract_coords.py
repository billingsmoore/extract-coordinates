from pypdf import PdfReader
import re
import csv

pdf = input('Enter name of pdf: ')

reader = PdfReader(pdf)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

pattern = r"\d+\.\d+/\s*\d+\.\d+"

text = str(text).replace('\00', '')

matches = re.findall(pattern, text)

for i in range(len(matches)):
    matches[i] = matches[i].split('/ ')


with open("Output.csv", "w") as f:
    writer = csv.writer(f)
    f.write('latitude, longitude\n')
    for match in matches:
        writer.writerow(match)