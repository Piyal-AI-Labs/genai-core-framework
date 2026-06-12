from genai_core.experiments.tracker import ExperimentTracker

tracker = ExperimentTracker(experiment_name="embedding_comparison")

tracker.log_params(
    {
        "embedding_model": "bge-small",
        "chunk_size": 512
    }
)

tracker.log_metrics(
    {
        "accuracy": 0.84,
        "faithfulness": 0.91
    }
)

tracker.log_metadatas(
    {
        "dataset": "hotpotqa",
        "research_area": "rag"
    }
)

tracker.save()