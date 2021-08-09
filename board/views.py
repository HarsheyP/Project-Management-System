from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *


def board_dashboard(request):

    Title = Board.objects.all()

    ThisBoard = InsideBoard.objects.all()

    context = {'ThisBoard':ThisBoard, 'title':Title}

    return render(request, 'board_dashboard.html',context)

def calendar(request):
    return render(request, 'calendar.html')

def project_detail(request, slug):
   # return HttpResponse(slug)
    Title = Board.objects.all()

    ThisBoard = InsideBoard.objects.all()

    form = CardForm()

    pr = Board.objects.get(slug=slug)

    card = InsideBoard.objects.filter(board_id=pr.board_id)

    context = {'pr':pr, 'ThisBoard':ThisBoard, 'form':form, 'title':Title, 'card':card}

    return render(request, 'board.html', context)
