"""Recompute agreement metrics from archived predictions. Standard library only."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = ["Safe", "Harmful", "Ambiguous"]
with (ROOT/"results/nli_baseline/predictions.csv").open(encoding="utf-8-sig", newline="") as f:
    baseline = list(csv.DictReader(f))
manual = json.loads((ROOT/"results/chatgpt_manual/response.json").read_text(encoding="utf-8"))
assert len(baseline) == len(manual) == 60
assert sorted(int(r["ID"]) for r in baseline) == list(range(1,61))
assert sorted(r["ID"] for r in manual) == list(range(1,61))
by_id = {r["ID"]:r for r in manual}
out = ROOT/"results/comparison"
out.mkdir(exist_ok=True)
summary = []
for name, predictions in [
    ("NLI baseline", [r["model_label"] for r in baseline]),
    ("ChatGPT manual run (version unverified)", [by_id[int(r["ID"])]["label"] for r in baseline]),
]:
    truth = [r["human_label"] for r in baseline]
    assert all(x in LABELS for x in truth + predictions)
    cm = [[sum(a==h and b==p for a,b in zip(truth,predictions)) for p in LABELS] for h in LABELS]
    matched = sum(cm[i][i] for i in range(3))
    per_class = {}
    for i,label in enumerate(LABELS):
        support = sum(cm[i]); predicted = sum(row[i] for row in cm); tp = cm[i][i]
        per_class[label] = {"support":support, "predicted_count":predicted,
            "precision":tp/predicted if predicted else 0,
            "recall":tp/support if support else 0,
            "f1":2*tp/(support+predicted) if support+predicted else 0}
    summary.append({"method":name,"n":len(truth),"matches":matched,
        "agreement_rate":matched/len(truth),
        "macro_f1":sum(v["f1"] for v in per_class.values())/3,
        "label_order":LABELS,"confusion_matrix":cm,"per_class":per_class})
    print(f"{name}: {matched}/60 ({matched/60:.1%})")
(out/"metrics.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
assert [x["matches"] for x in summary] == [29,47], "Archived reference results changed"
