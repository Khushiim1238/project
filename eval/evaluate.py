import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb

def evaluate_model(dataset_path, model_path):
    """Evaluates the trained model."""
    df = pd.read_csv(dataset_path)
    X = pd.DataFrame(df.index)
    y = df['depth']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    dataset_path = 'data/dataset.csv'
    model_path = 'models/model.pkl'
    evaluate_model(dataset_path, model_path)