#默认约会状态:False
#检测是否中途退出

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_devtest_topic",
            category=["Moi's dev"],
            prompt="测试一下对话",
            pool=True,
            unlocked=False
        )
    )
label moi_devtest_topic:
    call dokimonika_date1
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_devtest_change_bg",
            category=["Moi's dev"],
            prompt="换一下测试背景.",
            pool=True,
            unlocked=False
        )
    )

label moi_devtest_change_bg:
    menu:
        "换哪一张呢?"
        "text":
            $ mas_changeBackground(submod_moi_test_bg, by_user=None, set_persistent=False,)
        "clothes shop":
            $ mas_changeBackground(submod_moi_clothes_shop, by_user=None, set_persistent=False,)
        "sea sunset":
            $ mas_changeBackground(submod_moi_sea_sunset, by_user=None, set_persistent=False,)
        "sea park":
            $ mas_changeBackground(submod_moi_sea_park, by_user=None, set_persistent=False,)
        "moi game vs":
            $ mas_changeBackground(submod_moi_game_vs, by_user=None, set_persistent=False,)
        "empty":
            $ mas_changeBackground(submod_moi_empty, by_user=None, set_persistent=False,)

return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_devtest_bg",
            category=["Moi's dev"],
            prompt="我想试试换个背景.",
            pool=True,
            unlocked=True,
        )
    )

label moi_devtest_bg:
    $ mas_changeBackground(mas_background_submod_maiteasu_lr_gamedus, by_user=None, set_persistent=False,)
return
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_room_test",
            category=["Moi's dev"],
            prompt="房间代码是哪个？",
            pool=True,
            unlocked=True,
        ),
    )

label moi_room_test:
    python:
        e="Error"

    m 1eua "好吧...我判断不出来..."
    m 1eua "不过我说不定可以给你提供一些相关信息:"
    
    m "store.mas_background.MBG_DEF=[store.mas_background.MBG_DEF]"
    m "mas_background=[mas_background]"
    m "store.mas_background.loadMBGData()=[store.mas_background.loadMBGData()]"
    m "monika_day_room=error"
    m "mbg_id=[e]"
    m "mbg_obj.unlocked=[e]"
    m "MASBackground=[MASBackground]"
    m "background_id=[e]"
    m "mas_current_background=[mas_current_background]"
    m "persistent._mas_current_background=[persistent._mas_current_background]"

    m "加油,[player],我期待你完成的那天~~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_what_room_id",
            category=["Moi's dev"],
            prompt="我在哪个房间？",
            pool=True,
            unlocked=True,
        ),
    )

label moi_what_room_id:
    m 1eua "现在的房间id是:[persistent._mas_current_background]"
    m "希望能帮到你~"
return




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_now_our_in_dating",
            category=["Moi's dev"],
            prompt="我们现在在约会吗？",
            pool=True,
            unlocked=True,
        ),
    )

label moi_now_our_in_dating:
    if persistent._submod_moi_dating_mode == False:
        m 1eua "我们还没有准备去呢..."
        m "不过我很期待那天!"
    else:
        m 1eua "我们不就是在约会吗?啊哈哈~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_change_dating_mode",
            category=["Moi's dev"],
            prompt="可以停止约会吗?",
            pool=True,
            unlocked=True,
        ),
    )
label moi_change_dating_mode:
    m "ok"
    $ persistent._submod_moi_dating_quit_detect_saved=0
    $ persistent._submod_moi_dating_mode = False
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_change_dating_mode_to_true",
            category=["Moi's dev"],
            prompt="我们开始约会吧!",
            pool=True,
            unlocked=True,
        ),
    )

label moi_change_dating_mode_to_true:
    m 1eua "好!"
    $ persistent._submod_moi_dating_quit_detect = renpy.random.randint(0,500000)
    $ persistent._submod_moi_dating_quit_detect_saved=persistent._submod_moi_dating_quit_detect
    $ persistent._submod_moi_dating_mode = True
    m 1eua "一些必要的信息..."
    m "persistent._submod_moi_dating_quit_detect=[persistent._submod_moi_dating_quit_detect]"
    m "persistent._submod_moi_dating_quit_detect_saved=[persistent._submod_moi_dating_quit_detect_saved]"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_change_dating_mode_quit_detect",
            category=["Moi's dev"],
            prompt="我退出过游戏吗?",
            pool=True,
            unlocked=True,
        ),
    )

label moi_change_dating_mode_quit_detect:
    if persistent._submod_moi_dating_mode and persistent._submod_moi_dating_quit_detect_saved == persistent._submod_moi_dating_quit_detect:
        m "没有哦~"
    else:
        m "嗯哼~？"
    m "persistent._submod_moi_dating_mode=[persistent._submod_moi_dating_mode]"
    m "persistent._submod_moi_dating_quit_detect_saved=[persistent._submod_moi_dating_quit_detect_saved]"
    m "persistent._submod_moi_dating_quit_detect=[persistent._submod_moi_dating_quit_detect]"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_change_clothes_date",
            category=["Moi's dev"],
            prompt="换件出门的衣服吧.",
            pool=True,
            unlocked=True,
        ),
    )

