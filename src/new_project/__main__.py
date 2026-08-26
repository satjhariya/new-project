import sys
from pathlib import Path

if __package__:
    from .core import get_logger
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from new_project.core import get_logger

logger = get_logger(__name__)


def main() -> None:
    print("Hello from new_project!")
    logger.debug("Main function is called")


if __name__ == "__main__":
    main()
