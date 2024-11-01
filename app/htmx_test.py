from django.shortcuts import render
from django.http import HttpResponse

# Using a global variable to store the counter value
counter = 1

def index(request):
    # Render the index page with the current counter value
    return render(request, 'index.html', {'counter': counter})

def increment_count(request):
    global counter
    # Increment the counter
    print(counter)
    counter += 1
    # Return the updated counter in the partial template
    return render(request, 'counter.html', {'counter': counter})

def decrement_count(request):
    global counter
    # Decrement the counter
    counter -= 1
    # Return the updated counter in the partial template
    return render(request, 'counter.html', {'counter': counter})
