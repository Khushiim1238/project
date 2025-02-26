import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import pickle

def train_model(dataset_path, model_path):
    """Trains an XGBoost model."""
    df = pd.read_csv(dataset_path)
    X = pd.DataFrame(df.index)
    y = df['depth']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor()
    model.fit(X_train, y_train)

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    dataset_path = 'data/dataset.csv'
    model_path = 'models/model.pkl'
    train_model(dataset_path, model_path)