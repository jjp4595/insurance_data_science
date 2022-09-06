import tempfile
from pathlib import Path

# paths
PROJECT_DIR: Path = Path().resolve()
LOGGING_DIR: Path = Path(PROJECT_DIR / "logs/")
TMP_DIR: Path = Path(tempfile.gettempdir())
