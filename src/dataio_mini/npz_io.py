from __future__ import annotations

from pathlib import Path
import numpy as np


def save_npz(path: str | Path, **arrays: np.ndarray) -> None:
    """
    Sauvegarde des tableaux NumPy dans un .npz.
    Exemple: save_npz("x.npz", a=A, b=B)
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, **arrays)


def load_npz(path: str | Path) -> dict[str, np.ndarray]:
    """
    Charge un .npz et retourne un dict {name: array}.
    """
    path = Path(path)
    with np.load(path) as data:
        return {k: data[k] for k in data.files}
