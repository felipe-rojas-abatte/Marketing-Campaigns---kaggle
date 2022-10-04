from packages_library import *
import functions_library

colors = ['limegreen','royalblue','darkorange','m','b','orange','r','blueviolet','cyan','g','y','darkred','lightpink','grey','deepskyblue','k']
   

def Histogram_plot(ax, df, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats):   
    ax.set_title(title_name, size=20, color='k')
    plt.xlabel(xaxis_name, fontsize=18)
    plt.ylabel(yaxis_name, fontsize=18)
    plt.xlim(min_bin, max_bin)
    if log_axis:
        plt.yscale('log')

    max_val = df.max()
    min_val = df.min()
    nbins = int((max_val-min_val)/bin_size)  #numero de bins

    y_axis, bins, patches = plt.hist(x=df, bins=nbins, histtype='barstacked', color='royalblue', rwidth=1)
    
    max_y_val = max(y_axis)
    
    main_values = df.describe() 
    media = main_values['mean']
    Q1 = main_values['25%']
    Q2 = main_values['50%']
    Q3 = main_values['75%']
    
    if stats:
        if log_axis:
            ax.text(max_val*0.8, max_y_val*1.0, '25%: {:.2f}'.format(Q1), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.6, '50%: {:.2f}'.format(Q2), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.3, '75%: {:.2f}'.format(Q3), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.15, 'X: {:.2f}'.format(media), size=10, color='r')
        else:
            ax.text(max_val*0.8, max_y_val*1.0, '25%: {:.2f}'.format(Q1), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.9, '50%: {:.2f}'.format(Q2), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.8, '75%: {:.2f}'.format(Q3), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.7, 'X: {:.2f}'.format(media), size=10, color='r')

    ax.spines['right'].set_color('w')
    ax.spines['top'].set_color('w')

def Barh_plot(ax, df, title_name):
    ''' Horizontal bar plot '''
    categories = df.value_counts().index.tolist()
    values = df.value_counts().tolist()
    values_total = sum(values)
    values_perc = [100*i/values_total for i in values]
    
    ax.set_title(title_name, size=20, color='k')
    
    plt.barh(categories, values_perc, color ='royalblue')
    
    for i, v in enumerate(values_perc):
        ax.text(v+0.2, i, str(round(v, 1))+'%', color='k', va="center")
 
    ax.spines['right'].set_color('w')
    ax.spines['bottom'].set_color('w')
    ax.spines['left'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.tick_params(axis='x', colors='w')
    
def Barh_plot_custom_list(ax, df, title_name, list_of_bars):
    ''' Horizontal bar plot '''
    values = []
    for element in list_of_bars:
        number = df.tolist().count(element)
        values.append(number)  
    values_total = sum(values)
    values_perc = [100*i/values_total for i in values]
    list_of_bars = [str(x) for x in list_of_bars]
    ax.set_title(title_name, size=20, color='k')
    
    plt.barh(list_of_bars, values_perc, color ='royalblue')
    
    for i, v in enumerate(values_perc):
        ax.text(v+0.2, i, str(round(v, 1))+'%', color='k', va="center")
 
    ax.spines['right'].set_color('w')
    ax.spines['bottom'].set_color('w')
    ax.spines['left'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.tick_params(axis='x', colors='w')
    
def Pie_plot(ax, df, title_name, explode, colors):
    ''' Pie plot '''
    categories = df.value_counts().index.tolist()
    values = df.value_counts().tolist()
    
    ax.set_title(title_name, size=20, color='k')
    
    ax.pie(values, explode=explode, labels=categories, autopct='%1.2f%%', shadow=True, startangle=0, colors= colors, textprops={'fontsize': 12})

def Plot_bank_client_data(arg00, arg01, arg02, arg03, arg10, arg11, arg12):
    
    fig = plt.figure(figsize=(25,15))
    gs = GridSpec(nrows=2, ncols=4, width_ratios=[1, 1, 1, 1], height_ratios=[1, 1])
    gs.update(wspace = 0.3, hspace = 0.45)

    plt.title('Bank Cliente Data', fontsize=30, x=0.5, y=1.06)
    #plt.suptitle('      {} to {}'.format(fecha_init, fecha_end), fontsize=15, x=0.5, y=0.92)
   
    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])
    
    ########### Age #####################
    df00 = arg00[0]
    bin_size = arg00[1]
    min_bin = arg00[2]
    max_bin = arg00[3]
    title_name = arg00[4]
    xaxis_name = arg00[5]
    yaxis_name = arg00[6]
    log_axis = arg00[7]
    stats = arg00[8]
    
    ax00 = fig.add_subplot(gs[0,0])
    
    Histogram_plot(ax00, df00, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)

    ######### Job #########################
    ax01 = fig.add_subplot(gs[0,1])
    df01 = arg01[0]
    title_name = arg01[1]
    Barh_plot(ax01, df01, title_name)
    
    ######### Marital #########################
    ax02 = fig.add_subplot(gs[0,2])
    df02 = arg02[0]
    title_name = arg02[1]
    Barh_plot(ax02, df02, title_name)
    
    ######### Edication #######################
    ax03 = fig.add_subplot(gs[0,3])
    df03 = arg03[0]
    title_name = arg03[1]
    Barh_plot(ax03, df03, title_name)
    
    ######### Default #####################
    ax10 = fig.add_subplot(gs[1,0])
    df10 = arg10[0]
    title_name = arg10[1]
    colors = ['royalblue','darkorange','limegreen']
    
    explode = (0, 0, 0)
    Pie_plot(ax10, df10, title_name, explode, colors)
    
    ######### Housing #####################
    ax11 = fig.add_subplot(gs[1,1])
    df11 = arg11[0]
    title_name = arg11[1]
    colors = ['limegreen','royalblue','darkorange']
    
    explode = (0, 0, 0)
    Pie_plot(ax11, df11, title_name, explode, colors)
    
    ######### Top 15 Substitution Brand #####################
    ax12 = fig.add_subplot(gs[1,2])
    df12 = arg12[0]
    title_name = arg12[1]
    colors = ['royalblue','limegreen','darkorange']
    
    explode = (0, 0, 0)
    Pie_plot(ax12, df12, title_name, explode, colors)
    
    return

