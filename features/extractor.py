import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from features.synthesis_parser import parse_report

def extract_features(rtl_dir, report_dir, output_file):
    """Extracts features from RTL and reports."""
    data = []
    for filename in os.listdir(report_dir):
        if filename.endswith('.rpt'):
            module_name = filename.replace('.rpt', '')
            report_path = os.path.join(report_dir, filename)
            depth = parse_report(report_path)
            if depth is not None:
                data.append({'module': module_name, 'depth': depth})

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")

if __name__ == "__main__":
    rtl_dir = 'data/rtl'
    report_dir = 'data/reports'
    output_file = 'data/dataset.csv'
    extract_features(rtl_dir, report_dir, output_file)