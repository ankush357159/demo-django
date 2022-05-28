import datetime

from django.http import HttpResponse
from django.views.generic.edit import CreateView
import datetime
from django.views import View

from student.models import Person


def hello(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


class MyView(View):
    def get(self, request):
        # View logic
        return HttpResponse('result')


class MyCreateView(CreateView):
    model = Person
    fields = ["first_name", "last_name"]
