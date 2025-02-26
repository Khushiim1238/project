def parse_report(report_path):
    """Parses a synthesis report and extracts signal depth."""
    depth = None
    with open(report_path, 'r') as f:
        for line in f:
            if line.startswith('depth:'):
                depth = int(line.split(':')[1].strip())
                break
    return depth