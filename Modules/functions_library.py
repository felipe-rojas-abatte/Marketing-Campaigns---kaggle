from packages_library import *

def Join_words(text):
    text = ' '.join(text)
    return text

def ls1(path):
    """ lista los archivos de un directorio """
    return [obj for obj in listdir(path) if isfile(path + obj)]

def Classification_report_full(model, y_predition, y_test):
    ''' Report of Model Performance (KPIs)'''
    matrix = confusion_matrix(y_test, y_predition)
    matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]
    
    # Build the plot
    plt.figure(figsize=(4,4))
    sns.set(font_scale=1.4)
    sns.heatmap(matrix, annot=True, annot_kws={'size':10},
            cmap=plt.cm.Greens, linewidths=0.2)

    # Add labels to the plot
    class_names = ['No', 'Yes']
    tick_marks = np.arange(len(class_names))
    tick_marks2 = tick_marks + 0.5
    plt.xticks(tick_marks + 0.5, class_names, rotation=0)
    plt.yticks(tick_marks2, class_names, rotation=0)
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix for Random Forest Model')
    
    print('\nClassification Report:')
    print(classification_report(y_test, y_predition))
    accuracy = 100*accuracy_score(y_test, y_predition)
    errors = abs(y_predition - y_test)
    print('Model Performance:')
    print('Accuracy: {:.2f}%'.format(accuracy))
    print('Average Error: {:0.2f} degrees.'.format(np.mean(errors)))
    return



