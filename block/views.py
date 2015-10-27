from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Block
from message.models import UserMessage


# Create your views here.
def block_list(request):
    if request.user.is_authenticated():
        msg_cnt = UserMessage.objects.filter(owner=request.user, status=0).count()
    else:
        msg_cnt = 0
    blocks = Block.objects.all().order_by("-id")
    return render_to_response("block_list.html", {"blocks": blocks, "msg_cnt": msg_cnt},
                              context_instance=RequestContext(request))
