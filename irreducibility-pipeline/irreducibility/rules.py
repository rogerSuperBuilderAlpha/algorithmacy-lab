"""Parse a party's rule, written as a Boolean expression over party names, into a callable.

An encoding states each party's next state in plain logic:

    "S": "D and R"            the platform commits only when the driver and the rider are both in
    "D": "S"                  the driver acts on the platform's signal
    "C": "E and not A"        the claimant is paid when the engine approves and no adjuster flags
    "P": "(D1 or D2) and R"   any available driver will do

Allowed: party names, 0, 1, and, or, not, xor, parentheses. Anything else is rejected, so an
encoding cannot run arbitrary code.
"""

import ast
from typing import Callable, Sequence

_ALLOWED = (ast.Expression, ast.BoolOp, ast.And, ast.Or, ast.UnaryOp, ast.Not,
            ast.BinOp, ast.BitXor, ast.Name, ast.Load, ast.Constant)


def _rewrite_xor(expr: str) -> str:
    return " ^ ".join(part for part in expr.replace(" XOR ", " xor ").split(" xor "))


def compile_rule(expr: str, labels: Sequence[str]) -> Callable:
    """Compile one expression into ``f(state_tuple) -> 0/1`` with labels in rule order."""
    labels = tuple(labels)
    tree = ast.parse(_rewrite_xor(expr.strip()), mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED):
            raise ValueError(f"rule {expr!r}: {type(node).__name__} is not allowed")
        if isinstance(node, ast.Name) and node.id not in labels:
            raise ValueError(f"rule {expr!r}: unknown party {node.id!r} (parties: {labels})")
        if isinstance(node, ast.Constant) and node.value not in (0, 1, True, False):
            raise ValueError(f"rule {expr!r}: only 0 and 1 are allowed as constants")

    def ev(node, x):
        if isinstance(node, ast.Expression):
            return ev(node.body, x)
        if isinstance(node, ast.BoolOp):
            vals = [ev(v, x) for v in node.values]
            return int(all(vals)) if isinstance(node.op, ast.And) else int(any(vals))
        if isinstance(node, ast.UnaryOp):
            return 1 - ev(node.operand, x)
        if isinstance(node, ast.BinOp):
            return ev(node.left, x) ^ ev(node.right, x)
        if isinstance(node, ast.Name):
            return int(x[labels.index(node.id)])
        return int(node.value)

    def rule(x, _t=tree):
        return ev(_t, x)

    rule.expr = expr
    return rule


def compile_rules(rules: dict, labels: Sequence[str]):
    """Compile {party: expression} into a rule list in label order."""
    missing = [p for p in labels if p not in rules]
    if missing:
        raise ValueError(f"no rule for {missing}")
    return [compile_rule(rules[p], labels) for p in labels]
