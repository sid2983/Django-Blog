from django.shortcuts import render
from .models import Post,User,Room
# from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')


# def about(request):
#     return HttpResponse('<h1> Djblog About</h1>')



# posts = [
#     {
#         'author':'Siddharth Pandey',
#         'title':'Blog Post 1',
#         'content':'First post content',
#         'date_posted':'October 5,2022'
#     },
#     {
#         'author':'Javed Akram',
#         'title':'Blog Post 2',
#         'content':'Second post content',
#         'date_posted':'October 10,2022'
#     },
#     {
#         'author':'Shikhar Pandey',
#         'title':'Blog Post 3',
#         'content':'Third post content',
#         'date_posted':'October 15,2022'
#     }
# ]

# class RoomListView(ListView):
#     model = Room
#     template_name = 'djblog/base.html'
#     context_object_name = 'rooms'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)  
#         return context

class HomeView(TemplateView):
    template_name = 'djblog/home.html'  # Replace with your actual template name
    context_object_name = 'room_posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        default_room = Room.objects.get(pk=1)  # Replace 1 with appropriate ID of default room
        print(default_room)
        # context['default_room'] = default_room
        context['room_posts'] = Post.objects.filter(room=default_room.pk)
        print(context['room_posts'])
        return context


class EditorDetails(ListView):
    model = Room
    template_name = 'djblog/base.html'

class PostByRoomListView(ListView):
    model=Post
    template_name = 'djblog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=2

    def get_queryset(self):
    
        self.current_room_id= self.kwargs['pk']
        return Post.objects.filter(room=self.current_room_id)

    def get_context_data(self, **kwargs):
         
        context = super().get_context_data(**kwargs)
        
        context['current_room'] = Room.objects.get(pk=self.current_room_id)
        return context

# def home(request):
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request, 'djblog/home.html',context)



class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['room','title','content']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['room','title','content']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    




def about(request):
    return render(request, 'djblog/about.html', {'title':'About'})




# def room_authors(request,pk):
#     room_id = request.resolver_match.kwargs.get('pk')
#     authors = User.objects.filter(post__room__id=room_id).distinct()
    
#     print(room_id)
#     print(authors)
#     return render(request,'djblog/editors.html',{'authors': authors})

# def room_authors(request):
#     room_id = request.resolver_match.kwargs.get('pk')
#     authors = User.objects.filter(post__room__id=room_id).distinct()

#     print(room_id)
#     return {'authors': authors}

def newpage(request):
    return render(request,'djblog/new.html')