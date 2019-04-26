import mysql.connector as connector
from modules import *
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def plot_single_value(value_name,mean,max,min,var,std):
    plt.subplot(511)
    plt.bar(range(len(mean)), mean, color='rgb', tick_label=platforms_name)
    plt.title(value_name+"_MEAN",fontsize=27)
    plt.ylabel("Mean Value")
    plt.xlabel("The Platforms")
    plt.subplot(512)
    plt.bar(range(len(min)), min, color='rgb', tick_label=platforms_name)
    plt.title(value_name+"_MIN",fontsize=27)
    plt.ylabel("MIN Value")
    plt.xlabel("The Platforms")
    plt.subplot(513)
    plt.bar(range(len(max)), max, color='rgb', tick_label=platforms_name)
    plt.title(value_name+"_MAX",fontsize=27)
    plt.ylabel("MAX Value")
    plt.xlabel("The Platforms")
    plt.subplot(514)
    plt.bar(range(len(var)), var, color='rgb', tick_label=platforms_name)
    plt.title(value_name+"_VAR",fontsize=27)
    plt.ylabel("VAR Value")
    plt.xlabel("The Platforms")
    plt.subplot(515)
    plt.bar(range(len(std)), std, color='rgb', tick_label=platforms_name)
    plt.title(value_name+"_STD",fontsize=27)
    plt.ylabel("STD Value")
    plt.xlabel("The Platforms")
    plt.savefig(value_name+".jpg")
    plt.show()


params={
    'axes.labelsize': '35',
    'xtick.labelsize':'27',
    'ytick.labelsize':'27',
    'lines.linewidth':2 ,
    'legend.fontsize': '27',
    'figure.figsize'   : '40, 50'    # set figure size
}
pylab.rcParams.update(params)
mysql = connector.connect(user='root', password='00011122q', buffered=True, host='127.0.0.1')
cursor = mysql.cursor()
cursor.execute("use gamedata")

"""
选出不同的不同平台的游戏，分析其各类评分
"""
platforms = []
cursor.execute("select platform,NA_sales,EU_sales, FP_sales,other_sales,global_sales,critic_score,critic_count,user_score,user_count from videogame")
one = cursor.fetchone()
while one is not None:
    IS_NEW = True
    platform_name = one[0]
    NA_sales = one[1]
    EU_sales = one[2]
    FP_sales = one[3]
    other_sales = one[4]
    global_sales = one[5]
    critic_score = one[6]
    critic_count = one[7]
    user_score = one[8]
    user_count = one[9]
    for platform in platforms:
        if platform_name == platform.name:
            platform.num += 1
            platform.NA_sales = np.append(platform.NA_sales, NA_sales)
            platform.EU_sales = np.append(platform.EU_sales, EU_sales)
            platform.FP_sales = np.append(platform.FP_sales, FP_sales)
            platform.other_sales = np.append(platform.other_sales, other_sales)
            platform.global_sales = np.append(platform.global_sales, global_sales)
            if critic_score != 0:
                platform.critic_score = np.append(platform.critic_score, critic_score)
            if critic_count != 0:
                platform.critic_count = np.append(platform.critic_count, critic_count)
            if user_score != 0:
                platform.user_score = np.append(platform.user_score, user_score)
            if user_count != 0:
                platform.user_count = np.append(platform.user_count, user_count)
            IS_NEW = False
            break
    if IS_NEW:
        new_platform = platform_module(name=platform_name)
        platforms.append(new_platform)
        new_platform.NA_sales = np.append(new_platform.NA_sales,NA_sales)
        new_platform.EU_sales = np.append(new_platform.EU_sales, EU_sales)
        new_platform.FP_sales = np.append(new_platform.FP_sales, FP_sales)
        new_platform.other_sales = np.append(new_platform.other_sales, other_sales)
        new_platform.global_sales = np.append(new_platform.global_sales, global_sales)
        if critic_score !=0:
            new_platform.critic_score = np.append(new_platform.critic_score, critic_score)
        if critic_count != 0:
            new_platform.critic_count = np.append(new_platform.critic_count, critic_count)
        if user_score != 0:
            new_platform.user_score = np.append(new_platform.user_score, user_score)
        if user_count != 0:
            new_platform.user_count = np.append(new_platform.user_count,user_count)
        new_platform.num = 1
    one = cursor.fetchone()
"""
计算各类评价的均值，方差，标准差，最大值，最小值
"""
for platform in platforms:
    platform.cal_mean()
    platform.cal_var_and_std()
    platform.cal_max_and_min()

"""
可视化各类统计数值
"""
platforms_name = [ platform.name for platform in platforms]

