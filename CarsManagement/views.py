from django.shortcuts import render, get_object_or_404, redirect
from Comments.forms import CommentForm
from Comments.models import Comment
from Comments.views import add_comment_to_car
from .models import Car


def cars_list(request):
    cars = Car.objects.all().order_by('make', 'model', 'year_of_production', 'price_per_day')
    return render(request, 'cars_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    comments = Comment.objects.filter(car=car)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.car = car
            comment.save()
            return redirect('car_detail', car_id=car_id)
    else:
        comment_form = CommentForm()

    return render(request, 'car_detail.html', {
        'car': car,
        'comments': comments,
        'comment_form': comment_form
    })