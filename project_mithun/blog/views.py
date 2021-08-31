from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views import View

from .models import Post


def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {"post": data})
    # return JsonResponse(data, safe=False)


class BlogAddition(View):
    """
    Description about my API
    """

    def get(self, request):
        """
        This is get method override
        """
        return render(request, 'add.html')

    def post(self, request):
        """
        This is post method override
        """
        form_data = request.POST
        if 'title' in form_data:
            title = form_data['title']
        if 'content' in form_data:
            content = form_data['content']
        if 'slug' in form_data:
            slug = form_data['slug']
        if 'image' in form_data:
            image = form_data['image']

        try:
            Post.objects.create(title=title, content=content,
                                slug=slug, image=image)
            # Post.objects.filter(title=title).delete()
        except Exception as e:
            print(e)

        return HttpResponseRedirect('/')
