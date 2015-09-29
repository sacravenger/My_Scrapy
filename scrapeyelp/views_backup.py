from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Reviews
from .forms import PostForm, GetUrl

def reviews_list(request):
    reviews = get_list_or_404(Reviews)
    return render(request, 'reviews_list.html', {'reviews': reviews})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('scrapeyelp.views.reviews_list')
    else:
        form = PostForm()
    return render(request, 'review_edit.html', {'form': form})

def get_url(request):
    if request.method == "POST":
        Geturl = GetUrl(request.POST)
        if Geturl.is_valid():
            newurl = Geturl.url
            

            return redirect('scrapeyelp.views.reviews_list')
    else:
        Geturl = GetUrl()
    return render(request, 'Get_url.html', {'Geturl': Geturl})