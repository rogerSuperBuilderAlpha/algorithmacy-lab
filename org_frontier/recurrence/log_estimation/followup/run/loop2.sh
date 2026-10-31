#!/bin/bash
for i in 1 2 3 4; do ./fetch2.sh; echo "pass $i done: $(ls ev2/*.done|wc -l)"; [ $(ls ev2/*.done|wc -l) -ge 2160 ] && break; done
