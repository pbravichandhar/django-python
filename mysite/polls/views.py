# from django.http import HttpResponse, HttpResponseRedirect

# from .models import Question, Choice

# from django.shortcuts import get_object_or_404, get_list_or_404

# from django.urls import reverse


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return HttpResponse(question)

# def detail(request, question_id):
#     # using shortcuts
#     question = get_object_or_404(Question, pk=question_id)
#     return HttpResponse(question)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     choice = get_list_or_404(Choice, question_id=question_id)
#     return HttpResponse(choice)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=2)
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return HttpResponse({
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return HttpResponse(results(request, question_id))


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer

from bson import ObjectId

class PollView(APIView):

    def get(self, request):
        serializer = PollSerializer(Poll.objects.all(), many=True)
        response = {"polls": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            poll = Poll(**data)
            poll.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)

class EditPollView(APIView):
    
    def put(self, request, poll_id):
        data = request.data
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            poll = Poll.objects(id=ObjectId(poll_id)).first()
            poll.poll_name = serializer.data.get('poll_name')
            poll.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
    
    def delete(self, request, poll_id):
        Poll.objects(id=ObjectId(poll_id)).delete()
        return Response(None, status=status.HTTP_200_OK)