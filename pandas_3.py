import pandas as pd
import os
import json

# example usage of from_records format:
records = [("Espresso", "$5"),
           ("Flat White", "$10")]

pd.DataFrame.from_records(records)

pd.DataFrame.from_records(records,
                         columns = ["Coffee", "Price"])

# All columns that we need
KEYS_TO_USE = ['id', 'all_artists',
               'title', 'medium', 'dateText',
               'acquisitionYear', 'height',
               'width', 'units']

# Reading the JSON file:
def get_record_from_file(file_path, keys_to_use):
    """ Process single JSON file & return a tuple
        containing specific fields"""
    # Read these files 1 by 1 into JSON objects, put them into a tuple
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
        
        # Create an empty list, & for every key in the list, we extract the data & append to the record list,
        # then return the data in tuple form
        record = []
        for field in keys_to_use:
            record.append(content[field])
            
        return tuple(record)

# Single file processing function demo:
SAMPLE_JSON = os.path.join("C:/Users/jmcif/Downloads/ps/a00001-1035.json")
#SAMPLE_JSON = os.path.join('..', 'collection-master', 'artworks', 'a', '000',
                           #'a00001-1035.json')

sample_record = get_record_from_file(SAMPLE_JSON, KEYS_TO_USE)

def read_artworks_from_json(keys_to_use):
    """Traverse the directories with JSON files.
    For first file in each directory, call function for 
    processing single file & go to the next directory"""
    JSON_ROOT = os.path.join("C:/Users/jmcif/Downloads/ps")
    artworks = []
    for root, _, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith("json"):
                record = get_record_from_file(
                        os.path.join(root, f),
                        keys_to_use)
                artworks.append(record)
                break
        
    # Create the data frame
    df = pd.DataFrame.from_records(artworks,
                                   columns = keys_to_use,
                                   index = "id")
    return df

df = read_artworks_from_json(KEYS_TO_USE)
