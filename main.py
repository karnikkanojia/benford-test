# Import library
import numpy as np
import math
from benfordslaw import benfordslaw

# Create uniform random data which does definitely not follow Benfords distribution.
X = np.random.randint(0, high=math.inf, size=1000)

# Initialize with alpha and method.
bl = benfordslaw(alpha=0.05, method='chi2')

print(X)
# array([13, 12,  2,  4, 99, 33, 71, 69, 65, 55,  6, 30, 30, 99, 43, 36, 12,....]

# Fit
results = bl.fit(X)

# As expected, a significant P-value is detected for the inupt data X
# [benfordslaw] >Analyzing digit position: [1]
# [benfordslaw] >[chi2] Anomaly detected! P=3.46161e-73, Tstat=361.323

# Plot
bl.plot(title='Random data')