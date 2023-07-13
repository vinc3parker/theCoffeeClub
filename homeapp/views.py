from django.shortcuts import render, redirect
from .models import Review, CoffeeShop


def new_review(request):
    if request.method == 'POST':
        coffee_shop = request.POST.get('coffee_shop')
        overall_rating = float(request.POST.get('overall_rating'))
        coffee_rating = float(request.POST.get('coffee_rating'))
        food_rating = float(request.POST.get('food_rating'))
        review_text = request.POST.get('review')

        # Save the review to the database
        review = Review.objects.create(
            coffee_shop=coffee_shop,
            overall_rating=overall_rating,
            coffee_rating=coffee_rating,
            food_rating=food_rating,
            review_text=review_text
        )

        # Perform any additional actions you need (e.g., send notifications, calculate averages, etc.)

        return redirect('your_journey')  # Redirect the user back to the 'your_journey' page after submitting the review

    return render(request, 'homeapp/new_review.html')


def your_journey(request):
    coffee_shops = CoffeeShop.objects.all()
    coffee_shop_data = []

    for coffee_shop in coffee_shops:
        coffee_shop_data.append({
            'name': coffee_shop.name,
            'latitude': coffee_shop.latitude,  # Assuming you have latitude field in your model
            'longitude': coffee_shop.longitude,  # Assuming you have longitude field in your model
            'overall_rating': coffee_shop.overall_rating,
            'coffee_rating': coffee_shop.coffee_rating,
            'food_rating': coffee_shop.food_rating,
            'price_rating': coffee_shop.price_rating,
            'vibe_rating': coffee_shop.vibe_rating,
            'wifi_rating': coffee_shop.wifi_rating,
            'quiet_rating': coffee_shop.quiet_rating,
            'meeting_rating': coffee_shop.meeting_rating,
            'study_work_rating': coffee_shop.study_work_rating
        })

    context = {
        'coffee_shops': coffee_shop_data
    }

    return render(request, 'homeapp/your_journey.html', context)


def home(request):
    context = {}
    return render(request, 'homeapp/home.html', context)


def about(request):
    context = {}
    return render(request, 'homeapp/about.html', context)
