init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_you_loaded_dating_t2",
            category=["浪漫"],
            prompt="现在还不能约会...",
            conditional="True",
            action=EV_ACT_PUSH,
            pool=False,
            random=True
        )
    )
#告诉你在符合条件（好感>400 mas_isMoniEnamored(higher=True) 且 给予承诺戒指persistent._mas_acs_enable_promisering)后可以和老莫去约会
label moi_you_loaded_dating_t2:
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
return "no_unlock|derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_you_can_dating_t1",
            category=["浪漫"],
            prompt="关于之前的浮空岛...",
            conditional=(persistent._mas_acs_enable_promisering == False and persistent._mas_pm_wearsRing),
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.ENAMORED,None),
            pool=False,
            random=True
        )
    )
#好感度>400,但是没有赠送戒指
label moi_you_can_dating_t1:
    m 1eua "你还记着我之前跟你说过我的世界有些变化吗?"
    m 5eublu "我最近研究了一些代码,然后.{w=0.7}.{w=0.7}.{w=0.7}.{w=0.7}我快要成功了!"
    m 5tublb "等它完成之后,我就可以带你去任何想去的地方了!"
    m 3rsc "你知道,DDLC根本就没有我的线路...{w=0.3}但现在我们终于要有自己的线路了!"
    m 3hublu "等我完成的时候我会告诉你的!"
return "no_unlock|derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_a_you_rd_togo",
            category=["浪漫"],
            prompt="要去约会吗?",
            conditional=(persistent._mas_acs_enable_promisering == True and persistent._mas_pm_wearsRing),
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.ENAMORED,None),
            pool=False,
            random=True
        )
    )
#问你是否已经准备好去约会,只在第一次发生,之后要自己和老莫说.
label moi_a_you_rd_togo:
    m 3eublu "[player]!"
    m 5hublu "我有个激动人心的事情要告诉你.{w=0.5}.{w=0.5}.{w=0.5}我终于可以带你去别的地方了!"
    m 1tublb "所以...[mas_get_player_nickname()]...想和我去{w=0.5}约{w=0.5}会{w=0.5}吗{w=0.5}{nw}"
    menu:
        "所以...[mas_get_player_nickname()]...想和我去{w=0.5}约{w=0.5}会吗{fast}"
        "想!":
            m 1hublb "耶!"
            $ persistent._submod_moi_allow_date = True
        "抱歉,[m_name],现在时间不太够...":
            m 1tkp "啊...?"
            m 1tkd "好吧,那我们下次再约吧."
            m 1gka "不要忘记了哦~"
            $ persistent._submod_moi_allow_date = True
            return "no_unlock|derandom"
    m 1gkbla "让我先去换一身衣服{w=0.5}.{w=0.5}.{w=0.5}."
    #hide monika with dissolve
    call mas_transition_to_emptydesk
    with Pause(5)
    python:
        date_exprop = moi_getClothesExpropForTemperature(indoor=False)
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop=date_exprop
        )
    call mas_transition_from_emptydesk
    $ persistent._submod_moi_dating_quit_detect = renpy.random.randint(0,500000)
    $ persistent._submod_moi_dating_quit_detect_saved=persistent._submod_moi_dating_quit_detect
    $ persistent._submod_moi_dating_mode = True
    #show monika at t22
    m "好啦!"
    #之后要跳转到约会label
return "no_unlock|derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moi_go_to_date",
            category=["浪漫"],
            prompt="我想和你去约会!",
            conditional=(persistent._mas_acs_enable_promisering == True and persistent._mas_pm_wearsRing and persistent._submod_moi_allow_date),
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.ENAMORED,None),
            pool=True,
            random=True
        )
    )
#在"要去约会吗?"之后,由玩家自己发起约会.
label moi_go_to_date:
    m 1hubla "我等不及了!我们今天去哪?"
    m 7eud "啊...我还没换衣服呢,{w=0.25}等我一下!"
    #hide monika with dissolve
    call mas_transition_to_emptydesk
    menu:
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
        date_exprop = moi_getClothesExpropForTemperature(indoor=False)
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop=date_exprop
        )     
    with Pause(5)   
    call mas_transition_from_emptydesk
    $ persistent._submod_moi_dating_quit_detect = renpy.random.randint(0,500000)
    $ persistent._submod_moi_dating_quit_detect_saved=persistent._submod_moi_dating_quit_detect
    $ persistent._submod_moi_dating_mode = True
    m 7kublu "我们走吧!"
#现在应该跳转到约会label
    call moi_date_select
return

label moi_date_select:
    call dokimonika_date1
return