import base64,json
from flask import Blueprint,render_template, request,jsonify
from test_flask.test_简单的网站 import cmd_mysql
import datetime

router_db_version= Blueprint('router_db_version', __name__)


@router_db_version.route("/")
def index1():
    return render_template("index.html")


# index.html中请求数据版本
@router_db_version.route("/2")
def birthday10_13():
    return render_template("test3_db.html")


# # 获取当天ai识别的考勤结果
# @router_db_version.route("/test_sql_img/<para>")
# def test_sql_img(para):
#     database = cmd_mysql.Database('img_no_id')
#     data_raw = database.get_AI_handle_oneday_data(para)
#     data_raw = list(data_raw)
#     for i in range(len(data_raw)):
#         data_raw[i]=list(data_raw[i])
#         # print(type(data_raw[i][2]),data_raw[i][1])
#         data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
#         data_raw[i][2]= base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
#     return render_template('test3_db.html', data_raw=data_raw)


# 获取当天ai识别的考勤结果
@router_db_version.route("/test_sql_img/<para>")
def test_sql_img(para):
    # database = cmd_mysql.Database('img_no_id')
    # data_raw = database.get_AI_handle_oneday_data(para)
    # data_raw = list(data_raw)
    # for i in range(len(data_raw)):
    #     data_raw[i]=list(data_raw[i])
    #     # print(type(data_raw[i][2]),data_raw[i][1])
    #     data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
    #     data_raw[i][2]= base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
    print(para)
    return render_template('test3_db.html')

# 获取当天ai识别的考勤结果
@router_db_version.route("/get_ai_data/<para>")
def get_ai_data(para):
    database = cmd_mysql.Database('img_no_id')
    sql = 'select name_face,img_time,img_face,img_body,name_body from {} where substring(img_time,6,5)="{}" ' \
          'and result_mark is null order by img_time desc limit 18'.format('img_no_id', para)
    data_raw = database.get_(sql)

    if data_raw:
        data_raw = list(data_raw)
        for i in range(len(data_raw)):
            data_raw[i]=list(data_raw[i])
            # print(type(data_raw[i][2]),data_raw[i][1])
            data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
            if(data_raw[i][2] and len(data_raw[i][2])>10):
                data_raw[i][2]= 'data:image/jpeg;base64,'+base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
            elif(data_raw[i][3]):
                data_raw[i][2] = 'data:image/jpeg;base64,' + base64.b64encode(
                    data_raw[i][3]).decode()  # 把二进制图片数据转成base64字符流
                data_raw[i][0]=data_raw[i][4]
            data_raw[i].pop(3)
            data_raw[i].pop(3)

        return jsonify({'ai_data':data_raw})
    return '未获取到数据'

# html页面：获取所有标注后的考勤结果
@router_db_version.route("/show_all_marked_img")
def show_all_marked_img():
    return render_template('show_all_marked_img.html')


