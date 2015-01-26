#!/usr/bin/env python
# -*- coding: utf-8 -*-

from userproperty.models import UserProperty, GlobalProperty


def setIntegerProperty(request, name="", value=0, anUser=None):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser

        try:
            un = UserProperty.objects.get(user=theUser, name=name)
            un.value = value
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, name=name, value=value)
        un.save()
        return True
    except:
        pass
    return False


def getIntegerProperty(request, name="", value=0, anUser=None):
    """
    """
    if anUser is None:
        theUser = request.user
    else:
        theUser = anUser

    try:
        un = UserProperty.objects.get(user=theUser, name=name)
        value = un.value
        return value
    except UserProperty.DoesNotExist:
        return value
    return None


def addProperty(request, name="", anUser=None):
    """Add a notification for a user.
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, name=name)
            un.value = 1
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, name=name, value=1)
        un.save()
        return True
    except:
        return False


def removeProperty(request, name="", anUser=None):
    """
    Remove a notification for a user.
    """
    if anUser is None:
        theUser = request.user
    else:
        theUser = anUser
    try:
        un = UserProperty.objects.get(user=theUser, name=name)
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


def getProperty(request, name="", anUser=None):
    """Returns True if the user has this property set.
    """
    try:
        if anUser is None:
            un = UserProperty.objects.get(user=request.user, name=name)
        else:
            un = UserProperty.objects.get(user=anUser, name=name)
        return bool(un.value)
    except UserProperty.DoesNotExist:
        pass
    return False


def getUsersWithProperty(name=""):
    """Returns a list of Users having a Property
    """
    ans = []
    for u in UserProperty.objects.filter(name=name):
        ans.append(u.user)
    return ans


def incUserProperty(request, name="", anUser=None, incrementBy=1):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, name=name)
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, name=name, value=0)
        un.value += incrementBy
        un.save()
        return True
    except:
        return True


def decUserProperty(request, name="", anUser=None, decrementBy=1):
    """
    """
    try:
        if anUser is None:
            theUser = request.user
        else:
            theUser = anUser
        try:
            un = UserProperty.objects.get(user=theUser, name=name)
        except UserProperty.DoesNotExist:
            un = UserProperty(user=theUser, name=name, value=0)
        if un.value < 1:
            pass
        else:
            un.value -= decrementBy
            un.save()
        return True
    except:
        return True


### Global Property ###

def setGlobalProperty(name="", value=0):
    """
    """
    try:
        try:
            un = GlobalProperty.objects.get(name=name)
            un.value = value
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(name=name, value=value)
        un.save()
        return True
    except:
        return False


def getGlobalProperty(name="", value=0):
    """Returns True if this Property is set.
    """
    try:
        prop = GlobalProperty.objects.get(name=name)
        return bool(prop.value)
    except GlobalProperty.DoesNotExist:
        pass
    return False


def getIntegerGlobalProperty(name=""):
    """Returns Integer Value if this Property is set, else 0
    """
    try:
        prop = GlobalProperty.objects.get(name=name)
        return prop.value
    except GlobalProperty.DoesNotExist:
        pass
    return 0


def incGlobalProperty(name="", incrementBy=1):
    """Increments value Field by given value, creates Property if DoesNotExist
    """
    try:
        try:
            un = GlobalProperty.objects.get(name=name)
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(name=name, value=0)

        un.value += incrementBy
        un.save()
        return True
    except:
        return False


def decGlobalProperty(name="", decrementBy=1):
    """Decrements value Field by given value, creates Property if DoesNotExist
    """
    try:
        try:
            un = GlobalProperty.objects.get(name=name)
        except GlobalProperty.DoesNotExist:
            un = GlobalProperty(name=name, value=0)
        if un.value < 1:
            pass
        else:
            un.value -= decrementBy
            un.save()
        return True
    except:
        return False


# PEP8 #

### UserProperty ###

set_integer_property = setIntegerProperty
get_integer_property = getIntegerProperty
add_property = addProperty
remove_property = removeProperty
get_all_properties = getAllProperties
drop_all_properties_for_user = dropAllPropertiesForUser
get_property = getProperty
get_users_with_property = getUsersWithProperty
inc_user_property = incUserProperty
dec_user_property = decUserProperty

### Global Property ###

set_global_property = setGlobalProperty
get_global_property = getGlobalProperty
get_integer_global_property = getIntegerGlobalProperty
inc_global_property = incGlobalProperty
dec_global_property = decGlobalProperty