def Plot_last_contact_data(arg00, arg01, arg10, arg11):
    
    fig = plt.figure(figsize=(10,10))
    gs = GridSpec(nrows=2, ncols=2, width_ratios=[1, 1], height_ratios=[1, 1])
    gs.update(wspace = 0.3, hspace = 0.45)

    plt.title('Data related with last contact of the current Campaing', fontsize=30, x=0.5, y=1.08)
   
    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    ######### Contact #########################
    ax00 = fig.add_subplot(gs[0,0])
    df00 = arg00[0]
    title_name = arg00[1]
    colors = ['limegreen','royalblue']
    
    explode = (0, 0)
    Pie_plot(ax00, df00, title_name, explode, colors)
    
    ########### Month #####################
    ax01 = fig.add_subplot(gs[0,1])
    
    df01 = arg01[0]
    title_name = arg01[1]
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    
    Barh_plot_custom_list(ax01, df01, title_name, months)
    
    ######### Day of week #########################
    ax10 = fig.add_subplot(gs[1,0])
    df10 = arg10[0]
    title_name = arg10[1]
    day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri']
    
    Barh_plot_custom_list(ax10, df10, title_name, day_of_week)
    
    ########### Duration #####################
    df11 = arg11[0]
    bin_size = arg11[1]
    min_bin = arg11[2]
    max_bin = arg11[3]
    title_name = arg11[4]
    xaxis_name = arg11[5]
    yaxis_name = arg11[6]
    log_axis = arg11[7]
    stats = arg11[8]
    
    ax11 = fig.add_subplot(gs[1,1])
    
    Histogram_plot(ax11, df11, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)

    return

