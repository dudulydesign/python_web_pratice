# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from web import views

def index_redirect(request):
    return redirect('/weblogin/')
