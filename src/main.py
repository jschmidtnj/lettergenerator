import csv
import json
import sys
from pprint import pprint
from bs4 import BeautifulSoup
import errno
import os
import weasyprint

try:
    configfile = open('config.json')
except:
    print("problem with config file open")
    sys.exit()

try:
    config = json.load(configfile)
    #pprint(config)


except:
    print("problem with config file format")
    sys.exit()
try:
    csvfile = open(config["csvfilename"])
        
except:
    print("problem with csv file open")
    sys.exit()
try:
    csvreader = csv.reader(csvfile, delimiter=',')
except:
    print("problem with csv reader")
    sys.exit()

csv_data = []
for row in csvreader:
    #print(', '.join(row))
    row_data = []
    for item in row:
        row_data.append(item)
    csv_data.append(row_data)
#print(csv_data)

for i in range(len(csv_data)):
    if len(config["divsidstoreplace"]) != len(csv_data[i]):
        print("mismatch between csv data and num of divs to replace on line " + str(i+1) + " of " + config["csvfilename"] + ".")
        sys.exit()

try:
    templatehtml = open(config["templatefilename"])
except:
    print("problem with template open")
    sys.exit()

soup = BeautifulSoup(templatehtml, 'html.parser')
print(soup.prettify())

print(csv_data)
for i in range(len(csv_data)):
    for j in range(len(csv_data[i])):
        for div in soup.findAll("div", {"id": config["divsidstoreplace"][j]}):
            div.string = ((csv_data[i][j]))
            #print(div.string)
        #print(config["divsidstoreplace"][j], csv_data[i][j])
    if config["generatehtmlfiles"]:
        htmlfilename = config["htmloutputdirectory"] + "/file" + str(i)
        if not os.path.exists(os.path.dirname(htmlfilename)):
            try:
                os.makedirs(os.path.dirname(htmlfilename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(htmlfilename, "w") as outputfile:
            outputfile.write(str(soup))
    # generate pdf
    if config["generatepdffiles"]:
        pdffilename = config["pdfoutputdirectory"] + "/file" + str(i)
        if not os.path.exists(os.path.dirname(pdffilename)):
            try:
                os.makedirs(os.path.dirname(pdffilename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        pdf = weasyprint.HTML(str(soup)).write_pdf()
        with open(pdffilename, "w") as outputfile:
            outputfile.write(str(soup))