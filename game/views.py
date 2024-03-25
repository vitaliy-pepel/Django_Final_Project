from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random


def index(request):
    if request.method == 'POST':
        game_type = request.POST['game_type']
        num_results = int(request.POST['num_results'])

        results = []

        if game_type == 'coin_toss':
            for _ in range(num_results):
                results.append(random.choice(['орёл', 'решка']))
        elif game_type == 'dice_roll':
            for _ in range(num_results):
                results.append(random.randint(1, 6))
        elif game_type == 'random_number':
            for _ in range(num_results):
                results.append(random.randint(1, 100))

        context = {'results': results}
        return render(request, 'game/results.html', context)

    return render(request, 'game/index.html')
