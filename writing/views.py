from django.shortcuts import render
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

def writing_post(request):
    pass