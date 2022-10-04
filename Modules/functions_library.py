from packages_library import *

## Definimos funciones para estandarizar texto
def pre_process(text):
    '''function that normalize the text'''
    text = str(text)                             # Converting texto into string
    text = text.lower()                          # Converting text to Lowercase
    trantab = str.maketrans('áéíóú','aeiou')     # Create translation from word with tilde to word without tilde
    text = text.translate(trantab)               # Remove tilde from words
    text = re.sub(r'\s+', ' ', text, flags=re.I) # Substituting multiple spaces with single space
    return text

def pre_process_symbols(text):
    '''function that normalize the text'''
    text = str(text)                             # Converting texto into string
    text = text.lower()                          # Converting text to Lowercase               
    trantab = str.maketrans('áéíóú','aeiou')     # Create translation from word with tilde to word without tilde
    text = text.translate(trantab)               # Remove tilde from words
    text = re.sub(r'\W', ' ', text)              # Remove all the special characters
    text = re.sub(r'\s+', ' ', text, flags=re.I) # Substituting multiple spaces with single space
    return text

def stopwords(text):
    '''function that erase useless words'''
    text = str(text)                             # Converting texto into string
    tokens = word_tokenize(text)                 # Create a list with the words of the text
    filtered_sentence = [word for word in tokens if not word in stop_words] # Erase useless words
    text = [word for word in filtered_sentence]
    text = ' '.join(text)
    return text

def Lemmatization(text):
    ''' function that relates a word to its canonical form. we also eliminate pronouns'''
    text = nlp(text)
    lemmas = [word.lemma_ for word in text if word.pos_ != 'PRON']
    text = [word for word in lemmas]
    text = ' '.join(text)
    return text

def Tokenization(text):
    text = str(text)
    tokens = word_tokenize(text)
    text = [word for word in tokens]
    return text

def root_word(text):
    ''' function that takes only the latin root of a word'''
    tokens = word_tokenize(text)
    stems = [spanishstemmer.stem(token) for token in tokens]
    text = [word for word in stems]
    #text = ' '.join(text)
    return text

def count_words(text):
    ''' function that count the number of words of a row'''
    text = str(text)
    text = re.sub(r'\W', ' ', text)              # Remove all the special characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)  # remove all single characters
    tokens = word_tokenize(text)
    return len(tokens)

def count_letters(text):
    ''' function that count the number of letters of a row'''
    text = str(text)
    return len(text)

def is_english_word(text):
    #tokens = word_tokenize(text)
    #text = [word for word in tokens]
    english_text = [word in words.words() for word in text]
    return  english_text

def Join_words(text):
    text = ' '.join(text)
    return text

def ls1(path):
    """ lista los archivos de un directorio """
    return [obj for obj in listdir(path) if isfile(path + obj)]

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def Convert_list_to_DF(df):
    df_new = pd.DataFrame(columns=['1er T. mas buscado','2do T. mas buscado','3er T. mas buscado','freq 1','freq 2','freq 3'])
    df['keyword'].tolist()
    df['Total'].tolist()
    lista_total = df['keyword'].tolist() + df['Total'].tolist()
    df_new.loc[0] = lista_total
    df_new = df_new[['1er T. mas buscado','freq 1','2do T. mas buscado','freq 2','3er T. mas buscado','freq 3']]
    return df_new

def Search_by_keywords(df, word1, word2=None, word3=None, word4=None):
    ''' Funcion que Tokeniza un dataframe y luego hace una busqueda por palabras (acepta hasta 4 palabras) '''
    df['Token'] = df.apply(lambda x: find_intent(x['keyword tokenizado'], word1, word2, word3, word4), axis=1)
    cut = (df['Token']=='found')
    df_words = df[cut][['keyword','Total']].head(3)
    if df_words.empty:
        df_final = pd.DataFrame(columns=['1er T. mas buscado','2do T. mas buscado','3er T. mas buscado','freq 1','freq 2','freq 3'])
    else:
        df_final = Convert_list_to_DF(df_words)
    return df_final

def Search_by_list_of_synonyms(df, words):
    df_selected_words = pd.DataFrame()
    for word in words:
        df['Token'] = df.apply(lambda x: find_intent(x['keyword tokenizado'], word), axis=1)
        cut = (df['Token']=='found')
        df_selected_word = df[cut][['keyword','Total']].head()
        df_selected_words = pd.concat([df_selected_words, df_selected_word])
    df_selected_words = df_selected_words.sort_values(by=['Total'], ascending=False)
    df_selected_words = df_selected_words.head(3)
    if df_selected_words.empty:
        df_final = pd.DataFrame(columns=['1er T. mas buscado','2do T. mas buscado','3er T. mas buscado','freq 1','freq 2','freq 3'])
    else:
        df_final = Convert_list_to_DF(df_selected_words)
    return df_final

