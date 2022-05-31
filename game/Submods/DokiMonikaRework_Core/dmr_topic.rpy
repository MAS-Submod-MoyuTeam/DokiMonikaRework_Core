init 999 python:
    # 是否安装了自动换装子模组
    dmr_AOCenable = mas_submod_utils.isSubmodInstalled('Auto Outfit Change')

# 约会主体执行代码
label dmr_datemain:
    python:
        dmr_setDefData(dmr_global.Id)
        renpy.call(dmr_global.pre_StartLabel)
    # 切换至空房间
    $ bg_change_info_moi = mas_changeBackground(dmr_empty, by_user=None, set_persistent=False)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    python:
        renpy.call(dmr_global.StartLabel)
        renpy.call(dmr_global.pre_EndLabel)
    # 切回原房间
    $ bg_change_info_moi = mas_changeBackground(mas_background_def, set_persistent=False)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    python:
        renpy.call(dmr_global.EndLabel)
        dmr_saveDateData()
        dmr_unloadDateInfo()
        play_song(persistent.current_track, fadein = 1.3, fadeout = 1.3)

