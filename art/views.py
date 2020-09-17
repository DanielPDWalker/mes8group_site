from django.shortcuts import render
from django.core.paginator import Paginator

from general_models.models import GeneralModel


def art_home(request):
    art_posts = GeneralModel.objects.order_by('-publish_date').filter(is_published=True, category='art')

    paginator = Paginator(art_posts, 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Art',
        'posts': paged_posts
    }
    return render(request, 'art/art.html', context)

def art_post_detail(request):
    pass
