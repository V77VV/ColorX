"""
Minimal OpenMM simulation template.
Replace 'input.pdb' with your actual structure file.
"""

from openmm.app import *
from openmm import *
from openmm.unit import *


# --- Configuration ---
PDB_FILE = "data/input.pdb"
FORCE_FIELD = "amber14-all.xml"
WATER_MODEL = "amber14/tip3pfb.xml"
TEMPERATURE = 300 * kelvin
STEP_SIZE = 2 * femtoseconds
SIMULATION_STEPS = 500_000  # 1 ns at 2 fs steps
OUTPUT_INTERVAL = 1_000
OUTPUT_FILE = "output/trajectory.dcd"


def run():
    print("Loading structure...")
    pdb = PDBFile(PDB_FILE)
    forcefield = ForceField(FORCE_FIELD, WATER_MODEL)

    print("Building system...")
    modeller = Modeller(pdb.topology, pdb.positions)
    modeller.addHydrogens(forcefield)
    modeller.addSolvent(forcefield, model="tip3p", padding=1.0 * nanometers)

    system = forcefield.createSystem(
        modeller.topology,
        nonbondedMethod=PME,
        nonbondedCutoff=1.0 * nanometers,
        constraints=HBonds,
    )

    integrator = LangevinMiddleIntegrator(TEMPERATURE, 1 / picosecond, STEP_SIZE)
    simulation = Simulation(modeller.topology, system, integrator)
    simulation.context.setPositions(modeller.positions)

    print("Minimizing energy...")
    simulation.minimizeEnergy()

    print("Running simulation...")
    simulation.reporters.append(DCDReporter(OUTPUT_FILE, OUTPUT_INTERVAL))
    simulation.reporters.append(
        StateDataReporter(
            "output/log.csv",
            OUTPUT_INTERVAL,
            step=True,
            potentialEnergy=True,
            temperature=True,
        )
    )
    simulation.step(SIMULATION_STEPS)
    print(f"Done. Trajectory saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    import os
    os.makedirs("output", exist_ok=True)
    run()
