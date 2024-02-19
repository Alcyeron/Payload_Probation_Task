
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.inspection import PartialDependenceDisplay as pdd

from sklearn.metrics import mean_squared_error, r2_score, PredictionErrorDisplay as ped, confusion_matrix, ConfusionMatrixDisplay as cmd
iris = load_iris()

X = iris.data
print(X)

y = iris.target
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
#model = LinearRegression()
model = LogisticRegression()

est1 = model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred, y_test, sep='\n')
mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)

print("R-squared score:", r2)


#err_disp = ped.from_predictions(y_test, [y_pred])
# disp_0 = pdd.from_estimator(est1, X_train, features=[0, 1, 2, 3], target=0)
# disp_1 = pdd.from_estimator(est1, X_train, features=[0, 1, 2, 3], target=1)
# disp_2 = pdd.from_estimator(est1, X_train, features=[0, 1, 2, 3], target=2)
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = cmd(cm, display_labels=model.classes_)
disp.plot()


plt.show()