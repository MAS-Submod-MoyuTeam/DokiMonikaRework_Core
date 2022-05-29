define DMR_MAX_AFF = 120

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

init 900 python:
    dmr_initData()
init -5 python:
    pass

init 950 python:
    def dmr_getAff(aff = None, id = dmr_global.Id):
        """
        增加好感, 上限为10, 累计上限为120
        var:
            aff - 好感值
            id - 约会Id, 默认为已加载的Id
        """
        if aff > 10:
            aff = 10
        
        for data in dmr_DateData:
            if data['Id'] == id:
                if data['GetAff'] > DMR_MAX_AFF:
                    mas_submod_utils.submod_log.info('[DMR_C] {} increased {} aff, but reached the maximum value'.format(id, aff))
                else:
                    data['GetAff'] += aff
                    mas_gainAffection(aff, bypass = True)
                    mas_submod_utils.submod_log.info('[DMR_C] {} increased {} aff'.format(id, aff))
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
        
    def dmr_loseAff(aff = None, id = dmr_global.Id):
        """
        降低好感
        var:
            aff - 好感值 最大值为-10, 无累计上限
            id - 约会Id, 默认为已加载的Id
        """
        if aff > 10:
            aff = 10
        
        for data in dmr_DateData:
            if data['Id'] == id:
                    data['GetAff'] -= aff
                    mas_gainAffection(aff, bypass = True)
                    mas_submod_utils.submod_log.info('[DMR_C] {} decreased {} aff'.format(id, aff))
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
        
init -990 python:

    def dmr_resetDateData():
        """
        重置所有约会数据
        """
        dmr_DateData = list():
        dmr_initData()

    def dmr_delDateData(id):
        """
        删除单个ID的数据
        var:
            id - 约会id
        exception:
            在未找到约会ID时
        """
        for data in dmr_DateData:
            if data['Id'] == id:
                dmr_DateData.remove(data)
                dmr_createData(id)
                return True 
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))

    def dmr_enableDateList():
        """
        返回所有可用的约会, 如果Conditional不为T则不会添加
        return:
            所有可用的约会list
            list每个元素的格式为<约会id>, <约会名称>
        """
        enbDList = list()
        for date in dmr_DateList:
            if date['Conditional']:
                infodate = [date['Id'], date['Name']]
                enbDList.append(infodate)
        return enbDList

    def dmr_unreadDateList():
        """
        返回未阅读过的约会, 且目前可用
        return:
            未阅读过的约会list
            list每个元素的格式为<约会id>, <约会名称>
        """
        noReadList = list()
        enbDList = dmr_enableDateList()
        for date in enbDList:
            readtime = dmr_getDateDataKey(id = date[0], key = 'Count')
            if readtime == 0:
                noReadList.append(date)
        return noReadList

    def dmr_readedDateList():
        """
        返回已阅读过的约会, 且目前可用
        return:
            已阅读过的约会list
            list每个元素的格式为<约会id>, <约会名称>
        """
        noReadList = list()
        enbDList = dmr_enableDateList()
        for date in enbDList:
            readtime = dmr_getDateDataKey(id = date[0], key = 'Count')
            if readtime > 0:
                noReadList.append(date)
        return noReadList

    def dmr_randomDate():
        """
        随机返回一个约会
        return:
            约会ID
        """
        if len(DateList) == 0:
            return None
        else:
            enbDList=list()
            for date in dmr_DateList:
                if date['Conditional'] == True:
                    enbDList.append(date)
            if len(envDList) > 0:        
                a = renpy.random.choice(enbDList)
                res = a['Id']
            else:
                res = None
            return res

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
        iDateData = {
        'Id':id,
        'Count':0,
        'FirstTime':0,
        'GetAff':0
        }
        dmr_DateData.append(iDateData)

    def dmr_getDateDataKey(id, key):
        """
        获取保存在数据中的某个特定键值
        var:
            id - 约会id
            key - 要查找的键
        return:
            正常运行 - 返回对应的Key值
            未找到 - 返回None
        exception:
            未找到约会数据id时返回异常
        """
        result = None
        for data in dmr_DateData:
            if data['Id'] == id:
                try:
                    result = data[key]
                except:
                    pass
                return result
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))


    def dmr_setDefData(id=dmr_global.Id):
        """
        更新初始的约会数据, 即Count和FirstTime
        var:
            id - 约会id, 为空则为当前加载的约会id
        exception:
            当id未在约会数据中找到时, 引发异常
        """
        import time
        for data in dmr_DateData:
            if data['Id'] == id:
                data['Count'] = data['Count'] + 1
                if data['FirstTime'] == 0:
                    data['FirstTime'] = time.time()
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))

    def dmr_setDateData(id, ikey, value = None):
        """
        在约会数据中创建/更新特定的关键信息
        var:
            id - 约会id, 为空则为当前加载的id
            key - 创建的键
            value - key 对应的键值
        return:
            True - 修改成功
            False - 修改项不允许修改
        exception:
            当id未在约会数据中找到时, 引发异常
        """
        ignore = ['Id', 'Count', 'FirstTime', 'GetAff']
        for noeditkey in ignore:
            if ikey == noeditkey:
                return False
        for data in dmr_DateData:
            if data['Id'] == id:
                data[ikey] = value
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
    
    def dmr_saveDateData():
        """
        将约会信息存储至persistent
        """
        persistent.DateData = dmr_DateData
