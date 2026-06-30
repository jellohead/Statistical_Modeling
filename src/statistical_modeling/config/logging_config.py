from pathlib import Path
import os
import logging
import logging.config
from statistical_modeling.config.paths import PATHS


def setup_logging(level: int | None = None) -> None:
    if level is None:
        level_name = os.getenv('LOG_LEVEL', 'INFO').upper()
        level = getattr(logging, level_name, logging.INFO)

    log_dir = PATHS.logs_dir
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "Statistical_Modeling.log"

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'standard': {
                'format': '[%(asctime)s] %(levelname)s in %(name)s: %(message)s'
            },
        },

        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': level,
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': str(log_file),
                'mode': 'a',
                'level': level,
            },
        },

        'root': {
            'handlers': ['console', 'file'],
            'level': level,
        },
    }

    logging.config.dictConfig(logging_config)
