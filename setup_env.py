import subprocess
import sys
import venv
from pathlib import Path

ENV_DIR = Path("3000-env")

# Create venv
venv.create(ENV_DIR, with_pip=True)

if sys.platform == "win32":
    python = ENV_DIR / "Scripts" / "python.exe"
else:
    python = ENV_DIR / "bin" / "python"

packages = [
    "numpy==2.4.6",
    "pandas==2.3.3",
    "scikit-learn==1.8.0",
    "matplotlib==3.11.2",
    "seaborn==0.13.2",
    "shap==0.52.0",
    "ipykernel",
]

subprocess.check_call([python, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([python, "-m", "pip", "install", *packages])

subprocess.check_call([
    python, "-c",
    "import numpy, sklearn, shap; print('Setup complete')"
])
