import pickle
import sys

def predict_depth(model_path, fan_in):
    """Predicts combinational depth."""
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict([[fan_in]])
    print(f"Predicted Depth: {prediction[0]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inference.py <fan_in>")
    else:
        fan_in = int(sys.argv[1])
        model_path = r'C:\Users\Khush\Desktop\project\models\model.pkl'
        predict_depth(model_path, fan_in)