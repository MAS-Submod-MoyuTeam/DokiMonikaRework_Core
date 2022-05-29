
init -995 python in dmr_global:
    Id = ""
    Name = ""
    pre_StartLabel = ""
    StartLabel = ""
    pre_EndLabel = ""
    EndLabel = ""

init -5 python:
    def dmr_unloadDateInfo():
        """
        卸载当前约会
        """
        dmr_global.Id = a['Id']
        dmr_global.Name = a['Name']
        dmr_global.pre_StartLabel = a['pre_StartLabel']
        dmr_global.StartLabel = a['StartLabel']
        dmr_global.pre_EndLabel = a['pre_EndLabel']
        dmr_global.EndLabel = a['EndLabel']
        return True
        
    def dmr_loadDateInfo(Id):
        """
        加载指定的约会信息
        var:
            id - 约会id
        """
        for a in dmr_DateList:
            if a['Id'] == Id:
                dmr_global.Id = a['Id']
                dmr_global.Name = a['Name']
                dmr_global.pre_StartLabel = a['pre_StartLabel']
                dmr_global.StartLabel = a['StartLabel']
                dmr_global.pre_EndLabel = a['pre_EndLabel']
                dmr_global.EndLabel = a['EndLabel']
                return True
            else:
                continue
        raise DateSubmodException('Find Id Fail - 查找约会ID失败')

screen dmr_datelist_menu(items, display_area = (835, 40, 440, 528), scroll_align = -0.05, nvm_quit = "算了"):
    #"""
    #展示约会列表
    #var:
    #    items - 约会list (id, name)
    #return:
    #    约会id
    #    当点击'算了'返回-1
    #"""
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
                    for _id, _showname in items:
                        textbutton _showname:
                            xsize display_area[2]
                            action Return(_id)

            textbutton _(nvm_quit) action Return(-1) xsize display_area[2]


        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align

init python:

    def dmr_getShouldDressType(indoor):
        """
        用于获取自动换装所需的衣服种类
        var:
            indoor - 是否在室内
        """

        if mas_isWinter():
            return "sweater" if indoor else "jacket"

        #Likewise summer
        elif mas_isSummer():
            return "home" if indoor else "date"
    
        #Otherwise, we need to do a bit more work
        else:
            #Firstly, let's deal with hemispheres
            if persistent._mas_pm_live_south_hemisphere:
                winter_start = mas_summer_solstice
                winter_end = mas_fall_equinox
            else:
                winter_start = mas_winter_solstice
                winter_end = mas_spring_equinox
    
            if mas_isSpring():
                if datetime.date.today() <= mas_utils.add_months(winter_end, 1):
                    return "sweater" if indoor else "jacket"
                else:
                    return "home" if indoor else "date"
            
            else:
                if datetime.date.today() >= store.mas_utils.add_months(winter_start, -1):
                    return "sweater" if indoor else "jacket"
                else:
                    return "home" if indoor else "date"

    def dmr_getShouldDressTypeWithAAC(indoor=True):
        """
        Gets a clothes exprop for the current temperature if Auto Atmos Change is installed
        Otherwise, we'll use a timeframe to determine

        IN:
            indoor - whether or not this is for indoors or not
            (Default: True)
        """
        TEMP_COLD_MAX = 10
        TEMP_COOL_MAX = 20
        #First, let's see if we have AAC
        if mas_submod_utils.isSubmodInstalled("Auto Atmos Change") and awc_canGetAPIWeath():
            try:
                min_temp = awc_getTemperature(temp="temp_min")

            #Set to None here as this will also be consistent with those who do update AAC, as that _default will be None
            except:
                min_temp = None

            #If we couldn't get the temperature for any reason, we'll fall back to no-aac rules
            if min_temp is None:
                return no_aac_weather_exprop_get(indoor)

            #If the weather is below the cool thresh (cold), we'll opt for a jacket (unless indoors, in which case sweater)
            if min_temp <= TEMP_COLD_MAX:
                return "sweater" if indoor else "jacket"

            #Otherwise, if it's chilly out, we'll have a sweater
            elif TEMP_COLD_MAX < min_temp <= TEMP_COOL_MAX:
                return "sweater"

            else:
                return "home" if indoor else "date"

        else:
            return no_aac_weather_exprop_get(indoor)
            
