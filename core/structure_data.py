from dataclasses import dataclass
from typing import List

import numpy as np

@dataclass
class Site:
    element: str
    position: np.ndarray
    site_num: int
    type_num: int
    type: str
    magnetic_moment: float = 0.0

@dataclass
class Lattice:
    vectors: np.ndarray  # 3x3 матрица
    volume: float
    abc: np.ndarray
    angles: np.ndarray
    # sites: List[Site]

class Structure_data:
    def __init__(self, lattice: Lattice, sites: List[Site]):
        self.lattice = lattice
        self.sites = sites

    def get_formula(self):
        from collections import Counter
        counts = Counter([atom.element for atom in self.atoms])
        return ''.join(f"{el}{n}" if n != 1 else f'{el}' for el, n in counts.items())
