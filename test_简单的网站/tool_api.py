import datetime
import time


################ 统计模块 ######################

#  接口get_data_arrive_leave_time_staffs用到
#  根据年月获取所有周一列表
def get_mondays(date_one):
    if is_valid_date(date_one)==False:
        return '输入日期数据格式不对'
    date_y_m = date_one[0:7]
    # date = datetime.datetime.strptime(date_one, '%Y-%m-%d')
    # print(date,type(date))
    # print(date.weekday()+1)

    result_monday = []
    month_31=[1,3,5,7,8,10,12]
    month_30=[4,6,9,11]
    # print(date_one[1],type(date_one))
    date_year = int(date_one[0:4])
    date_month = int(date_one[5:7])
    print('date_month:',date_month)
    if date_month in  month_31:
        print('在31天中')
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m + '-' + '0' + str(i+1))
                # print('从0-9中获取到周一信息')
        for i in range(9, 31):
            date_ = date_y_m + '-' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m + '-' + str(i+1))
                # print('从10-31中获取到周一信息')
    elif date_month in  month_30:
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m+ '-' + '0' + str(i+1))
        for i in range(9, 30):
            date_ = date_y_m + '-' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m + '-' + str(i+1))
    elif date_month == 2:
        print(date_year)
        if (date_year%4 == 0 and date_year % 100 != 0) | (date_year % 400 == 0 and date_year % 100 == 0):
            month_end = 29
        else:
            month_end = 28
        print(month_end)
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m + '-' + '0' + str(i+1))
        for i in range(9, month_end):
            date_ = date_y_m + '-' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_monday.append(date_y_m + '-' + str(i+1))
    print(result_monday)
    return result_monday


