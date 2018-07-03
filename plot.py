import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1//2000',periods=1000))
ts = ts.cumsum()
plt.interactive(True)
ts.plot()
plt.show(block=True)