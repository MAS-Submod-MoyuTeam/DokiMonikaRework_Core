init -985 python in dmr_global:
    Id = ""
    Name = ""
    pre_StartLabel = ""
    StartLabel = ""
    pre_EndLabel = ""
    EndLabel = ""

init -5 python:
    def dmr_loadDateInfo(Id):
    """
    加载制定的约会信息
    var:
        Id - 约会id
    exception:
        找不到约会Id时引发异常
    """
        for a in dmr_DateList:
            if a['Id'] == Id:
                dmr_global.Id = a['Id']
                dmr_global.Name = a['Name']
                dmr_global.pre_StartLabel = a['pre_StartLabel']
                dmr_global.StartLabel = a['StartLabel']
                dmr_global.pre_EndLabel = a['pre_EndLabel']
                dmr_global.EndLabel = a['EndLabel']
            else:
                raise DateSubmodException('Find Id Fail - 查找约会ID失败')

screen dmr_datelist_menu(items, display_area, scroll_align, nvm_quit):
    style_prefix "scrollable_menu"

    fixed:
        area display_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    for date in items:
                        $ _id = date['Id']
                        $ _showname = date['Name']
                        textbutton [_showname]:
                            xsize display_area[2]
                            action Return(_id)

            textbutton _(nvm_quit) action Return(-1) xsize display_area[2]


        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align
