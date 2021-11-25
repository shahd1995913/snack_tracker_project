from django.shortcuts import render


from snacks.models import Snack
# Create your views here.

from django.shortcuts import render

from django.views.generic import ListView, DetailView

# Create your views here.

class SnackDetailView(DetailView):

    template_name = "snacks_details.html"

    
 
    context_object_name = "snack_object"

    model = Snack


class SnackListView(ListView):

    template_name = "snacks_list.html"

    model = Snack

