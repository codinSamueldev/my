from django.shortcuts import render
from django.db.models import Q


from user.models import UserModel


# Create your views here.
def search_username(request):
    #username_list = UserModel.objects.all().filter(username__icontains=username)

    query = request.GET.get('username_query', '')
    if query:
        qset = (
            Q(username__icontains=query)
        )
        results = UserModel.objects.filter(qset).distinct()
    else:
        results = list()

    return render(request, 'search/username_list.html', {'results': results, 'query': query})

