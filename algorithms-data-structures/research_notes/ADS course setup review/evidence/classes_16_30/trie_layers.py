"""Distinct prefixes per depth for 10,000 random 8-letter words (the #208/#212 memory scenario), 5 seeds."""
import random, string
for seed in range(5):
    random.seed(seed)
    W = ["".join(random.choice(string.ascii_lowercase) for _ in range(8)) for _ in range(10_000)]
    layers = [len({w[:d] for w in W}) for d in range(1, 9)]
    print(f"seed {seed}: per-depth {layers}, total nodes incl. root {sum(layers) + 1}")
print("key's formula sum_d min(26^d, 10000) =", sum(min(26 ** d, 10_000) for d in range(1, 9)))
