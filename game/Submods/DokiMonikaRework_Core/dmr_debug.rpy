define dmr_debug = True

init 999 python:
    if dmr_debug:
        renpy.config.developer = True
        renpy.config.debug = True

init 5 python:
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

label dmr_testDateTopic:
    $ dmr_loadDateInfo('dmr_testDoki')
    call dmr_datemain
    return

label dmr_raiseError:
    $ raise Exception('Error')

