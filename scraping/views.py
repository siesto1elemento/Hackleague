from django.core.paginator import Paginator
from django.shortcuts import render
from .utils import hackathon_

def hackathon_view(request):
    
    hackathon_data = hackathon_()
    paginator = Paginator(hackathon_data, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    website = 'devfolio'
    context = {'page_obj': page_obj, 'website':website}
    return render(request, 'home.html', context)

# def search(request):
#     if request.method == '':
#         search = request.POST.get('search')



