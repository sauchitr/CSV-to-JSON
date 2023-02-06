import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .forms import CSVFileForm
from django.apps import apps


def upload_csv(request):
    """First if the request method is POST then we will accept the file using django's forms. 
    There is a forms.py file which contains the form to accept the file as well as the time frame as integer"""
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)

        # checking if the form is valid and saving it.
        if form.is_valid():
            form.save()
            # fetching the file and the integer from the input.
            csv_file = request.FILES['csv_file']
            time_frame = form.cleaned_data.get('time_frame')

            # using pandas to read the csv file. It is the fastest to read csv files.
            # setting parameter low_memory to false for allowing Pandas to
            # figure the data type on its own.
            df = pd.read_csv(csv_file, low_memory=False)
            # Creating an empty list and appending values in by iterating over the csv file.
            candles = []
            for i, row in df.iterrows():
                candle = {
                    "id": i,
                    "date": row[1],
                    "open": row[3],
                    "high": row[4],
                    "low": row[5],
                    "close": row[6]  
                }
                
                candles.append(candle)
            
            # using another list to get the data within the given time frame
            new_data = []
            for i in range(time_frame):
                new_data.append(candles[i])

            # using another dictionary to add the required values
            result = {}
            
            # adding the date for the trade which would be the 
            # last value withing the given time frame
            result["date"] = new_data[-1]["date"]

            # adding the first value to the open price of the stock
            result["open"] = new_data[0]['open']
            
            # iterating over high to find the highest value 
            # and then adding the highest value to result.
            high_values = [x['high'] for x in new_data]
            result['high'] = max(high_values)

            # iterating over the low to find the lowest value
            # adding the lowest value to the result.
            low_values = [x['low'] for x in new_data]
            result['low'] = min(low_values)

            # adding the final value to the result
            result['close'] = new_data[-1]['close']

            result_list = [result]

            # using pandas DataFrame to convert the list of dictionary
            # to 2-D array.
            df_out = pd.DataFrame(result_list)
            # using to_json(orient="records" for converting the data frame to json strings)
            json_data = df_out.to_json(orient="records")
            # creating a jsonresoponse by loading the json string and converting it into 
            # a json downloadable file attachment by declaring content type to json.
            response = JsonResponse(json.loads(json_data), content_type="application/json", safe=False)
            response["Content-Disposition"] = "attachment; filename=data.json"
            return response

    # rendering the form as context for the users in the front end.
    context = {
        'CSVFileForm': CSVFileForm
    }
    
    return render(request, "MainApp/upload.html", context)
