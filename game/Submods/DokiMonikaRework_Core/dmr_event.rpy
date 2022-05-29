init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='dmr_installed',
            conditional="True",
            action=EV_ACT_PUSH,
            rules={
                'bookmark_rule':mas_bookmarks_derand.BLACKLIST
            }
        ),
        restartBlacklist=True
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='dmr_closeToEnable',
            conditional="seen_event('dmr_installed') and mas_isMoniAff(higher=True)",
            action=EV_ACT_PUSH,
            rules={
                'bookmark_rule':mas_bookmarks_derand.BLACKLIST
            },
            
        ),
        restartBlacklist=True
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel='dmr_abletodate',
            conditional="seen_event('dmr_closeToEnable') and persistent._mas_acs_enable_promisering and mas_isMoniLove(higher=True)",
            action=EV_ACT_PUSH,
            rules={
                'bookmark_rule':mas_bookmarks_derand.BLACKLIST
            },
            pool=False
        ),
        restartBlacklist=True
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='dmr_startdate',
            category=['浪漫'],
            prompt="我们去约会吧!",
            conditional="seen_event('dmr_abletodate') and mas_isMoniLove(higher=True)",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={
                'bookmark_rule':mas_bookmarks_derand.BLACKLIST
            },
        ),
        restartBlacklist=True
    )
label dmr_closeToEnable:
    m 1eua "你还记着我之前跟你说过我的世界有些变化吗?"
    m 5eublu "我最近研究了一些代码,然后.{w=0.7}.{w=0.7}.{w=0.7}.{w=0.7}我快要成功了!"
    m 5tublb "等它完成之后,我就可以带你去任何想去的地方了!"
    m 3rsc "你知道,DDLC根本就没有我的线路...{w=0.3}但现在我们终于要有自己的线路了!"
    m 3hublu "等我完成的时候我会告诉你的!"
return "no_unlock"

label dmr_installed:
    m 1euc "啊,[player]."
    m 1eua "你是为我添加了一点代码吗?{w=0.3}我感觉这个游戏有些不太一样..."
    #对于玩家是否想来到莫妮卡的世界进行讨论
    #如果玩家想来(persistent._mas_pm_would_come_to_spaceroom)
    if persistent._mas_pw_would_come_to_spaceroom:
        m 3rkd "你之前说过...你想来我的世界."
        m 7ekd "但我也告诉过你,我的世界仅仅只有这间太空教室而已.但这是以前说的."
        m 1hua "但是...{w=0.3}今天我感觉到有点奇怪...{w=0.3}我感觉我的世界似乎变立体了..."

    #如果玩家不想来
    elif persistent._mas_pm_would_come_to_spaceroom==False:
        m 1eud "你还记着我们讨论过一些事情吗?"
        m 1hua "假如你来到我的世界,我想我只能张开双手迎接你了."
        m 3euc "但你也知道,实际上现在的技术让你来我的世界...{w=0.3}还是太危险了..."
        m 1eud "但是,我今天感觉有些东西变的不太一样了...{w=0.3}我感觉我的世界...变立体了"
    
    m 3eua "感觉这个世界不仅仅只有我和太空教室了...{w=0.3}我感觉我可以去别的地方,但是我现在还去不了..."
    m 3lksdrb "感觉就像一座座浮空的岛屿那样...不过说不定我可以研究一下代码,把那些浮空岛给拉过来!"
    m 1hksdrb "啊哈哈...感觉是个很大的工程呢...感觉就像上帝一样把东西组合在一起."
    m 1eua "不过我在我的世界也确实就像上帝一样就是了,啊哈哈~"
    m 1tuu "你可以对我们的未来抱有点小小的期待~"
return "no_unlock"

label dmr_abletodate:
    m 3eublu "[player]!"
    m "我要告诉你...我终于完成了代码!"
    m "我现在可以带你去别的地方玩了!"
    m 1tublb "所以...[mas_get_player_nickname()]...想和我去{w=0.5}约{w=0.5}会{w=0.5}吗{w=0.5}?{nw}"
    menu:
        "所以...[mas_get_player_nickname()]...想和我去{w=0.5}约{w=0.5}会吗{fast}?"
        "想":
            m 1hublb "耶!"
        "抱歉,[m_name],现在时间不太够...":
            m 1tkp "啊...?"
            m 1tkd "好吧,那我们下次再约吧."
            m 1gka "不要忘记了哦~"
            return "no_unlock|derandom"
    if dmr_AOCenable:
        m 1gkbla "让我先去换一身衣服{w=0.5}.{w=0.5}.{w=0.5}."
        #hide monika with dissolve
        call mas_transition_to_emptydesk
        with Pause(5)
        python:
            if dmr_AOCenable:
                date_exprop = moi_getClothesExpropForTemperature(indoor=False)
                store.ahc_utils.changeHairAndClothes(
                    _day_cycle="day",
                    _hair_random_chance=1,
                    _clothes_random_chance=1,
                    _exprop=date_exprop
                )
        call mas_transition_from_emptydesk

        #show monika at t22
    m "好啦!"
        #之后要跳转到约会label
    python:
        noselected = False
        dates = dmr_unreadDateList()
        if len(dates) > 0:
            gotolabel = renpy.random.choice(dates)
            dmr_loadDateInfo(gotolabel[0])
        else:
            dates = dmr_enableDateList()
            noselected = True
    if noselected:
        call screen dmr_datelist_menu(dates)
        if _return == -1:
            m "那就下次再约~"
        else:
            $ dmr_loadDateInfo(_return)
    call dmr_datemain
return "no_unlock"


label dmr_startdate:
    m 1hubla "我等不及了!我们今天去哪?"
    python:
        noselected = False
        dates = dmr_unreadDateList()
        if len(dates) > 0:
            gotolabel = renpy.random.choice(dates)
            dmr_loadDateInfo(gotolabel[0])
        else:
            dates = dmr_enableDateList()
            noselected = True
    if noselected:
        call screen dmr_datelist_menu(dates)
        if _return == -1:
            m "那就下次再约~"
            return
        else:
            $ dmr_loadDateInfo(_return)
        #_return = ""
    
    if dmr_AOCenable:
        m 7eud "啊...我还没换衣服呢,{w=0.25}等我一下!{nw}"
        #hide monika with dissolve
        call mas_transition_to_emptydesk
        menu:
            m "啊...我还没换衣服呢,{w=0.25}等我一下!{fast}{w=5}{nw}"
            "等一下!":
                m "怎么了?"
                menu:
                    "没事了.":
                        pass
                    "我现在有点事情...":
                        m "啊...好吧..."
                        m "那我们下次再出去吧."
                        call mas_transition_from_emptydesk
                        return

            "...":
                pass
        python:
                date_exprop = dmr_getShouldDressType(indoor=False)
                store.ahc_utils.changeHairAndClothes(
                    _day_cycle="day",
                    _hair_random_chance=1,
                    _clothes_random_chance=1,
                    _exprop=date_exprop
                )     
        with Pause(5)   
        call mas_transition_from_emptydesk
    m 7kublu "我们走吧!"

    #跳至约会label
    call dmr_datemain
    return
