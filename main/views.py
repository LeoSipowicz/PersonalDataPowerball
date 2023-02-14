from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,Http404
from django.db import models

import datetime

from .models import PersonalDataModel
from .forms import PersonalDataForm, PowerBallPickForm
from .random_balls import randomLottoBalls, randomLottoPowerBall
from .winner_email import send_winner_email


def get_data(request):
    request.session['form-submitted'] = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            request.session['form-submitted'] = True
            request.session['balls-picked'] = False
            request.session['balls-rolled'] = False
            request.session['user-email'] = form.cleaned_data['email']
            return HttpResponseRedirect('./big-spin/')

    # if a GET (or any other method) create blank form
    else:
        form = PersonalDataForm()

    userCount = PersonalDataModel.objects.count() +100
    
    dataValue = f'{.007 * (PersonalDataModel.objects.count() +100):.3f}'

    return render(request, 'home.html', {'form': form, 'dataValue': dataValue,'userCount':userCount})


def big_spin(request):
    print(request.session.get('form-submitted'))
    if (request.session.get('form-submitted') == False or
        request.session.get('balls-picked') == True):
            raise Http404("Poll does not exist")
    else:
        if request.method == 'POST':
            form = PowerBallPickForm(request.POST)
            if form.is_valid():
                request.session['balls-picked'] = True

                playerBalls = [
                    form.cleaned_data['ball1'],
                    form.cleaned_data['ball2'],
                    form.cleaned_data['ball3'],
                    form.cleaned_data['ball4'],
                    form.cleaned_data['ball5']]
                request.session['PlayerBalls'] = sorted(playerBalls)
                request.session['PlayerPowerBall'] = form.cleaned_data['powerBall']
                request.session['balls-picked'] = True
                return HttpResponseRedirect('./lotto-results/')
        else:
            form = PowerBallPickForm()
    return render(request, 'play.html', {'form': form})


def lotto_results(request):
    if (
        request.session.get('form-submitted') == False or
        request.session.get('balls-picked') == False or
        request.session.get('balls-rolled') == True
        ):
        raise Http404("Poll does not exist")

    else:
        PlayerBalls = request.session['PlayerBalls']
        PlayerPowerBall = request.session['PlayerPowerBall']
        dateTimeString = str(datetime.datetime.now().strftime("%m/%d at %I:%M %p"))

        # Only let balls be rolled once
        if request.session['balls-rolled'] == False:
            LottoBalls = randomLottoBalls()
            LottoPowerBall = randomLottoPowerBall()

            # NEVER USE TO CHECK WIN
            # only to publish results
            request.session['LottoBalls'] = LottoBalls
            request.session['LottoPowerBall'] = LottoPowerBall

            request.session['balls-rolled'] = True

            # the magic
            if PlayerBalls == LottoBalls and PlayerPowerBall == LottoPowerBall:
                Useremail = request.session['user-email']
                send_winner_email(Useremail)
                return render(request,
                        'winner.html',{'PlayerBall1': PlayerBalls[0],
                        'PlayerBall2': PlayerBalls[1],
                        'PlayerBall3': PlayerBalls[2],
                        'PlayerBall4': PlayerBalls[3],
                        'PlayerBall5': PlayerBalls[4],
                        'PlayerPowerBall': PlayerPowerBall,
                        'LottoBall1': request.session['LottoBalls'][0],
                        'LottoBall2': request.session['LottoBalls'][1],
                        'LottoBall3': request.session['LottoBalls'][2],
                        'LottoBall4': request.session['LottoBalls'][3],
                        'LottoBall5': request.session['LottoBalls'][4],
                        'LottoPowerBall': request.session['LottoPowerBall'],
                        'dateTimeString': dateTimeString,
                        'Useremail':Useremail})

        return render(request,
                      'results.html',
                      {'PlayerBall1': PlayerBalls[0],
                        'PlayerBall2': PlayerBalls[1],
                        'PlayerBall3': PlayerBalls[2],
                        'PlayerBall4': PlayerBalls[3],
                        'PlayerBall5': PlayerBalls[4],
                        'PlayerPowerBall': PlayerPowerBall,
                        'LottoBall1': request.session['LottoBalls'][0],
                        'LottoBall2': request.session['LottoBalls'][1],
                        'LottoBall3': request.session['LottoBalls'][2],
                        'LottoBall4': request.session['LottoBalls'][3],
                        'LottoBall5': request.session['LottoBalls'][4],
                        'LottoPowerBall': request.session['LottoPowerBall'],
                        'dateTimeString': dateTimeString})
