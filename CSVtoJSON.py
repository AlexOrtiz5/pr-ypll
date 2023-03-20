##Version 1
import pandas as pd

df = pd.read_csv (r'dataset_defunciones.csv')
print(df)
df.to_json (r'dataset_defunciones.json')

# The code was taken from https://datatofish.com/csv-to-json-string-python/#:~:text=Step%203%3A%20Convert%20the%20CSV%20to%20JSON%20String%20using%20Python&text=You'll%20need%20to%20modify,be%20stored%20on%20your%20computer.&text=Run%20the%20code%20in%20Python,created%20at%20your%20specified%20location.

#################################################################################
#Version 2

# import csv
# import json

# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
     
#     # create a dictionary
#     data = {}
     
#     # Open a csv reader called DictReader
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)
         
#         # Convert each row into a dictionary
#         # and add it to data
#         for rows in csvReader:
             
#             # Assuming a column named 'No' to
#             # be the primary key
#             key = rows['No']
#             data[key] = rows
 
#     # Open a json writer, and use the json.dumps()
#     # function to dump data
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))
         
# # Driver Code
 
# # Decide the two file paths according to your
# # computer system
# csvFilePath = r'dataset_defunciones.csv'
# jsonFilePath = r'dataset_defunciones.json'
 
# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)

# The code was taken from https://www.geeksforgeeks.org/convert-csv-to-json-using-python/