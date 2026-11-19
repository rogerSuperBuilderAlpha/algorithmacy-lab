"""Scratch check made permanent: residual network after freezing X with the frozen node's OUTGOING edges removed (rules rewritten without X), vs q161 freeze. P|X:=0 -> Y'=Y, H'=H ; Q|X:=0 -> Y'=~(Y^H), H'=H."""
import itertools, pyphi
from pyphi import new_big_phi
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import major_complex
pyphi.config.PROGRESS_BARS=False
L=("X","Y","H")
for nm,rules in (("P|X:=0",[lambda x:0, lambda x:x[1], lambda x:x[2]]),("Q|X:=0",[lambda x:0, lambda x:1-(x[1]^x[2]), lambda x:x[2]]),("Yself only",[lambda x:x[0], lambda x:x[1], lambda x:x[2]])):
    tpm,cm=tpm_from_rules(rules),cm_from_rules(rules)
    net=pyphi.Network(tpm,cm=cm,node_labels=L)
    print(nm,"cm",cm.tolist(),"major_complex",major_complex(rules,L))
    for s in reachable_states(tpm,3):
        st=tuple((s>>i)&1 for i in range(3)); ph=[]
        for r in (1,2,3):
            for nodes in itertools.combinations(range(3),r):
                try: v="%.2f"%float(new_big_phi.sia(pyphi.Subsystem(net,st,nodes)).phi)
                except Exception as e: v=type(e).__name__[:12]
                ph.append("".join(L[i] for i in nodes)+":"+v)
        try: mc=new_big_phi.maximal_complex(net,st); mcs=(mc.node_indices, float(mc.phi)) if not isinstance(mc,new_big_phi.NullPhiStructure) else "Null"
        except Exception as e: mcs=type(e).__name__
        print("  ",st," ".join(ph)," maximal_complex:",mcs)
