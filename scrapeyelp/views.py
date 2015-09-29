from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import Reviews, Urls
from .forms import PostForm, GetUrl
import urllib
from bs4 import BeautifulSoup


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
            NewUrl = Geturl.save(commit=False)
            #NewUrl.save()
            OldUrl=NewUrl.url
            html = urllib.urlopen(OldUrl).read()
            soup = BeautifulSoup(html,'html.parser')
            #Find company name
            #Generate company ID by company name using bijective funcion
            #title = soup.find('h1',itemprop="name",text=True)
            ALPHABET=list("/_-.wtp=abcdefghijklmnoqrsuvxyz?0123456789:")
            i = 0
            base = len(ALPHABET)
            for char in NewUrl.url:
                i =  i + ALPHABET.index(char)
            #Get number of reviews
            NumberofReviews=soup.find('span',attrs={"itemprop":"reviewCount"}).getText()
            scrapingTimmes = int(NumberofReviews)/40
            #Get username rating and reviews and write to the database
            for next in range(0,scrapingTimmes+1):
            	url=OldUrl+"?start="+str(next*40)
            	html = urllib.urlopen(url).read()
            	soup = BeautifulSoup(html,"html.parser")
            	authors = soup.find_all(attrs={"itemprop":"author"})
            	rating = soup.find_all(attrs={"itemprop":"ratingValue"})
            	review = soup.find_all('p',{"itemprop":"description"})
            	for x in range(0,len(review)):
            		quarry=Reviews.objects.create(username=authors[x]['content'], rating=rating[x+1]['content'], note=review[x].getText(),companyid=i , sourceid='1')
            		quarry.save()
            #return render(request, 'reviews_list.html', {'reviews': reviews})
            return redirect('scrapeyelp.views.reviews_list')
    else:
        Geturl = GetUrl()
    return render(request, 'Get_url.html', {'Geturl': Geturl})