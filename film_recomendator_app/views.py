from django.shortcuts import render, redirect
from chromaDB_interface.chromaDB_service import ChromaDBService
from .forms import QueryForm
from film_recomendator import settings
from .models import HistorySearchFilm, FilmSearches
from django.contrib.auth.decorators import login_required

db_service = ChromaDBService()

def convert_to_string(*args):
    return [str(arg) for arg in args]

def save_user_search_history(user, meta):
    for movie in meta:
        search = HistorySearchFilm(owner=user, title=movie['title'], movie_id=movie['id'])
        search.save()

def add_search_to_top(meta):
    for movie in meta:
        top_film, created = FilmSearches.objects.get_or_create(title=movie['title'], movie_id=movie['id'])
        top_film.count += 1
        top_film.save()

@login_required
def append_query_results(request, meta):
    save_user_search_history(request.user, meta)
    add_search_to_top(meta)

def index(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            genres = form.cleaned_data["genre"]
            query_text = form.cleaned_data["query_text"]
            n_results = int(form.cleaned_data["n_results"])
            genres, query_text = convert_to_string(genres, query_text)

            readable, meta = db_service.query(query_texts=query_text, n_results=n_results, genres=genres)
            
            append_query_results(request, meta)

            request.session["meta"] = meta

            return redirect("query_results")
        
    form = QueryForm()
    return render(request, "film_recomendator_app/index.html", {"form": form})

@login_required
def query_result(request):
    meta = request.session['meta']
    return render(request, "film_recomendator_app/query_result.html", {"meta": meta, "media_url": settings.MEDIA_URL})

@login_required
def search_history(request):
    history = HistorySearchFilm.objects.filter(owner=request.user).order_by('date')
    return render(request, 'film_recomendator_app/search_history.html', {'history': history})

@login_required
def top_searches(request):
    top = FilmSearches.objects.all().order_by('-count')[:10]
    return render(request, "film_recomendator_app/top_searches.html", {"top": top})

@login_required
def delete_history(request):
    history = HistorySearchFilm.objects.filter(owner=request.user)
    history.delete()
    return redirect('index')