def find_intent(tokens, word1, word2=None, word3=None, word4=None):
    if (word1!=None)&(word2==None)&(word3==None)&(word4==None):
        count1 = 0
        for token in tokens:
            if str(token) == word1:
                count1 += 1
        return 'found' if count1 > 0 else 'not found'
    if (word1!=None)&(word2!=None)&(word3==None)&(word4==None):
        count1 = 0
        count2 = 0
        for token in tokens:
            if str(token) == word1:
                count1 += 1
            if str(token) == word2:
                count2 += 1
        return 'found' if (count1 > 0)&(count2 > 0) else 'not found'
    if (word1!=None)&(word2!=None)&(word3!=None)&(word4==None):
        count1 = 0
        count2 = 0
        count3 = 0
        for token in tokens:
            if str(token) == word1:
                count1 += 1
            if str(token) == word2:
                count2 += 1
            if str(token) == word3:
                count3 += 1
        return 'found' if (count1 > 0)&(count2 > 0)&(count3 > 0) else 'not found'
    if (word1!=None)&(word2!=None)&(word3!=None)&(word4!=None):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for token in tokens:
            if str(token) == word1:
                count1 += 1
            if str(token) == word2:
                count2 += 1
            if str(token) == word3:
                count3 += 1
            if str(token) == word4:
                count4 += 1
        return 'found' if (count1 > 0)&(count2 > 0)&(count3 > 0)&(count4 > 0) else 'not found'

def get_ngrams(tkns, num):
    '''Generate ngrams from tokens'''
    return list(ngrams(tkns, num))

def Most_frequent_grama(tokens, n_grams):
    ''' Funcion que busca los gramas mas frecuentes, desde 1 a n palabras '''
    df = tokens.copy()
    mcdf = pd.DataFrame()

    col_name = '1_grams'
    # Get ngram tokens
    cols = [col_name]
    for i in range(2, n_grams + 1):
        ngram_col = '{}_grams'.format(i)
        cols.append(ngram_col)
        # Get ngram tokens
        print('[INFO] Getting {}-gram tokens'.format(i))
        df[ngram_col] = df[col_name].apply(get_ngrams, args=(i,))
    # Get most common n-grams

    n_most_common = 25
    for col in cols:
        # Make bag of words
        print('[INFO] Creating bag of words for {}'.format(col))
        all_tkns = itertools.chain.from_iterable(df[col])
        bow = Counter(all_tkns)

        # Show most common words
        print('[INFO] Retrieving {} most common {}'.format(n_most_common, col))
        mc_bag = bow.most_common(n_most_common)

        print('[INFO] Writing {} most common {} to dataframe'.format(n_most_common, col))
        phrases = [' '.join(g[0]) if isinstance(g[0], (list, tuple)) else g[0] for g in mc_bag]
        freqs = [g[1] for g in mc_bag]
        mcdf[col] = phrases
        mcdf['{}_count'.format(col)] = freqs

    return mcdf

def q10(x):
    return x.quantile(0.1)
def q25(x):
    return x.quantile(0.25)
def q50(x):
    return x.quantile(0.5)
def q75(x):
    return x.quantile(0.75)
def q90(x):
    return x.quantile(0.9)

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

def Statistical_testing_2_means(sample1, sample2, alternative_hyp, LOC):
    '''Realiza test te hipotesis verificando si las distribuciones son normales o no. En caso de ser normal aplica t_tes, de lo contrario aplica Mann-Whitney U test '''
    alpha = 1.0 - LOC
    check_normality1 = pg.normality(sample1, method = 'normaltest')
    check_normality2 = pg.normality(sample2, method = 'normaltest')
    
    if check_normality1['normal'][0] & check_normality2['normal'][0]:
        t, p = stats.ttest_ind(sample1, sample2, alternative=alternative_hyp)
    else: 
        t, p = stats.mannwhitneyu(sample1, sample2, alternative=alternative_hyp)
    if (p < alpha):
        return 'Reject Ho'
    else:
        return 'Failed to reject Ho'
    
def Statistical_testing_2_means_v2(sample1, sample2, alternative_hyp, LOC):
    '''Realiza test te hipotesis verificando si las distribuciones son normales o no. En caso de ser normal aplica t_tes, de lo contrario aplica Mann-Whitney U test '''
    alpha = 1.0 - LOC
    check_normality1 = pg.normality(sample1, method = 'normaltest')
    check_normality2 = pg.normality(sample2, method = 'normaltest')
    
    if check_normality1['normal'][0] & check_normality2['normal'][0]:
        t, p = stats.ttest_ind(sample1, sample2, alternative=alternative_hyp)
    else: 
        t, p = stats.mannwhitneyu(sample1, sample2, alternative=alternative_hyp)
    if (p < alpha):
        return 'Reject Ho', p
    else:
        return 'Failed to reject Ho', p
    
