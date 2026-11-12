"""Recompute each memory figure in the key (classes 16-30) from the course's own size table.

Columns: key figure as printed | key's formula evaluated | my formula (same table, corrected counts where the
key's counting is wrong) | aux measured by memory_measure.py (copied from out_memory.txt for side-by-side).
Binary units (KiB/MiB), because the key's figures match them (5,000 x 100 B is printed as "488 KB").
"""
K, M = 1024, 1024 * 1024
INT, NODE, FRAME = 28, 100, 150


def f(b):
    return f"{b/M:.2f} MiB" if b >= M else (f"{b/K:.1f} KiB" if b >= K else f"{b:.0f} B")


rows = [
    # problem, part, key figure, key formula value, my formula value, measured, note
    ("#700", "input", "488 KB", 5000 * NODE, 5000 * (NODE + INT), "628 KiB", "node values 1..10^7 are mostly > 256: add an int each"),
    ("#98", "aux", "2.1 KB", 14 * FRAME + 2 * 24, 14 * FRAME + 2 * 24, "384 B traced (frames untraced)", "ok"),
    ("#703", "aux", "88 KB", 56 + 9 * 10_000, 56 + 9 * 10_000, "83.7 KiB", "ok, but the scenario breaks LeetCode limits"),
    ("#347", "aux", "5.0 MB", 52 * 100_000 + 100 * 56 + 56 + 800 + 56 + 800,
     1.5 * 52 * 100_000 + 100 * 56 + 1712, "7.50 MiB", "dict resize peak (key's own 1.5x rule) omitted"),
    ("#733", "aux", "79 KB", 1250 * 64, 1250 * 64, "77.2 KiB", "ok"),
    ("#200", "aux", "3.1 MB", 45_000 * 72, 45_000 * 72, "3.17 MiB", "ok"),
    ("#1971", "aux", "20.0 MB", 100_000 * (52 + 28 + 88) + 42 * 100_000, 100_000 * (52 + 28 + 88) + 42 * 100_000, "22.44 MiB", "ok (12% low)"),
    ("#994", "aux", "1.9 KB", 760 + 10 * 64, 760 + 10 * 64, "2.2 KiB", "ok"),
    ("#207", "aux", "259 KB", 56 + 8 * 2000 + 2000 * 88 + 56 + 8 * 2000 + 760 + 28 * 2000,
     56 + 8 * 2000 + 2000 * 88 + 56 + 8 * 2000 + 760, "204.8 KiB", "drop the 28V ints: none are created and kept"),
    ("#210", "aux", "276 KB", 56 + 8 * 2000 + 88 * 2000 + 56 + 8 * 2000 + 760 + 56 + 9 * 2000 + 28 * 2000,
     56 + 8 * 2000 + 88 * 2000 + 56 + 8 * 2000 + 760 + 56 + 9 * 2000, "220.1 KiB", "drop the 28V ints"),
    ("#743", "input", "469 KB", 6000 * (64 + 8), 6000 * (56 + 3 * 8) + 56 + 8 * 6000, "521.4 KiB",
     "a 3-element list is 80 B (not 64) plus the outer list; 469 KiB = 6000 x 80 only"),
    ("#1631", "aux", "98 KB", 101 * 856 + 200 * 72, 101 * 856 + 100 * 72, "94.4 KiB", "ok"),
    ("#684", "aux", "35 KB", 56 + 8 * 1001 + 28 * 1000, 56 + 8 * 1001 + 28 * (1000 - 256), "31.6 KiB", "ints 0..256 are cached"),
    ("#208", "aux", "11.6 MB", 53_000 * 200, 58_247 * 184, "10.36 MiB", "53,000 x 200 B is 10.1 MiB, not 11.6; real node count 58,247"),
    ("#212", "aux", "11.6 MB", 53_000 * 200, 58_247 * 184, "10.37 MiB", "same as #208"),
    ("#78", "input", "416 B", 56 + 80 + 280, 56 + 80, "136 B", "nums are in [-10, 10]: cached ints"),
    ("#78", "aux", "105 KB", 1024 * 56 + 8 * 5120 + 9 * 1024, 1024 * 56 + 8 * 5120 + 9 * 1024, "105.3 KiB", "ok"),
    ("#51", "aux", "51 KB", 92 * (120 + 8 * 49) + 9 * 92 + 3 * 730 + 8 * 200, 92 * (120 + 8 * 49) + 9 * 92 + 3 * 730 + 8 * 150, "50.6 KiB", "frames: table says 150 B, key uses 200"),
    ("#135", "aux", "696 KB", 56 + 8 * 20_000 + 28 * (20_000 - 256), 56 + 8 * 50_000 + 28 * (50_000 - 256), "773.7 KiB (n=20k); 1.90 MiB (n=50k)", "LeetCode limit is n = 5x10^4"),
    ("#56", "aux", "869 KB", 56 + 8 * 10_000 + 72 * 10_000 + 9 * 10_000, 56 + 8 * 10_000 + 72 * 10_000 + 9 * 10_000, "864.6 KiB", "ok"),
    ("#218", "aux", "3.4 MB", 20_000 * 73 + 28 * 10_000 + 65 * 10_000 + 8 * 10_000 + 10_000 * (72 + 28 + 9),
     20_000 * 73 + 28 * 10_000 + 65 * 10_000 + 8 * 10_000 + 10_000 * (72 + 28 + 9), "3.38 MiB", "ok"),
    ("#322", "input", "164 B", 56 + 24 + 3 * 28, 56 + 24, "88 B", "coins 1, 2, 5 are cached ints"),
    ("#322", "aux", "316 KB", 56 + 8 * 10_001 + 28 * 0.87 * 10_000, 56 + 8 * 10_001 + 28 * 0.87 * 10_000, "351.1 KiB", "ok (int is 32 B traced)"),
    ("#300", "aux", "81 KB", 56 + 8 * 2500 + 28 * (2500 - 256), 56 + 8 * 2500 + 28 * (2500 - 256), "90.1 KiB", "ok (int is 32 B traced)"),
    ("#1143", "aux", "8.1 MB", 1001 * (56 + 8 * 1001) + 0.4e6, 1002 * (56 + 8 * 1001) + 32 * 2600, "7.79 MiB", "LCS ~ 310-320, not ~400; ints add ~0.08 MiB"),
    ("#72", "aux", "6.3 MB", 501 * (56 + 8 * 501) + 28 * 0.65 * 250_000, 502 * (56 + 8 * 501) + 32 * 154_755, "6.67 MiB", "share of new ints confirmed (64%); 32 B per traced int"),
    ("#10", "aux", "4.9 KB", 21 * (56 + 8 * 21) + 56 + 8 * 21, 21 * (56 + 8 * 21) + 56 + 8 * 21, "5.1 KiB", "ok"),
    ("#127", "aux", "507 KB", 3125 * (42 + 42 + 46 + 36), 3125 * (42 + 42 + 46 + 36), "483.3 KiB", "ok"),
    ("#295", "aux", "1.8 MB", 28 * 50_000 + 9 * 50_000 + 112, 28 * 50_000 + 9 * 50_000 + 112, "1.94 MiB", "ok (int is 32 B traced)"),
]
print(f"{'prob':<6}{'part':<6}{'key printed':>12}{'key formula':>14}{'my formula':>14}   measured                       note")
for p, part, kp, kf, mf, meas, note in rows:
    print(f"{p:<6}{part:<6}{kp:>12}{f(kf):>14}{(f(mf) if mf is not None else '-'):>14}   {meas:<30} {note}")
