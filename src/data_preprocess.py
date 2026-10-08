#файл с stateless препроцессингом — изменения которые необходимо сделать с датасетом в любом случае до fit/transfrom-а 
import pandas as pd
from config import config

import columns_specification

def create_data():

    raw_data = pd.read_csv(config.path.raw_data)
    
    #дропаем айди — оно уникально и идет по порядку, смысла нет
    raw_data.drop(columns=["Id"],
                   inplace=True)

    

    #редактируем по маппингу ординальные колонки 
    for col, mapping in columns_specification.ordinal_maps.items():
        raw_data[col] = raw_data[col].map(mapping)

    #заменяем пропуски в ординальных признаках на нули
    raw_data[columns_specification.ordinal_absence_cols] = raw_data[columns_specification.ordinal_absence_cols].fillna(0)

    #заменяем пропуски в категориальных признаках на "нет объекта", там где пропуск связан скорее всего с ответствуем описываемого объекта
    raw_data[columns_specification.nominal_absence_cols] = raw_data[columns_specification.nominal_absence_cols].fillna("No Object")
    
    #заменяем пропуски в категориальных признаках на "нет информации", там где пропуск связан скорее всего с ответствуем сведений
    raw_data[columns_specification.noinfo_cols] = raw_data[columns_specification.noinfo_cols].fillna("No Info")

    #сохраняем с категориальными признаками для катбуста
    raw_data.to_csv(config.path.preprocessed, index=False)

    #one-hot'аем наши категориальные фичи и записываем
    one_hoted_data = pd.get_dummies(raw_data, columns=config.columns.categorial, dtype=pd.Int16Dtype())
    one_hoted_data.to_csv(config.path.prepcocessed_onehot, index=False)



#служебная функция для обработки результата
def result_data(results, model):
    result = {
        "model": model,
        "mean": round(results.mean(), 3),
        "std": round(results.std(), 3),
        "fold1": round(results[0], 3),
        "fold2": round(results[1], 3),
        "fold3": round(results[2], 3),
        "fold4": round(results[3], 3),
        "fold5": round(results[4], 3)
    }

    return result