#мапинги по всему этому файлу сгенерированы ИИ

ordinal_maps = {

    # Форма участка: от наиболее неправильной к регулярной
    "LotShape": {
        "IR3": 0,
        "IR2": 1,
        "IR1": 2,
        "Reg": 3
    },

    # Уклон участка
    "LandSlope": {
        "Sev": 0,
        "Mod": 1,
        "Gtl": 2
    },

    # Доступность коммуникаций
    "Utilities": {
        "ELO": 0,
        "NoSeWa": 1,
        "NoSewr": 2,
        "AllPub": 3
    },

    # Качество внешней отделки
    "ExterQual": {
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Состояние внешней отделки
    "ExterCond": {
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Качество подвала
    "BsmtQual": {
        "None": 0,
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Состояние подвала
    "BsmtCond": {
        "None": 0,
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Экспозиция подвала
    "BsmtExposure": {
        "None": 0,
        "No": 1,
        "Mn": 2,
        "Av": 3,
        "Gd": 4
    },

    # Качество отделанной площади подвала
    "BsmtFinType1": {
        "None": 0,
        "Unf": 1,
        "LwQ": 2,
        "Rec": 3,
        "BLQ": 4,
        "ALQ": 5,
        "GLQ": 6
    },

    "BsmtFinType2": {
        "None": 0,
        "Unf": 1,
        "LwQ": 2,
        "Rec": 3,
        "BLQ": 4,
        "ALQ": 5,
        "GLQ": 6
    },

    # Качество отопления
    "HeatingQC": {
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Качество кухни
    "KitchenQual": {
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Функциональность дома
    "Functional": {
        "Sal": 0,
        "Sev": 1,
        "Maj2": 2,
        "Maj1": 3,
        "Mod": 4,
        "Min2": 5,
        "Min1": 6,
        "Typ": 7
    },

    # Качество камина
    "FireplaceQu": {
        "None": 0,
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Отделка гаража
    "GarageFinish": {
        "None": 0,
        "Unf": 1,
        "RFn": 2,
        "Fin": 3
    },

    # Качество гаража
    "GarageQual": {
        "None": 0,
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Состояние гаража
    "GarageCond": {
        "None": 0,
        "Po": 1,
        "Fa": 2,
        "TA": 3,
        "Gd": 4,
        "Ex": 5
    },

    # Подъездная дорожка
    "PavedDrive": {
        "N": 0,
        "P": 1,
        "Y": 2
    },

    # Качество бассейна
    "PoolQC": {
        "None": 0,
        "Fa": 1,
        "TA": 2,
        "Gd": 3,
        "Ex": 4
    }
}


#объекты, none в которых означает отсутсвие объекта, а не отсутствие значения

nominal_absence_cols = ["Alley", "MasVnrType", "GarageType", "Fence", "MiscFeature"]
ordinal_absence_cols = ["BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1", "BsmtFinType2", "FireplaceQu", "GarageFinish", "GarageQual", "GarageCond", "PoolQC"]

noinfo_cols = [
    "MSZoning",
    "Utilities",
    "Exterior1st",
    "Exterior2nd",
    "Electrical",
    "SaleType",
]

ordinal_cols = [
    "LotShape",
    "LandSlope",

    "ExterQual",
    "ExterCond",

    "BsmtQual",
    "BsmtCond",
    "BsmtExposure",
    "BsmtFinType1",
    "BsmtFinType2",

    "HeatingQC",

    "KitchenQual",
    "Functional",

    "FireplaceQu",

    "GarageFinish",
    "GarageQual",
    "GarageCond",

    "PavedDrive",
    "PoolQC"
]