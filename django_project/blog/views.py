from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # used to redirect user to login page, if tried topost without being logged in, as well that only the user who made the post can edit it
from django.contrib.auth.models import User
from .models import Post #.models means models from same directory
 
 #Dummy data:
posts = [
    {
        'author': 'Ritvik',
        'title': 'First Post',
        'content': 'Hi How are you?',
        'date_posted':  'August 15, 2019'
    },
        {
        'author': 'Jessica',
        'title': " Myths Busted",
        'content': 'Is this actually possible?',
        'date_posted':  'September 12, 2019'
    },
        {
        'author': 'John',
        'title': 'You wont believe this!',
        'content': 'This so true',
        'date_posted':  'December 20, 2019'
    }

]


#handles traffic from home page of blog
#return what the user sees when route is selected 
def home(request):
    context = { # a dictionary of posts and passing it in render allows us to see them
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #default response


class PostListView(ListView): #shows blog posts on home page in a list view
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #to ensure that posts are in reverse chrnological order
    paginate_by = 5 #pagination has limits to 5 posts per page


class UserPostListView(ListView): 
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): #shows blog posts on home page in a list view
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #shows blog posts on home page in a list view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #sets author of post to current logged in user
        return super().form_valid(form) #runs form valid method on parent class


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False                     #whole code only allows user who made post to edit it


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #allows only user who is logged in and created the post to delete the post
    model = Post
    success_url ='/'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title':'About'}) #default response
