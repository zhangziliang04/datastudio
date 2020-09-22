# -*- coding: UTF-8 -*-
# 案例1：业务逻辑部分
from data_01 import *


# 第一部分：业务逻辑
# 01. 实时指标监控
def rt_index_base():
    paysum = pay_sum_query()
    ordersum = order_sum_query()
    inventsum = inventory_sum_query()

    cur = {'paysum' : paysum, 'ordersum': ordersum, 'inventsum': inventsum}
    return cur


# 02：历史数据趋势


