init -999 python:
    dmr_DateList = list()
    if persistent.DateData == None:
        persistent.DateData = list()
    dmr_DateData = persistent.DateData
    class DateSubmodException(Exception):
        '''当输出有误时，抛出此异常'''
        #自定义异常类型的初始化
        def __init__(self, value):
            self.value = value
        # 返回异常类对象的说明信息
        def __str__(self):
            return (self.value)

init -990 python:
    # 声明本次约会的变量
    # 变量名字可以改变
    DateInfo = {
        # 约会事件id 唯一
        'Id':'id',
        # 名称
        'Name':'NormalName',
        # 推送条件 python表达式
        'Conditional':'python code here',
        # 约会开始之前的label(从默认房间跳转到约会场景)
        # 不要包含call/jump语句
        'pre_StartLabel':'dmr_def_pSL',
        # 约会开始label
        # 在这里随意跳转label
        'StartLabel':'dmr_start_label',
        # 约会结束之前label
        # 类似于pre_StartLabel
        # 不要包含call/jump语句
        'pre_EndLabel':'dmr_def_pEL',
        # 约会结束label
        # 回到太空教室后的对话
        'EndLabel':'dmr_EndLabel'
    }

    # 保存在存档中的约会记录
    DateData = {
        'Id':'id',
        'Count':0,
        'FirstTime':0
    }
    # info为你声明约会使用的变量
    #dmr_DateList.append(DateInfo)

    def dmr_randomDate():
        """
        随机返回一个约会
        return:
            约会ID
        """
        if DateList.length == 0:
            return None
        else:
            a = renpy.random.choice(DateList)
            return a['Id']

    def dmr_initData():
        """
        对全部约会对话进行初始化
        """
        for dateinfo in dmr_DateList:
            existdata = False
            for datedata in dmr_DateData:
                if datedata['Id'] == dateinfo['Id']:
                    existdata = True
            if not existdata:
                dmr_createData(dateinfo['Id'])

    def dmr_createData(id):
        """
        在存档中创建约会数据
        var:
            id - 约会id
        """
        DateData = {
        'Id':id,
        'Count':0,
        'FirstTime':0
        }
        dmr_DateData.append(data)

    def dmr_setDefData(id):
        """
        更新初始的约会数据, 即Count和FirstTime
        var:
            id - 约会id
        exception:
            当id未在约会数据中找到时, 引发异常
        """
        for data in dmr_DateData:
            if data['Id'] == id:
                data['Count'] = data['Count'] + 1
                if data['FirstTime'] == 0:
                    data['FirstTime'] == time.time()
            else:
                raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))

    def dmr_setDateData(id, key, value = None):
        """
        在约会数据中创建/更新特定的关键信息
        var:
            id - 约会id
            key - 创建的键
            value - 创建的键值 不填则为None
        exception:
            当id未在约会数据中找到时, 引发异常
        """
        for data in dmr_DateData:
            if data['Id'] == id:
                data['key'] = value
            else:
                raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
    
    def dmr_saveDateData():
        """
        将约会信息存储至persistent
        """
        persistent.DateData = dmr_DateData