def Plot_other_attributes_data(arg00, arg01, arg10, arg11):
    
    fig = plt.figure(figsize=(10,10))
    gs = GridSpec(nrows=2, ncols=2, width_ratios=[1, 1], height_ratios=[1, 1])
    gs.update(wspace = 0.3, hspace = 0.45)

    plt.title('Other attribures', fontsize=30, x=0.5, y=1.12)
   
    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    ########### Duration #####################
    df00 = arg00[0]
    bin_size = arg00[1]
    min_bin = arg00[2]
    max_bin = arg00[3]
    title_name = arg00[4]
    xaxis_name = arg00[5]
    yaxis_name = arg00[6]
    log_axis = arg00[7]
    stats = arg00[8]
    
    ax00 = fig.add_subplot(gs[0,0])
    Histogram_plot(ax00, df00, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Contact #########################
    df01 = arg01[0]
    bin_size = arg01[1]
    min_bin = arg01[2]
    max_bin = arg01[3]
    title_name = arg01[4]
    xaxis_name = arg01[5]
    yaxis_name = arg01[6]
    log_axis = arg01[7]
    stats = arg01[8]
    
    ax01 = fig.add_subplot(gs[0,1])
    Histogram_plot(ax01, df01, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)

    ########### Month #####################
    df10 = arg10[0]
    bin_size = arg10[1]
    min_bin = arg10[2]
    max_bin = arg10[3]
    title_name = arg10[4]
    xaxis_name = arg10[5]
    yaxis_name = arg10[6]
    log_axis = arg10[7]
    stats = arg10[8]
    
    ax10 = fig.add_subplot(gs[1,0])
    Histogram_plot(ax10, df10, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Day of week #########################
    ax11 = fig.add_subplot(gs[1,1])

    df11 = arg11[0]
    title_name = arg11[1]
    colors = ['darkorange','royalblue','limegreen']
    
    explode = (0, 0, 0)
    Pie_plot(ax11, df11, title_name, explode, colors)
   
    return

def Plot_social_economic_data(arg00, arg01, arg02, arg10, arg11):
    
    fig = plt.figure(figsize=(15,10))
    gs = GridSpec(nrows=2, ncols=3, width_ratios=[1, 1 , 1], height_ratios=[1, 1])
    gs.update(wspace = 0.3, hspace = 0.45)

    plt.title('Social and Economic attributes', fontsize=30, x=0.5, y=1.08)
   
    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    ########### Duration #####################
    df00 = arg00[0]
    title_name = arg00[1]
    list_values = df00.unique().tolist()
    list_values = sorted(list_values)
    
    ax00 = fig.add_subplot(gs[0,0])
    Barh_plot_custom_list(ax00, df00, title_name, list_values)
    
    ######### Contact #########################  
    df01 = arg01[0]
    bin_size = arg01[1]
    min_bin = arg01[2]
    max_bin = arg01[3]
    title_name = arg01[4]
    xaxis_name = arg01[5]
    yaxis_name = arg01[6]
    log_axis = arg01[7]
    stats = arg01[8]
    
    ax01 = fig.add_subplot(gs[0,1])
    Histogram_plot(ax01, df01, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Contact #########################  
    df02 = arg02[0]
    bin_size = arg02[1]
    min_bin = arg02[2]
    max_bin = arg02[3]
    title_name = arg02[4]
    xaxis_name = arg02[5]
    yaxis_name = arg02[6]
    log_axis = arg02[7]
    stats = arg02[8]
    
    ax02 = fig.add_subplot(gs[0,2])
    Histogram_plot(ax02, df02, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
   
    ########### Month #####################
    df10 = arg10[0]
    bin_size = arg10[1]
    min_bin = arg10[2]
    max_bin = arg10[3]
    title_name = arg10[4]
    xaxis_name = arg10[5]
    yaxis_name = arg10[6]
    log_axis = arg10[7]
    stats = arg10[8]
    
    ax10 = fig.add_subplot(gs[1,0])
    Histogram_plot(ax10, df10, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Day of week #########################
    df11 = arg11[0]
    title_name = arg11[1]
    list_values = df11.unique().tolist()
    list_values = sorted(list_values)
    
    ax11 = fig.add_subplot(gs[1,1])
    Barh_plot_custom_list(ax11, df11, title_name, list_values)
   
    return



