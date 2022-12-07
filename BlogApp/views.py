from django.shortcuts import render,get_object_or_404,redirect
from BlogApp.models import Post
from django.core.mail import send_mail
from BlogApp.forms import EmailSendForm,PostForms
from django.contrib.auth.decorators import login_required
#from BlogApp.models import Employee

#from BlogApp.forms import EmployeeForm


# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all();
    return render(request, 'BlogApp/post_list.html', {"post_list":post_list})

def post_detail_view(request, year,month,day,post):
    post=get_object_or_404(Post,slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day);
    return render(request, "BlogApp/post_detail.html", {'post':post})


#post-list-view with paginator-codes...
#post-list-view with paginator-codes...
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from BlogApp.models import Post
from taggit.models import Tag
# Create your views here.
def post_list_view(request,tag_slug=None):
    #print("post_list_view with paginator")
    post_list=Post.objects.all()
    for post in post_list:
        print(post.image.name)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator=Paginator(post_list,2)            #no.of.pages(20/2-rec=>10-pages)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request, 'BlogApp/post_list.html', {"post_list":post_list, 'tag':tag})


#Listview with pagination
from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=1


from django.core.mail import send_mail
def send(request):
    print(send_mail('Hell0 frnd', 'enjoy pandogoyyyyy....','venkatchouhan01@gmail.com',['venkateshajmira007@gmail.com']))

from django.core.mail import send_mail
from BlogApp.forms import EmailSendForm,CommentForm
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id, status='published')
    sent=False
    form = EmailSendForm()
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = '{}({}) recommends you to read "{}"'.format(cd['name'], cd['email'], post.title)

            message = "Read Post At: \n{}\n\n{} Comments:\n{}".format(post_url, cd['name'], cd['comments'])

            send_mail(subject, message, 'venkatchouhan01@gmail.com', [cd['to']])  # use[]

            sent = True;

        else:
            form = EmailSendForm()
    return render(request, 'BlogApp/sharebymail.html', {'post': post, 'form': form, 'sent': sent})

def bs_smaple_view(request):
    return render(request, "BlogApp/Sample.html")


# comment form-view
from BlogApp.models import Comment
from BlogApp.forms import CommentForm
from django.db.models import Count

def post_detail_view(request, year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                status='published',
                publish__year=year,
                publish__month=month,
                publish__day=day)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]

    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request, 'BlogApp/post_detail.html', {"post":post, 'form':form, 'comments':comments, 'csubmit':csubmit, 'similar_posts':similar_posts, })


def post_view(request):
    return render(request, 'BlogApp/post_view.html');

def logout(request):
    request.session.clear()
    return render(request, 'BlogApp/logout.html')


from BlogApp.forms import SignupForm
from django.http import HttpResponseRedirect


def Signup_view(request):
    form= SignupForm()
    if request.method== "POST":
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'BlogApp/signup.html', {'form':form})


from BlogApp.forms import PostForms

def post_form(request):
    form = PostForms()
    print("hello")
    if request.method=='POST':
        form=PostForms(request.POST,request.FILES)
        if form.is_valid():
            print("verify")
            user = form.save(commit=True)
            return HttpResponseRedirect('/thankyou/')
    return render(request, 'BlogApp/postmain.html', {'form':form})

def homepage(request):

    return render(request, 'BlogApp/homepage.html')

def thankyou(request):
    return render(request, 'BlogApp/thankyou.html')

from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView,CreateView,DetailView

'''
class commentdelview(DeleteView):
    model = Comment
    success_url = reverse_lazy('succ')
'''

def succview(request):
    return render(request, 'BlogApp/delete.html')


class postdeleteview(DeleteView):
    model = Post
    success_url = reverse_lazy('postsucc')


def postsuccview(request):
    return render(request, 'BlogApp/delete.html')


class  postupdateview(UpdateView):
    model = Post
    fields =('title','slug','author','body','image')












