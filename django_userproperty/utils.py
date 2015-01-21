from .models import UserProperty, GlobalProperty


### UserProperty ###

def setIntegerProperty(request, tag="", value=0, anUser=None):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser

        try:
            un = UserProperty.objects.get(user=theUser, tag=tag)
            un.switch = value
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, tag=tag, switch=value)
        un.save()
        return True
    except:
        pass
    return False


def getIntegerProperty(request, tag="", value=0, anUser=None):
    """
    """
    if anUser is None:
        theUser = request.user
    else:
        theUser = anUser

    try:
        un = UserProperty.objects.get(user=theUser, tag=tag)
        value = un.switch
        return value
    except UserProperty.DoesNotExist:
        return value
    return None


def addProperty(request, tag="", anUser=None):
    """Add a notification for a user.
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, tag=tag)
            un.switch = 1
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, tag=tag, switch=1)
        un.save()
        return True
    except:
        return False


def removeProperty(request, tag="", anUser=None):
    """
    Remove a notification for a user.
    """
    if anUser is None:
        theUser = request.user
    else:
        theUser = anUser
    try:
        un = UserProperty.objects.get(user=theUser, tag=tag)
        un.delete()
    except UserProperty.DoesNotExist:
        pass


def getAllProperties(request):
    """
    """
    try:
        un = UserProperty.objects.filter(user=request.user)
        return un
    except UserProperty.DoesNotExist:
        pass
    return None


def dropAllPropertiesForUser(anUser=None):
    """Removes all properties for the given user... is used to remove ghosts.
    """
    UserProperty.objects.filter(user=anUser).delete()


def getProperty(request, tag="", anUser=None):
    """Returns True if the user has this property set.
    """
    try:
        if anUser is None:
            un = UserProperty.objects.get(user=request.user, tag=tag)
        else:
            un = UserProperty.objects.get(user=anUser, tag=tag)
        return bool(un.switch)
    except UserProperty.DoesNotExist:
        pass
    return False


def getUsersWithProperty(tag=""):
    """Returns a list of Users having a Property
    """
    ans = []
    for u in UserProperty.objects.filter(tag=tag):
        ans.append(u.user)
    return ans


def incUserProperty(request, tag="", anUser=None, incrementBy=1):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, tag=tag)
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, tag=tag, switch=0)
        un.switch += incrementBy
        un.save()
        return True
    except:
        return True


def decUserProperty(request, tag="", anUser=None, decrementBy=1):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, tag=tag)
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, tag=tag, switch=0)
        if un.switch < 1:
            pass
        else:
            un.switch -= decrementBy
            un.save()
        return True
    except:
        return True


### Global Property ###

def setGlobalProperty(tag="", value=0):
    """
    """
    try:
        try:
            un = GlobalProperty.objects.get(tag=tag)
            un.switch = value
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(tag=tag, switch=value)
        un.save()
        return True
    except:
        return False


def getGlobalProperty(tag="", value=0):
    """Returns True if this Property is set.
    """
    try:
        prop = GlobalProperty.objects.get(tag=tag)
        return bool(prop.switch)
    except GlobalProperty.DoesNotExist:
        pass
    return False


def getIntegerGlobalProperty(tag=""):
    """Returns Integer Value if this Property is set, else 0
    """
    try:
        prop = GlobalProperty.objects.get(tag=tag)
        return prop.switch
    except GlobalProperty.DoesNotExist:
        pass
    return 0


def incGlobalProperty(tag="", incrementBy=1):
    """Increments switch Field by given value, creates Property if DoesNotExist
    """
    try:
        try:
            un = GlobalProperty.objects.get(tag=tag)
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(tag=tag, switch=0)

        un.switch += incrementBy
        un.save()
        return True
    except:
        return False


def decGlobalProperty(tag="", decrementBy=1):
    """Decrements switch Field by given value, creates Property if DoesNotExist
    """
    try:
        try:
            un = GlobalProperty.objects.get(tag=tag)
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(tag=tag, switch=0)
        if un.switch < 1:
            pass
        else:
            un.switch -= decrementBy
            un.save()
        return True
    except:
        return False
