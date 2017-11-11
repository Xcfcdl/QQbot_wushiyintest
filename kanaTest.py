#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sql_do import *
import time

def getTimu():
    import random
    data = get_timu(random.randint(1, 46))
    return data[0]


def get_timenow():
    import time
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


def getKana(_qq):
    if not get_onekana(_qq):
        try:
            sql_do.bulid_db()
        except:
            pass
        finally:
            kanamodelinsert(_qq, 0, 0, '2017-01-01 00:00:00')
    return get_onekana(_qq)[0]


def time_cul(starttime):
    from datetime import datetime
    d, h, m, s = 0, 0, 0, 0
    cul = datetime.now() - datetime.strptime(starttime, "%Y-%m-%d %H:%M:%S")
    d = cul.days
    s = cul.seconds
    if s > 60:
        m = s // 60
        s = s % 60
        if m > 60:
            h = m // 60
            m = m % 60
    return [d, h, m, s]


def get_neirong():
    # 返回题目容许字符
    a = get_kana()
    # a = a + get_ao_yin()
    a = str(a)
    for i in ["(", ")", "[", "]", ",", " ", "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        a = a.replace(i, '')
    return a


class TestSystem():
    """接收信息返回信息"""

    def __init__(self, qq, content):
        self.msg = content.lower()
        self.answer_now = ''
        self.goals = 0
        self.qq, self.modeswitch, self.count, self.starttime = getKana(qq)
        self.testtime = time_cul(self.starttime)
        # 间隔时间

    def main(self):
        """
        1检测是否已经开始做题了
        2检测是否为相关命令
        3检测是否为答案
        """
        if self.modeswitch:

            if self.msg in get_neirong():
                if get_onegoals(str(int(time.mktime(time.strptime(self.starttime, '%Y-%m-%d %H:%M:%S')))) + str(self.qq)):
                    self._qq, self._sq, self.goals, self.timu = get_onegoals(
                        str(int(time.mktime(time.strptime(self.starttime, '%Y-%m-%d %H:%M:%S')))) + str(self.qq))[0]

                else:
                    return '数据库出错'
                
                if self.count < 10:
                    self.timu = get_timu(self.timu)
                    self.answer_now = self.msg
                    self.count += 1
                    # 做题..
                    if self.answer_now == self.timu[0][2]:
                        self.goals += 10
                        r = '回答正确，'
                    else:
                        r = '回答错误，'
                    update_kanamodel(self.qq, self.modeswitch,
                                     self.count, self.starttime)
                    chigi = getTimu()

                    update_usergoals(self.qq, str(int(time.mktime(time.strptime(self.starttime,'%Y-%m-%d %H:%M:%S')))) + str(self.qq), self.goals, chigi[0])
                    return r + '次は： 【' + chigi[1] + '】\nの片仮名は？'

                else:
                    return '你打穿了题库请输入【结束】来结束本次测试。'

            else:

                if self.msg == '结束':
                    self.modeswitch = 0
                    update_kanamodel(self.qq, self.modeswitch,
                                     self.count, self.starttime)
                    self._qq, self._sq, self.goals, self.timu = get_onegoals(
                        str(int(time.mktime(time.strptime(self.starttime, '%Y-%m-%d %H:%M:%S')))) + str(self.qq))[0]
                    return '已结束五十音测试，您的成绩为：' + str(self.goals)

                else:
                    return "输入有误，只能输入正确的相关命令/假名/罗马音/相关命令"
        elif self.msg == '开始':
            self.modeswitch = 1
            self.count = 0
            self.goals = 0
            self.starttime = get_timenow()
            update_kanamodel(self.qq, self.modeswitch,
                             self.count, self.starttime)
            chigi = getTimu()
            usergoalsinsert(self.qq, str(int(time.mktime(time.strptime(self.starttime,'%Y-%m-%d %H:%M:%S')))) +
                            str(self.qq), self.goals, chigi[0])
            return '开始答题，你可以随时输入[结束]来结束测试。\n首は： 【' + chigi[1] + '】の片仮名は？'
        elif self.msg == '查询历史成绩':
            datas = get_one_allgoals(str(self.qq))
            print(datas)
            if datas:
                goals = ''
                for data in datas:
                    dt = int(str(data[1]).replace(str(self.qq), ''))
                    x = time.localtime(dt)
                    dt = time.strftime('%Y-%m-%d %H:%M:%S',x)
                    goals = goals + dt + '分数:' + str(data[2]) + '\n'
            else:
                goals= '未创建'
            return goals
        elif self.msg == "退出":
            _model1 = 1
            _model2 = 0
            _model3 = 0
            _model4 = 0
            _model5 = 0
            update_users(self.qq, _model1, _model2, _model3, _model4, _model5)
            return "已退出五十音测试"
        else:
            return "是否开始五十音测试？请输入：\n开始\n查询历史成绩\n退出"
