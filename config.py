# config.py
import os

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    ENABLED_FEATURES = os.getenv("ENABLED_FEATURES", "core_agent").split(",")
    MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "6"))
    
    @classmethod
    def is_feature_enabled(cls, feature: str) -> bool:
        return feature in cls.ENABLED_FEATURES