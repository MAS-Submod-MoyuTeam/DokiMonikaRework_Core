label dmr_def_pSL:
    $ bg_change_info_moi = mas_changeBackground(dmr_empty, by_user=None, set_persistent=False,)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=dmr_empty, force_exp=None)
    # 约会场景 
    # show moi_sea_park with Fade(0.5,2,0.5,color="#FFF")

label dmr_def_pEL:
    $ bg_change_info_moi = mas_changeBackground(persistent._mas_current_background, by_user=None, set_persistent=False,)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)