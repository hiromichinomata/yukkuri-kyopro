import subprocess
from pathlib import Path


def test_aplusb() -> None:
    root = Path(__file__).parent
    proc = subprocess.run(
        ["python3", "main.py"],
        input="3 5\n",
        text=True,
        capture_output=True,
        cwd=root,
        check=True,
    )
    assert proc.stdout.strip() == "8"
