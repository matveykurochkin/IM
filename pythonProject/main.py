import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

# Если нет какой либо из этих библиотек можно воспользоваться данной командой: pip install pandas numpy statsmodels scikit-learn

# 1. Загрузка данных
def load_data(file_path):
    data = pd.read_csv(file_path, delimiter=',')
    return data

# 2. Оценка параметров линейной многофакторной модели
def fit_linear_model(X, y):
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model

# 3. Отбор значимых факторов
def feature_selection(model, significance_level):
    significant_factors = model.pvalues[model.pvalues < significance_level].index
    return significant_factors

# 4. Оценка коэффициента корреляции
def correlation_analysis(data):
    correlation_matrix = data.corr()
    return correlation_matrix

# 5. Оценка адекватности модели
def model_adequacy(model, y, X):
    y_pred = model.predict(sm.add_constant(X))
    r_squared = model.rsquared
    f_statistic = model.fvalue
    p_value = model.f_pvalue
    mse = mean_squared_error(y, y_pred)
    # Другие показатели адекватности модели
    return r_squared, f_statistic, p_value, mse

# 6. Предсказание на основе модели
def predict(model, new_data):
    # Добавляем постоянный член только к признакам новых данных
    new_data_with_const = sm.add_constant(new_data)
    # Предсказываем значения
    predictions = model.predict(new_data_with_const)
    return predictions

# Пример использования функций
file_path = r'C:\Temp\data.csv'
data = pd.read_csv(file_path)
print(data.columns)

# Выбор зависимой переменной и факторов
y_col = 'Target'
X_cols = ['Feature1', 'Feature2']

y = data[y_col]
X = data[X_cols]

# 1. Оценка параметров линейной многофакторной модели
model = fit_linear_model(X, y)

# 2. Отбор значимых факторов
significance_level = 0.05
significant_factors = feature_selection(model, significance_level)

# 3. Оценка коэффициента корреляции
correlation_matrix = correlation_analysis(data[X_cols])

# 4. Оценка адекватности модели
r_squared, f_statistic, p_value, mse = model_adequacy(model, y, X)

# 5. Предсказание на основе новых данных
new_data_path = r'C:\Temp\newdata.csv'
new_data = pd.read_csv(new_data_path)
predictions = predict(model, new_data)

# Вывод результатов
print("Значимые факторы:", significant_factors)
print("Корреляционная матрица:")
print(correlation_matrix)
print("Коэффициент детерминации (R-squared):", r_squared)
print("F-статистика:", f_statistic)
print("P-значение:", p_value)
print("Среднеквадратичная ошибка (MSE):", mse)
print("Прогнозы:")
print(predictions)
