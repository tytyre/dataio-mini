from __future__ import annotations

from pathlib import Path
import numpy as np
import h5py


def save_hdf5(path: str | Path, group: str = "arrays", **arrays: np.ndarray) -> None:
    """
    Sauvegarde des tableaux dans un fichier HDF5 sous /<group>/<name>.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with h5py.File(path, "w") as f:
        g = f.require_group(group)
        for name, arr in arrays.items():
            g.create_dataset(name, data=np.asarray(arr))


def load_hdf5(path: str | Path, group: str = "arrays") -> dict[str, np.ndarray]:
    """
    Charge /<group> et retourne {name: array}.
    """
    path = Path(path)
    out: dict[str, np.ndarray] = {}
    with h5py.File(path, "r") as f:
        g = f[group]
        for name in g.keys():
            out[name] = np.array(g[name])
    return out
