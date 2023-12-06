def fractalReader(filePath):
    fracDict = {}
    file = open(filePath)
    for line in file:
        if not line.startswith('#'):
            line = line.lower()
            line = line.replace(" ", "")
            line = line.replace('\n', "")
            lineList = line.split(':')
            if len(lineList) > 1:
                lineList[1] = checkType(lineList[0], lineList[1])
                fracDict[lineList[0]] = lineList[1]
    file.close()
    checkForErrors(fracDict)
    additionalInfo(fracDict)
    return fracDict
def checkType(key, value):
    if key == 'type':
        return safe_convert(value, str)
    elif key == 'centerx':
        return safe_convert(value, float)
    elif key == 'centery':
        return safe_convert(value, float)
    elif key == 'axislength':
        return safe_convert(value, float)
    elif key == 'pixels':
        return safe_convert(value, int)
    elif key == 'iterations':
        return safe_convert(value, int)
    elif key == 'creal':
        return safe_convert(value, float)
    elif key == 'cimag':
        return safe_convert(value, float)
    else:
        return None

def safe_convert(obj, new_type):
    try:
        return new_type(obj)
    except ValueError:
        return None

def checkForErrors(dict):
    mustNeed = ['type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations']
    for param in mustNeed:
        if param not in dict.keys():
            print("entered")
            raise RuntimeError(f"The value of the '{param}' parameter is missing")

    if dict['type'] is None:
        raise RuntimeError("The value of the 'type' is not a string")
    if dict['centerx'] is None:
        raise RuntimeError("The value of the 'centerx' is not a number")
    if dict['centery'] is None:
        raise RuntimeError("The value of the 'centery' is not a number")
    if dict['axislength'] is None:
        raise RuntimeError("The value of the 'axislength' is not a number")
    if dict['pixels'] is None or dict['pixels'] < 0:
        raise RuntimeError("The value of the 'pixels' is not an integer")
    if dict['iterations'] is None or dict['iterations'] < 0:
        raise RuntimeError("The value of the 'iterations' is not an integer")

    if dict['type'] == 'phoenix' or dict['type'] == 'julia' or dict['type'] == 'burningshipjulia':
        if 'creal' not in dict:
            raise RuntimeError(f"This is a {dict['type']} fractal, but 'creal' parameter was not specified")
        if 'cimag' not in dict:
            raise RuntimeError(f"This is a {dict['type']} fractal, but 'cimag' parameter was not specified")

def additionalInfo(dict):
    dict['min'] = {'x': dict['centerx'] - (dict['axislength'] / 2.0), 'y': dict['centery'] - (dict['axislength'] / 2.0)}
    dict['max'] = {'x': dict['centerx'] + (dict['axislength'] / 2.0), 'y': dict['centery'] + (dict['axislength'] / 2.0)}





