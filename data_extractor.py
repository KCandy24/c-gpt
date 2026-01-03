import kagglehub
import shutil
from pathlib import Path

path = Path(kagglehub.dataset_download("adarshbiradar/c-programs"))
print("Path to dataset files:", path)

dst = Path.cwd() / path.name

shutil.copytree(path, dst, dirs_exist_ok=True)
