from pathlib import Path
import json


def list_experiments(
    experiment_dir="experiments"
):
    
    path = Path(experiment_dir)

    return [
        file.stem
        for file in path.glob("*.json")
    ]

def load_metrics(
    filepath
):
    
    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:
        
        data = json.load(f)

    return data["metrics"]