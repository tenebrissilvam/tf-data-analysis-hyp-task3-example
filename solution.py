import pandas as pd
import numpy as np
from scipy import stats

chat_id = 227118805 # Ваш chat ID, не меняйте название переменной

def solution(control: np.array, test: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t_stat, p_val = stats.ttest_ind(control, test)
    return p_val < 0.01 # Ваш ответ, True или False
