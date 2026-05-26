import os
from datetime import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import HistoryForm

def history_view(request):
    log_path = settings.EX02_LOG_FILE

    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['text_input']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {user_text}\n"

            with open(log_path, 'a') as file:
                file.write(log_entry)

            return redirect('/ex02')
    else:
        form = HistoryForm()

    history_data = []
    if os.path.exists(log_path):
        with open(log_path, 'r') as file:
            history_data = [line.strip() for line in file.readlines()]

    return render(request, 'ex02/index.html', {
        'form': form,
        'history': history_data
    })
