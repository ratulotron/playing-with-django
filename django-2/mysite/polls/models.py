import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        yesterday = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date >= yesterday

    def __str__(self):
        return str(self.question_text)

    """
    q = Question(
        question_text="What's new?",
        pub_date=timezone.now()
    )
    q
    q.save()
    q.question_text
    q.id
    q.pub_date
    q.was_published_recently()
    Question.objects.all().filter(id=1)
    Question.objects.filter(id=1)
    Question.objects.filter(id=1)
    current_year = timezone.now()
    Question.objects.get(pub_date__year=current_year)
    Question.objects.get(pub_date__year=current_year)
    current_year = timezone.now().year
    Question.objects.get(pub_date__year=current_year)
    Question.objects.prefetch_related
    q.choice_set.all()
    q.choice_set.create(choice_text='Not much')
    q.choice_set.create(choice_text='The sky')
    q.choice_set.create(choice_text='Just hacking again')
    q.choice_set
    q.choice_set.all()
    q.choice_set.all()[2]
    c = q.choice_set.all()[2]
    c.question
    q.choice_set.count()
    Choice.objects.filter(Question)
    Choice.objects.filter(question__pub_date__year=current_year)

    """


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
