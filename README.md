# LLBP-X Reproduction (ACA Research Project)

Reproduction of **"The Last-Level Branch Predictor Revisited"** (Schall, Durackova, Grot, HPCA 2026).

Group: Vishal Verma, R. Pitchumani, Nishkarsh Verma

## What this repo contains
- `run_experiments.sh`: runs 64K TAGE-SC-L, LLBP and LLBP-X on the chosen traces
- `plot_results.py`: parses the result files, computes MPKI reduction, and plots a bar chart
- `results/`: raw simulator output (`<trace>_<model>.txt`)
- `analysis_out/`: `summary.csv` and `mpki_reduction.png`
- `report/`: final report (PDF and Word)

The predictor models and the simulator are the authors' artifact (MIT licence):
https://github.com/dhschall/LLBP-X
We do not copy that code here. We use it as is, and our work is the experiments, scripts, analysis and comparison with the paper.

## How to reproduce (Ubuntu 22.04/24.04)
```bash
sudo apt install -y cmake libboost-all-dev build-essential parallel wget git python3-pandas python3-matplotlib
git clone [https://github.com/dhschall/LLBP-X.git](https://github.com/dhschall/LLBP-X.git)
cd LLBP-X
mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && cd ..
cmake --build ./build -j 8
mkdir -p traces results
# download one trace (about 2 GB), for example NodeApp
wget -O traces/nodeapp-nodeapp.champsim.trace.gz "[https://zenodo.org/records/13133243/files/nodeapp-nodeapp.champsim.trace.gz?download=1](https://zenodo.org/records/13133243/files/nodeapp-nodeapp.champsim.trace.gz?download=1)"
```
Copy `run_experiments.sh` and `plot_results.py` from this repo into the `LLBP-X` folder, then:
```bash
bash run_experiments.sh
python3 plot_results.py
```

## Setup used
- Simulator: CBP-based trace simulator from the authors (branch predictor only, no pipeline)
- Models: `tage64kscl` (baseline), `llbp`, `llbpx`
- Warm-up 100M and measurement 200M instructions per run (same as the paper)
- Metric: ROI branch MPKI and percent reduction over 64K TSL
- Machine: Ubuntu VirtualBox VM, 13th-gen Intel laptop, 16 GB RAM

## Results (so far)
| Trace | 64K TSL | LLBP | LLBP-X | LLBP-X reduction over TSL |
|---|---|---|---|---|
| NodeApp | 4.4250 | 3.2265 | 3.1652 | 28.5% |

More traces will be added in `analysis_out/summary.csv`.

## Not reproduced
The gem5 speedup, energy and bandwidth studies of the paper are not reproduced.
