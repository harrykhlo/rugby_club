import uuid


def getID():
    return uuid.uuid4().fields[1]


print(getID())
