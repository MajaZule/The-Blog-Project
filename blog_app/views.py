from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.utils import timezone
from blog_app.models import Post, Comment
from blog_app.forms import CommentForm
from django.http import HttpResponse

def dummy(request, pk):
    return HttpResponse("hello" + str(pk))

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        x = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
        print(x)
        return x


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def add_comment(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'post':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.post = post
            comment.published_date = timezone.now
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog_app/comment_form.html')
