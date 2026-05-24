# API Documentation

## Data Source

This project uses data from the RescueGroups.org API.

## API Endpoint Used

```text
https://api.rescuegroups.org/v5/public/animals/search/available

Authentication

The API requires an API key passed through the Authorization header.

The API key is stored locally in a .env file and is not uploaded to GitHub.

Example:

headers = {
    "Authorization": RG_API_KEY
}

Extraction Method

Data was pulled using Python with the requests library.

The API response was returned in JSON format, then converted into a pandas DataFrame.

The final dataset was exported as a CSV file.

Output File
data/raw/rescue_groups_animals.csv
Dataset Size

The extracted dataset contains approximately 61,433 animal records.

Main Fields Collected
Animal ID
Name
Species ID
Primary Breed
Secondary Breed
Sex
Age Group
Age String
Current Size/Weight
Adoption Pending Status
Foster Need Status
Picture Count
Thumbnail URL
Created Date
Updated Date
Description
Notes

The raw API data may contain missing values, HTML encoding, and long text descriptions. These will be handled during the cleaning phase.