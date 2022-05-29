init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="DokiMonikaReworkCore",
        description="和莫妮卡进行约会 - 约会系统的核心部分",
        version='0.0.3'
    )
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="DokiMonikaReworkCore",
            user_name="PencilMario",
            repository_name="DokiMonikaRework_Core",
            update_dir="",
            attachment_id=None
        )