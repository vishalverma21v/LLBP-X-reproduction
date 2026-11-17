#!/bin/bash
# Runs 64K TAGE-SC-L, LLBP and LLBP-X on every trace found in ./traces
# Usage (from the LLBP-X folder): bash run_experiments.sh
set -e
mkdir -p results
WARMUP=100000000
SIM=200000000

for trace in traces/*.champsim.trace.gz; do
    name=$(basename "$trace" .champsim.trace.gz)
    for model in tage64kscl llbp llbpx; do
        out="results/${name}_${model}.txt"
        if [ -s "$out" ]; then
            echo "skip $out (already exists)"
            continue
        fi
        echo "running $model on $name"
        ./build/predictor --model "$model" -w $WARMUP -n $SIM "$trace" > "$out"
    done
done
echo "All runs finished. Now run: python3 plot_results.py"
