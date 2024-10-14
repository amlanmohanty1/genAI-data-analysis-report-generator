from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from report_generator import generate_report

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages


@app.route('/', methods=['GET', 'POST'])
def index():
    report = None
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No file part'
            return render_template('index.html', error=error)
        file = request.files['file']
        if file.filename == '':
            error = 'No selected file'
            return render_template('index.html', error=error)

        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            try:
                groq_api_key = os.getenv("GROQ_API_KEY")
                report = generate_report(df, groq_api_key)
            except Exception as e:
                error = str(e)
        else:
            error = 'File must be a CSV'

    return render_template('index.html', report=report, error=error)


if __name__ == '__main__':
    app.run(debug=True)
