import os


def reloadPresets(folderPath=None):
    presetsPath = os.path.join(os.path.dirname(
        os.path.split(os.path.abspath(__file__))[0]), "aq_bones_snap/")
    global presetList
    presetList = []
    if folderPath is None:
        relPathStart = os.path.join(presetsPath, "bone_name_list")
    else:
        relPathStart = os.path.join(presetsPath, folderPath, "bone_name_list")
    if os.path.exists(relPathStart):
        for entry in os.scandir(relPathStart):
            if entry.name.endswith(".py") and entry.is_file():
                presetList.append((os.path.relpath(os.path.join(
                    relPathStart, entry), start=presetsPath), os.path.splitext(entry.name)[0], ""))
    return presetList
