from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album
#from django.template import loader

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    '''
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    #print( "html: " + html )
    return HttpResponse(html)
    '''
    '''
    template = loader.get_template( 'music/index.html' )
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render( context, request) )
    '''
    context = {
        'all_albums' : all_albums,
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    #return HttpResponse("<h2>Details for  album id: " + str(album_id) + "</h2>")
    '''
    all_albums = Album.objects.all()
    template = loader.get_template( 'music/detail.html' )
    context = {
        'album' : all_albums[int(album_id)-1],
    }
    return HttpResponse(template.render( context, request) )
    '''
    '''
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    '''
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', { 'album': album })
