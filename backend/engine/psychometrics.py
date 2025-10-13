from __future__ import annotations
from dataclasses import dataclass
import numpy as np

DEFAULT_NORMS = {
    "openness": {"mean": 0.5, "sd": 0.1},
    "conscientiousness": {"mean": 0.5, "sd": 0.1},
    "extraversion": {"mean": 0.5, "sd": 0.1},
    "agreeableness": {"mean": 0.5, "sd": 0.1},
    "neuroticism": {"mean": 0.5, "sd": 0.1},
}
REVERSE_KEYS = set(["BF3", "BF7", "BF12", "BF28", "BF44"])

@dataclass
class BigFiveResult:
    openness: float
    conscientiousness: float
    extraversion: float
    agreeableness: float
    neuroticism: float
    def as_dict(self): return self.__dict__

class BigFiveScorer:
    def __init__(self, norms: dict | None = None): self.norms = norms or DEFAULT_NORMS
    def score(self, responses: dict[str, int]) -> BigFiveResult:
        traits = {
            "openness": ["BF1","BF6","BF11","BF16","BF21","BF26","BF31","BF36","BF41","BF46","BF51","BF56"],
            "conscientiousness": ["BF2","BF7","BF12","BF17","BF22","BF27","BF32","BF37","BF42","BF47","BF52","BF57"],
            "extraversion": ["BF3","BF8","BF13","BF18","BF23","BF28","BF33","BF38","BF43","BF48","BF53","BF58"],
            "agreeableness": ["BF4","BF9","BF14","BF19","BF24","BF29","BF34","BF39","BF44","BF49","BF54","BF59"],
            "neuroticism": ["BF5","BF10","BF15","BF20","BF25","BF30","BF35","BF40","BF45","BF50","BF55","BF60"],
        }
        def transform(k,v): 
            v = 6 - v if k in REVERSE_KEYS else v
            return (v-1)/4
        scores = {}
        for t, keys in traits.items():
            vals = [transform(k, responses.get(k, 3)) for k in keys]
            raw = float(np.mean(vals))
            m = self.norms[t]["mean"]; sd = self.norms[t]["sd"] or 0.1
            z = (raw - m)/sd
            pct = float(0.5*(1+np.math.erf(z/np.sqrt(2))))
            scores[t] = max(0.0, min(1.0, pct))
        return BigFiveResult(**scores)
