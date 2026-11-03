"""同じディレクトリの Python 解答と Go 解答が、同じ入力に同じ出力を返すか。

入力は solutions/python/NN/<name>/input.txt（なければ空入力）。
Go はまとめてビルドしてから実行する（go が入っていなければスキップ）。
"""

import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import pytest
from conftest import GO, PY, ROOT

PAIRS = sorted(
    str(p.parent.relative_to(PY))
    for p in PY.glob("*/*/main.py")
    if (GO / p.parent.relative_to(PY) / "main.go").exists()
)


@pytest.fixture(scope="session")
def go_bins(tmp_path_factory):
    if shutil.which("go") is None:
        pytest.skip("go が見つからない")
    out = tmp_path_factory.mktemp("gobin")
    bins = {rel: out / rel.replace("/", "_") for rel in PAIRS}

    def build(rel):
        subprocess.run(["go", "build", "-o", str(bins[rel]), f"./solutions/go/{rel}"], cwd=ROOT, check=True)

    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        list(ex.map(build, PAIRS))
    return bins


@pytest.mark.parity
@pytest.mark.parametrize("rel", PAIRS)
def test_same_output(rel, go_bins):
    inp = PY / rel / "input.txt"
    data = inp.read_text() if inp.exists() else ""
    py = subprocess.run([sys.executable, str(PY / rel / "main.py")], input=data, capture_output=True, text=True, timeout=60)
    go = subprocess.run([str(go_bins[rel])], input=data, capture_output=True, text=True, timeout=60)
    assert py.returncode == 0, py.stderr
    assert go.returncode == 0, go.stderr
    assert py.stdout.split("\n") == go.stdout.split("\n")
