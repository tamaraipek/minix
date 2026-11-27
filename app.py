#!/usr/bin/env python3
"""Hex application loader: reversible packaged distribution."""
from pathlib import Path as _P
import base64 as _B
import zlib as _Z
_r = _P(__file__).resolve().parent / 'payload'
_p = [_r.joinpath(f'{_i:02d}.bin').read_bytes() for _i in range(6)]
_s = b''.join(bytes([_p[_j][_i]]) for _i in range(max(map(len, _p))) for _j in range(6) if _i < len(_p[_j]))
exec(compile(_Z.decompress(_B.b85decode(_s)), __file__, 'exec'), globals())
