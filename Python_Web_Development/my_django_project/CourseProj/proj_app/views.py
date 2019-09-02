from django.shortcuts import render
from django.db.models import Q
from proj_app.models import Topic,WebPage,AccessRecord
from proj_app import forms
# Create your views here.
def index(request):
    webpage_list= AccessRecord.objects.order_by('date')
    date_dict={'access_records': webpage_list}
    return render (request,"proj_app/INDEX.html",context=date_dict)

def HomePage(request):
    return render(request,'proj_app/homepage.html')

def form_name_view(request):
    form = forms.FormX()
    if request.method == "POST":
        form = forms.FormX(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("NAME:", form.cleaned_data['name'])
            print("EMAIL:", form.cleaned_data['email'])
            print("TEXT:", form.cleaned_data['text'])
    return render(request,'proj_app/forms.html',{"form":form})

# Search Code
def searchAccess(request):

    keywords=''

    if request.method=='POST': # form was submitted

        keywords = request.POST.get("keywords", "") # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('name__name','date') # change accordingly
        for keyword in keywords.split(' '): # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        accesses = AccessRecord.objects.filter(all_queries).distinct()
        context = {'accesses':accesses}
        return render(request, 'proj_app/search.html', context)

    else: # no data submitted

        context = {}
        return render(request, 'proj_app/index.html', context)

def searchWebPage(request):

    keywords=''

    if request.method=='POST': # form was submitted

        keywords = request.POST.get("webpage", "") # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('topic__top_name','name','url') # change accordingly
        for keyword in keywords.split(' '): # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        pages= WebPage.objects.filter(all_queries).distinct()
        context = {'pages':pages}
        return render(request, 'proj_app/search.html', context)

    else: # no data submitted

        context = {}
        return render(request, 'proj_app/index.html', context)
