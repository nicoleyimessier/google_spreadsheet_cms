#!/usr/bin/python

import GoogleAPI
import json
import io
import sys
import os


# Helper for looking up cells by column name
def getCell(colName, rowIndex, values):
    return values[rowIndex][values[0].index(colName)]

def downloadData(keyfile, location):
    print "--- BEGIN RETRIEVING DATA ---"

    # Set up JSON
    data = { "materials": []}
 

    # Download from Google Sheets
    # https://github.com/burnash/gspread
    # https://github.com/googleapis/oauth2client
    gsheet = GoogleAPI.GSheets(keyfile)
    

    # First, download food tab by feeding the ("spreadsheet name", "spreadsheet tab name")
    objects = gsheet.download("CFC_Sample_Spreadsheet", "Materials") 
    values = objects.get_all_values()

    for rowIndex in range(1, len(values)):
        material = {}
        material["Title"] = (getCell("Title", rowIndex, values));
        material["Description"] = getCell("Description", rowIndex, values);
        material["Materials"] = getCell("Materials", rowIndex, values);
        material["Uses"] = (getCell("Uses", rowIndex, values));
        material["UnexpectedUses"] = getCell("UnexpectedUses", rowIndex, values);
        material["LogoFileName"] = getCell("LogoFileName", rowIndex, values);
        material["TopDown"] = (getCell("TopDown", rowIndex, values));
        material["Angled"] = getCell("Angled", rowIndex, values);
        material["MaterialColor"] = getCell("MaterialColor", rowIndex, values);
        material["DrawerLabel"] = getCell("DrawerLabel", rowIndex, values);
        material["UID"] = getCell("UID", rowIndex, values);
        material["CompanyAbout"] = getCell("CompanyAbout", rowIndex, values);

        # Add this assets to the list
        data["materials"].append(material)

    # Write to file
    with io.open(location, 'w+', encoding='utf8') as json_file:
        data = json.dumps(data, indent=4, ensure_ascii=False)
        json_file.write(unicode(data))

    print "--- FINISHED RETRIEVING DATA ---"

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) != 3:
        print "usage: <path/to/api/keyfile> <path/to/downloaded/json>"
        exit()
    elif os.path.exists(sys.argv[1]):
        downloadData(sys.argv[1], sys.argv[2])
    else:
        print "ERROR: keyfile arg is not valid path!"
        exit()

