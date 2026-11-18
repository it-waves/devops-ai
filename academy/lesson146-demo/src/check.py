from shop import total
cases = [(5, 3, 15), (0, 9, 0)]
bad = [(p, q, w, total(p, q)) for p, q, w in cases if total(p, q) != w]
for p, q, w, g in bad:
    print(f"[test]    FAILED: total({p}, {q}) gave {g}, wanted {w}")
if bad: raise SystemExit(1)
print(f"[test]    {len(cases)} checks passed")
