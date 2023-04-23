from django.shortcuts import render, redirect




def login_with_google(request):
    if not request.user.is_authenticated:
        return redirect('social:begin', 'google-oauth2')
    else:
        return redirect('home')
