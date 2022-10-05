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
    print('\nNº rows \nbefore cleaning: {}    after cleaning:{} \n'.format(n_df_init, n_df_end))

    final_time = time.time() - start_time
    if (final_time < 60.0): print('time final = {:.2f} seconds'.format(final_time))
    if (final_time >= 60.0 and final_time < 3600): print('time final = {:.2f} minutes'.format(final_time/60.0))
    if (final_time >= 3600): print('time final = {:.2f}'.format(final_time/3600.0))
    return df


