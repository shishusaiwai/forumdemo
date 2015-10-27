# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from block.models import Block
from comment.models import Comment
from models import Article
from utils.paginator import paginate_queryset


def article_list(request, block_id):
    block_id = int(block_id)
    page_no = int(request.GET.get("page_no", "1"))
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block, status__gte=0).order_by("-last_update_timestamp")

    object_list, pagination_data = paginate_queryset(articles, page_no, cnt_per_page=1)
    return render_to_response("article_list.html",
                              {"articles": object_list, "b": block, "pagination": pagination_data},
                              context_instance=RequestContext(request))


@login_required
def create_article(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render_to_response("article_create.html", {"b": block},
                                  context_instance=RequestContext(request))
    else:  # request.method == "POST"
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u'标题和内容均不能为空')
            return render_to_response("article_create.html",
                                      {"b": block, "title": title, "content": content},
                                      context_instance=RequestContext(request))
        new_article = Article(block=block, owner=request.user, title=title, content=content)
        new_article.save()
        messages.add_message(request, messages.INFO, u'成功发布文章.')
        return redirect(reverse("article_list", args=[block.id]))


def article_detail(request, article_id):
    page_no = int(request.GET.get("comment_page_no", "1"))
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article, status=0)
    comments, pagination_data = paginate_queryset(comments, page_no, cnt_per_page=3)
    return render_to_response("article_detail.html", {"article": article,
                              "comments": comments, "pagination": pagination_data},
                              context_instance=RequestContext(request))
