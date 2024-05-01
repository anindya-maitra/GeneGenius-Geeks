#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:29:15 2024

@author: anindya_maitra
"""

import numpy as np
import pandas as pd
from pymoo.model.problem import Problem
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.optimize import minimize
import matplotlib.pyplot as plt

class MyProblem(Problem):
    def __init__(self, dataframe):
      self.df=dataframe
      super().__init__(
            n_var=1,
            n_obj=2,
            xl=[0],
            xu=[200],
        )

    def _evaluate(self, x, out, *args, **kwargs):
        selected_rows = self.df.iloc[x.astype(int).flatten()]
        out["F"] = np.array( - selected_rows['condensed weight'])




df = pd.read_csv("output_C_pscore_gf.csv")
problem = MyProblem(df)

algorithm = NSGA2(pop_size=351)

termination = ("n_gen", 10)


result = minimize(problem=problem,
                  algorithm=algorithm,
                  termination=termination,
                  seed=1,
                  verbose=True,
                  save_history=True)
# Convert the Pareto front to a Pandas DataFrame
print(result.F)
for i in range(len(result.F)):
    value = - result.F[i].item()
    res = df[df['condensed weight'] ==  value]
print(res)

# Plot the Pareto front
plt.figure(figsize=(30, 10))
plt.scatter(x=df['index'], y=df['condensed weight'], color="blue")
plt.scatter(x=res['index'], y=res['condensed weight'], color="red")
plt.xlabel('Drug Vector')
plt.ylabel('Condensed Weight')
plt.xticks(range(0, len(df), 5), df['drug vector'][::5], rotation=90)  # Rotate x-tick labels for better visibility
plt.title('Pareto Front')
plt.show()