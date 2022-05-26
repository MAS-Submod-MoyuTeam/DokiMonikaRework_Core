init -985 python in dmr_global:
    Id = ""
    Name = ""
    pre_StartLabel = ""
    StartLabel = ""
    pre_EndLabel = ""
    EndLabel = ""

init -5 python:
    def dmr_loadDateInfo(Id):
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