from django.http import Http404
from django.shortcuts import redirect

from blog.models import Post


def not_found_handler(request):
    url = request.path

    # if blog is in the url, it searches posts by slug
    # and returns the correct url.
    if 'blog' in url:
        slug = url.rsplit('/')[-2]
        try:
            post = Post.objects.get(slug=slug)
            return redirect(post.get_absolute_url())
        except Post.DoesNotExist:
            raise Http404('Page not found.')

    return redirect('404')
