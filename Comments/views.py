from django.shortcuts import redirect
from .forms import CommentForm
from .models import Comment


def add_comment_to_car(request, car_id):
    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.car_id = car_id
            comment.save()
            return redirect('car_detail', car_id=car_id)
    else:
        comment_form = CommentForm()
    return comment_form
