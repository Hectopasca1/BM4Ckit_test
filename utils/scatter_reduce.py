#  Copyright (c) 2025.2.25, BM4Ckit.
#  Authors: Pu Pengxin, Song Xin
#  Version: 0.7b
#  File: scatter_reduce.py
#  Environment: Python 3.12
"""
Scatter reducing the irregular tensor with given batch_indices
"""
import torch as th
from typing import Optional, Literal

def scatter_reduce(
        src: th.Tensor,
        batch_indices: th.Tensor,
        dim: int = -1,
        ops: Literal['sum', 'prod', 'mean', 'amin', 'amax'] = 'sum'
) -> th.Tensor:
    # manage batch_indices
    _batch_indices = batch_indices.clone().to(th.int64)
    if dim < 0:
        dim = src.dim() + dim
    if _batch_indices.dim() == 1:
        for _ in range(0, dim): _batch_indices.unsqueeze_(0)
    for _ in range(_batch_indices.dim(), src.dim()): _batch_indices.unsqueeze_(-1)
    _batch_indices = _batch_indices.expand(src.shape)
    # main
    src_shape = list(src.shape)
    src_shape[dim] = th.max(_batch_indices).item() + 1
    out = th.zeros(src_shape, device=src.device)
    out.scatter_reduce_(
        dim,
        _batch_indices,
        src,
        ops
    )

    return out