# 给定年月日，得到所有周一到周天的日期信息
def get_weeks_days(date_one):
    if is_valid_date(date_one) == False:
        return '输入日期数据格式不对'
    date_y_m = date_one[0:7]

    result_weeks_days = []
    count=0
    month_31=[1,3,5,7,8,10,12]
    month_30=[4,6,9,11]
    # print(date_one[1],type(date_one))
    date_y = date_one[0:4]
    date_m = date_one[5:7]
    date_year = int(date_one[0:4])
    date_month = int(date_one[5:7])
    print('date_month:', date_month)
    if date_month in month_31:
        print('在31天中')
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_weeks_days.append([])
                for j in range(1,8):
                    a=str(i+j)
                    if len(a)==1:
                        a = '0'+a
                    result_weeks_days[count].append(date_y_m + '-' + a )
                count+=1

                # print('从0-9中获取到周一信息')
        for i in range(9, 31):
            date_ = date_y_m + '-' + str(i+1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday()+1 == 1:
                result_weeks_days.append([])
                for j in range(1,8):
                    a = i+j
                    if a>31 and date_month==12:
                        temp_year = date_year+1
                        temp_month = 1
                        a='0'+str(a-31)
                    elif a>31:
                        temp_year=date_year
                        temp_month=date_month+1
                        a='0'+str(a-31)
                    else:
                        temp_year = date_year
                        temp_month= date_month
                    if len(str(temp_month))==1:
                        temp_month = '0'+str(temp_month)
                    else:
                        temp_month = str(temp_month)
                    result_weeks_days[count].append(str(temp_year)+'-'+str(temp_month)+'-'+str(a))
                count += 1
                # print('从10-31中获取到周一信息')
    elif date_month in  month_30:
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i + 1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday() + 1 == 1:
                result_weeks_days.append([])
                for j in range(1, 8):
                    a = str(i + j)
                    if len(a) == 1:
                        a = '0' + a
                    result_weeks_days[count].append(date_y_m + '-' + a)
                count += 1

                # print('从0-9中获取到周一信息')
        for i in range(9, 30):
            date_ = date_y_m + '-' + str(i + 1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday() + 1 == 1:
                result_weeks_days.append([])
                for j in range(1, 8):
                    a = i + j
                    if a > 30 :
                        temp_year = date_year
                        temp_month = date_month +1
                        a= '0' + str(a-30)
                    else:
                        temp_year = date_year
                        temp_month = date_month
                    if len(str(temp_month))==1:
                        temp_month = '0'+str(temp_month)
                    else:
                        temp_month = str(temp_month)
                    result_weeks_days[count].append(str(temp_year) + '-' + temp_month + '-' + str(a))
                count += 1
                # print('从10-30中获取到周一信息')
    elif date_month == 2:
        print(date_year)
        if (date_year%4 == 0 and date_year % 100 != 0) | (date_year % 400 == 0 and date_year % 100 == 0):
            month_end = 29
        else:
            month_end = 28
        print(month_end)
        for i in range(9):
            date_ = date_y_m + '-' + '0' + str(i + 1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday() + 1 == 1:
                result_weeks_days.append([])
                for j in range(1, 8):
                    a = str(i + j)
                    if len(a) == 1:
                        a = '0' + a
                    result_weeks_days[count].append(date_y_m + '-' + a)
                count += 1

                # print('从0-9中获取到周一信息')
        for i in range(9, month_end):
            date_ = date_y_m + '-' + str(i + 1)
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            if date_.weekday() + 1 == 1:
                result_weeks_days.append([])
                for j in range(1, 8):
                    a = i + j
                    if a > month_end:
                        temp_year = date_year
                        temp_month = 3
                        a= '0'+str(a-month_end)
                    else:
                        temp_year = date_year
                        temp_month = 2
                    result_weeks_days[count].append(str(temp_year) + '-' + '0' +str(temp_month) + '-' + str(a))
                count += 1

                # print('从10-month_end中获取到周一信息')
    print(result_weeks_days)
    return result_weeks_days


# '''判断是否是一个有效的日期字符串'''
def is_valid_date(strdate):
    try:
        time.strptime(strdate, "%Y-%m-%d")
        return True
    except:
        return False


import yaml
class CallYaml(object):
    """
    调用yaml 方法，操作yaml文件
    """

    def read_yaml(self,yaml_file):
        """
        读取yaml文件
        @file 文件路径
        """
        with open(yaml_file,"r",encoding="utf-8") as file:
            file_data = file.read()
            file.close()
            yaml_data = yaml.full_load(file_data) # 将数据格式化
            return yaml_data


# 获取工作日信息,出去周末和节假日
# y_m:'2023-04'
def get_workdays_except_holidays(y_m):
    res_=[]
    date_y = y_m[0:4]
    date_year = int(date_y)
    date_m = y_m[5:7]
    date_month = int(date_m)
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    yaml_file = 'yaml文件.yaml'
    yml = CallYaml()
    yaml_data = yml.read_yaml(yaml_file)
    # print(yaml_data)
    holidays = yaml_data['holiday_workday'][date_year]['holidays']
    extra_work_day = yaml_data['holiday_workday'][date_year]['extra_work_day']
    print('holidays',holidays)
    print('extra_work_day',extra_work_day)
    month_end=30
    if date_month == 2:
        if (date_year % 4 == 0 and date_year % 100 != 0) | (date_year % 400 == 0 and date_year % 100 == 0):
            month_end = 29
        else:
            month_end =28
    elif date_month in month_31:
        month_end = 31
    elif date_month in month_30:
        month_end = 30

    for i in range(1,month_end+1):
        if i<10:
            date_ = y_m+'-'+ '0' +str(i)
        else:
            date_ = y_m + '-' + str(i)
        date_1 = datetime.datetime.strptime(date_, '%Y-%m-%d')
        if date_ in extra_work_day:
            res_.append(date_)
        elif date_1.weekday()+1 not in [6,7] and date_ not in holidays:
            res_.append(date_)
    return res_



if __name__ =='__main__':
    # 测试get_workdays_except_holidays接口
    input_ = '2023-06'
    data = get_workdays_except_holidays(input_)
    print(data)
    print(len(data))


    # date1 = '2023-10-03'
    # date_list1 = ['2022-01-03','2022-02-03','2022-03-03','2022-04-03',
    #              '2022-05-03','2022-06-03','2022-07-03','2022-08-03',
    #              '2022-09-03','2022-10-03','2022-11-03','2022-12-03',]
    # date_list2 = ['2024-01-03', '2024-02-03', '2024-03-03', '2024-04-03',
    #               '2024-05-03', '2024-06-03', '2024-07-03', '2024-08-03',
    #               '2024-09-03', '2024-10-03', '2024-11-03', '2024-12-03', ]
    # date_list3 = ['2020-01-03', '2020-02-03', '2020-03-03', '2020-04-03',
    #               '2020-05-03', '2020-06-03', '2020-07-03', '2020-08-03',
    #               '2020-09-03', '2020-10-03', '2020-11-03', '2020-12-03', ]
    # date_list4 = ['2000-01-03', '2000-02-03', '2000-03-03', '2000-04-03',
    #               '2000-05-03', '2000-06-03', '2000-07-03', '2000-08-03',
    #               '2000-09-03', '2000-10-03', '2000-11-03', '2000-12-03', ]
    # for i in date_list4:
    #     # get_mondays(i)
    #     res = get_weeks_days(i)
    # print(res)