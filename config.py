from pathlib import Path
from omegaconf import OmegaConf

PROJECT_ROOT = Path(__file__).resolve().parent.parent #ai

conf = {
    "models": ['logreg', 'knn', 'simpletree', 'randforest', 'xgboost', 'lightgbm', 'catboost', 'nn', 'all'],
    
    "path": {
        "raw_data": str(PROJECT_ROOT / "raw_dataset" / "train.csv"), #ai
        "preprocessed": str(PROJECT_ROOT / "preprocessed_data" / "preprocessed_data.csv"), #ai
        "prepcocessed_onehot": str(PROJECT_ROOT / "preprocessed_data" / "one_hoted_data.csv"), #ai
        "result": str(PROJECT_ROOT / "results" / "results.csv")
    },
    "columns": {
        "categorial": ["MSSubClass", "MSZoning", "Street", "Alley", "LandContour", "LotConfig", "Neighborhood", "Condition1", "Condition2", "BldgType", "HouseStyle", "RoofStyle", "RoofMatl", "Exterior1st", "Exterior2nd", "MasVnrType", "Foundation", "Heating", "CentralAir", "Electrical", "GarageType", "Fence", "MiscFeature", "SaleType", "SaleCondition"],
        "numerical": ["LotFrontage", "LotArea", "OverallQual", "OverallCond", "YearBuilt", "YearRemodAdd", "MasVnrArea", "BsmtFinSF1", "BsmtFinSF2", "BsmtUnfSF", "TotalBsmtSF", "1stFlrSF", "2ndFlrSF", "LowQualFinSF", "GrLivArea", "BsmtFullBath", "BsmtHalfBath", "FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr", "TotRmsAbvGrd", "Fireplaces", "GarageYrBlt", "GarageCars", "GarageArea", "WoodDeckSF", "OpenPorchSF", "EnclosedPorch", "3SsnPorch", "ScreenPorch", "PoolArea", "MiscVal", "MoSold", "YrSold", "LotShape", "LandSlope", "Utilities", "ExterQual", "ExterCond", "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2", "HeatingQC", "KitchenQual", "Functional", "FireplaceQu", "GarageFinish", "GarageQual", "GarageCond", "PavedDrive", "PoolQC"]
    },
    "params": {
        "logreg": {
                # Используем Ridge вместо LogisticRegression
                "alpha": 20.0,
                "fit_intercept": True,
                "solver": "auto"
        },

        "knn": {
                "n_neighbors": 8,
                "weights": "distance",
                "algorithm": "auto",
                "leaf_size": 30,
                "p": 2,
                "metric": "minkowski",
                "n_jobs": -1
        },

        "simpletree": {
                "criterion": "squared_error",
                "max_depth": 8,
                "min_samples_split": 10,
                "min_samples_leaf": 5,
                "max_features": None,
                "random_state": 13
        },

        "randforest": {
                "n_estimators": 500,
                "criterion": "squared_error",
                "max_depth": None,
                "min_samples_split": 4,
                "min_samples_leaf": 2,
                "max_features": 0.8,
                "bootstrap": True,
                "random_state": 13,
                "n_jobs": -1
        },

        "xgboost": {
                "n_estimators": 1200,
                "learning_rate": 0.025,
                "max_depth": 3,
                "min_child_weight": 3,
                "subsample": 0.8,
                "colsample_bytree": 0.8,
                "gamma": 0,
                "reg_alpha": 0.05,
                "reg_lambda": 2.0,
                "objective": "reg:squarederror",
                "eval_metric": "rmse",
                "tree_method": "hist",
                "random_state": 13,
                "n_jobs": 1
        },

        "lightgbm": {
                "n_estimators": 1000,
                "learning_rate": 0.025,
                "num_leaves": 15,
                "max_depth": 5,
                "min_child_samples": 20,
                "subsample": 0.8,
                "subsample_freq": 1,
                "colsample_bytree": 0.8,
                "reg_alpha": 0.05,
                "reg_lambda": 1.0,
                "random_state": 13,
                "n_jobs": 1,
                "verbosity": -1
        },

        "catboost": {
                "iterations": 1200,
                "learning_rate": 0.03,
                "depth": 5,
                "l2_leaf_reg": 5,
                "random_strength": 0.5,
                "bagging_temperature": 1,
                "bootstrap_type": "Bayesian",
                "loss_function": "RMSE",
                "eval_metric": "RMSE",
                "random_seed": 13,
                "thread_count": 1,
                "verbose": False
        },

        "nn": {
                "epochs": 500,
                "layers_size": (128, 64, 32),
                "dropout": 0.25,
                "batch_size": 32,
                "patience": 25,
                "learning_rate": 0.001,
                "weight_decay": 0.0001
        }
	}
}

config = OmegaConf.create(conf)