from flask import Flask, render_template, request,redirect, url_for
import datetime
import nepali_datetime

app = Flask(__name__)

def ad_to_bs(ad_date):
    """Converts a single AD date to BS."""
    # Parse the input date in the format 'yyyy-mm-dd'
    ad_date_obj = datetime.datetime.strptime(ad_date, "%Y/%m/%d")
    # Convert the AD date to a BS date
    bs_date_obj = nepali_datetime.date.from_datetime_date(ad_date_obj.date())
    return bs_date_obj.isoformat()  # Returns date in 'YYYY-MM-DD' format

def bs_to_ad(bs_date):
    """Converts a single BS date to AD."""
    # Parse the BS date in the format 'yyyy-mm-dd'
    bs_year, bs_month, bs_day = map(int, bs_date.split("/"))
    bs_date_obj = nepali_datetime.date(bs_year, bs_month, bs_day)
    # Convert the BS date to an AD date
    ad_date_obj = bs_date_obj.to_datetime_date()
    return ad_date_obj.isoformat()  # Returns date in 'YYYY-MM-DD' format

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert_ad_to_bs', methods=['POST'])
def convert_ad_to_bs():
    ad_date = request.form['ad_date']
    # Ensure the date is in 'yyyy-mm-dd' format before processing
    try:
        ad_date_obj = datetime.datetime.strptime(ad_date, "%Y/%m/%d")
        bs_date = ad_to_bs(ad_date)

        return render_template('index.html', ad_date=ad_date, bs_date=bs_date, ad_to_bs=True)
    except ValueError:
        error_message = "Please enter a valid AD date in YYYY/MM/DD format."
        return render_template('index.html', error_message=error_message)

@app.route('/convert_bs_to_ad', methods=['POST'])
def convert_bs_to_ad():
    bs_date = request.form['bs_date']
    # Ensure the date is in 'yyyy-mm-dd' format before processing
    try:
        bs_date_obj = datetime.datetime.strptime(bs_date, "%Y/%m/%d")
        ad_date = bs_to_ad(bs_date)
        return render_template('index.html', bs_date=bs_date, ad_date=ad_date, bs_to_ad=True)
    except ValueError:
        error_message = "Please enter a valid BS date in YYYY/MM/DD format."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
