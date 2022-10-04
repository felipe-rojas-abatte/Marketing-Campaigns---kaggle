from packages_library import *
import functions_library

#####################################
####### Module for Load Data ########
#####################################

def Load_data():
    ''' Pick all excel and csv files from input data folder '''
    start_time = time.time()
    path_to_data = os.path.abspath('Input_data')

    df = load_csv_files(path_to_data+'/', sep = True)

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return df

def load_csv_files(path, sep):
    ''' Import all cvs files from path folder '''
    print('Importing csv file')
    list_csv = []
    csv_files = functions_library.ls1(path)
    for file in csv_files:
        if file == '.DS_Store':
            continue
        else:
            if sep:
                files = pd.read_csv(path+file, sep=';', engine='python', on_bad_lines='skip')
            else:
                files = pd.read_csv(path+file, sep=',', engine='python', on_bad_lines='skip')
            list_csv.append(files)
    df_csv = pd.concat(list_csv, ignore_index=True)
   
    return df_csv

##########################################
####### Module for cleansing Data ########
##########################################

def Clean_raw_data(df_init):
    ''' Clean raw csv file  '''
    start_time = time.time()
    df = df_init.copy()

    # initial number of rows
    n_df_init = len(df)
    
    # change value of pdays from 999 to -1 for plotting proposes
    df.loc[(df.pdays==999),'pdays'] = -1
    
    # checking missing values
    total_n_missing_values = df.isnull().sum().sum()
    if total_n_missing_values == 0:
        print('No missing values on dataset')
    else:
        n_missing_values = df.isnull().sum()
        for i, col in enumerate(n_missing_values.index):
            if n_missing_values[i] != 0:
                print('{} missing values on column: {}'.format(n_missing_values[i], col))
              
    # checking duplicated values
    cut_dup = df.duplicated()
    df_dup = df[cut_dup]
    df_nodup = df[~cut_dup]
    if len(df_dup) != 0:
        print('There are {} duplicated rows'.format(len(df_dup)))
        df_clean = df_nodup
        if len(df_clean) >= len(df):
              print('Warning. No duplicate values were removed')
    else: 
        print("There aren't duplicated rows")
        df_clean = df_nodup
        if len(df_clean) != len(df):
              print('Warning. Duplicate values were removed')

    n_df_end = len(df_clean)
    print('\nNº rows \nafter cleaning: {}    before cleaning:{} \n'.format(n_df_init, n_df_end))

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return df

###########################################
####### Module for processing Data ########
###########################################

def Process_search_data(df_init):
    start_time = time.time()
    df = df_init.copy()

    # Agrupamos por producto, numero de tienda, y correlation id
    # Calculamos maxima pagina de busqueda, Nº productos aparecidos en busqueda
    #first_process = df.groupby(['exact_search','request_store_number','correlation_id']).aggregate({'request_page_number':'max','response_total':'mean'}).rename(columns={'request_page_number':'max_request_page_number'})
    #first_process = first_process.reset_index()

    # Agrupamos por producto, numero de tienda
    # Calculamos promedio, percentil (10,25,50,75,90) de maxima pagina de busqueda por producto, promedio de Nº productos aparecidos en busqueda, Nº de clientes que buscaron producto
    #second_process = df.groupby(['exact_search','request_store_number']).aggregate({'request_page_number':['mean', libreria.q10, libreria.q25, libreria.q50, libreria.q75, libreria.q90],'response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    #second_process = df.groupby(['scl_created_date']).aggregate({'request_page_number':['mean', libreria.q10, libreria.q25, libreria.q50, libreria.q75, libreria.q90],'response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    second_process = df.groupby(['exact_search','request_store_number']).aggregate({'request_page_number':'mean','response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    second_process = second_process.reset_index()

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return second_process

def Process_search_per_store(df_init):
    start_time = time.time()
    df = df_init.copy()

    # Agrupamos por producto, numero de tienda, y correlation id
    # Calculamos maxima pagina de busqueda, Nº productos aparecidos en busqueda
    first_process = df.groupby(['exact_search','request_store_number','correlation_id']).aggregate({'request_page_number':'max','response_total':'mean'}).rename(columns={'request_page_number':'max_request_page_number'})
    first_process = first_process.reset_index()

    # Agrupamos por producto, numero de tienda
    # Calculamos promedio, percentil (10,25,50,75,90) de maxima pagina de busqueda por producto, promedio de Nº productos aparecidos en busqueda, Nº de clientes que buscaron producto
    second_process = first_process.groupby(['exact_search','request_store_number']).aggregate({'max_request_page_number':['mean', libreria.q10, libreria.q25, libreria.q50, libreria.q75, libreria.q90],'response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    second_process = second_process.reset_index()

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return second_process

def Process_search_per_date(df_init):
    start_time = time.time()
    df = df_init.copy()

    # Agrupamos por producto, numero de tienda, y correlation id
    # Calculamos maxima pagina de busqueda, Nº productos aparecidos en busqueda
    first_process = df.groupby(['scl_created_date','exact_search','correlation_id']).aggregate({'request_page_number':'max','response_total':'mean'}).rename(columns={'request_page_number':'max_request_page_number'})
    first_process = first_process.reset_index()

    # Agrupamos por producto, numero de tienda
    # Calculamos promedio, percentil (10,25,50,75,90) de maxima pagina de busqueda por producto, promedio de Nº productos aparecidos en busqueda, Nº de clientes que buscaron producto
    second_process = first_process.groupby(['scl_created_date','exact_search']).aggregate({'max_request_page_number':['mean', libreria.q10, libreria.q25, libreria.q50, libreria.q75, libreria.q90],'response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    second_process = second_process.reset_index()

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return second_process

def Process_search_per_date_total(df_init):
    start_time = time.time()
    df = df_init.copy()

    # Agrupamos por producto, numero de tienda, y correlation id
    # Calculamos maxima pagina de busqueda, Nº productos aparecidos en busqueda
    first_process = df.groupby(['scl_created_date','correlation_id']).aggregate({'request_page_number':'max','response_total':'mean'}).rename(columns={'request_page_number':'max_request_page_number'})
    first_process = first_process.reset_index()

    # Agrupamos por producto, numero de tienda
    # Calculamos promedio, percentil (10,25,50,75,90) de maxima pagina de busqueda por producto, promedio de Nº productos aparecidos en busqueda, Nº de clientes que buscaron producto
    second_process = first_process.groupby(['scl_created_date']).aggregate({'max_request_page_number':['mean', libreria.q10, libreria.q25, libreria.q50, libreria.q75, libreria.q90],'response_total':'mean','correlation_id':'count'}).rename(columns={'response_total':'promedio_productos_encontrados','correlation_id':'cant_busquedas_por_local'})
    second_process = second_process.reset_index()

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return second_process
