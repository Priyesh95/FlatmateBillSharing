from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate
from flatmates_bill.reports import PdfReport

app = Flask(__name__)


class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',bill_form = bill_form)

class ResultsPage(MethodView):
        
        def post(self):
            billForm = BillForm(request.form)
            
            bill = Bill(int(billForm.amount.data),billForm.period.data)
            flatmate1 = Flatmate(billForm.name1.data,int(billForm.days_in_house1.data))
            flatmate2 = Flatmate(billForm.name2.data,int(billForm.days_in_house2.data))

            result = [flatmate1.pays(bill,flatmate2),flatmate2.pays(bill,flatmate1)]

            report = PdfReport(bill.period)
            report.generate(flatmate1,flatmate2,bill)


            return render_template("results.html", period = bill.period,name1 = flatmate1.name, amount1 = result[0], name2 = flatmate2.name, amount2 = result[1])

class BillForm(Form):
    amount = StringField("Bill amount: ", default="100")
    period = StringField("Bill Period: ", default= "December 2020")
    
    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Day is house: ", default= "20")

    name2 = StringField("Name: ", default="Mary")
    days_in_house2 = StringField("Day is house: ", default="12")

    submit = SubmitField("Calculate")

app.add_url_rule("/",view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill",view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results",view_func=ResultsPage.as_view("results_page"))

app.run(debug=True)