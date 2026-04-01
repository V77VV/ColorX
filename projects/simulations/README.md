# Simulations

Computational science simulations — molecular dynamics, physics, and beyond.

## Contents

| Folder | What it simulates |
|--------|------------------|
| `molecular-dynamics/` | Protein / molecule simulations with OpenMM |
| `physics/` | Classical physics (pendulum, n-body, fluid) |

## Quick Start

```bash
git clone https://github.com/v77vv/simulations
cd simulations
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running a Simulation

```bash
# Molecular dynamics
cd molecular-dynamics
python simulate.py        # run simulation
python analyze.py         # compute RMSD, plot trajectory

# Physics demos
cd physics
python pendulum.py        # double pendulum chaos demo
python nbody.py           # n-body gravitational simulation
```

## Project Structure

```
simulations/
├── molecular-dynamics/
│   ├── simulate.py       # OpenMM MD run
│   ├── analyze.py        # MDAnalysis trajectory analysis
│   └── data/             # Input PDB structures go here
├── physics/
│   ├── pendulum.py       # Double pendulum simulation
│   └── nbody.py          # Gravitational n-body system
├── requirements.txt
└── README.md
```

## Tools Used

- [OpenMM](https://openmm.org) — molecular dynamics engine
- [MDAnalysis](https://mdanalysis.org) — trajectory analysis
- [NumPy](https://numpy.org) + [Matplotlib](https://matplotlib.org) — numerics & plotting

## License

MIT
