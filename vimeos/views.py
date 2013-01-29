from django.shortcuts import render_to_response
from django.http import HttpResponse
from vim.vimeos.models import Vimeouserinfo

def search_form(request):
    return render_to_response('search.html')

def search(request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET.get('q')
            vim = Vimeouserinfo.objects.filter(Name__icontains=q)
            return render_to_response('search_form.html',
            {'vimeos': vim[0:100], 'query': q,'length':len(vim)})
        else:
            return HttpResponse('Please submit a search term.')
            

            
def searchpay(request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET.get('q')
            vim = Vimeouserinfo.objects.filter(Name__icontains=q,Paying="YES")
            return render_to_response('search_form.html',
            {'vimeos': vim[0:100], 'query': q,'length':len(vim)})
        else:
            return HttpResponse('Please submit a search term.')
            
def searchupl(request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET.get('q')
            vim = Vimeouserinfo.objects.filter(Name__icontains=q,Video="YES")
            return render_to_response('search_form.html',
            {'vimeos': vim[0:100], 'query': q,'length':len(vim)})
        else:
            return HttpResponse('Please submit a search term.')
            
def searchspk(request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET.get('q')
            vim = Vimeouserinfo.objects.filter(Name__icontains=q,StaffPick="YES")
            return render_to_response('search_form.html',
            {'vimeos': vim[0:100], 'query': q,'length':len(vim)})
        else:
            return HttpResponse('Please submit a search term.')
