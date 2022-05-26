init -1 python:
    dmr_empty = MASBackground(
        "dmr_empty",
        "dmr empty",
        "dmr_empty1",
        "dmr_empty1",
        hide_calendar=True,
        hide_masks=True,
        disable_progressive=True,
        unlocked=False
    )
image dmr_empty1 = "Submods/DokiMonikaRework_Core/assets/empty.png"

    #$ bg_change_info_moi = mas_changeBackground(dmr_empty, by_user=None, set_persistent=False,)
    #call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=dmr_empty, force_exp=None)