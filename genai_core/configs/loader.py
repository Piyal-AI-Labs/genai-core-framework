from pathlib import Path
import yaml

from .schemas import AppConfig
from .exceptions import ConfigError

class ConfigLoader:

    @staticmethod
    def load(
        filepath: str
    ) -> AppConfig:
        
        path = Path(filepath)

        if not path.exists():
            raise ConfigError(
                f"Config file not found: {filepath}"
            )
        
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:
            config_data = yaml.safe_load(f)

        return AppConfig(
            **config_data
        )