mean_NA_sales =  [platform.mean_NA_sales for platform in platforms]
max_NA_sales = [platform.max_NA_sales for platform in platforms]
var_NA_sales = [platform.var_NA_sales for platform in platforms]
std_NA_sales = [platform.std_NA_sales for platform in platforms]
min_NA_sales = [platform.min_NA_sales for platform in platforms]

mean_critic_count =  [platform.mean_critic_count for platform in platforms]
max_critic_count =  [platform.max_critic_count for platform in platforms]
min_critic_count =  [platform.min_critic_count for platform in platforms]
var_critic_count =  [platform.var_critic_count for platform in platforms]
std_critic_count =  [platform.std_critic_count for platform in platforms]

mean_critic_score =  [platform.mean_critic_score for platform in platforms]
max_critic_score =  [platform.max_critic_score for platform in platforms]
min_critic_score =  [platform.min_critic_score for platform in platforms]
var_critic_score =  [platform.var_critic_score for platform in platforms]
std_critic_score =  [platform.std_critic_score for platform in platforms]

mean_EU_sales =  [platform.mean_EU_sales for platform in platforms]
max_EU_sales =  [platform.max_EU_sales for platform in platforms]
min_EU_sales =  [platform.min_EU_sales for platform in platforms]
var_EU_sales =  [platform.var_EU_sales for platform in platforms]
std_EU_sales =  [platform.std_EU_sales for platform in platforms]

mean_FP_sales =  [platform.mean_FP_sales for platform in platforms]
max_FP_sales =  [platform.max_FP_sales for platform in platforms]
min_FP_sales =  [platform.min_FP_sales for platform in platforms]
var_FP_sales =  [platform.var_FP_sales for platform in platforms]
std_FP_sales =  [platform.std_FP_sales for platform in platforms]

mean_global_sales =  [platform.mean_global_sales for platform in platforms]
max_global_sales =  [platform.max_global_sales for platform in platforms]
min_global_sales =  [platform.min_global_sales for platform in platforms]
var_global_sales =  [platform.var_global_sales for platform in platforms]
std_global_sales =  [platform.std_global_sales for platform in platforms]

mean_other_sales =  [platform.mean_other_sales for platform in platforms]
max_other_sales =  [platform.max_other_sales for platform in platforms]
min_other_sales =  [platform.min_other_sales for platform in platforms]
var_other_sales =  [platform.var_other_sales for platform in platforms]
std_other_sales =  [platform.std_other_sales for platform in platforms]

mean_user_count =  [platform.mean_user_count for platform in platforms]
max_user_count =  [platform.max_user_count for platform in platforms]
min_user_count =  [platform.min_user_count for platform in platforms]
var_user_count =  [platform.var_user_count for platform in platforms]
std_user_count =  [platform.std_user_count for platform in platforms]

mean_user_score =  [platform.mean_user_score for platform in platforms]
max_user_score =  [platform.max_user_score for platform in platforms]
min_user_score =  [platform.min_user_score for platform in platforms]
var_user_score =  [platform.var_user_score for platform in platforms]
std_user_score =  [platform.std_user_score for platform in platforms]

plot_single_value(value_name="NA_SALES",max=max_NA_sales,min=min_NA_sales,var=var_NA_sales,std=std_NA_sales,mean=mean_NA_sales)
plot_single_value(value_name="FP_SALES",max=max_FP_sales,min=min_FP_sales,var=var_FP_sales,std=std_FP_sales,mean=mean_FP_sales)
plot_single_value(value_name="EU_SALES",max=max_EU_sales,min=min_EU_sales,var=var_EU_sales,std=std_EU_sales,mean=mean_EU_sales)
plot_single_value(value_name="other_SALES",max=max_other_sales,min=min_other_sales,var=var_other_sales,std=std_other_sales,mean=mean_other_sales)
plot_single_value(value_name="global_SALES",max=max_global_sales,min=min_global_sales,var=var_global_sales,std=std_global_sales,mean=mean_global_sales)
plot_single_value(value_name="critic_count",max=max_critic_count,min=min_critic_count,var=var_critic_count,std=std_critic_count,mean=mean_critic_count)
plot_single_value(value_name="critic_score",max=max_critic_score,min=min_critic_score,var=var_critic_score,std=std_critic_score,mean=mean_critic_score)
plot_single_value(value_name="user_count",max=max_user_count,min=min_user_count,var=var_user_count,std=std_user_count,mean=mean_user_count)
plot_single_value(value_name="user_score",max=max_user_score,min=min_user_score,var=var_user_score,std=std_user_score,mean=mean_user_score)


"""
选出不同种类的游戏，统计其各类数值
"""

    