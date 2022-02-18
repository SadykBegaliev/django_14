from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse


def get_shows_all(request):
    shows = models.TVShow.objects.filter().order_by("-id")
    return render(request, "shows_list.html", {"shows": shows})


def get_show_detail(request, id):
    global comment
    try:
        show = get_object_or_404(models.TVShow, id=id)
        try:
            comment = models.ShowComment.objects.filter(shows_id=id).order_by("created_date")
        except models.TVShow.DoesNotExist:
            print('No comments')
    except models.TVShow.DoesNotExist:
        raise Http404('TVSHOW does not exist, try another id')
    return render(request, "shows_detail.html", {"show": show, 'shows_comment': comment})


def add_show(request):
    method = request.method
    if method == "POST":
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("shows:shows_list"))
            # return HttpResponse("Show Created Successfully")
    else:
        form = forms.TVShowForm()
    return render(request, "add_shows.html", {"form": form})


def put_shows_update(request, id):
    show_id = get_object_or_404(models.TVShow, id=id)
    if request.method == "POST":
        form = forms.TVShowForm(instance=show_id,
                                data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("shows:shows_list"))
    else:
        form = forms.TVShowForm(instance=show_id)
    return render(request, "shows_update.html", {"form": form,
                                                 "show": show_id})


def shows_delete(request, id):
    show_id = get_object_or_404(models.TVShow, id=id)
    show_id.delete()
    # return HttpResponse("Show Deleted")
    return redirect(reverse("shows:shows_list"))
