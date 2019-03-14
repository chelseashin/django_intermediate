from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    # 여기에 딕셔너리 만들어서 context를 받아옴!
    context = {
        'boards' : boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')
    
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board, 
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
    
    
def edit(request, pk):
        # UPDATE
    if request.method == 'POST':
        board = Board.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        # EDIT
        board = Board.objects.get(pk=pk)
        context = {
            'board': board, 
        }
        return render(request, 'boards/edit.html', context)

