import pandas as pd

def create_report(results):

    return pd.DataFrame(
        results.items(),
        columns=["Metric", "Score"]
    )