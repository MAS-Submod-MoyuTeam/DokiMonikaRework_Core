define DMR_MAX_AFF = 120
define DMR_MIN_AFF = -120

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

init -2 python in mas_sprites:
    import store

    def _outfit_wear_if_found(_moni_chr, outfit_name, by_user=False, outfit_mode=False):
        """
        Wears the outfit if it exists and has been gifted/reacted.
        It has been gifted/reacted if the selectable is unlocked.
        IN:
            _moni_chr - MASMonika object
            outfit_name - name of the outfit
            by_user - True if this action was mandated by user, False if not.
                (Default: False)
            outfit_mode - True means we should change hair/acs if it
                completes the outfit. False means we should not.
                (Default: False)
        """
        outfit_to_wear = store.mas_sprites.get_sprite(
            store.mas_sprites.SP_CLOTHES,
            outfit_name
        )
        if outfit_to_wear is not None:
            _moni_chr.change_clothes(outfit_to_wear, by_user=by_user, outfit_mode=outfit_mode)

init 995 python:
    def dmr_setAcs(id):
        """
        穿戴指定id的ACS饰品(发饰, 呆毛, 水杯等)
        无视是否解锁
        IN:
            id - 饰品字符串NAME(名称)
        """
        store.mas_sprites._acs_wear_if_found(store.monika_chr, id)
    
    def dmr_setOutfit(id):
        """
        穿戴指定名称的衣服, 无视是否解锁
        IN:
            id - 衣服名称 name
        """
        store.mas_sprites._outfit_wear_if_found(store.monika_chr, id)

    def dmr_wearClothesAndHairwithAOC(_group="date", _hairgroup="day"):
        """
        使用AOC切换衣服/发饰, 未安装时会在submod_log留下ERROR
        注意 AOC切换为随机切换 有极低概率不切换
        执行失败返回False, 否则返回True
        IN:
            group - 衣服的种类 默认为date 可用 - home/date/formal/sweater/jacket/pajamas
            _hairgroup - 头发类型 默认为day 可用 - day/night/down
        RETURN:
            执行结果T/F
        """
        if mas_submod_utils.isSubmodInstalled('Auto Outfit Change'):
            store.ahc_utils.changeHairAndClothes(
                    _day_cycle=_hairgroup,
                    _hair_random_chance=10,
                    _clothes_random_chance=10,
                    _exprop=_group
                )
            return True
        else:
            mas_submod_utils.submod_log.error("[DMR_C] Not installed submod 'Auto Outfit Change', change clothes/hair fail")
            return False

    def dmr_wearClotheswithAOC(_group="date"):
        """
        使用AOC切换衣服, 未安装时会在submod_log留下ERROR
        注意 AOC切换为随机切换 必定切换
        执行失败返回False, 否则返回True
        IN:
            _group - 衣服的种类 默认为date
            
        RETURN:
            执行结果T/F
        """
        if mas_submod_utils.isSubmodInstalled('Auto Outfit Change'):
            store.ahc_utils.changeClothesOfExprop(_group, chance=False)
            return True
        else:
            mas_submod_utils.submod_log.error("[DMR_C] Not installed submod 'Auto Outfit Change', change clothes fail")
            return False

init -5 python:
    def dmr_checkDDLCFanmodSaveDir(game):
        """
        检测指定Renpy游戏存档文件夹是否存在
        可以用来检查玩家是否玩过某个DDLC粉丝mod
        IN:
            game - 存档文件夹名称
        RETURN:
            bool
        """
        import os
        appdata = os.getenv('APPDATA')
        saveDir = appdata + "/RenPy/" + game

        return os.path.exists(saveDir)


    def dmr_gainAff(aff = 3, id = store.dmr_global.Id):
        """
        增加好感, 上限为10, 累计上限为120
        var:
            aff - 好感值 默认为3
            id - 约会Id, 默认为已加载的Id
        """
        if aff > 10:
            aff = 10
        
        for data in dmr_DateData:
            if data['Id'] == id:
                if data['GetAff'] > DMR_MAX_AFF:
                    mas_submod_utils.submod_log.warning("[DMR_C] '{}' increased {} aff, but reached the maximum value".format(id, aff))
                else:
                    data['GetAff'] += aff
                    mas_gainAffection(aff, bypass = True)
                    mas_submod_utils.submod_log.info("[DMR_C] '{}' increased {} aff".format(id, aff))
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
        
    def dmr_loseAff(aff = 3, id = store.dmr_global.Id):
        """
        降低好感, 上限为-10, 累计上限为-120
        var:
            aff - 好感值 默认为3
            id - 约会Id, 默认为已加载的Id
        """
        if aff > 10:
            aff = 10
        
        for data in dmr_DateData:
            if data['Id'] == id:
                if data['GetAff'] < DMR_MIN_AFF:
                    mas_submod_utils.submod_log.warning("[DMR_C] '{}' decreased '{}' aff, but reached the minimum value".format(id, aff))
                else:
                    data['GetAff'] -= aff
                    mas_loseAffection(aff)
                    mas_submod_utils.submod_log.info("[DMR_C] '{}' decreased '{}' aff".format(id, aff))
                return True
            else:
                continue
        raise DateSubmodException('Unable find dateid - 未找到约会数据id\n -> {}'.format(id))
        
init -990 python:

    def dmr_resetDateData():
        """
        重置所有约会数据
        """
        a = list()
        dmr_DateData = a
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
