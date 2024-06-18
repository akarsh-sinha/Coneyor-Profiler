import os
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .models import DataFile
from .forms import DataFileForm, DateForm
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request):
    if request.method == 'POST':
        form = DataFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            
            # Save files temporarily
            file1_path = default_storage.save(request.FILES['file1'].name, ContentFile(request.FILES['file1'].read()))
            file2_path = default_storage.save(request.FILES['file2'].name, ContentFile(request.FILES['file2'].read()))

            # Assign temporary file paths to the instance
            instance.file1.name = file1_path
            instance.file2.name = file2_path
            
            instance.save()
            return redirect('home')
    else:
        form = DataFileForm()

    date_form = DateForm()
    selected_date = request.GET.get('date')
    graph = None

    if selected_date:
        data_files = DataFile.objects.filter(date=selected_date).first()
        if data_files:
            try:
                # Read CSV files using Pandas
                print(f"Reading file1 from path: {data_files.file1.path}")
                print(f"Reading file2 from path: {data_files.file2.path}")

                df1 = pd.read_csv(data_files.file1.path, header=None, names=['x', 'y'])
                df2 = pd.read_csv(data_files.file2.path, header=None, names=['x', 'y'])

                print(f"File1 data: {df1.head()}")
                print(f"File2 data: {df2.head()}")

                # Plot the data
                plt.figure(figsize=(10, 5))
                plt.plot(df1['x'], df1['y'], label='Left Profile')
                plt.plot(df2['x'], df2['y'], label='Right Profile')
                plt.legend()
                plt.title(f'Data for {selected_date}')
                #plt.xlabel('X-axis')
                #plt.ylabel('Y-axis')

                # Save the plot
                graph_path = os.path.join('dashboard/static/dashboard', 'graph.png')
                plt.savefig(graph_path)
                plt.close()
                graph = 'dashboard/graph.png'
            except Exception as e:
                print(f"Error processing the data files: {e}")
                graph = 'Error processing the data files.'
        else:
            graph = 'No data available for this date.'

    return render(request, 'dashboard/home.html', {
        'form': form,
        'date_form': date_form,
        'graph': graph,
        'current_time': timezone.now()
    })