# 获取所有标注后的考勤结果
@router_db_version.route("/get_all_marked_data")
def get_all_marked_data():
    oneday_date = request.args.get('date')  # 获取日期
    if(oneday_date):
        database = cmd_mysql.Database('img_no_id')
        data_raw = database.get_AI_handle_oneday_data(oneday_date)
        data_raw = list(data_raw)
        for i in range(len(data_raw)):
            data_raw[i]=list(data_raw[i])
            # print(type(data_raw[i][2]),data_raw[i][1])
            data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
            data_raw[i][2]= 'data:image/jpeg;base64,'+base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
        return jsonify({'ai_data':data_raw})
    else:
        sql = 'select result_mark,img_time,img_face from img_no_id where result_mark is not null'
        database = cmd_mysql.Database('img_no_id')
        data_raw = database.get_(sql)
        data_raw = list(data_raw)
        for i in range(len(data_raw)):
            data_raw[i] = list(data_raw[i])
            # print(type(data_raw[i][2]),data_raw[i][1])
            data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
            data_raw[i][2] = 'data:image/jpeg;base64,' + base64.b64encode(
                data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
        return jsonify({'ai_data': data_raw})


# 获取标注后的考勤结果，名字是result_mark字段的名字
@router_db_version.route("/test_sql_img_marked/<para>")
def test_sql_img_marked(para):
    database= cmd_mysql.Database('img_no_id')
    data_raw = database.get_AI_handle_oneday_data_marked(para)
    data_raw = list(data_raw)
    for i in range(len(data_raw)):
        data_raw[i]=list(data_raw[i])
        # print(type(data_raw[i][2]),data_raw[i][1])
        data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
        data_raw[i][2]= base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
    return render_template('test3_db_marked.html', data_raw=data_raw)


# 获取聚类后的考勤结果，名字是result_mark字段的名字
@router_db_version.route("/test_sql_img_julei/<para>")
def test_sql_img_julei(para):
    database= cmd_mysql.Database('img_no_id')
    data_raw = database.get_multi_data_julei(para, ['result_cluster', 'img_time', 'img_face'])
    # print('路由函数test_sql_img_julei，获取聚类结果data_raw:', data_raw)
    if data_raw:
        data_raw = list(data_raw)
        for i in range(len(data_raw)):
            data_raw[i]=list(data_raw[i])
            # print(type(data_raw[i][2]),data_raw[i][1])
            data_raw[i][1] = data_raw[i][1].strftime('%Y-%m-%d %H:%M:%S')  # 把datetime.datetime类型转换成字符串类型
            data_raw[i][2]= base64.b64encode(data_raw[i][2]).decode()  # 把二进制图片数据转成base64字符流
        return render_template('test3_db_julei.html', data_raw=data_raw)
    return '未获取到数据'


l_name = ['万华营','于福帅 - 全职','关敬徽 - 访问生','刘文宇','史老板','周富强','周睿','周福佳-访问生',
              '姚嘉巍','孙姝君-博士生','张可心-博士生','张树韬-博士生','张泽慧-访问生','张登涛-访问生',
              '朱光旭','朱朝阳-访问生','李勉','李哲','李明晓','李晓阳','李洋','李航','柴姝奇','毛经纬',
              '汪文宇','王嘉辰-访问生','王学梅-访问生','王浩-访问生','王烟濛-博士生','石睿-博士生',
              '祝久煜-访问生','祝文鑫','葛颂阳-博士生','蒲文强','蔡智捷-博士生','蔡腾浩-博士生','薛烨',
              '谈思颖-访问生','赖文海','赵立成','邱添羽','金锐','陈廷尉-访问生','陈怿','陈爱军','陈雁南',
              '雷振华','骆豪-访问生','龙寿伦','陌生人','NULL']

# 更新数据库操作，标注功能中的修改数据库result_mark字段
@router_db_version.route("/update_result_mark")
def update_result_mark():
    name = request.args.get('name')
    datetime_ = request.args.get('datetime_')
    res_mark_value = request.args.get('res_mark')
    # print(type(request.args.get('id')),request.args.get('id'))
    if res_mark_value in l_name:
        database = cmd_mysql.Database('img_no_id')
        # id=1 时，根据日期和名字修改result_mark
        if request.args.get('id')=='1':
            database.update_table_one_kv('result_mark',res_mark_value,name,datetime_)
            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
        # id=2时，根据日期时间修改result_mark字段
        else:
            database.update_table_one_kv_by_time('result_mark', res_mark_value, datetime_)
            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
    # print(name, datetime_, res_mark_value)
    # print(type(name), type(datetime_), type(res_mark_value),len(res_mark_value))
    print('输入的名称有误，请确认输入姓名是否正确')
    return '输入的名称有误，请确认输入姓名是否正确'

def update_res_mark(name,datetime_,res_mark_value,id):
    if res_mark_value in l_name:
        database = cmd_mysql.Database('img_no_id')
        # id=1 时，根据日期和名字修改result_mark
        if str(id)=='1':
            print('跳转到第1种情况更新','id的类型：',type(id))
            database.update_table_one_kv('result_mark',res_mark_value,name,datetime_)

            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
        # id=2时，根据日期时间修改result_mark字段
        elif str(id)=='2':
            print('跳转到第2种情况更新','id的类型：',type(id))
            print('result_mark是：===============================', res_mark_value)
            database.update_table_one_kv_by_time('result_mark', res_mark_value, datetime_)
            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
        elif str(id)=='3':
            #  所有标注结果中使用，根据result_mark,datetime_修改标注结果
            print('跳转到第3种情况更新', 'id的类型：', type(id))
            database.update_table_one_kv_by_mark_date('result_mark', res_mark_value, name, datetime_)

            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
        else:
            print('跳转到第三种情况更新','id的类型：',type(id))
            database.update_table_one_kv('result_mark', res_mark_value, name, datetime_)
            print('修改{}为{}，成功！'.format('result_mark', res_mark_value))
            return '修改{}为{}，成功！'.format(name, res_mark_value)
    # print(name, datetime_, res_mark_value)
    # print(type(name), type(datetime_), type(res_mark_value),len(res_mark_value))
    print('输入的名称有误，请确认输入姓名是否正确')
    return '输入的名称有误，请确认输入姓名是否正确'

# 更新数据库操作，标注功能中的修改数据库result_mark字段
@router_db_version.route("/update_batch_mark",methods=['POST'])
def update_batch_mark():
    print(request.data.decode('utf-8'))
    all_data = json.loads(request.data.decode('utf-8'))

    img_checkbox = all_data['img_checkbox']
    res_mark_value = all_data['res_mark']
    id = all_data['id']
    for i in img_checkbox:
        if id == 1:
            name, date_ = i.split('_')
            print(name,date_,'==========================================================')
            update_res_mark(name, date_, res_mark_value, id)
        elif id == 2:
            date_= i
            name=''
            update_res_mark(name,date_,res_mark_value,id)
        elif id ==3:
            res_mark, date_ = i.split('_')
            print(res_mark, date_, '==========================================================')
            update_res_mark(res_mark, date_, res_mark_value, id)
        print('更新resmark成功')
    return '哈哈哈，标注成功{}张图片'.format(len(img_checkbox))

# 更新数据库操作，标注功能中的修改数据库result_mark字段
# @router_db_version.route("/update_batch_mark_from_julei",methods=['POST'])
# def update_batch_mark_from_julei():
#     print(request.data.decode('utf-8'))
#     all_data = json.loads(request.data.decode('utf-8'))
#
#     img_checkbox = all_data['img_checkbox']
#     res_mark_value = all_data['res_mark']
#     for i in img_checkbox:
#         name, date_ = i.split('_')
#         print(name,date_,'==========================================================')
#         update_res_mark(name,date_,res_mark_value)
#         print('更新resmark成功')
#     return '哈哈哈'


@router_db_version.route("/select_all_status_name")
def select_all_status_name():
    database = cmd_mysql.Database('status_name')
    all_status = database.select_all_status_name()
    print(all_status)
    l =[]
    for status in all_status:
        l.append(status[0])
    return jsonify({'list_status': l})

# 获取表status_name_part中的员工名字
@router_db_version.route("/select_part_status_name")
def select_part_status_name():
    database = cmd_mysql.Database('status_name_part')
    all_status = database.select_all_status_name()
    # print(all_status,'=============================================================================================')
    l =[]
    for status in all_status:
        l.append(status[0])
    # print(l,'==================================================================================================')
    return jsonify({'list_status': l})

############################################### 统计模块 ######################################################
# 去重查询，查找一天中最早上班记录
@router_db_version.route("/select_name_date_groupby_name")
def select_name_date_groupby_name():
    time_one_day = request.args.get('time_one_day')
    print(time_one_day)
    database = cmd_mysql.Database('img_no_id')
    all_data = database.get_name_date_groupby_name(time_one_day)
    # print(all_data,'=============================================================================================')
    l1 =[]
    l2 =[]
    l3 = []
    for data in all_data:
        if data[0] != '陌生人':
            str_time = data[1].strftime('%Y-%m-%d %H:%M:%S')
            l1.append(data[0])
            l2.append(str_time)
            l3.append(data[0]+"--到达时间--"+str_time)
    print(l3,'=================select_name_date_groupby_name l3=====================================')
    return jsonify({'name_list': l1, 'time_list': l2, 'all_data': l3})


# 统计模块主页
@router_db_version.route("/tongji")
def tongji():
    return render_template("test4_db_tongji.html")


# 获取个人一周数据
@router_db_version.route("/get_one_week_one_person_data")
def get_one_week_one_person_data():
    database = cmd_mysql.Database('img_no_id')
    name_select = request.args.get('name')
    sql = "select * from " \
          "(select name_face,img_time,img_face from img_no_id where name_face = '{}' group by substring(img_time,6,5)" \
          "order by img_time desc limit 7) as a order by img_time asc;".format(name_select)
    all_data = database.get_(sql)
    if all_data:

        all_data = list(all_data)
        for i in range(len(all_data)):
            all_data[i] = list(all_data[i])
            all_data[i][1] = all_data[i][1].strftime('%Y-%m-%d %H:%M:%S')
            all_data[i][2] = 'data:image/jpeg;base64,' + base64.b64encode(all_data[i][2]).decode()
        # print(all_data)

        return jsonify({'all_data': all_data})
    return '未查询到结果'


############################# 统计模块 ###############################################

@router_db_version.route("/onePeopleOneDay")
def onePeopleOneDay():
    return render_template("allPeopleOneDay.html")
# 获取所有人人一天数据
@router_db_version.route("/get_data_arrive_leave_time_staffs",methods=['POST'])
def get_data_arrive_leave_time_staffs():
    database = cmd_mysql.Database('img_no_id')

    print(request.data.decode('utf-8'))
    req_data = json.loads(request.data.decode('utf-8'))
    staffs = req_data['staffs']
    # print(staffs,'**************************************************')
    date_one_day = req_data['date_one_day']
    # print(date_one_day,'111111111111111111111111111111111111111111111111111111111111111111111111')
    all_data=[]
    for staff in staffs:
        # select max(img_time),min(img_time),name_face from img_no_id where substring(img_time,6,5)='04-01' and name_face='周富强';
        sql = "select max(img_time),min(img_time),name_face from img_no_id " \
              "where substring(img_time,1,10)='{}' and name_face='{}';"\
            .format(date_one_day,staff)
        data = database.get_(sql)
        if data[0][0]:
            data = list(data)
            # print(data,'################ get_data_arrive_leave_time_staffs ################')

            for i in range(len(data)):
                t = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
                data[i] = list(data[i])
                data[i][0] = data[i][0].strftime('%Y-%m-%d %H:%M:%S')[11:]  # 去除年月日
                data[i][1] = data[i][1].strftime('%Y-%m-%d %H:%M:%S')[11:]
                # a = datetime.datetime.strptime(data[i][0], '%Y-%m-%d %H:%M:%S')
                a = datetime.datetime.strptime(data[i][0], '%H:%M:%S')
                b = datetime.datetime.strptime(data[i][1], '%H:%M:%S')
                data[i][0] = (a-t).seconds
                data[i][1] = (b-t).seconds
                data[i].append((a-b).seconds)
            all_data.append(data[0])
            # print(all_data)
        else:
            all_data.append([0,0,staff,0])
    print(all_data)
    return jsonify({'all_data': all_data})


@router_db_version.route("/allPeopleOneWeek")
def allPeopleOneWeek():
    return render_template("allPeopleOneWeek.html")
# 获取所有人人一周数据
@router_db_version.route("/all_data_one_week",methods=['POST'])
def get_all_data_one_week():
    database = cmd_mysql.Database('img_no_id')

    print(request.data.decode('utf-8'))
    req_data = json.loads(request.data.decode('utf-8'))
    staffs = req_data['staffs']
    # print(staffs,'**************************************************')

    date_select = req_data['date_select']
    date_y_m_d = date_select[0:7]+'-01'
    num_week = int(date_select[8:])
    from .tool_api import get_weeks_days
    day_list = get_weeks_days(date_y_m_d)
    if num_week == 5 and num_week != len(day_list):
        num_week = len(day_list)
    # print(date_one_day,'111111111111111111111111111111111111111111111111111111111111111111111111')
    all_data=[[],[]]
    all_data[0]=day_list[num_week-1]
    print(date_select,num_week,'===================== num_week =============================')
    seq_stuff = 0
    for staff in staffs:
        # seq_stuff+=1
        # select max(img_time),min(img_time),name_face from img_no_id where substring(img_time,6,5)='04-01' and name_face='周富强';
        # all_data.append([])
        s_one_week = []
        print(staff,day_list[num_week-1])
        for item_day in day_list[num_week-1]:

            sql = "select max(img_time),min(img_time) from img_no_id " \
                  "where substring(img_time,1,10)='{}' and name_face='{}';"\
                .format(item_day,staff)
            data = database.get_(sql)
            # print(data,'=====================data==============================')
            if data[0][0]:
                data = list(data)
                # print(data,'################ get_data_arrive_leave_time_staffs ################')
                for i in range(len(data)):
                    t = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
                    data[i] = list(data[i])
                    data[i][0] = data[i][0].strftime('%Y-%m-%d %H:%M:%S')[11:]  # 去除年月日
                    data[i][1] = data[i][1].strftime('%Y-%m-%d %H:%M:%S')[11:]
                    # a = datetime.datetime.strptime(data[i][0], '%Y-%m-%d %H:%M:%S')
                    a = datetime.datetime.strptime(data[i][0], '%H:%M:%S')
                    b = datetime.datetime.strptime(data[i][1], '%H:%M:%S')
                    # data[i][0] = (a-t).seconds
                    # data[i][1] = (b-t).seconds
                    s_one_week.append(round((a-b).seconds/3600,2))

            else:
                s_one_week.append(0)
        all_data[1].append(s_one_week)

    print(all_data)
    return jsonify({'all_data': all_data})


@router_db_version.route("/allPeopleOneMonth")
def allPeopleOneMonth():
    return render_template("allPeopleOneMonth.html")
# 获取所有人人一周数据
@router_db_version.route("/get_all_data_one_month",methods=['POST'])
def get_all_data_one_month():
    database = cmd_mysql.Database('img_no_id')

    # print(request.data.decode('utf-8'))
    req_data = json.loads(request.data.decode('utf-8'))
    staffs = req_data['staffs']
    date_select = req_data['date_select']
    date_y_m = date_select[0:7]
    from .tool_api import get_workdays_except_holidays
    day_list = get_workdays_except_holidays(date_y_m)
    # print(date_one_day,'111111111111111111111111111111111111111111111111111111111111111111111111')
    all_data=[[],[],[],[],[]]
    # print(date_select,num_week,'===================== num_week =============================')
    all_data[3]=day_list
    for staff in staffs:
        # seq_stuff+=1
        # select max(img_time),min(img_time),name_face from img_no_id where substring(img_time,6,5)='04-01' and name_face='周富强';
        # all_data.append([])
        work_hours_one_month = []
        abnormal_day=[]
        num_abnormal_days=0
        # print(staff)
        for item_day in day_list:
            time_arrive_reference = '09:00:00'
            time_leave_reference = '17:30:00'

            sql = "select max(img_time),min(img_time) from img_no_id " \
                  "where substring(img_time,1,10)='{}' and name_face='{}';"\
                .format(item_day, staff)
            data = database.get_(sql)
            # print(data,'=====================data==============================')
            if data[0][0]:
                data = list(data)
                # print(data,'################ get_data_arrive_leave_time_staffs ################')
                for i in range(len(data)):
                    # t = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
                    data[i] = list(data[i])
                    data[i][0] = data[i][0].strftime('%Y-%m-%d %H:%M:%S')[11:]  # 去除年月日
                    data[i][1] = data[i][1].strftime('%Y-%m-%d %H:%M:%S')[11:]
                    if data[i][0]<time_leave_reference or data[i][1]>time_arrive_reference:
                        abnormal_day.append(item_day+' ' +data[i][0]+' '+data[i][1])
                        num_abnormal_days+=1
                    else:
                        abnormal_day.append(item_day + '考勤正常')
                    # a = datetime.datetime.strptime(data[i][0], '%Y-%m-%d %H:%M:%S')
                    a = datetime.datetime.strptime(data[i][0], '%H:%M:%S')
                    b = datetime.datetime.strptime(data[i][1], '%H:%M:%S')
                    # data[i][0] = (a-t).seconds
                    # data[i][1] = (b-t).seconds
                    work_hours_one_month.append(round((a-b).seconds/3600,2))

            else:
                work_hours_one_month.append(0)
                abnormal_day.append(item_day+'未到岗')
                num_abnormal_days+=1
        all_data[0].append(work_hours_one_month)
        all_data[2].append(abnormal_day)
        num_workdays = len(work_hours_one_month)
        sum_hours_workdays = 0
        for i in work_hours_one_month:
            sum_hours_workdays+=i
        average_work_hours = sum_hours_workdays/num_workdays
        all_data[1].append(round(average_work_hours,2))
        all_data[4].append(num_abnormal_days)
    print(len(all_data[0]),all_data[0])
    print(len(all_data[0][0]),all_data[0][0])
    print(len(all_data[1]),all_data[1])
    print(len(all_data[2][0]),all_data[2][0])
    print(len(all_data[3]),all_data[3])
    print(len(all_data[4]),all_data[4])
    return jsonify({'all_data': all_data})

@router_db_version.route("/showRealtimeVideo")
def showRealtimeVideo():
    return render_template("showRealtimeVideo.html")

@router_db_version.route("/get_num_imgs/<para>")
def get_num_imgs(para):
    database = cmd_mysql.Database('img_no_id')
    sql='select count(*) from img_no_id where substring(img_time,6,5)="{}" '.format(para)
    data_raw = database.get_(sql)[0][0]
    print(data_raw)
    return str(data_raw)
@router_db_version.route("/updateMark")
def updateMark():
    return render_template("updateMark.html")




