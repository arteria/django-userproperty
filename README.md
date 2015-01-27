# [django-userproperty](https://github.com/arteria/django-userproperty)

[django-userproperty](https://github.com/arteria/django-userproperty) is a pluggable/reusable Django app that manages per user and global properties. In addition,
[django-userproperty](https://github.com/arteria/django-userproperty) provides helper functions to set, get, incerement and decrement these properties.



## Installation

Install the package:

    pip install django-userproperty

Add the app in you settings.py:

    INSTALLED_APPS = (
        'userproperty',
    )

Update your root urls.py file:

    ...
    url(r'^properties/', include('userproperty.urls')),
    ...


And finally sync your db

    python manage.py syncdb

## Usage

### API for asynchronous Usage

This app is designed to be used with JavaScript/jQuery and asynchronous requests. It provides so besic API interfaces to get and set Properties

#### `get-uproperty`

> logged-in user is required

**name**: name of the user-property
default: default value, will be retuned if user-property not found

    $.get("/get-uproperty/?name=<name>&default=<value>", function(data) {
            alert(data);
        });

response:

    {"status": "success", "number-of-items": "50"} // or 100 if the property number-of-items was not found

#### `set-uproperty`

> logged-in user is required

**name**: name of the user-property
**value**: value of the user-property to set

    $.get("/set-uproperty/?name=<name>&value=<value>", function(data) {
        alert(data);
    });

response:

    {"status": "success", "number-of-items": "100"}

#### `get-gproperty`

> staff member is required

**name**: name of the global-property
default: default value, will be retuned if global-property not found

        $.get("/get-gproperty/?name=<name>&default=<value>", function(data) {
            alert(data);
        });

response:

    {"status": "success", "number-of-items": "50"}

#### `set-gproperty` - staff member is required

> staff member is required

**name**: name of the global-property
**value**: value of the global-property to set

    $.get("/set-gproperty/?name=<name>&value=<value>", function(data) {
        alert(data);
    });

returns

    {"status": "success", "number-of-items": "100"}


### More examples:

After creating an account on your website, the user needs to do some tasks before he can enter his profile. In this example adding more information and agreeing to the terms and conditions.

When creating the new user you create a new property:

    from userproperty.utils import addProperty

    addProperty(request, tag='setup')
    # if the user is not saved in the request add: anUser=yourNewUser

In your login view you can now have different outcomes based on the UserProperty

    from userproperty.utils import getIntegerProperty, setIntegerProperty, removeProperty

    #in your login view

    setupProperty = getIntegerProperty(request,'setup')

    if setupProperty == 1:
        #redirect, a form for adding phone number etc
    elif setupProperty == 2:
        #redirect, accepting the terms and conditions
    elif setupProperty:
        removeProperty(request, tag='setup')

    # stuff when no property was set

The only thing left to do is setting the property to a new value when the respective actions(forms in this case) are done:

    from userproperty.utils import setIntegerProperty, removeProperty

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

Other examples: setup tour, saving user specific properties(number of data entries displayed in js datatables), etc.

## PEP8

The functions are available in pep8 (lowercase with _ as separator between words)

setIntegerProperty() ==> set_integer_property()
