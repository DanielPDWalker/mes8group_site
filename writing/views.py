from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from general_models.models import GeneralModel


def writing_home(request):
    writing_posts = GeneralModel.objects.order_by('-publish_date').filter(is_published=True, category='writing')

    paginator = Paginator(writing_posts, 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Writing',
        'posts': paged_posts
    }

    return render(request, 'writing/writing.html', context)

def writing_post_detail(request, post_slug):
    post = get_object_or_404(GeneralModel, slug=post_slug)

    context = {
        'post': post
    }

    return render(request, 'general_post_detail.html', context)
