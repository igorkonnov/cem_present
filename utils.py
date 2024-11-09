from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import train_test_split



def model_list( Z1, Y):
    Ridgem =Ridge(alpha=0.001,fit_intercept = True)
    Huber = HuberRegressor(max_iter=3000)
    HistGradientBoosting = HistGradientBoostingRegressor(learning_rate=0.2, max_leaf_nodes =25, max_iter = 100,  min_samples_leaf = 10)
    Lassom = Lasso(alpha = 0.001  )

    Polinomalreg = ExtraTreesRegressor(n_estimators=200, random_state=3, max_depth=20)
    x_train, x_test, y_train, y_test = train_test_split(Z1, Y, test_size=15, random_state=42)
    Ridgem.fit(x_train, y_train)
    Huber.fit( x_train , y_train )
    HistGradientBoosting.fit(x_train, y_train)
    Lassom.fit( x_train , y_train )
    Polinomalreg.fit( x_train , y_train )

    modeldata = [Ridgem,  HistGradientBoosting, Huber, Lassom, Polinomalreg ]
    return modeldata
