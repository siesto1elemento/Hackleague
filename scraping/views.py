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

def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        hackathon_data = hackathon_()
        new_hackathod_data = []
        for hacks in hackathon_data:
            if search.lower() in hacks['heading'].lower() or search.lower() in hacks['theme'].lower() or search.lower() in hacks['theme_result'].lower():
                new_hackathod_data.append(hacks)

        
        
        return render(request, 'search.html', {'hackathon_data': new_hackathod_data})
        





