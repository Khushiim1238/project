# RTL Combinational Depth Prediction

This project predicts the combinational logic depth of signals in RTL modules to identify potential timing violations early in the design process.


## Overview

Timing analysis is a crucial step in complex IP/SoC design. However, timing analysis reports are generated after synthesis is complete, which is time-consuming. This project creates an AI solution to predict combinational logic depth of signals directly from behavioral RTL code, greatly speeding up the process.

The solution uses a gradient boosting approach (with XGBoost, LightGBM, or Gradient Boosting Regressor) to predict logic depth based on features extracted from RTL code.

## Setup

1.  Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Place RTL files in `data/rtl/` and corresponding synthesis reports in `data/reports/`.
2.  Run feature extraction: `python features/extractor.py`.
3.  Train the model: `python models/train.py`.
4.  Evaluate the model: `python eval/evaluate.py`.
5.  Predict combinational depth: `python predict.py  <fan_in>`.

## Example Data

Example RTL and report files are provided in `data/rtl/` and `data/reports/`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.