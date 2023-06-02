from pypdf import PdfReader
import re
import csv

# get name of pdf from user
pdf = input('Enter name of pdf: ')

# initialize a pdf reader
reader = PdfReader(pdf)

# read the text off of the pdf
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

# regex to get the coordinates from text
pattern = r"\d+\.\d+/\s*\d+\.\d+"

# strip out the null values when the pdf reader mangles ukrainian
# nulls mess up the pattern matching
text = str(text).replace('\00', '')

matches = re.findall(pattern, text)

# turn the coordinates into a csv friendly syntax
for i in range(len(matches)):
    matches[i] = matches[i].split('/ ')

# write the coordinates out to csv
with open("Output.csv", "w") as f:
    writer = csv.writer(f)
    # put header in the csv
    f.write('latitude, longitude\n')
    for match in matches:
        writer.writerow(match)