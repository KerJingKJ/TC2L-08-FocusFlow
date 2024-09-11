# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def motivation(request):
#     return render(request,'motivation.html')


    # Django's Template Loader: By default, Django automatically looks for templates inside each app’s templates directory, as well as in any directories you’ve specified in the DIRS option in settings.py. You only need to specify the path relative to the templates directory.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Actor, Quote
from django.contrib import messages
import random

def motivation(request):
    all_actors = Actor.objects.all()

    if request.method == 'POST':
        actor_name = request.POST.get('actor_name')

        if not actor_name:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'You have to select an actor'}, status=400)
            else:
                messages.error(request, 'You have to select an actor')
                return redirect('motivation')

        try:
            get_actor = Actor.objects.get(quoter=actor_name)
            get_quotes = Quote.objects.filter(actor=get_actor)
            random_quote = random.choice(get_quotes)
        except Actor.DoesNotExist:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Selected actor does not exist'}, status=400)
            else:
                messages.error(request, 'Selected actor does not exist')
                return redirect('motivation')
        except IndexError:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'No quotes found for the selected actor'}, status=400)
            else:
                messages.error(request, 'No quotes found for the selected actor')
                return redirect('motivation')

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'quote': random_quote.quote,
                'actor': get_actor.quoter
            })

        context = {
            "quote": random_quote,
            "actors": all_actors,
        }
        return render(request, 'motivation/motivation.html', context)

    context = {
        "actors": all_actors,
    }
    return render(request, 'motivation/motivation.html', context)

