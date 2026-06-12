from bert_score import score
from ..base import BaseMetric

import warnings
from transformers import logging

warnings.filterwarnings('ignore')
logging.set_verbosity_error()

class BERTScoreMetric(BaseMetric):

    def compute(
        self,
        predictions,
        references
    ):
        
        _, _, f1 = score(predictions, references, lang='en', verbose=False)

        return float(f1.mean())