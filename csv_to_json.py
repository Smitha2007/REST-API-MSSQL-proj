import csv 
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)
        
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray, indent=4))

csvFilePath = r"OWGR_Ranking.csv"
jsonFilePath = r"OWGR_Ranking.json"

csv_to_json(csvFilePath, jsonFilePath)