import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

def plot_correlation_heatmap(stock_data):
    df = pd.read_csv(stock_data)

    # Compute correlation matrix
    df.drop('Date', axis=1, inplace=True)
    correlation_matrix = df.corr()

    # Create a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'Correlation Heatmap for {os.path.basename(stock_data)}')

    output_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'visualizations')
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, f'Correlation Heatmap for {os.path.basename(stock_data)}.png')
    plt.savefig(output_file_path)

    plt.show()

def plot_machine_learning_results(stock_data):
    df = pd.read_csv(stock_data)
    data = df.drop(['Date', 'Close*', 'Adj Close**'], axis=1)
    training_x, testing_x , training_y, testing_y = train_test_split(
        data, df['Close*'], test_size=0.20,shuffle = False
    )
    print("This is the head of the training features: \n", training_x.head())
    print("This is the head of the testing features: \n",testing_x.head())
    model = LinearRegression()
    model.fit(training_x, training_y)
    predictions = model.predict(testing_x)
    rmse = sqrt(mean_squared_error(testing_y, predictions))
    mae = mean_absolute_error(testing_y, predictions)
    r_squared = r2_score(testing_y, predictions)
    RMSE = []
    MAE = []
    R_SQUARED = []
    RMSE.append(rmse)
    MAE.append(mae)
    R_SQUARED.append(r_squared)
    print(f"Test RMSE for {os.path.basename(stock_data)}: {rmse}")
    print(f"Test MAE for {os.path.basename(stock_data)}: {mae}")
    print(f"Test R-SQUARED for {os.path.basename(stock_data)}: {r_squared}")

    plt.figure(figsize=(12,7))
    plt.plot(testing_y.index, testing_y, label='Actual Prices')
    plt.plot(testing_y.index, predictions, label='Predicted Prices')
    plt.title(f'Predicted VS Actual Prices for {os.path.basename(stock_data)}')
    plt.legend()

    output_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'visualizations')
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, f'Predicted VS Actual Prices for {os.path.basename(stock_data)}.png')
    plt.savefig(output_file_path)

    plt.show()

def main():
    parser = argparse.ArgumentParser(description='output correlation heatmap for stock data and machine learning results')
    parser.add_argument('stock_data', help='file path to stock data')

    args = parser.parse_args()
    plot_correlation_heatmap(args.stock_data)
    plot_machine_learning_results(args.stock_data)


if __name__ == "__main__":
    main()