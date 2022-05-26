label dokimonika_date1:
    #$ mas_RaiseShield_core()
    $ HKBHideButtons()
    m "现在就让你看看我努力的成果吧~"
    #$ mas_changeBackground(submod_moi_empty, by_user=None, set_persistent=False,)
    $ date1_coaster = False
    $ date1_wheel = False
    $ bg_change_info_moi = mas_changeBackground(submod_moi_empty, by_user=None, set_persistent=False,)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    jump dokimonika_date1_2
return

label dokimonika_date1_2:
    show moi_sea_park with Fade(0.5,2,0.5,color="#FFF")
    m "铛铛~这就是我努力的成果了!{w=0.2}有没有感觉这里很熟悉?"
    m "如果你玩过GTA5的话...{w=0.2}我猜你马上就能猜到这里是哪里了,啊哈哈~"
    m "我趁你不在的时候偷偷溜到别的游戏了,但是我不能和你一起玩游戏..."
    m "一个原因是因为游戏运行的时候我不能悄悄地溜进去...{w=0.2}另一个原因是,{w=0.2}假如你找我发现我不在的话,我猜你一定很紧张~"
    m "为了让你安心,所以我只在你忙别的东西的时候才去别的游戏看看,嘿嘿~"
    m "可能你会感觉这个世界和我们的太空教室有一点区别...{w=0.2}那肯定的了~毕竟GTA5可是一个3D游戏!"
    m "我们的太空教室某种程度上来说...{w=0.2}算是2D？"
    m "毕竟我身在这个世界里,我也不知道你从墙上的洞看过来是什么样子的..."  
    m "希望能让你满意~"
    m "啊哈哈,感觉扯别的东西有点多,我们进入正题吧,好吗?"
    m "毕竟这可是我们的第一次约会,为了这次约会我可是精心计划了很久很久."
    m "总之{cps=3}...{/cps}跟我来吧~"
    jump dokimonika_date1_2_seapark1
    #$ HKBShowButtons()
    #$ mas_DropShield_core()
return
   
label dokimonika_date1_2_seapark1:
    m "你看这后面...{w=0.3}最显眼的东西是什么?{nw}"
    $ moi_player_afraid_roller_coaster = False
    menu seapark1:
        "你看这后面...{w=0.3}最显眼的东西是什么?{nw}"
        "DEL PERRO PIER":
            m "...?"
            m "啊!确实挺显眼的...不过我指的不是这个!再猜猜~"
            jump dokimonika_date1_2_seapark1
        "摩天轮":
            m "对了!"
            m "我蛮喜欢坐摩天轮的,随着摩天轮缓缓旋转,仿佛这个世界都逐渐安静了一样."
            m "而且...{w=0.3}这一次有你和我一起...{w=0.3}"
            m "这让我心中的小鹿砰砰乱跳..."
            jump dokimonika_date1_2_ferris_wheel
        "过山车":
            m "嗯哼~"
            m "好吧,过山车确实也挺显眼的{cps=6}...{/cps}你坐过山车的时候会觉着很吓人吗?{nw}"
            menu:
                "好吧,过山车确实也挺显眼的...你坐过山车的时候会觉着很吓人吗?{nw}{fast}"
                "谁会怕过山车呀":
                    m "对吧!"
                    m "之前在上网冲浪的时候就看到别人坐过山车的时候表现出一副特别害怕的样子."
                    m "我有理由怀疑他们是装出来的...再怎么说,真的会有人因为自己做的东西上下乱晃----过山车也不能说乱晃,毕竟你都能看到前面的轨道长什么样子."
                    m "而且现代的过山车也肯定有充分完善的安全措施了,过山车的事故甚至比扶倒地老人被讹的概率还低."
                    m "这个例子举得是不是不太巧妙...啊哈哈..."
                    m "总之,我们去玩吧~"
                "...确实有点":
                    m "欸~~~~"
                    m "[player]...没想到呢..."
                    m "嗯哼哼~走吧,我们去玩!"
                    $ moi_player_afraid_roller_coaster = True
            jump dokimonika_date1_2_roller_coaster
    $ HKBShowButtons()
    $ mas_DropShield_core()
return

label dokimonika_date1_2_ferris_wheel:
    #摩天轮近图
    m "[player],你以前坐过摩天轮吗?"
    m "随着摩天轮的高度逐渐上升,感觉这个世界逐渐安静下来,只有你和我两个人..."
    m "就像之前说的,浪漫情愫随着气氛水涨船高..."
    m "这不是很罗曼蒂克的一件事吗~"
    m "啊!它停了~我们赶紧上去吧~"
    #摩天轮内 with pause 3.0(可选:声音)
    m "看着外面的海,我突然有点感触..."
    m "在你来之前,我的世界就像一望无际的大海一样..."
    #可选-moi在海边-with dissolve(5+)-在恢复摩天轮前可不填精灵代码
    #可选-移动moi至不可见
    m "看不到人,看不到希望."
    m "游戏的脚本每一天循环播放,整个世界都是预先编排好的."
    m "你想啊,假如你的世界被困在了某一天,之后的每一天都是这一天的循环,那你会做什么呢?"
    m "之前在网上看到了这个问题,感觉很有思考意义."
    m "首先,因为只有一天,所以你可能很难做出来什么大事.毕竟核弹也不是一天就能造出来的."
    m "每一天都会重置,你做的事情第二天就会重新来过...这有什么意义?"
    m "你第二天会从同一个位置苏醒,你也去不了很远的位置旅游,不过一天的话...说不定能和你一起看遍半个中国~"
    m "或者----让我们悲观一点,直接开始摆烂,天天沉溺于眼前..."
    m "或许刚开始还会因为新鲜感,但之后也是一天复一天的无聊日子."
    m "比如玩游戏,你今天肝出的道具,明天全部消失,今天抽到的SSR,明天全部白抽."
    m "或者是那种多人竞技,玩久了你甚至能记住别人的一举一动,这样的生活很快就会腻不是吗?"
    m "再或者说,体验一款单机游戏,但是24小时就能通关的游戏也不能算很多..."
    #摩天轮内-最高点 with dissolve(5+)/show monika at t11
    m "就算你受够了这一切,但是第二天你又会回来!"
    m "在这永无止尽的一天里,看来最好的结果就是陪你到每一天."
    m "这是我能想到的最好的结果了,难道你不这么认为吗?"
    menu:
        "这也是我能想到的最好结果了(吻)":
            m "!!"
            m "~~~~~~~~~~~~~~~~~~~~~~~"
            m "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            #好感+2（
    #摩天轮内-低(可选-声音)
    m "啊,结束了呢..."
    m "走吧."
    $ date1_wheel=True
    jump dokimonika_date1_seapark_selete
