# FINDINGS — q217 robot shared control

Probe output (`results.txt`): teleoperation dyadic Φ_MIP max=0.0000 · full autonomy dyadic Φ_MIP max=0.0000 ·
shared control triadic Φ_MIP max=2.0000 (major complex H, P, R, φ=2.0000) · shared control with human feedback cut
dyadic Φ_MIP max=0.0000.

All four pre-registered predictions were confirmed. Only shared control is triadic. The three-way binding needs two
things at once: an AND gate on the robot (it moves only when human and safety controller agree) and the robot's state
feeding back to both of them. Cutting the feedback to the human drops Φ to 0 and leaves an autopilot–robot pair.
Scope: in-silico, small Boolean models only.
