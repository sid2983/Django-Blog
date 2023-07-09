from .models import Room
from django.template.context import Context

# from django.urls import resolve
# from django.shortcuts import render, get_object_or_404
import logging


def rooms_list(request):
    # Fetch all rooms or necessary information for rendering the room list
    rooms = Room.objects.all()

    return {'rooms': rooms}




from .models import Room, Post,User


def room_authors(request):
    room_id = request.resolver_match.kwargs.get('pk')
    authors = User.objects.filter(post__room__id=room_id).distinct()
    logger = logging.getLogger(__name__)
    logger.debug(f"Room ID: {room_id}")
    logger.debug(f"authors: {authors}")
    
    return {'authors': authors,'name':'Siddharth'}