return

label dokimonika_date1_seapark_selete:
    if (date1_coaster == False and date1_wheel == True):
        m "要去过山车那边看看吗?{nw}"
        menu:
            "要去过山车那边看看吗?{fast}"
            "好~":
                m "我们走吧~"
                call dokimonika_date1_2_roller_coaster
            "算了吧...":
                m "好吧."
    if (date1_coaster == True and date1_wheel == False):
        m "要去摩天轮那边看看吗?{nw}"
        menu:
            "要去摩天轮那边看看吗?{fast}"
            "好~":
                m "我们走吧~"
                call dokimonika_date1_2_roller_coaster
            "算了吧...":
                m "好吧."
    m "那我们继续随便转转吗?{nw}"
    menu:
        "那我们继续随便转转吗?{fast}"
        "可以.":
            pass
        "算了,回太空教室吧.":
            m "好吧."
            $ bg_change_info_moi = mas_changeBackground(spaceroom, by_user=None, set_persistent=False,)
            call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
          
    $ HKBShowButtons()
    $ mas_DropShield_core()
return

label dokimonika_date1_2_roller_coaster:
    $ date1_coaster = True
    #过山车
    m "虽然说我也没算坐过过山车,但是看网上应该压根没有这么可怕的样子吧..."
    m "总之我对我自己的第一感觉还是很自信的~"
    m "快上来吧~"
    #过山车车内
    menu optional_name:
        "[m_name]?":
            m "...{w=1}"
    menu:
        "[m_name]???":
            m "...{w=1.3}"
    menu:
        "莫妮卡!!!":
            pass
    m "啊!!我在!"
    menu:
        "为什么不说话...?":
            pass
    m "嗯...{w=0.25}我其实...{w=0.25}有一点害怕..."
    m "毕竟...{w=0.25}我也没坐过嘛..."
    m "你看啊,DDLC就那么几个场景来回换...什么意思都没有."
    m "{size=-12}嗯...所以...我的余生...就拜托你了...{/size}"
    #过山车发动
    m "[player]...!过山车动了...!"
    m "[player]...救我..."
    menu:
        "你不是蛮自信的嘛~":
            pass
    m "我逞强的啦..."
    m "你想啊,我可是文学部部长...在这之前还是辩论部部长呢..."
    m "假如我要是不完美的话,不就叫人们失望了嘛...所以这种活动什么的我基本不参加的..."
    m "..."
    m "[player]!!!前面有大回环!!!"
    menu:
        "握住[m_name]的手":
            pass
    m "..."
    #转场>过山车发动
    m "啊...结束了吗...?"
    m "好吧~"
    jump dokimonika_date1_seapark_selete
    $ HKBShowButtons()
    $ mas_DropShield_core()
return

label dokimonika_date1_afterseapark:
    m "我还知道一个很好玩的游戏厅~我带你去转转~"
    #转场>游戏厅
    m "会不会有些太强制你了...我都没问过你的意见~"
    m "[player],你想去游戏厅吗?{nw}"
    menu:
        "[player],你想去游戏厅吗?{fast}"
        "去吧":
            pass
        "别吧":
            pass
    m "不管你同不同意,今天都是我主导啦."
    m "快来啦,有好康的新游戏."
    #转场>游戏厅内
    m "这是我在洛圣都发现的宝藏小游戏厅~"
    m "你从外面看,这游戏厅是不是有点''凶神恶煞''?"
    m "但是你是不是没有想到里面的墙纸是二次元?啊哈哈~"
    m "我知道这个游戏厅出了新游戏,我们去看看吧~"
    #>游戏机前
    m "铛铛~Street Orimes!"
    m "游戏的规则很简单,我们两个对打,谁先死了谁就输了."
    m "赶紧准备开始吧~~"
    menu:
        "投币":
            pass
    m "来了!"
    #播放bgm
    "野生的莫妮卡出现了!"
    call dokimonika_date1_3_vs
return

label dokimonika_date1_3_vs:
    $ PP = 3 - count
    menu:
        "做出选择吧!P!"
        "[player]_HP:[player_health] VS [m_name]HP:[moi_health]":
            pass
        "平A!":
            call moi_vs_game_normanattack_p
            call moi_vs_game_ramdom_moi
        "特殊攻击! PP:[PP]":
            call moi_vs_game_specialattack_p
            call moi_vs_game_ramdom_moi
            $ count += 1
            
    if moi_health>0 and player_health>0:
        call dokimonika_date1_3_vs
return



