from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    # Don't save blank items for every request
    # Code smell: POST test is too long?
    # Display multiple items in the table
    # Support more than one list
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
