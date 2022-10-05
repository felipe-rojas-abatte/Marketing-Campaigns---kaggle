from packages_library import *

def Join_words(text):
    text = ' '.join(text)
    return text

def ls1(path):
    """ lista los archivos de un directorio """
    return [obj for obj in listdir(path) if isfile(path + obj)]

def fechas(df, column_to_look):
    '''Agrupa y cuenta los datos en diferentes periodos y los agrega al dataframe original'''
    column_to_look = str(column_to_look)
    df['Datetime'] = pd.to_datetime(df[column_to_look],format='%Y-%m-%d').dt.date
    df['Dia'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.day.astype('int')
    df['Semana'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.isocalendar().week
    df['Mes'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.month.astype('int')
    df['Ano'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.year.astype('int')
    df['Dia-Mes'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.strftime('%d-%m')
    df['Semana-Ano'] = df['Semana'].astype(str)+'-'+df['Ano'].astype(str)
    df['Dia_semana'] = pd.to_datetime(df[column_to_look], dayfirst=True).dt.dayofweek.astype('int')
    return df

def Classification_report(model, y_predition, y_test):
    print('Confusion Matrix: \n')
    print(confusion_matrix(y_test, y_predition))
    print('\nClassification Report:')
    print(classification_report(y_test, y_predition))
    accuracy = 100*accuracy_score(y_test, y_predition)
    errors = abs(y_predition - y_test)
    print('Model Performance:')
    print('Accuracy: {:.2f}%'.format(accuracy))
    print('Average Error: {:0.2f} degrees.'.format(np.mean(errors)))
    return