from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

import numpy as np
import pandas

df = pandas.read_excel(r'C:\Users\MARK\Desktop\AI HACKATHON\datasets\Dataset.xlsx')
x = []
y = []
output = []
for i, column in df.iterrows():
    x.append([column.values[0]])
    y.append([column.values[1]])
    output.append([column.values[2]])
input = np.column_stack((x, y))
output = np.ravel(output)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(input, output)
MLPClassifier(activation='ReLU', alpha=1e-05, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False,
              epsilon=1e-08, hidden_layer_sizes=(5, 2),
              learning_rate='constant', learning_rate_init=0.001,
              max_iter=200, momentum=0.9, n_iter_no_change=10,
              nesterovs_momentum=True, power_t=0.5, random_state=1,
              shuffle=True, solver='lbfgs', tol=0.0001,
              validation_fraction=0.1, verbose=False, warm_start=False)
joblib.dump(clf, 'Train.joblib')
