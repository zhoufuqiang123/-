from datetime import datetime

import pymysql


class Database():
    '''
        Description:
            database demo to store image in MySQL RDBMS
        Attributes:
            None
    '''

    # 初始化，连接数据库并获得操作对象
    def __init__(self,table):
        self.connection = pymysql.connect(host='10.20.14.27', user='root', passwd='root', db='test',
                                          charset='utf8')
        self.cursor = self.connection.cursor()
        # 存储的表名
        # self.table = 'imags2_no_id'
        self.table = table

        '''
            Description:
                create table to store imagestest
            Args:
                None
            Return:
                None
        '''

    # 判断数据库表imags2是否存在，不存在则新建
    def create_image_table(self):
        sql = 'create table if not exists {} (name varchar(50),img_date date,img_data longblob);'.format(self.table)
        # 建表命令 create talbe imags (
        #           id int not null primaty key auto_increment,
        #           name varchar(50),
        #           img_date date,

        #           img_data longblob);
        try:
            self.cursor.execute(sql)

            self.connection.commit()

        except pymysql.Error:
            print(pymysql.Error)

        '''
            Description:
                insert image into table
            Args:
                image:
                    image to store
            Returns:
                None
        '''

    # 往imags2表中插入图片
    def insert_image(self, image):
        sql = "insert into {}(name,img_date,img_data) values(%s,%s,%s)".format(self.table)
        try:
            self.cursor.execute(sql, image)
            self.connection.commit()
        except pymysql.Error:
            print(pymysql.Error)

    def get_(self,sql):
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            all_data = self.cursor.fetchall()
            print('数据条数：', len(all_data))
            return all_data
        except pymysql.Error:
            print(pymysql.Error)
            print('获取数据失败')

    # 根据date获取当天name,img_date,img_data,
    def get_AI_handle_oneday_data(self, date):
        sql = 'select name,img_date,img_data from {} where substring(img_date,6,5)="{}" and result_mark is null'.format(self.table, date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            all_data = self.cursor.fetchall()
            print(date, '照片数量：', len(all_data))
            return all_data
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')

    # 根据日期获取标注数据，标注结果，日期，图片数据
    def get_AI_handle_oneday_data_marked(self, date):
        sql = 'select result_mark,img_date,img_data from {} where substring(img_date,6,5)="{}" and result_mark is not null'.format(self.table, date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            all_data = self.cursor.fetchall()
            print(date, '照片数量：', len(all_data))
            return all_data
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')

    #     获取某天所有数据
    def get_AI_handle_oneday_alldata(self, date):
        sql = 'select * from {} where substring(img_date,6,5)="{}"'.format(self.table, date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            all_data = self.cursor.fetchall()
            print(date,'照片数量：',len(all_data))
            return all_data
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')


    # 根据date获取当天AI识别到的人名，date 格式04-05
    def get_AI_handle_person(self, date):
        sql = 'select name from {} where substring(img_date,6,5)="{}" group by name'.format(self.table, date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            names = self.cursor.fetchall()
            return names
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')

    # 从数据库中获取所有数据
    def get_data(self,):
        sql = 'select * from {}'.format(self.table)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            image = self.cursor.fetchone()[2]
            return image
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')

    # 根据name,img_date获取单个值
    def get_single_value(self,key,name,img_date):
        # sql = 'select %s from {} where name=%s and img_date=%s'.format(self.table)
        sql = 'select {} from {} where name="{}" and img_date="{}"'.format(key,self.table,name,img_date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            value = self.cursor.fetchone()[0]
            print('value:',value)
            return value
        except pymysql.Error:
            print(pymysql.Error)
            print('获取照片失败')

    # 根据日期查询值，date格式：'04-07',list_keys:['name','imag_date']
    def get_multi_data(self, date, list_keys):
        s = list_keys[0]
        for i in range(1, len(list_keys)):
            s = s+',' + list_keys[i]
        sql = 'select ' + s + ' from {} where substring(img_date,6,5)="{}"'.format(self.table,date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            result = self.cursor.fetchall()
            return result
        except pymysql.Error:
            print(pymysql.Error)
            print('获取数据失败')

        # 查询聚类数据，不包含已标注的，date格式：'04-07',list_keys:['name','imag_date']
    def get_multi_data_julei(self, date, list_keys):
        s = list_keys[0]
        for i in range(1, len(list_keys)):
            s = s + ',' + list_keys[i]
        sql = 'select ' + s + ' from {} where substring(img_date,6,5)="{}" and result_mark' \
                              ' is null ORDER BY result_cluster'.format(self.table, date)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            result = self.cursor.fetchall()
            return result
        except pymysql.Error:
            print(pymysql.Error)
            print('获取数据失败')

    # 去重查询，查找一天中最早上班记录
    def get_name_date_groupby_name(self,time_one_day):
        # sql = "select name,img_date from imags2_no_id where substring(img_date,6,5)="04-05" group by name;"
        sql = 'select name,img_date from {} where substring(img_date,6,5)="{}" group by name;'.format(self.table,time_one_day)
        try:
            print('开始获取数据库数据')
            self.cursor.execute(sql)
            print('成功获取数据库数据')
            result = self.cursor.fetchall()
            # print("结果：", result)
            return result
        except pymysql.Error:
            print(pymysql.Error)
            print('获取数据失败')
    # 根据名字和日期修改聚类值字段
    # key是要修改的字段名，value是修改后的字段值
    # name和img_date是数据库字段名，根据这两个字段得到要修改的记录
    # result_cluster是聚类结果值（int类型），result_mark是标记后的结果（字符串类型）
    def update_table_one_kv(self,key,value,name,img_date):
        if type(value)==str:
            sql = 'update {} set {}="{}" where name="{}" and img_date ="{}"'.format(self.table, key, value, name,img_date)
        else:
            sql = 'update {} set {}={} where name="{}" and img_date ="{}"'.format(self.table,key,value,name,img_date)
        try:
            print('开始修改数据库数据')
            self.cursor.execute(sql)
            self.connection.commit()
            print('成功修改:记录{}，{}的字段{}聚类值为{}'.format(name,img_date,key,value))
        except pymysql.Error:
            print(pymysql.Error)
            print('修改数据失败')

    def update_table_one_kv_by_mark_date(self,key,value,name,img_date):
        if type(value)==str and value != 'NULL':
            sql = 'update {} set {}="{}" where result_mark="{}" and img_date ="{}"'.format(self.table, key, value, name,img_date)
        else:
            sql = 'update {} set {}={} where result_mark="{}" and img_date ="{}"'.format(self.table,key,value,name,img_date)
        try:
            print('开始修改数据库数据')
            self.cursor.execute(sql)
            self.connection.commit()
            print('成功修改:记录{}，{}的字段{}聚类值为{}'.format(name,img_date,key,value))
        except pymysql.Error:
            print(pymysql.Error)
            print('修改数据失败')

    def update_table_one_kv_by_time(self,key,value,img_date):
        if type(value)==str:
            sql = 'update {} set {}="{}" where img_date ="{}"'.format(self.table, key, value, img_date)
        else:
            sql = 'update {} set {}={} where img_date ="{}"'.format(self.table,key,value, img_date)
        try:
            print('开始修改数据库数据')
            start_time = datetime.now()
            print('start_time:',start_time)
            self.cursor.execute(sql)
            mid_time = datetime.now()
            print('mid_time',mid_time)
            self.connection.commit()
            end_time = datetime.now()
            print('end_time:',end_time)
            print('成功修改:记录{}的字段{}聚类值为{}'.format(img_date,key,value))
        except pymysql.Error:
            print(pymysql.Error)
            print('修改数据失败')

    def update_table_two_kv(self,key1,value1,key2,value2,name,img_date):
        if type(value1)==str and type(value1)==str:
            sql = 'update {} set {}="{}",{}="{}" where name="{}" and img_date ="{}"'.format(self.table, key1, value1, key2,value2, name,img_date)
        elif type(value1)!=str and type(value1)==str:
            sql = 'update {} set {}={},{}="{}" where name="{}" and img_date ="{}"'.format(self.table, key1, value1,
                                                                                            key2, value2, name,
                                                                                            img_date)
        elif type(value1)==str and type(value1)!=str:
            sql = 'update {} set {}="{}",{}={} where name="{}" and img_date ="{}"'.format(self.table, key1, value1,
                                                                                            key2, value2, name,
                                                                                            img_date)
        else:
            sql = 'update {} set {}={},{}={} where name="{}" and img_date ="{}"'.format(self.table, key1, value1, key2, value2, name, img_date)
        try:
            print('开始修改数据库数据')
            self.cursor.execute(sql)
            self.connection.commit()
            print('成功修改:记录{}，{}的字段{}聚类值为{}'.format(name,img_date,key1,value1))
            print('成功修改:记录{}，{}的字段{}聚类值为{}'.format(name,img_date,key2,value2))
        except pymysql.Error:
            print(pymysql.Error)
            print('修改数据失败')
    # def get_image(self, path):
    #     sql = 'select * from imags2'
    #     try:
    #         print('开始获取数据库数据')
    #         self.cursor.execute(sql)
    #         print('成功获取数据库数据')
    #         image = self.cursor.fetchone()[3]
    #         print(image)
    #         with open(path, "wb") as file:
    #             file.write(image)
    #     except pymysql.Error:
    #         print(pymysql.Error)
    #         print('获取照片失败')
    #     except IOError:
    #         print(IOError)

    # 插入入人名数据库表 status_name
    def insert_to_status_name(self,name):
        sql = 'insert into {} (name) values("{}")'.format(self.table,name)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except pymysql.Error:
            print(pymysql.Error)

    # 获取所有职员名字
    def select_all_status_name(self):
        # sql = 'select name from {} '.format(self.table) # 正常取人名数据
        # 按姓氏排名获取名字
        sql = 'select name from {} order BY CONVERT(name USING GBK) ASC'.format(self.table)
        try:
            self.cursor.execute(sql)
            all_data = self.cursor.fetchall()
            return all_data
        except pymysql.Error:
            print(pymysql.Error)

    def __del__(self):
        self.connection.close()
        self.cursor.close()


# 数据写入指定目录的文件中
def imag_to_path(path,image):
    try:
        with open(path, "wb") as file:
            file.write(image)
    except IOError:
            print(IOError)



if __name__ == "__main__":
    #  status_name_part,status_name
    # database = Database('status_name_part')  # 全职人员姓名的数据库，不包括研究科学家
    # database = Database('status_name')  # 所有人名数据库
    database = Database('imags2_no_id')  # 存图片的数据库
    # data_raw = database.get_multi_data('04-05', ['result_cluster', 'img_date', 'img_data'])
    # print(len(data_raw))
    # print('路由函数test_sql_img_julei，获取聚类结果data_raw:', data_raw[0][0], data_raw[0][1])
    # database.update_table_one_kv_by_time()
    # database = Database('status_name')  # 人名数据库
        #  查询所有人名
    # all_names = database.select_all_status_name()
    # print(all_names[0][0])
    # 插入人名
    # l_name = ['万华营', '于福帅 - 全职', '关敬徽 - 访问生', '刘文宇', '史老板', '周富强', '周睿', '周福佳 - 访问生',
    #           '姚嘉巍', '孙姝君 - 博士生', '张可心 - 博士生', '张树韬 - 博士生', '张泽慧 - 访问生', '张登涛 - 访问生',
    #           '朱光旭', '朱朝阳 - 访问生', '李勉', '李哲', '李明晓', '李晓阳', '李洋', '李航', '柴姝奇', '毛经纬',
    #           '汪文宇', '王嘉辰 - 访问生', '王学梅 - 访问生', '王浩 - 访问生', '王烟濛 - 博士生', '石睿 - 博士生',
    #           '祝久煜 - 访问生', '祝文鑫', '葛颂阳 - 博士生', '蒲文强', '蔡智捷 - 博士生', '蔡腾浩 - 博士生', '薛烨',
    #           '谈思颖 - 访问生', '赖文海', '赵立成', '邱添羽', '金锐', '陈廷尉 - 访问生', '陈怿', '陈爱军', '陈雁南',
    #           '雷振华', '骆豪 - 访问生', '龙寿伦','陌生人']
    l_name = ['万华营', '于福帅-全职', '关敬徽-访问生', '刘文宇', '史老板', '周富强', '周睿', '周福佳-访问生',
              '姚嘉巍', '孙姝君-博士生', '张可心-博士生', '张树韬-博士生', '张泽慧-访问生', '张登涛-访问生',
              '朱光旭', '朱朝阳-访问生', '李勉', '李哲', '李明晓', '李晓阳', '李洋', '李航', '柴姝奇', '毛经纬',
              '汪文宇', '王嘉辰-访问生', '王学梅-访问生', '王浩-访问生', '王烟濛-博士生', '石睿-博士生',
              '祝久煜-访问生', '祝文鑫', '葛颂阳-博士生', '蒲文强', '蔡智捷-博士生', '蔡腾浩-博士生', '薛烨',
              '谈思颖-访问生', '赖文海', '赵立成', '邱添羽', '金锐', '陈廷尉-访问生', '陈怿', '陈爱军', '陈雁南',
              '雷振华', '骆豪-访问生', '龙寿伦','陌生人']
    l_name1 = ['万华营', '于福帅-全职',  '周富强',
               '李哲',  '毛经纬',
               '祝文鑫', '陈爱军',
               '龙寿伦']
    start_time = datetime.now()
    for i in range(20):
        # database.insert_to_status_name(i)

        database.update_table_one_kv_by_time('result_mark', '张泽慧-访问生', '2023-04-05 11:21:20')
    end_time = datetime.now()
    print('一共花费时间：', end_time-start_time)
    # read image from current directory
    # 读取图片接口
    # with open("./test.jpeg", "rb") as file:
    #     image = file.read()
    # 创建数据库表接口
    # database.create_image_table()
    # 插入图片接口
    # database.insert_image(['陌生人', '2023-04-02 10:31:11', image])
    # database.insert_image(['陌生人','2023-04-03 09:31:11',image])
    # 获取第一张图片接口
    # img = database.get_image()
    # 写入图片接口
    # imag_to_path('./result1.jpeg', img)
    # 获取当天人名
    # names = database.get_AI_handle_person('04-05')
    # print(names)
    # print(names[0][0])
    #获取所有数据
    # all_data = database.get_AI_handle_oneday_data('04-05')
    # print(len(all_data))
    # print(all_data[0][0])
    # for item in all_data:
    #     # print(item[1].strftime('%Y%m%d'))
    #     path = './static/img/'+item[1].strftime('%Y%m%d')+'/'+item[0]+item[1]+'.png'
    #     imag_to_path(path,item[2])
    # 修改聚类结果
    # database.update_table('result_cluster',1,'陌生人','2023-04-02 10:31:11') # 修改聚类结果为1
    # database.update_table('result_mark','张三','陌生人','2023-04-02 10:31:11') # 修改标注为张三
    # database.update_table('result_mark','NULL','陌生人','2023-04-02 10:31:11') # 修改标注为默认NULL
    #
    # database.get_single_value('result_mark','陌生人','2023-04-02 10:31:11')
    # data = database.get_AI_handle_oneday_data('04-07')
    # for i in data:
    #
    #     print(i[0],i[1])
    # print(len(data))
l_name =['万华营',
    '于福帅 - 全职',
    '关敬徽 - 访问生',
    '刘文宇',
    '史老板',
    '周富强',
    '周睿',
    '周福佳 - 访问生',
    '姚嘉巍',
    '孙姝君 - 博士生',
    '张可心 - 博士生',
    '张树韬 - 博士生',
    '张泽慧 - 访问生',
    '张登涛 - 访问生',
    '朱光旭',
    '朱朝阳 - 访问生',
    '李勉',
    '李哲',
    '李明晓',
    '李晓阳',
    '李洋',
    '李航',
    '柴姝奇',
    '毛经纬',
    '汪文宇',
    '王嘉辰 - 访问生',
    '王学梅 - 访问生',
    '王浩 - 访问生',
    '王烟濛 - 博士生',
    '石睿 - 博士生',
    '祝久煜 - 访问生',
    '祝文鑫',
    '葛颂阳 - 博士生',
    '蒲文强',
    '蔡智捷 - 博士生',
    '蔡腾浩 - 博士生',
    '薛烨',
    '谈思颖 - 访问生',
    '赖文海',
    '赵立成',
    '邱添羽',
    '金锐',
    '陈廷尉 - 访问生',
    '陈怿',
    '陈爱军',
    '陈雁南',
    '雷振华',
    '骆豪 - 访问生',
    '龙寿伦']