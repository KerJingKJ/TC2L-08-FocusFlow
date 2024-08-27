# from django.shortcuts import render, redirect
# from .models import Actor, Quote
# from django.contrib import messages
# import random

# def homepage(request):
#     all_actors = Actor.objects.all()

#     if request.method == 'POST':
#         actor_name = request.POST.get('actor_name')

#         if not actor_name: # return an error 
#             messages.error(request, 'You have to select an actor')
#             return redirect('home')
        
#         get_actor = Actor.objects.get(quote=actor_name)
#         get_quotes = Quote.objects.filter(actor=get_actor)

#         random_quote = random.choice(get_quotes) # selects on item randomly

#         context = {
#             "quote"; random_quote,
#             "actors": all_actors,
#         }
#         return render(request, 'motivation.html', context)

#     context = {
#         "actors": all_actors,
#     }
from django.shortcuts import render, redirect
from .models import Actor, Quote
from django.contrib import messages
import random

def homepage(request):
    all_actors = Actor.objects.all()

    if request.method == 'POST':
        actor_name = request.POST.get('actor_name')

        if not actor_name:  # return an error
            messages.error(request, 'You have to select an actor')
            return redirect('homepage')  # Ensure 'homepage' matches your URL name

        get_actor = Actor.objects.get(quoter=actor_name)  # Corrected field name
        get_quotes = Quote.objects.filter(actor=get_actor)

        random_quote = random.choice(get_quotes)  # selects one item randomly

        context = {
            "quote": random_quote,  # Corrected the semicolon
            "actors": all_actors,
        }
        return render(request, 'motivation.html', context)

    # Return the initial context for GET requests
    context = {
        "actors": all_actors,
    }
    return render(request, 'motivation.html', context)  # Added return for GET requests
