from django.shortcuts import render
from .models import *
from django.views import  View
from django.views.generic import ListView,DetailView




class VariantList(ListView):
    model = Variant

    def get_context_data(self, **kwargs):
        context = super(VariantList, self).get_context_data(**kwargs)
        context['theme_list'] = Theme.objects.all()
        return context

class ThemeDetail(DetailView):
    model = Theme
    slug_field = 'id'

class QuestionsView(View):
    def get(self, request, pk):
        variant = Variant.objects.get(id=pk)
        questions = variant.questions.all()
        return render(request, "schoolTestApp/variant.html", {'list': questions, 'variant': variant})

    def post(self, request, pk):
        variant = Variant.objects.get(id=pk)
        questions = variant.questions.all()

        you = []
        right_list = []
        status = []
        for q in questions:
            answer = request.POST.get(str(q.id))

            if q.answer.is_integer():
                right = int(q.answer)
            else:
                right = q.answer
            right_list.append(str(right))
            if answer == '':
                you.append('-')
            if answer != '':
                you.append(str(answer))

        lens = [i + 1 for i in range(len(right_list))]

        for i in range(len(right_list)):
            if you[i] == right_list[i]:
                status.append('Правильно')
            elif you[i] == '-':
                status.append('Не решено')
            else:
                status.append('Неверно')

        return render(request, "schoolTestApp/result.html", {'u': you, 'r': right_list, 'status': status, 'len': lens})
