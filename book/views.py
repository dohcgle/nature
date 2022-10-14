from django.shortcuts import render

from book.models import Topic, Page


def index(request):
    return render(request, 'book/index.html')


def topic_list(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'book/topic_list.html', context)


def topic_detail(request, pk):
    topic = Topic.objects.get(id=pk)
    category_topics = Topic.objects.filter(category=topic.category)
    context = {
        'topic': topic,
        'category_topics': category_topics
    }
    return render(request, 'book/topic_detail.html', context)


def test_list(request):
    tests = Page.objects.filter(category='T', is_published=True).all()
    context = {
        'tests': tests,
    }
    return render(request, 'book/test_list.html', context)


def test_detail(request, pk):
    test = Page.objects.get(id=pk)
    context = {
        'test': test,
    }
    return render(request, 'book/test_detail.html', context)


def slide_list(request):
    slides = Page.objects.filter(category='P', is_published=True).all()
    context = {
        'slides': slides,
    }
    return render(request, 'book/slide_list.html', context)


def slide_detail(request, pk):
    slide = Page.objects.get(id=pk)
    context = {
        'slide': slide,
    }
    return render(request, 'book/slide_detail.html', context)


def video_list(request):
    videos = Page.objects.filter(category='V', is_published=True).all()
    print(videos)
    context = {
        'videos': videos,
    }
    return render(request, 'book/video_list.html', context)


def video_detail(request, pk):
    video = Page.objects.get(id=pk)
    context = {
        'video': video,
    }
    return render(request, 'book/video_detail.html', context)


def edumat_list(request):
    materials = Page.objects.filter(category='OA', is_published=True).all()
    context = {
        'materials': materials,
    }
    return render(request, 'book/edumat_list.html', context)


def edumat_detail(request, pk):
    material = Page.objects.get(id=pk)
    context = {
        'material': material,
    }
    return render(request, 'book/edumat_detail.html', context)
