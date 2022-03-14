from django.shortcuts import render

# Create your views here.
def about_page(request):
    diction={
        'title':'About',
        'text':'This is About page'
    }
    return render(request, 'About/about_page.html', context=diction)