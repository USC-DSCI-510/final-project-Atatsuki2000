[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12742596&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project

## Name of the Project

## Team Members (Name and Student IDs)

Ming Shan Lee, 1895899214
Takaaki Morita, 

## Instructions to create a conda enviornment

## Instructions on how to install the required libraries

`requirements.txt` lists out all the requiring packages you will need to reproduce this project. Run the code below to install all packages.

### Usage

```bash
pip install -r requirements.txt
```

## Instructions on how to download the data

In this project, we would be scraping data from yahoo finance and also using the yahoo finance python package. By running `get_data.py`, we would be scraping stock prices of the listing companies from September 2017 to October 2023:

- Goldman Sachs Group Inc. (GS)
- Morgan Stanley (MS)
- JP Morgan Chase &co. (JPM)
- Bank of America Corporation (BAC)
- Citigroup Inc. (C)

As for the yahoo finance package, it is imported in the `requirements.txt` and then

### Usage

```bash
python get_data.py ticker
```

## Instructions on how to clean the data

`clean_data.py` would be converting time attribute to datetime using python datetime package, dropping missing values, removing comma separators, converting data types, sorting data to ensure it's in chronological order, resetting index, and at last, dropping values that is 0, which indicates that the market was not open.

### Usage

```bash
python clean_data.py df
```

## Instrucions on how to run analysis code

## Instructions on how to create visualizations
