# coding: utf-8
from django.contrib.auth.decorators import login_required

from article.models import Article
from models import Comment
from utils.response import json_response


@login_required
def create_comment(request):
    article_id = int(request.POST["article_id"])
    to_comment_id = int(request.POST["to_comment_id"])
    content = request.POST["content"].strip()

    article = Article.objects.get(id=article_id)
    comment = Comment(block=article.block, article=article,
                      owner=request.user, to_comment_id=to_comment_id,
                      content=content)
    comment.save()
    return json_response({})


@login_required
def comment_list(request):
    pass
