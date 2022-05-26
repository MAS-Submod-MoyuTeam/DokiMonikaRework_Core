default moi_health=200
default player_health=200
default vs_player_special_pp = 3


init python in moi_vsgame:
    """
    小游戏系统
    """

    
    def moi_vs_attack_ranselect():
        """
        莫妮卡的攻击策略(?)
        """
        moi_method=renpy.random.randint(0,100)
        #nor_attack=(0,70)
        #special_attack=(71,81)
        if moi_method in range(0,62):
            return "normal"
        elif moi_method in range(63,85):
            return "hard"
        else:
            return "miss"
 

    def moi_vs_attack_nor(p):
        """
        小游戏的平A攻击方法
        IN：
            p - 攻击者(moi/player)

        return - 攻击伤害(不计算暴击和闪避) 
        """

        if p=="player":
            vs_damage=renpy.random.randint(10,30)#伤害
        elif p=="moi":
            vs_damage=renpy.random.randint(25,55)

        vs_final_damage = vs_damage
        
        return vs_final_damage

    def moi_vs_attack_critical():
        """
        小游戏的暴击判定,无输入值
        默认概率=0.2(当>8时暴击)
        return - 暴击值(1/1.5)
        """
        vs_critical=renpy.random.randint(0,9)
        if vs_critical >= 8:
            vs_critical = 1.5
        else:
            vs_critical = 1
        
        return vs_critical
    
    def moi_vs_attack_miss(p):
        """
        小游戏的闪避判定,默认Moi低闪避,player高闪避
        IN  
            p - 被攻击者(moi/player)
        
        return - 是否闪避(是=0/否=1)
        """
        vs_miss=renpy.random.randint(1,10)
        if p=="moi":
            vs_hitpossible = 9
        elif p == "player":
            vs_hitpossible = 8
        
        if vs_miss >= vs_hitpossible:
            vs_miss = 0
        else:
            vs_miss = 1

        return vs_miss


    def moi_vs_attack_special(p):
        """
        莫妮卡蓄力重拳!/玩家的特别攻击方式
        
        IN:
            P - 攻击方(moi/player)
        """


        if p == "moi":
            vs_final_damage=renpy.random.randint(45,100)

        elif p == "player":
            if True:
                sp=renpy.random.randint(1,3)
                if sp == 1:
                    #narrator("[player]使用了Windows CMD!")
                    #narrator("[m_name]被暂停了!")
                    #玩家可以再次攻击()
                    return "skip"
                elif sp == 2:
                    #narrator("[player]使用了游戏内命令行!")
                    vs_final_damage = renpy.random.randint(45,120)
                elif sp == 3:
                    #narrator("[player]使用了恢复药!")
                    player_health += 140
                    return "heal"         
        return vs_final_damage

label moi_vs_game_normanattack_p:
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
return

label moi_vs_game_normanattack_moi:
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

label moi_vs_moi_specialattack:
    "[m_name]发动了{cps=4}...{/cps}"
    m "{size=+15}{cps=4}莫 妮 卡 蓄 力 重 拳 !{/cps}{/size}"
    $ moi_spatk_dmg = moi_vsgame.moi_vs_attack_special(p="moi")
    $ miss = moi_vsgame.moi_vs_attack_miss(p="player")
    $ vs_critical = moi_vsgame.moi_vs_attack_critical()
    $ c_damage = moi_spatk_dmg * vs_critical
    if vs_critical != 1:
        "效果拔群!"
    "[m_name]对[player]造成了[c_damage]点伤害!!"
    if miss == 0:
        "但是[player]躲开了!"
    $ f_damage= c_damage * miss
    $ player_health -= f_damage
    "当前玩家HP:[player_health]"
return

label moi_vs_moi_miss:
    "莫妮卡走神了"
return

label moi_vs_game_specialattack_p:
    $ spatk = moi_vsgame.moi_vs_attack_special(p="player")
    if count == 3:
        "你忘了你的技能没PP了! 你被莫妮卡抓住了机会!"
    jump moi_vs_game_ramdom_moi
    if spatk == "skip":
        "[player]使用了Windows CMD!"
        "[m_name]被暂停了!"
        jump dokimonika_date1_3_vs
    elif spatk == "heal" :
        "[player]使用了圣灵药!!"
        $ rndheal = renpy.random.randint(150,300)
        "[player]恢复了[rndheal]点HP"
        $ player_health += rndheal
    else:
        "[player]使用了游戏控制台!!"
        call updateconsole(text="os.chmod(monika.chr,stats.S_IREAD)",history="Fail")
        with Pause(2)
        call hideconsole
        "[player]造成了[spatk]点伤害!!"
        $ moi_health -= spatk
return
    

label moi_vs_game_ramdom_moi:
    $ rndselect = moi_vsgame.moi_vs_attack_ranselect()
    if rndselect == "normal":
        call moi_vs_game_normanattack_moi
    elif rndselect == "hard":
        call moi_vs_moi_specialattack
    elif rndselect == "miss":
        call moi_vs_moi_miss
    else:
        m "..."
return

    
#"""
#    def vs_mistakeing(reason):
#    #你走神了!（选择了非攻击/防御选择项)
#    #reason：
#    if reason==vs_select_health
#        renpy.say("[player]沉迷于看血条被[m_name]抓住了机会!")
#"""


        
        
        
        
        
        
            