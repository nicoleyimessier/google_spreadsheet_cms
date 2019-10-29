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
    data = { "foods": [],"furniture": []}
 

    # Download from Google Sheets
    # https://github.com/burnash/gspread
    # https://github.com/googleapis/oauth2client
    gsheet = GoogleAPI.GSheets(keyfile)
    

    # First, download food tab by feeding the ("spreadsheet name", "spreadsheet tab name")
    objects = gsheet.download("spreadsheet_cms_example", "food") 
    values = objects.get_all_values()

    for rowIndex in range(1, len(values)):
        foodObj = {}
        foodObj["fruitName"] = (getCell("fruits", rowIndex, values));
        foodObj["veggieName"] = getCell("veggies", rowIndex, values);
        foodObj["dessertName"] = getCell("dessert", rowIndex, values);

        # Add this assets to the list
        data["foods"].append(foodObj)

    #second, download the furniture tab
    objects = gsheet.download("spreadsheet_cms_example", "furniture")
    values = objects.get_all_values()

    for rowIndex in range(1, len(values)):
        furnitureObj = {}
        furnitureObj["livingRoom"] = getCell("Living Room", rowIndex, values);
        furnitureObj["bedroom"] = (getCell("Bedroom", rowIndex, values));

        # Add this assets to the list
        data["furniture"].append(furnitureObj)

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

