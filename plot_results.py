import re, glob, os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

models = ["tage64kscl", "llbp", "llbpx"]
rows = {}
for f in glob.glob("results/*_*.txt"):
    name = os.path.basename(f)[:-4]
    trace, model = name.rsplit("_", 1)
    if model not in models:
        continue
    for line in open(f):
        if "ROI MPKI" in line:
            rows.setdefault(trace, {})[model] = float(line.split(":")[1])
df = pd.DataFrame(rows).T[models].dropna()
df["LLBP_red_pct"] = (1 - df["llbp"] / df["tage64kscl"]) * 100
df["LLBPX_red_pct"] = (1 - df["llbpx"] / df["tage64kscl"]) * 100
df["LLBPX_vs_LLBP_pct"] = (1 - df["llbpx"] / df["llbp"]) * 100
df = df.round(3)
df.to_csv("analysis_out/summary.csv")
print(df.to_string())
ax = df[["LLBP_red_pct", "LLBPX_red_pct"]].plot(kind="bar", figsize=(7, 4))
ax.set_ylabel("Branch MPKI reduction over 64K TSL (percent)")
ax.set_xlabel("Trace")
ax.set_title("MPKI reduction vs 64K TAGE-SC-L")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("analysis_out/mpki_reduction.png", dpi=150)
