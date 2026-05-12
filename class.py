import pandas as pd

b = 'var7.csv'
class Data():
    def __init__(self, a : str):
        try:
            self._df = pd.read_csv(a, sep=',')
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {str(e)}")
        except pd.errors.EmptyDataError:
            print(f"Возникла следующая ошибка: Датафрейм пуст")
        else:
            self._df = pd.read_csv(a, sep=',')
            try:
                cols = ['Участники гражданского оборота',
                         'Тип операции',
                         'Сумма операции',
                           'Вид расчета',
                             'Место оплаты',
                               'Терминал оплаты',
                                 'Дата оплаты',
                                   'Время оплаты',
                                     'Результат операции',
                                       'Cash-back',
                                         'Сумма cash-back']
                if list(self._df.columns) != cols:
                    raise ValueError(f"Названия стобцов не совпадают. \n Ожидаемые: {cols} \n Фактические: {list(self._df.columns)}")
                cols_type = {'Участники гражданского оборота' : 'str',
                             'Тип операции' : 'str',
                             'Сумма операции' : 'float64',
                             'Вид расчета' : 'str',
                             'Место оплаты' : 'str',
                             'Терминал оплаты' : 'str',
                             'Дата оплаты' : 'str',
                             'Время оплаты' : 'str',
                             'Результат операции' : 'str',
                             'Cash-back' : 'str',
                             'Сумма cash-back' : 'float64'}
                for c, type in cols_type.items():
                    if self._df[c].dtype != type:
                        raise TypeError(f"- В столбце {c} тип данных не соответствует ожидаемому. \n Ожидается: {cols_type[c]}, Фактически - {self._df[c].dtype}")
            except ValueError as e:
                print(str(e))
            except TypeError as e:
                print(str(e))
df = Data(b)
