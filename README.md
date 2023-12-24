# Разработка программы построения и оценки линейной многофакторной модели

### Цель работы и постановка задачи

Цель работы заключается в построении и оценке линейной многофакторной модели (ЛМФМ) для предсказания зависимой переменной на основе входных факторов. В данном контексте предполагается использование библиотек pandas, statsmodels и scikit-learn для загрузки данных, построения модели и оценки ее эффективности.

Для установки необходимых модулей используется команда: `pip install pandas numpy statsmodels scikit-learn`

### Процедура построения и оценки ЛМФМ
Загрузка данных: Используя библиотеку pandas, данные загружаются из CSV-файла.

Выбор зависимой переменной и факторов: Определение зависимой переменной (целевой) и факторов, которые будут использованы для построения модели.

Оценка параметров ЛМФМ: С использованием библиотеки statsmodels, строится ЛМФМ и оцениваются ее параметры.

Отбор значимых факторов: Используя статистические тесты, отбираются значимые факторы.

Оценка адекватности модели: Проводятся тесты на адекватность модели, включая вычисление коэффициента детерминации, F-статистики и среднеквадратичной ошибки.

Предсказание на основе модели: С использованием обученной модели и новых данных, строятся прогнозы.

### Демонстрация работы программы

#### Входные данные:

* data.csv - CSV-файл с обучающими данными.
* newdata.csv - CSV-файл с новыми данными для предсказания.

1. Содержимое data.csv

| Target | Feature1 | Feature2 |
|--------|----------|----------|
| 25     | 8        | 10       |
| 30     | 12       | 15       |
| 22     | 6        | 8        |
| 35     | 15       | 18       |
| 28     | 10       | 12       |

2. Содержимое newdata.csv

| Feature1 | Feature2 |
|----------|----------|
| 9        | 11       |
| 13       | 17       |
| 15       | 20       |
| 12       | 15       |
| 18       | 22       |

Процесс запуска происходит в 2 этапа, сначала запускается CreateTable.py для создания таблиц, далее запускается main.py, после мы видим сообщение: 

**Корреляционная матрица:**
|         | Feature1 | Feature2 |
|---------|----------|----------|
| Feature1 | 1.000000 | 0.997565 |
| Feature2 | 0.997565 | 1.000000 |

**Коэффициент детерминации (R-squared):** 0.9991836734693877

**F-статистика:** 1224.0

**P-значение:** 0.0008163265306122449

**Среднеквадратичная ошибка (MSE):** 0.016

**Прогнозы:**
|      | Predictions |
|------|-------------|
| 0    | 26.56       |
| 1    | 30.64       |
| 2    | 32.68       |
| 3    | 30.16       |
| 4    | 38.44       |

### Выводы: 

Результаты демонстрируют очень высокий коэффициент детерминации (R-squared), близкий к 1. Это говорит о том, что модель соответствует данным, и объясняет большую часть дисперсии в зависимой переменной (Target) с использованием факторов (Feature1 и Feature2).

#### Ключевые результаты:

Значимые факторы: Из вывода видно, что для вашей модели значимыми факторами являются 'const' и 'Feature1'. Последний означает, что Feature1 является значимым предиктором в модели.

* Корреляционная матрица: Коэффициент корреляции между Feature1 и Feature2 близок к 1, что также подтверждает сильную корреляцию между этими факторами.

* Коэффициент детерминации (R-squared): Близкий к 1 (0.9992), что указывает на высокую долю объясненной дисперсии.

* F-статистика и P-значение: F-статистика высока, а P-значение низко, что говорит о статистической значимости модели.

* Среднеквадратичная ошибка (MSE): Низкое значение MSE указывает на то, что модель хорошо предсказывает зависимую переменную.

* Прогнозы: Прогнозы для новых данных также могут быть рассмотрены как хорошие, так как они базируются на хорошо настроенной модели.