from django.shortcuts import render_to_response
from django.template import RequestContext

from usercenter.models import UserProfile
from message.models import UserMessage
from models import Block


# Create your views here.
def block_list(request):
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(owner=request.user, status=0).count()
        user_avatar = UserProfile.objects.get(owner=request.user).avatar
    else:
        msg_cnt = 0
        user_avatar = ""
    blocks = Block.objects.all().order_by("-id")
    return render_to_response("block_list.html",
                              {"blocks": blocks, "msg_cnt": msg_cnt, "user_avatar": user_avatar},
                              context_instance=RequestContext(request))
