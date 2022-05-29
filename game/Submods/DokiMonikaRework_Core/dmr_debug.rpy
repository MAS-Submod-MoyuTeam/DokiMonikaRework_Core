define dmr_debug = True


init 999 python:
    if dmr_debug:
        renpy.config.developer = True
        renpy.config.debug = True

init 5 python:
    if dmr_debug:
        addEvent(
                Event(
                    persistent.event_database,          
                    eventlabel="dmr_testDateTopic",        
                    pool=True,
                    unlocked=True
                )
            )
        addEvent(
                Event(
                    persistent.event_database,          
                    eventlabel="dmr_raiseError",        
                    pool=True,
                    unlocked=True
                )
            )   
        addEvent(
                Event(
                    persistent.event_database,          
                    eventlabel="dmr_showAllDateList",        
                    pool=True,
                    unlocked=True
                )
            )   


label dmr_testDateTopic:
    $ dmr_loadDateInfo('dmr_testDoki')
    call dmr_datemain.
    return

label dmr_raiseError:
    $ raise Exception('Error')
    return

label dmr_showAllDateList:
    $ alldatelist = dmr_enableDateList()
    call screen dmr_datelist_menu(alldatelist)
    "[_return]"
    return
