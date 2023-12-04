[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h_LXMCrc)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12742596&assignment_repo_type=AssignmentRepo)
# DSCI 510 Final Project

## Name of the Project

Post-Pandemic Analysis of Leading Investment Banks

## Team Members (Name and Student IDs)

Ming Shan Lee (ID: 1895899214), 
Takaaki Morita (ID: 7075405771) 

## Instructions to create a conda enviornment

Before starting, create a conda environment to reproduce the work.

Use 
```bash
conda create --name final_project_510 python=3.9
``` 
to create a conda environment.

And then use
```bash
conda activate final_project_510
```
to activate the conda environment.

## Instructions on how to install the required libraries

`requirements.txt` lists out all the requiring packages you will need to reproduce this project. Run the code below to install all packages.

Before running any code, please redirect your repository to `final-project-Atatsuki2000`

### Usage

```bash
cd final-project-Atatsuki2000
```

then

### Usage

```bash
pip install -r requirements.txt
```

## Instructions on how to redirect the repository before running project

Before running any code, please redirect your repository to `src`

### Usage

```bash
cd src
```

## Instructions on how to reproduce the work in one run

`main.py` would automatically run everything and doesn't require user to input any parameter. 

### Usage

```bash
python main.py
```

## Instructions on how to reproduce the work separately

Every script in this project are designed to be run individually. Follow the instructions in the following sections to do so.

## Instructions on how to download the data

In this project, we would be scraping data from the yahoo finance webpage and also using the yahoo finance python package. By running `get_data.py`, we would be scraping stock prices of the listing companies (ticker) from September 2017 to October 2023 and fetching the financial data from yfianance package:

- Goldman Sachs Group Inc. (GS)
- Morgan Stanley (MS)
- JP Morgan Chase & co. (JPM)
- Bank of America Corporation (BAC)
- Citigroup Inc. (C)

### Usage

```bash
python get_data.py ticker
```

After running this code, the terminal will output some snippet of the data and then save the data into the data\raw folder.

## Instructions on how to clean the data

`clean_data.py` would be converting time attribute to datetime using python datetime package, dropping missing values, removing comma separators, converting data types, sorting data to ensure it's in chronological order, resetting index, and at last, dropping values that is 0, which indicates that the market was not open. 

### Usage

Run this when cleaning stock price data:
```bash
python clean_data.py --stock_data stock_data_path
```

Run this when cleaning financial price data:
```bash
python clean_data.py --financial_data financial_data_path
```

After running this code, the terminal will output some snippet of the data and then save the data into the data\processed folder.

## Instrucions on how to run analysis code

`run_analysis.py` would be outputting analyses including statistical analysis of the financial data. We've tried to present the financial health of the companies, but due to lack of data, we were unable to do so.

```bash
python run_analysis.py financial_data_path
```

After running this code, the terminal will output some snippet of the analysis and a new folder `analysis` will be created if not already exsists. The statistical analyses will be saved here.

## Instructions on how to create visualizations

`visualize_results.py` would be outputting the heatmap of the stock prices data. In addition, we will also present the visualizations of the machine learning model that predicts future stock prices. To see more visulizations like simple moving average, exponential moving average, volatility, please refer to `FInal_project _510.ipynb` in the `results` folder.

### Usage
```bash
python visualize_results.py stock_data_path
```

After running this code, the terminall will first output the heatmap of the stock price data. Then, output some snippet of the data used in training and testing, the visualization of the machine learning model, and the metrics of the model. Both figures will be saved into a new folder `visualizations`.