from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from config import config

#в этом файле инициализируются сразу все модели кроме катбуста чтобы передать их как аргумент в функцию в цикле

params = config.params
base_models = {
    "logreg": Ridge(**params.logreg),
    "knn": KNeighborsRegressor(**params.knn),
    "simpletree": DecisionTreeRegressor(**params.simpletree),
    "randforest": RandomForestRegressor(**params.randforest),
    "xgboost": XGBRegressor(**params.xgboost),
    "lightgbm": LGBMRegressor(**params.lightgbm),
}