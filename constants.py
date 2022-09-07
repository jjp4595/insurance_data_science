import tempfile
from pathlib import Path
import os

# paths
PROJECT_DIR: Path = Path(os.path.dirname(os.path.abspath(__file__)))
LOGGING_DIR: Path = Path(PROJECT_DIR / "logs/")
TMP_DIR: Path = Path(tempfile.gettempdir())
