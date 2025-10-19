from pathlib import Path

class VaspReader:
    def __init__(self, system_path: Path):
        self.poscar_path = Path.joinpath(system_path, 'POSCAR')
        self.outcar_path = Path.joinpath(system_path, 'OUTCAR')
        self.potcar_path = Path.joinpath(system_path, 'POTCAR')
        self.incar_path = Path.joinpath(system_path, 'INCAR')

    def read_poscar(self):
        with open(self.poscar_path) as f:
            lines = f.readlines()
        # Разбор POSCAR (упрощённый пример)
        scale = float(lines[1].strip())
        lattice = [list(map(float, l.split())) for l in lines[2:5]]
        # ...
        return lattice, []  # структура, атомы и т.п.
