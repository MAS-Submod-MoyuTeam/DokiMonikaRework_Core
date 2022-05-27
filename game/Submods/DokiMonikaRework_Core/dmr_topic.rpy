init 999 python:
    # 是否安装了自动换装子模组
    dmr_AOCenable = mas_submod_utils.isSubmodInstalled('Auto Outfit Change')

# 约会主体执行代码
label dmr_datemain:
    python:
        dmr_setDefData(dmr_global.Id)
        renpy.call(dmr_global.pre_StartLabel)
        renpy.call(dmr_global.StartLabel)
        renpy.call(dmr_global.pre_EndLabel)
        renpy.call(dmr_global.EndLabel)
        dmr_saveDateData()
        play_song(persistent.current_track, fadein = 1, fadeout = 1)

