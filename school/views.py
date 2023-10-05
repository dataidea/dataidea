from .models import Quiz
from .models import Video
from .models import Course
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def quiz_view(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        context = {'message': 'Quiz Not Found', 'state': 'danger'}
        template_name = 'components/message.html'
        return render (request=request, 
                       template_name=template_name, 
                       context=context)
    questions = quiz.questions.all()

    # Calculate correct answers for each question
    correct_answers = {}
    for question in questions:
        correct_choices = question.choice_set.filter(is_correct=True)
        correct_answers[f'{question.id}'] = [choice.text for choice in correct_choices]

    if request.method == 'POST':
        score = 0

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}', None)
            if selected_choice_id:
                selected_choice = question.choice_set.get(pk=selected_choice_id)

                # Check if the selected choice is correct
                if selected_choice.is_correct:
                    score += 1

        # You can also store the user's score in the user's profile or a separate model here

        return render(request, 'school/results.html',
                      {'quiz': quiz, 'questions': questions,
                       'score': score, 'correct_answers': correct_answers})

    return render(request, 'school/quiz.html', {'quiz': quiz, 'questions': questions})


def browse(request):
    courses = Course.objects.all().order_by('-pk')
    course_level_key_map = {'reception-1': 'Introduction'}

    # pagination
    paginator = Paginator(courses, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'courses': page_obj,
               'course_level_key_map': course_level_key_map}
    template_name = 'school/browse.html'
    return render(request=request, 
                  template_name=template_name,
                   context=context )


def searchCourses(request):
    query = request.POST.get(key='query')

    if query:
        courses = Course.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        course_level_key_map = {'reception-1': 'Introduction'}
        context = {'courses': courses,
                'course_level_key_map': course_level_key_map}
        template_name = 'school/browse.html'
        return render(request=request, 
                    template_name=template_name,
                    context=context )
    
    elif query == '' or query == None:
        return redirect('school:browse')

# @login_required(login_url='accounts:signin')
def course_details(request, id):
    course = Course.objects.get(id=id)
    videos = course.videos.all()

    # pagination
    paginator = Paginator(videos, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'course': course,
               'videos': page_obj,
               'user': request.user}
    template_name = 'school/course_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def comment(request, id):
    try:
        video = Video.objects.get(id=id)
        comment = request.POST['comment']
        user = request.user
        if user.is_anonymous:
            video.comments.create(comment=comment)
            message = """
                    Thanks for your comment! Please sign in to enjoy the full benefits of our services. 
                    Your comment has been saved and will be visible to other users after you refresh the page 😊.
                    """
            context = {'message': message, 'state': 'success'}
            template_name = 'components/message.html'
            return render(request=request, template_name=template_name, context=context)
        else:
            video.comments.create(comment=comment, user=user)
            return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        message = """
                    Sorry, something went wrong while saving your comment. 
                    Please try again later.
                    """
        context = {'message': message, 'state': 'warning'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)






# http://127.0.0.1:8000/schoolcourse-details/3?page=2