from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np

from .npz_io import save_npz, load_npz


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="dataio-mini")
    sub = p.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("write-demo", help="write demo arrays to a file")
    w.add_argument("path", type=Path)
    w.add_argument("--fmt", choices=["npz", "h5"], default="npz")

    r = sub.add_parser("read", help="read a file and list keys/shapes")
    r.add_argument("path", type=Path)
    r.add_argument("--fmt", choices=["npz", "h5"], default="npz")

    args = p.parse_args(argv)

    if args.cmd == "write-demo":
        a = np.arange(10, dtype=float)
        b = np.eye(3, dtype=float)
        if args.fmt == "npz":
            save_npz(args.path, a=a, b=b)
        else:
            from .hdf5_io import save_hdf5
            save_hdf5(args.path, a=a, b=b)
        print(f"Wrote {args.path}")
        return 0

    if args.cmd == "read":
        if args.fmt == "npz":
            data = load_npz(args.path)
        else:
            from .hdf5_io import load_hdf5
            data = load_hdf5(args.path)
        for k, v in data.items():
            print(k, v.shape, v.dtype)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
