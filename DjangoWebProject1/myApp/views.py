"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Suggestion, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contacts',
            'message':'You can contact us via email or phone!',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message1':'FOR THE COMMUNITY:',
            'message2':'BY THE COMMUNTY:',
            'year':datetime.now().year,
        }
    )


def index(request):
    suggestions_list = Suggestion.objects.all().order_by('-pub_date')
    return render(
        request, 
        'app/suggestions.html', 
        {
            'suggestions_list':suggestions_list,
            'title':'Suggestions',
            'message':'Bring your suggestions here!',
            'year':datetime.now().year,     
        }
    )

def new_suggestion(request):
       return render(
        request, 
        'app/new_suggestion.html', 

    )


def SaveSuggestion(request):
    suggestion_title = request.POST['name']
    suggestion_text = request.POST['text']
    suggestion_author = request.user.get_username()
    pub_date = datetime.now()
    a = Suggetions.objects.create(suggestion_title = suggetion_title,
                                        suggestion_author = suggetions_author,
                                        suggetion_text = suggetion_text,
                                        pub_date = pub_date)
    return HttpResponseRedirect(reverse('detail', args = (a.id,)))

def detail(request, suggestion_id):
    try:
        a = Suggestion.objects.get(id = suggestion_id)
    except:
        raise Http404("Suggestion is not found!")

    comments_list = a.comment_set.order_by('-id')

    return render(
        request, 
        'app/detail.html', 
        {
            'suggestion': a,
            'comments_list': comments_list,
            'year':datetime.now().year,  
        }
    )
    

def leave_comment(request, suggestion_id):
    try:
        a = Suggestion.objects.get(id = suggestion_id)
    except:
        raise Http404("Suggestion is not found!")
    a.comment_set.create(comment_author = request.user.get_username(), 
                         comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('detail', args = (a.id,)))