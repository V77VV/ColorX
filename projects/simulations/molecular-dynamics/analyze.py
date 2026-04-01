"""
Analyze MD trajectory: RMSD over time.
Run after simulate.py.
"""

import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis import rms

TOPOLOGY = "data/input.pdb"
TRAJECTORY = "output/trajectory.dcd"


def main():
    print("Loading trajectory...")
    u = mda.Universe(TOPOLOGY, TRAJECTORY)
    backbone = u.select_atoms("backbone")

    print("Computing RMSD...")
    r = rms.RMSD(backbone, backbone, select="backbone")
    r.run()

    times_ns = r.results.rmsd[:, 1] / 1000
    rmsd_A = r.results.rmsd[:, 2]

    plt.figure(figsize=(9, 4))
    plt.plot(times_ns, rmsd_A, linewidth=1, color="steelblue")
    plt.xlabel("Time (ns)")
    plt.ylabel("RMSD (Å)")
    plt.title("Backbone RMSD")
    plt.tight_layout()
    plt.savefig("output/rmsd.png", dpi=150)
    plt.show()
    print("Saved: output/rmsd.png")
    print(f"Mean RMSD: {np.mean(rmsd_A):.2f} Å  |  Max: {np.max(rmsd_A):.2f} Å")


if __name__ == "__main__":
    main()
