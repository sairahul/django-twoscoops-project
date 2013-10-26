
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


def home(request):
    params = {}
    return render(request, 'base.html', params)

