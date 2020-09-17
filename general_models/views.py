from django.shortcuts import render, get_object_or_404

from .models import GeneralModel

def general_detail(request, post_slug):
    post = get_object_or_404(GeneralModel, slug=post_slug)

    context = {
        'post': post
    }

    return render(request, 'general_post_detail.html', context)
