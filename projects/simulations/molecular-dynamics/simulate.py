"""
OpenMM molecular dynamics simulation.
Place your PDB file at data/input.pdb before running.
"""

from openmm.app import *
from openmm import *
from openmm.unit import *
import os

PDB_FILE = "data/input.pdb"
TEMPERATURE = 300 * kelvin
STEP_SIZE = 2 * femtoseconds
STEPS = 500_000       # 1 ns
REPORT_EVERY = 1_000
OUTPUT_DCD = "output/trajectory.dcd"
OUTPUT_LOG = "output/log.csv"


def run():
    print("Loading structure...")
    pdb = PDBFile(PDB_FILE)
    ff = ForceField("amber14-all.xml", "amber14/tip3pfb.xml")

    modeller = Modeller(pdb.topology, pdb.positions)
    modeller.addHydrogens(ff)
    modeller.addSolvent(ff, model="tip3p", padding=1.0 * nanometers)

    system = ff.createSystem(
        modeller.topology,
        nonbondedMethod=PME,
        nonbondedCutoff=1.0 * nanometers,
        constraints=HBonds,
    )
    integrator = LangevinMiddleIntegrator(TEMPERATURE, 1 / picosecond, STEP_SIZE)
    sim = Simulation(modeller.topology, system, integrator)
    sim.context.setPositions(modeller.positions)

    print("Minimizing energy...")
    sim.minimizeEnergy()

    sim.reporters.append(DCDReporter(OUTPUT_DCD, REPORT_EVERY))
    sim.reporters.append(StateDataReporter(
        OUTPUT_LOG, REPORT_EVERY,
        step=True, potentialEnergy=True, temperature=True,
    ))

    print(f"Running {STEPS:,} steps ({STEPS * 2 / 1e6:.1f} ns)...")
    sim.step(STEPS)
    print(f"Done. Saved to {OUTPUT_DCD}")


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    run()
