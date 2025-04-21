
import pandas as pd

def validate_predictions(system_output, historical_csv):
    historical_data = pd.read_csv(historical_csv)
    predicted_price = float(system_output['price'])
    actual_price = historical_data.iloc[-1]['Close']
    accuracy = abs(predicted_price - actual_price) / actual_price
    return {"validation_passed": accuracy < 0.05, "accuracy": accuracy}

if __name__ == "__main__":
    system_output = {"price": "1500"}  # replace with real system output
    historical_csv = 'historical_INFOSYS.csv'  # provide the path to actual historical CSV file
    result = validate_predictions(system_output, historical_csv)
    print("Validation Result:", result)
