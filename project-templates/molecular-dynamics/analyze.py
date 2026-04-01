"""
Basic trajectory analysis with MDAnalysis.
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

    # RMSD relative to starting structure
    print("Computing RMSD...")
    backbone = u.select_atoms("backbone")
    rmsd_analysis = rms.RMSD(backbone, backbone, select="backbone")
    rmsd_analysis.run()

    times = rmsd_analysis.results.rmsd[:, 1]  # time in ps
    rmsd_values = rmsd_analysis.results.rmsd[:, 2]  # RMSD in Angstroms

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(times / 1000, rmsd_values, linewidth=1)
    plt.xlabel("Time (ns)")
    plt.ylabel("RMSD (Å)")
    plt.title("Backbone RMSD over time")
    plt.tight_layout()
    plt.savefig("output/rmsd.png", dpi=150)
    plt.show()
    print("Saved: output/rmsd.png")


if __name__ == "__main__":
    main()
