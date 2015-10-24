# coding: utf-8
from django.contrib.auth.decorators import login_required


@login_required
def create_comment(request):
    pass


@login_required
def comment_list(request):
    pass