def Boxplot_product(sample1, sample2, product):
    mean_s1 = sample1.mean()
    mean_s2 = sample2.mean()
    n_s1 = len(sample1)
    n_s2 = len(sample2)
    var_s1 = sample1.var()
    var_s2 = sample2.var()
    fig, ax = plt.subplots(figsize = (8, 6))
    ax.grid(False)
    ax.set_frame_on(False)
    sns.kdeplot(data = df, x = dv, hue = iv, fill = False, ax = ax)
    plt.show()
    
def Performance_comparison(df_test, column_to_test, CL):
    
    df = df_test.copy()
    # Creamos rango de fecha para realizar la comparación. Una semana para cada motor
    ES_init = pd.Timestamp('2022-07-01')
    ES_end = pd.Timestamp('2022-07-07')
    A_init = pd.Timestamp('2022-07-08')
    A_end = pd.Timestamp('2022-07-14')
    cut_elastic_search = ((df['fecha'] >= ES_init)&(df['fecha'] <= ES_end))
    cut_algolia = ((df['fecha'] >= A_init)&(df['fecha'] <= A_end))
    
    # Calculo de Test de Hipotesis
    level_of_confidence = CL/100.0
    print('----------------------------------------\nTest de Hipotesis para {} \nconsiderando Nivel de confienza: {}%'.format(column_to_test, CL))
    print('Estimador: Promedio de {}'.format(column_to_test))
    print('Ho: mu_ES < mu_A    Hipotesis nula')
    print('Ha: mu_ES > mu_A    Hipotesis alternativa')   
    
    #Seleccionamos las muestras con los cortes de rango de fechas
    samp_ES = df[cut_elastic_search][column_to_test]
    samp_A = df[cut_algolia][column_to_test]
    
    test_PMA, pval = Statistical_testing_2_means_v2(samp_ES, samp_A, 'greater',  level_of_confidence) # Escribimos Hip alternativa
    mean_ES = samp_ES.mean()
    mean_A = samp_A.mean()
    
    if test_PMA == 'Reject Ho':
        diff = 100*(mean_A - mean_ES)/mean_ES
        magnitud = mean_A - mean_ES
        print('{}   p-val: {:.2e} \nmu_A - mu_ES = {:.2f} => {:.2f}%'.format(test_PMA, pval, magnitud, diff))
    else:
        diff = 100*(mean_A - mean_ES)/mean_ES
        magnitud = mean_A - mean_ES
        print('{}   p-val: {:.2e} \nmu_A - mu_ES = {:.2f} => {:.2f}%'.format(test_PMA, pval, magnitud, diff))
    return

def Performance_comparison_by_product(df_test, top_products, column_to_test, CL):
    sorted_search = df_test.groupby(['exact_search']).aggregate({'cant_busquedas_por_local':'sum'}).sort_values(by=['cant_busquedas_por_local'], ascending=False).reset_index()
    top50 = sorted_search['exact_search'][0:top_products].tolist()
    df = df_test.copy()
    # Calculo de Test de Hipotesis
    level_of_confidence = CL/100.0
    
    ES_init = pd.Timestamp('2022-07-01')
    ES_end = pd.Timestamp('2022-07-07')
    A_init = pd.Timestamp('2022-07-08')
    A_end = pd.Timestamp('2022-07-14')
    cut_elastic_search = ((df['fecha'] >= ES_init)&(df['fecha'] <= ES_end))
    cut_algolia = ((df['fecha'] >= A_init)&(df['fecha'] <= A_end))
    
    count_reject = 0
    count_fail = 0
    print('-------------------------------------------------------\n Test de Hipotesis por producto considerando {:.1f}% C.L. \n-------------------------------------------------------'.format(CL))
    for product in top50:
        cut_product = (df['exact_search'] == product)
        samp_ES = df[cut_elastic_search & cut_product][column_to_test]
        samp_A = df[cut_algolia & cut_product][column_to_test]
        test_PMA, pval = Statistical_testing_2_means_v2(samp_ES, samp_A, 'greater', level_of_confidence)
        mean_ES = samp_ES.mean()
        mean_A = samp_A.mean()
        if test_PMA == 'Reject Ho':
            count_reject = count_reject + 1
            diff = 100*(mean_A - mean_ES)/mean_ES
            magnitud = mean_A - mean_ES
            print('{}:  {}   p-val: {:.2e}  mu_A - mu_ES = {:.2f} => {:.2f}%'.format(product, test_PMA, pval, magnitud, diff))
        else:
            count_fail = count_fail + 1
            diff = 100*(mean_A - mean_ES)/mean_ES
            magnitud = mean_A - mean_ES
            print('{}:  {}   p-val: {:.2e}  mu_A - mu_ES = {:.2f} => {:.2f}%'.format(product, test_PMA, pval, magnitud, diff))
    total_count = count_reject + count_fail
    print('---------------------------')
    print('Reject Ho: {:.2f}% \nFail to reject Ho: {:.2f}%'.format(100*count_reject/total_count, 100*count_fail/total_count))
    print('---------------------------')
    
    return

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