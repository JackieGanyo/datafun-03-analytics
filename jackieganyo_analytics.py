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
# Text DATA FETCH
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
     '''
     Parameters for text data file retrieval
     -txt_url (str): URL where text file is located
     -txt_folder_name (str):  Name of text folder where text data will be saved
     -txt_file (str): Name of text file to be created
     '''
     try:
         #Create folder if it does not exist
        if not os.path.exists(txt_folder_name):
            os.makedires(txt_folder_name)
        
        # Fetch data from url    
        response = requests.get(txt_url)
        if response.status_code == 200:
                
        #Write text data to output file
            output_file_path = os.path.join(txt_folder_name, txt_filename)
        with open(output_file_path, 'w', endcoding='utf-8') as file:
            file.write(response.text)
            
        print(f"Text data successfully written to '{output_file_path}'.")
     except Exception as e:
        print(f"Error fetching text data file: {e}")
   
# CSV DATA FETCH
     
def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    """
    Parameters for CSV Data Fetch:
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
 
 # Excel DATA FETCH
 
def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):
    """
    Parameters for Excel Data Fetch:
    - excel_folder_name (str): Name of the folder where excel file will be saved.
    - excel_filename (str): Name of the excel file to be created.
    - excel_url (str): The URL of the online excel file.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(excel_folder_name):
            os.makedirs(excel_folder_name)

        # Fetch Excel data from the URL
        response = requests.get(excel_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write Excel data to the output file
        output_file_path = os.path.join(excel_folder_name, excel_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Excel data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing Excel data: {e}")

# JSON DATA FETCH
def fetch_and_write_json_data(json_folder_name, json_filename, json_url):
    """
    Parameters for JSON Data Fecth:
    - json_folder_name (str): The name of the folder where the JSON file will be saved.
    - json_filename (str): The name of the JSON file to be created.
    - json_url (str): The URL of the online JSON data.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(json_folder_name):
            os.makedirs(json_folder_name)

        # Fetch JSON data from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON data
        json_data = response.json()
        
        # Write JSON data to the output file
        output_file_path = os.path.join(json_folder_name, json_filename)
        with open(output_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        print(f"JSON data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing JSON data: {e}")
        
# Function to process text data.  Since this is a text only document
# word count analysis along will be used.
def process_txt_file(txt_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(txt_folder_name, input_filename)
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            text_data = input_file.read()

        # Split text into words and caluclate word count
        word_count = len(text_data.split())

        # Convert the Counter object to a string for writing to file
        processed_data = f"Word Count: {word_count}\n{text_data}"

        # Define output file path
        output_file_path = os.path.join(txt_folder_name, output_filename)
            
        # Write processed data to output text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)
            
        print(f"Processed data written to '{output_file_path}'")
    except Exception:
        print("Error processing text file.")

# Function to process excel data.  This data set contains information on cattle, 
# summary statitsics run. 
def process_excel_file(excel_folder_name, input_filename, output_filename):
    try:
        # Construct the file paths
        input_file_path = os.path.join(excel_folder_name, input_filename)
        output_file_path = os.path.join(excel_folder_name, output_filename)
        
        # Read input Excel file
        df = pd.read_excel(input_file_path)
        
        # Calculate summary statistics
        summary_stats = df.describe()
        
        # Convert the summary statistics DataFrame to a string for writing to file
        summary_stats_str = summary_stats.to_string()
        
        # Write summary statistics to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(summary_stats_str)
        
        print(f"Summary statistics written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing Excel file: {e}")

# Function to process json data 
def process_json_file(json_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(json_folder_name, input_filename)
        with open(input_file_path, 'r') as file:
            json_data = json.load(file)
        
        # Print the loaded JSON data to see its structure
        print("JSON Data Structure:")
        print(json_data)
        
        # Check if "people" key exists in the JSON data
        if "people" in json_data:
            people_list = json_data["people"]
            for person in people_list:
                name_value = person["name"]
                craft_value = person["craft"]
                print(f"Name: {name_value}, Craft: {craft_value}")
                
                # Construct formatted information
                json_info = f"Name: {name_value}\nCraft: {craft_value}"
                
                # Define output file path for each person
                output_person_path = os.path.join(json_folder_name, f"{name_value}_{output_filename}")
                
                # Write information to output text file for each person
                with open(output_person_path, 'w') as output_file:
                    output_file.write(json_info)
                
                print(f"Formatted information saved to '{output_person_path}'")
        else:
            print("Error: 'people' key not found in JSON data.")
            return
        
    except Exception as e:
        print(f"Error parsing JSON data: {e}")