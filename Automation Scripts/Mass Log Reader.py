#Python script that allows multiple CSV's to be read based on dictionary values.

import os
import pandas as pd

folder_path = "/home/andurin/Downloads/"
folder_contents = []

search_criteria = {
        'date' : '01-01-2025',
        'event_type' : 'Error',
        'details' : 'Lost Connectivity'
}

folder_contents = os.listdir(folder_path)

for file in folder_contents:
    if file.endswith(".csv"):
        print(file + " - Following events met search criteria")
        
        fr = pd.read_csv(folder_path + file)

        filtered_file = fr[
            (fr['date'] == search_criteria['date']) &
            (fr['event_type'] == search_criteria['event_type']) &
            (fr['details'].str.contains(search_criteria['details']))
        ]

        print(filtered_file)
