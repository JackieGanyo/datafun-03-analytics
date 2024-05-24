'''Project 3:  During this project, the analyst is tasked with 
using Git for version control, creating and maintaining Python
virtual environments, and handling different types of data. 
'''
# Standard library imports
import csv
import os
import pathlib 
import json

# External library imports (requires virtual environment)
import requests  
from collections import Counter
import panda as pd
import xlrd

#Data Acquisition using requests library to fetch data from web APIs

def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
     '''
     Parameters for text data file retrieval
     -txt_url (str): URL where text file is located
     -txt_folder_name (str):  Name of text folder where text data will be saved
     -txt_file (str): Name of text file to be created
     '''
     try:
        # Fetch data from url    
        response = requests.get(txt_url)
        if response.status_code == 200:
        
        #Create folder if it does not exist
        if not os.path.exists(txt_folder_name):
            os.makedires(txt_folder_name)
        
        #Write text data to output file
        output_file_path = os.path.join(txt_folder_name, txt_filename)
        with open(output_file_path, 'w', endcoding='utf-8') as file:
            file.write(text_data)
            
        print(f"Text data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching text data file: {e}")
        
def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    """
    Fetches CSV data from the specified URL and writes it to a new file.

    Parameters:
    - csv_folder_name (str): Name of the folder where CSV file will be saved.
    - csv_filename (str): Name of the CSV file to be created.
    - csv_url (str): The URL of the online CSV file.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(csv_folder_name):
            os.makedirs(csv_folder_name)

        # Fetch CSV data from the URL
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write CSV data to the output file
        output_file_path = os.path.join(csv_folder_name, csv_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"CSV data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing CSV data: {e}")
        