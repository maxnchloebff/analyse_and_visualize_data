import numpy as np


class platform_module():

    def __init__(self, name):
        self.name = name
        self.num = 0
        self.NA_sales = np.array([])
        self.EU_sales = np.array([])
        self.FP_sales = np.array([])
        self.other_sales = np.array([])
        self.global_sales = np.array([])
        self.critic_score = np.array([])
        self.critic_count = np.array([])
        self.user_score = np.array([])
        self.user_count = np.array([])

    def cal_mean(self):
        self.mean_NA_sales = self.NA_sales.mean()
        self.mean_EU_sales = self.EU_sales.mean()
        self.mean_FP_sales = self.FP_sales.mean()
        self.mean_other_sales = self.other_sales.mean()
        self.mean_global_sales = self.global_sales.mean()
        self.mean_critic_score = self.critic_score.mean()
        self.mean_critic_count = self.critic_count.mean()
        self.mean_user_score = self.user_score.mean()
        self.mean_user_count = self.user_count.mean()

    def cal_var_and_std(self):
        self.var_NA_sales = self.NA_sales.var()
        self.var_EU_sales = self.EU_sales.var()
        self.var_FP_sales = self.FP_sales.var()
        self.var_other_sales = self.other_sales.var()
        self.var_global_sales = self.global_sales.var()
        self.var_critic_score = self.critic_score.var()
        self.var_critic_count = self.critic_count.var()
        self.var_user_score = self.user_score.var()
        self.var_user_count = self.user_count.var()
        self.std_NA_sales = self.NA_sales.std()
        self.std_EU_sales = self.EU_sales.std()
        self.std_FP_sales = self.FP_sales.std()
        self.std_other_sales = self.other_sales.std()
        self.std_global_sales = self.global_sales.std()
        self.std_critic_score = self.critic_score.std()
        self.std_critic_count = self.critic_count.std()
        self.std_user_score = self.user_score.std()
        self.std_user_count = self.user_count.std()

    def cal_max_and_min(self):
        if len(self.NA_sales)!=0:
            self.max_NA_sales = self.NA_sales.max()
            self.min_NA_sales = self.NA_sales.min()
        else:
            self.max_NA_sales = 0
            self.min_NA_sales = 0
        if len(self.EU_sales) != 0:
            self.max_EU_sales = self.EU_sales.max()
            self.min_EU_sales = self.EU_sales.min()
        else:
            self.max_EU_sales = 0
            self.min_EU_sales = 0

        if len(self.FP_sales) != 0:
            self.max_FP_sales = self.FP_sales.max()
            self.min_FP_sales = self.FP_sales.min()
        else:
            self.max_FP_sales = 0
            self.min_FP_sales = 0
        if len(self.other_sales) != 0:
            self.max_other_sales = self.other_sales.max()
            self.min_other_sales = self.other_sales.min()
        else:
            self.max_other_sales = 0
            self.min_other_sales = 0
        if len(self.global_sales) != 0:
            self.max_global_sales = self.global_sales.max()
            self.min_global_sales = self.global_sales.min()
        else:
            self.max_global_sales = 0
            self.min_global_sales = 0
        if len(self.critic_score) != 0:
            self.max_critic_score = self.critic_score.max()
            self.min_critic_score = self.critic_score.min()
        else:
            self.max_critic_score = 0
            self.min_critic_score = 0
        if len(self.critic_count) != 0:
            self.max_critic_count = self.critic_count.max()
            self.min_critic_count = self.critic_count.min()
        else:
            self.max_critic_count = 0
            self.min_critic_count = 0
        if len(self.user_score) != 0:
            self.max_user_score = self.user_score.max()
            self.min_user_score = self.user_score.min()
        else:
            self.max_user_score = 0
            self.min_user_score = 0
        if len(self.user_count) != 0:
            self.max_user_count = self.user_count.max()
            self.min_user_count = self.user_count.min()
        else:
            self.max_user_count = 0
            self.min_user_count = 0





class gener_module():

    def __init__(self, genre):
        self.genre = genre
        self.num = 0
        self.NA_sales = np.array([])
        self.EU_sales = np.array([])
        self.FP_sales = np.array([])
        self.other_sales = np.array([])
        self.global_sales = np.array([])
        self.critic_score = np.array([])
        self.critic_count = np.array([])
        self.user_score = np.array([])
        self.user_count = np.array([])

    def cal_mean(self):
        self.mean_NA_sales = self.NA_sales.mean()
        self.mean_EU_sales = self.EU_sales.mean()
        self.mean_FP_sales = self.FP_sales.mean()
        self.mean_other_sales = self.other_sales.mean()
        self.mean_global_sales = self.global_sales.mean()
        self.mean_critic_score = self.critic_score.mean()
        self.mean_critic_count = self.critic_count.mean()
        self.mean_user_score = self.user_score.mean()
        self.mean_user_count = self.user_count.mean()

    def cal_var_and_std(self):
        self.var_NA_sales = self.NA_sales.var()
        self.var_EU_sales = self.EU_sales.var()
        self.var_FP_sales = self.FP_sales.var()
        self.var_other_sales = self.other_sales.var()
        self.var_global_sales = self.global_sales.var()
        self.var_critic_score = self.critic_score.var()
        self.var_critic_count = self.critic_count.var()
        self.var_user_score = self.user_score.var()
        self.var_user_count = self.user_count.var()
        self.std_NA_sales = self.NA_sales.std()
        self.std_EU_sales = self.EU_sales.std()
        self.std_FP_sales = self.FP_sales.std()
        self.std_other_sales = self.other_sales.std()
        self.std_global_sales = self.global_sales.std()
        self.std_critic_score = self.critic_score.std()
        self.std_critic_count = self.critic_count.std()
        self.std_user_score = self.user_score.std()
        self.std_user_count = self.user_count.std()

    def cal_max_and_min(self):
        self.max_NA_sales = self.NA_sales.max()
        self.max_EU_sales = self.EU_sales.max()
        self.max_FP_sales = self.FP_sales.max()
        self.max_other_sales = self.other_sales.max()
        self.max_global_sales = self.global_sales.max()
        self.max_critic_score = self.critic_score.max()
        self.max_critic_count = self.critic_count.max()
        self.max_user_score = self.user_score.max()
        self.max_user_count = self.user_count.max()
        self.min_NA_sales = self.NA_sales.min()
        self.min_EU_sales = self.EU_sales.min()
        self.min_FP_sales = self.FP_sales.min()
        self.min_other_sales = self.other_sales.min()
        self.min_global_sales = self.global_sales.min()
        self.min_critic_score = self.critic_score.min()
        self.min_critic_count = self.critic_count.min()
        self.min_user_score = self.user_score.min()
        self.min_user_count = self.user_count.min()