label moi_change_clothes_date:
    m "OK!"
    python:
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop="date"
        )
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_change_clothes_nor",
            category=["Moi's dev"],
            prompt="换件常服吧.",
            pool=True,
            unlocked=True,
        ),
    )

label moi_change_clothes_nor:
    m "OK!"
    python:
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop="sweater"
        )
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_what_weather",
            category=["Moi's dev"],
            prompt="我现在该穿什么衣服?",
            pool=True,
            unlocked=True,
        ),
    )

label moi_what_weather:
    $ what_clothes = moi_no_aac_weather_exprop_get(indoor=False)
    m "我应该穿[what_clothes]"
    m "现在的季节winter=[mas_isWinter()],summer=[mas_isSummer()],spring=[mas_isSpring()],autumn=Error"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_what_temp",
            category=["Moi's dev"],
            prompt="我现在该穿什么衣服?(根据awc获取的温度)",
            pool=True,
            unlocked=True,
        ),
    )
label moi_what_temp:
    $ what_clothes = moi_getClothesExpropForTemperature(indoor=False)
    $ min_temp = awc_getTemperature(temp="temp_min")
    m "我应该穿[what_clothes]"
    m "现在的最低温度=[min_temp]"
    m "现在的季节winter=[mas_isWinter()],summer=[mas_isSummer()],spring=[mas_isSpring()],autumn=Error"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_dev_info",
            category=["Moi's dev"],
            prompt="我想看一些信息",
            pool=True,
            unlocked=True,
        ),
    )

label moi_dev_info:
    m "好的!"
    m "persistent._mas_pw_would_come_to_spaceroom=[persistent._mas_pw_would_come_to_spaceroom]{nw}{fast}"
    m "persistent._mas_pm_wearsRing=[persistent._mas_pm_wearsRing]{nw}{fast}"
    m "persistent._mas_acs_enable_promisering=[persistent._mas_acs_enable_promisering]{nw}{fast}"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_dev_vs_game",
            category=["Moi's dev"],
            prompt="测试VS小游戏",
            pool=True,
            unlocked=True,
        ),
    )

label moi_dev_vs_game:
    menu:
        "[player],做出选择吧!"
        "你的HP:[moi_vsgame.moi_vs_get_health(player)]":
            pass
        "莫妮卡的HP:[moi_vsgame.moi_vs_get_health(moi)]":
            pass
        "平A!  |PP:--":
            $ moi_vsgame.moi_vs_health_system(False,moi,moi_vsgame.moi_vs_attack_nor(moi))
            $ moi_vsgame.moi_vs_attack_ranselect()
        "代码技能!  |PP:[vs_player_special_pp]":
            if moi_vsgame.moi_vs_attack_special(p="player") == Skip:
                pass
            else:
                $ moi_vsgame.moi_vs_attack_ranselect()
        "法术攻击!  |PP:-1":
            pass
        "防御!  |PP-1":
            pass
        "DEV-退出":
            return
    if player_health >0 and moi_health >0:
        call moi_dev_vs_game
return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_dev_vs_game_test1",
            category=["Moi's dev"],
            prompt="测试攻击,当前HP=[moi_health]/[player_health]",
            pool=True,
            unlocked=True,
        ),
    )
label moi_dev_vs_game_test1:
    call moi_vs_reset
    call dokimonika_date1_3_vs
return
    

label moi_dev_vs_game_test1_bak:
    "[player]对[m_name]发起了平A!"
    $ damage = moi_vsgame.moi_vs_attack_nor(p="player")
    $ miss = moi_vsgame.moi_vs_attack_miss(p="moi")
    $ vs_critical = moi_vsgame.moi_vs_attack_critical()
    $ c_damage = damage * vs_critical
    if vs_critical == 1.5:
        "效果拔群!"
    "[player]对[m_name]造成了[c_damage]点伤害"
    if miss == 0:
        "但是[m_name]躲开了!"
    $ f_damage = c_damage * miss 
    $ moi_health -= f_damage
    "当前moiHP:[moi_health]"

    "[m_name]对[player]发起了平A!"
    $ damage = moi_vsgame.moi_vs_attack_nor(p="moi")
    $ miss = moi_vsgame.moi_vs_attack_miss(p="player")
    $ critical = moi_vsgame.moi_vs_attack_critical()
    $ c_damage = damage * vs_critical
    if vs_critical == 1.5:
        "效果拔群!"
    "[m_name]对[player]造成了[c_damage]点伤害"
    if miss == 0:
        "但是[player]躲开了!"
    $ f_damage = c_damage * miss 
    $ player_health -= f_damage
    "当前玩家HP:[player_health]"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_vs_moi_specialattack",
            category=["Moi's dev"],
            prompt="测试[m_name]特殊攻击",
            pool=True,
            unlocked=True,
        ),
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_vs_reset",
            category=["Moi's dev"],
            prompt="重置HP",
            pool=True,
            unlocked=True,
        ),
    )
label moi_vs_reset:
    $ moi_health = 200
    $ player_health = 200
    $ count = 0
return
    