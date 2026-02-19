import numpy as np
from dataio_mini.npz_io import save_npz, load_npz


def test_npz_roundtrip(tmp_path):
    a = np.arange(10, dtype=float)
    b = np.eye(3, dtype=float)
    p = tmp_path / "sample.npz"

    save_npz(p, a=a, b=b)
    out = load_npz(p)

    assert np.allclose(out["a"], a)
    assert np.allclose(out["b"], b)
