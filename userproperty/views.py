#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compat import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from userproperty.models import UserProperty, GlobalProperty


@login_required
def get_user_property(request):
    """
    $.get("/get-uproperty/?name=<name>&default=<value>", function(data) {
        alert(data);
    });
    """
    name = request.GET.get('name', None)
    default = request.GET.get('default', None)

    if not name:
        return JsonResponse({
            'status': 'error',
            'message': 'invalid request',
        })

    try:
        uprop = UserProperty.objects.get(name=name, user=request.user)
    except UserProperty.DoesNotExist:
        if default:
            uprop = UserProperty(name=name, user=request.user, value=default)
        else:
            uprop = None

    if uprop:
        return JsonResponse({
            'status': 'success',
            uprop.name: uprop.value,
        })

    return JsonResponse({
        'status': 'error',
        'message': 'property not found',
    })


@login_required
def set_user_property(request):
    """
    $.get("/set-uproperty/?name=<name>&value=<value>", function(data) {
        alert(data);
    });
    """
    name = request.GET.get('name', None)
    value = request.GET.get('value', None)

    if not name or not value:
        return JsonResponse({
            'status': 'error',
            'message': 'invalid request',
        })

    name = request.GET.get('name')
    value = request.GET.get('value')

    uprop, created = UserProperty.objects.get_or_create(name=name, user=request.user)
    uprop.value = value
    uprop.save()

    return JsonResponse({
        'status': 'success',
        uprop.name: uprop.value,
    })


@staff_member_required
def get_global_property(request):
    """
    $.get("/get-gproperty/?name=<name>&default=<value>", function(data) {
        alert(data);
    });
    """
    name = request.GET.get('name', None)
    default = request.GET.get('default', None)

    if not name:
        return JsonResponse({
            'status': 'error',
            'message': 'invalid request',
        })

    try:
        gprop = GlobalProperty.objects.get(name=name)
    except GlobalProperty.DoesNotExist:
        if default:
            gprop = GlobalProperty(name=name, value=default)
        else:
            gprop = None

    if gprop:
        return JsonResponse({
            'status': 'success',
            gprop.name: gprop.value,
        })

    return JsonResponse({
        'status': 'error',
        'message': 'property not found',
    })


@staff_member_required
def set_global_property(request):
    """
    $.get("/set-gproperty/?name=<name>&value=<value>", function(data) {
        alert(data);
    });
    """
    name = request.GET.get('name', None)
    value = request.GET.get('value', None)

    if not name or not value:
        return JsonResponse({
            'status': 'error',
            'message': 'invalid request',
        })

    name = request.GET.get('name')
    value = request.GET.get('value')

    gprop, created = GlobalProperty.objects.get_or_create(name=name, value=value)
    gprop.value = value
    gprop.save()

    return JsonResponse({
        'status': 'success',
        gprop.name: gprop.value,
    })
