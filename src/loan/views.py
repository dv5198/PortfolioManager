from re import template
from django.shortcuts import render
from .models import Loan
from . import check_loan


def add_loan(request):
    template = 'loans/add_loan.html'
    
    if request.method == 'POST':
        user = request.POST.get('User')
        gender = request.POST.get('gender')
        married = request.POST.get('married')
        dependents = request.POST.get('dependents')
        education = request.POST.get('education')
        self_employed = request.POST.get('self_employed')
        applicant_income = request.POST.get('applicant_income')
        coapplicant_income = request.POST.get('coapplicant_income')
        loan_amount = request.POST.get('loan_amount')
        loan_amount_term = request.POST.get('loan_amount_term')
        credit_history = request.POST.get('credit_history')
        property_area = request.POST.get('property_area')
        
        print(user, gender, married, dependents, education, self_employed, applicant_income,
                             coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)
        
        data = check_loan.models(user, gender, married, dependents, education, self_employed, applicant_income,
                             coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)
        
        
        
        message = ''
        if data == 1:
            message_color = 'green'
            loan_status='eligible'
            message = "You are eligible to get Loan"
        else:
            message_color = 'red'
            loan_status='not eligible'
            message = "Sorry! You are not eligible to get Loan.."

        loan = Loan(
            
            user=user,
            gender=gender,
            married=married,
            dependents=dependents,
            education=education,
            self_employed=self_employed,
            applicant_income=applicant_income,
            coapplicant_income=coapplicant_income,
            loanAmount=loan_amount,
            loan_Amount_term=loan_amount_term,
            credit_history=credit_history,
            property_area=property_area,
            loan_status=loan_status
        )
        loan.save()

        context = {'message': message,'message_color': message_color}
        return render(request, template,context)
    return render(request,template)

def loan_details(request):
    template="loans/loan_detail.html"
    loan_data=Loan.objects.all()
    total_user=Loan.objects.count()
    # print("Loan",total_user)
    applicant_income=0
    coapplicant_income=0
    eligible_user=0
    not_eligible_user=0
    data=dict()
    total_user=Loan.objects.count()
    for income in loan_data:
        applicant_income+=income.applicant_income
        coapplicant_income+=income.coapplicant_income
        if income.loan_status=='eligible':
            eligible_user+=1
        else:
            not_eligible_user+=1

    return render(request,template,{'context':loan_data,'total_user':total_user,'applicant_income':applicant_income,'coapplicant_income':coapplicant_income,'eligible_user':eligible_user,'not_eligible_user':not_eligible_user})



# def loan_details(request):
#     template="loans/loan_detail.html"
#     loan_data=Loan.objects.all()
#     data=dict()
#     applicant_income=0
#     coapplicant_income=0
#     eligible=0
#     not_eligible=0
#     data['total_user']=Loan.objects.count()
#     for income in loan_data:
#         applicant_income+=income.applicant_income
#         coapplicant_income+=income.coapplicant_income
#     return data


