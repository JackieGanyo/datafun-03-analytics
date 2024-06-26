'''Project 3:  During this project, the analyst is tasked with 
using Git for version control, creating and maintaining Python
virtual environments, and handling different types of data. 
'''
# Standard library imports
import csv
import encodings
import os
import pathlib 
import json

# External library imports (requires virtual environment)
import pandas as pd
import requests
from collections import Counter
import xlrd

#Data Acquisition using requests library to fetch data from web APIs
# Text DATA FETCH
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    '''
    Fetches text data from a given URL and writes it to a text file.

    Parameters:
    - txt_folder_name (str): Name of the folder where the text file will be saved.
    - txt_filename (str): Name of the text file to be created.
    - txt_url (str): The URL of the online text data.

    Returns:
    None
    '''
    try:
        # Create folder if it does not exist
        if not os.path.exists(txt_folder_name):
            os.makedirs(txt_folder_name)
        
        # Fetch data from url    
        response = requests.get(txt_url)
        if response.status_code == 200:
            # Write text data to output file
            with open(os.path.join(txt_folder_name, txt_filename), 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Text data successfully written to '{os.path.join(txt_folder_name, txt_filename)}'.")
        
    except Exception as e:
        print(f"Error fetching or writing text data: {e}")
        
# CSV DATA FETCH
def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    '''
    Fetches CSV data from a given URL and writes it to a CSV file.

    Parameters:
    - csv_folder_name (str): Name of the folder where the CSV file will be saved.
    - csv_filename (str): Name of the CSV file to be created.
    - csv_url (str): The URL of the online CSV data.

    Returns:
    None
    '''
    try:
        # Create folder if it does not exist
        if not os.path.exists(csv_folder_name):
            os.makedirs(csv_folder_name)
        
        # Fetch data from url
        response = requests.get(csv_url)
        if response.status_code == 200:
            # Write CSV data to output file
            with open(os.path.join(csv_folder_name, csv_filename), 'wb') as file:
                file.write(response.content)
            print(f"CSV data successfully written to '{os.path.join(csv_folder_name, csv_filename)}'.")
        
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
        
# Function to process csv data
def process_csv_file(csv_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(csv_folder_name, input_filename)

        # Read input CSV file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Read the header to dynamically determine column names
            header = next(csv_reader)

            # Read data and convert rows to tuples
            data = [tuple(row) for row in csv_reader]

        # Pandas dataframe for analysis
        df = pd.DataFrame(data, columns=header)

        # Calculate summary statistics
        summary_stats = df.describe()

        #convert summary statistics to string
        summary_stats_str = str(summary_stats)

        # Define output file path
        output_summary_path = os.path.join(csv_folder_name, output_filename)

        # Write summary statistics to output text file
        with open(output_summary_path, 'w') as output_file:
            output_file.write(summary_stats_str)
        print(f"Summary statistics saved to '{output_summary_path}'")
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        
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

#Main Function - Implement a main() function to test the folder creation functions and demonstrate 
#the use of imported modules.
def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print my name
    name = "Jackie Ganyo"
    print(f"Name: {name}")

    # URL's where data was pulled
    txt_url = 'https://www.thecompleteworksofshakespeare.com/tragedy/romeo-and-juliet'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'
    
    # Folder names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 
    
    # File names
    txt_filename = 'romeoJuliet.txt'
    csv_filename = 'countryLadderScore.csv'
    excel_filename = 'cattle.xls' 
    json_filename = 'astronauts.json' 
    
    # Functions to take web data and convert it to a specified file format
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)
    
    # Functons for text processing in different file formats
    process_txt_file('data-txt', 'romeoJuliet.txt', 'romeoJuliet_analysis.txt')
    process_csv_file('data-csv', 'countryLadderScore.csv', 'countryLadderScore_analysis.txt')
    process_excel_file('data-excel', 'cattle.xls', 'cattle_analysis.txt')
    process_json_file('data-json', 'astronauts.json', 'astronauts_analysis.txt')

#9. Conditional Script Execution (At the end of the file) - Ensure the main function only executes when 
#the script is run directly, not when imported as a module by using standard boilerplate code.
if __name__ == '__main__':
    main()