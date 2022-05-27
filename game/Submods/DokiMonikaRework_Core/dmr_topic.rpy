

label dmr_datemain:
    python:
        dmr_setDefData(dmr_global.Id)
        renpy.call(dmr_global.pre_StartLabel)
        renpy.call(dmr_global.StartLabel)
        renpy.call(dmr_global.pre_EndLabel)
        renpy.call(dmr_global.EndLabel)

