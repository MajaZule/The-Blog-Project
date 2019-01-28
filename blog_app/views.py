from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView, View
from django.utils import timezone
from blog_app.models import Post, Comment, Gallery
from blog_app.forms import CommentForm
from django.http import HttpResponse



class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.filter(post=self.kwargs['pk'])
        context['form'] = CommentForm()
        return context


class GalleryListView(ListView):
    model = Gallery


def add_comment(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        print("Adding comment to post " + str(pk))
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.post = post
            comment.author = form.cleaned_data['author']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog_app/comment_form.html', {'form':form})
