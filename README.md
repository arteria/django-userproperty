#Django-UserProperty

Dajngo-UserProperty gives you the possibility to save values to a in relation to a user. There are endless possibilities for use cases.

## Installation

Install the package:

    pip install django-userproperty
    
Add the app in you settings.py:

    INSTALLED_APPS = (
        'django-userproperty',
    )

## Usage

### Example: 

Other examples: setup tour, saving user specific properties(number of data entries displayed in js datatables), etc.

After creating an account on your website, the user need to do some tasks before the can go to his profile. In this example adding more information to his profile.

When creating the new user you create a new property:

    from django_userproperty.utils import addProperty
    
    addProperty(request, tag='setup') 
    # if the user is not saved in the request add: anUser=yourNewUser
    
In your login view you can now have different outcomes based on the UserProperty

    from django_userproperty.utils import getIntegerProperty, setIntegerProperty, removeProperty

    #in your login view
    
    setupProperty = getIntegerProperty('setup')
    
    if setupProperty:
        if setupProperty is 1:
            #redirect, a form for adding phone number etc
        elif setupProperty is 2:
            #redirect, acceppting the terms and conditions
        else:
            removeProperty(request, tag='setup')
    
    # stuff when no property was set
    
The only thing left to do is setting the property to a new value when the respective actions(form in this case) are done:

    from django_userproperty.utils import setIntegerProperty, removeProperty

    #in the view with the form for the phonenumer etc.
    form.is_valid():
        #do stuff
        
        setIntegerProperty(request, tag='setup', value=2)
        
        #redirect login
        
        
    #in the view for terms and conditions
    form.is_valid():
        #do stuff
        
        removeProperty(request, tag='setup')
        
        #redirect login
