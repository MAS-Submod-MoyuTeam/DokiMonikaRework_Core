#是否允许约会,默认为False
default persistent._submod_moi_allow_date = False
#默认约会状态:False
default persistent._submod_moi_dating_mode = False
#检测是否中途退出
default persistent._submod_moi_dating_quit_detect_saved = 0
default persistent._submod_moi_dating_quit_detect = renpy.random.randint(0,500000)
 
init python:
    persistent._submod_moi_dating_quit_detect= renpy.random.randint(0,500000)
    if ((persistent._submod_moi_dating_quit_detect_saved != persistent._submod_moi_dating_quit_detect) and persistent._submod_moi_dating_mode):
        persistent._submod_moi_dating_mode = False #如果中途退出了,则为False
        #这里应该推送中途离开的对话.

    def moi_no_aac_weather_exprop_get(indoor):
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

    def moi_getClothesExpropForTemperature(indoor=True):
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
            
