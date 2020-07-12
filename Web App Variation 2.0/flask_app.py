from flask import Flask, make_response, request

from date_shifter import process_data

import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def file_summer_page():
    if request.method == "POST":

        input_date_unformatted = request.form["input_date"]             #takes input of the input date
        input_date =  datetime.datetime.strptime(input_date_unformatted, '%Y-%m-%d').date()     #converts to correct date input for calendar use

        input_file = request.files["input_file"]    #takes input of input calendar


        output_data = process_data(input_file.read(),input_date)    #shifts calendar, logic goes to date_shifter



        response = make_response(output_data)
        response.headers["Content-Disposition"] = "attachment; filename=ouputcal.ics"     #downloads new calendar
        return response

    return '''
        <html>
            <!<link rel="stylesheet" link href="/static/css/dateformat.css">
            <link rel="stylesheet" link href="/static/css/dateformat.css">

            <div class="one">

                <p style = "font-size:30px">Select the calendar file you want to edit and the new start date you want to shift to. Files typically end in .ics or iCalendar.</p>
                <form method="post" action="." enctype="multipart/form-data">
                <p><input type="file" name="input_file" /></p>

                <label for="start">Start date:</label>
                <input type="date" id="start" name="input_date">

                <p><input type="submit" value="Process the file" /></p>
                </form>

            <div>




</html>

    '''
