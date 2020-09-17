from django.shortcuts import render

from general_models.models import GeneralModel


def index(request):
    featured_posts = GeneralModel.objects.order_by(
        'frontpage_feature_slot').filter(
        is_published=True, frontpage_feature_bool=True)

    context = {
        'posts': featured_posts
    }
    return render(request, 'frontpage/index.html', context)
