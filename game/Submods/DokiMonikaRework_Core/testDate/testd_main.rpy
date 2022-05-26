init -900 python:
    # 声明本次约会的变量
    # 变量名字必须改变
    testDoki = {
        # 约会事件id 唯一
        'Id':'dmr_testDoki',
        # 名称
        'Name':'testDoki',
        # 推送条件 python表达式
        'Conditional':None,
        # 约会开始之前的label(从默认房间跳转到约会场景)
        # 不要包含call/jump语句
        'pre_StartLabel':'dmr_doki_test',
        # 约会开始label
        # 在这里随意跳转label
        'StartLabel':'dmr_start_label_test',
        # 约会结束之前label
        # 类似于pre_StartLabel
        # 不要包含call/jump语句
        'pre_EndLabel':'dmr_def_pEL_test',
        # 约会结束label
        # 回到太空教室后的对话
        'EndLabel':'dmr_EndLabel_test'
    }

    # 添加到可用的约会列表
    dmr_DateList.append(testDoki)

image 9nine_ev103d = "Submods/DokiMonikaRework_Core/assets/ev103d.png"
label dmr_doki_test:
    "首先, 无论如何都避免使用jump, 使用jump可能导致逻辑卡死"
    "这里是pre_StartLabel, 主要用来从当前房间过渡到新的房间"
    "不建议使用任何call语句"
    # 这两行代码是必须的 切换至MAS空房间, 用于场景切换
    $ bg_change_info_moi = mas_changeBackground(dmr_empty, by_user=None, set_persistent=False)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    # 约会场景 
    show 9nine_ev103d with Fade(0.5,2,0.5,color="#000000")


label dmr_start_label_test:
    "这里是StartLabel, 标志着约会的开始"
    "请记住, 你可以使用call, 但千万不能使用jump"

label dmr_def_pEL_test:
    "这里是pre_EndLabel, 类似于pre_StartLabel, 同样用作场景转换"
    "同样的, 不建议使用任何跳转语句"
    # 隐藏约会场景
    hide 9nine_ev103d with Fade(0.5,2,0.5,color="#000000")
    # 必要代码
    $ bg_change_info_moi = mas_changeBackground(spaceroom, by_user=None, set_persistent=False,)
    call spaceroom(scene_change=None, dissolve_all=True, bg_change_info=bg_change_info_moi, force_exp=None)
    call spaceroom()

label dmr_EndLabel_test:
    "这里是EndLabel"
    "一般来说, 执行这个label说明你已经回到太空教室了"
