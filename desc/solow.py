import numpy as np
import matplotlib.pyplot as plt
from itertools  import product

def function_solow(axe, a_s, s_s, b_s, time_series=50):
    k = np.empty(50)

    for a, s, b in product(a_s, s_s, b_s):
        k[0]=1
        for t in range(time_series-1):
            k[t+1] = s * k[t]**a + (1 - b) * k[t]
        
        axe.plot(k, 'o-', label=rf"$\alpha = {a},\; s = {s},\; \delta={b}$")

    axe.set_ylim(0, 18)
    axe.set_xlabel('time')
    axe.set_ylabel('capital')
    axe.grid(lw=0.2)
    axe.legend(loc='upper left', frameon=True)

fig, axes = plt.subplots(3, 1, figsize=(8, 16))

ties = [
    ([0.25, 0.33, 0.45], [0.4], [0.1]),
    ([0.33], [0.3, 0.4, 0.5], [0.1]),
    ([0.33], [0.4], [0.05, 0.1, 0.15])
]

for i, (a_s, s_s, b_s) in enumerate(ties):
    function_solow(axes[i], a_s, s_s, b_s)

plt.show()