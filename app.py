from flask import Flask,request ,render_template , jsonify

import random

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


# @app.route('/math',methods=['POST'])
# def math_ops():
#     if(request.method == 'POST'):
#         ops = request.form['operation']
#         num1 = int(request.form['num1'])
#         num2 = int(request.form['num2'])
#         if ops == 'add':
#             r = num1+num2
#             result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'subtract':
#             r = num1-num2
#             result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'multiply':
#             r = num1*num2
#             result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'divide':
#             r = num1/num2
#             result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
#         return render_template('results.html' , result = result)



# below is the code to test in POSTMAN
    # select POST , PASTE your URL, and inside RAW selet JSON
    # and give 
    # { 'operation':"add","nums1":23,"nums2":3} 
    # and click SEND


# @app.route('/postman_action',methods=['POST'])
# def math_ops1():
#     if(request.method == 'POST'):
#         ops = request.json['operation']
#         num1 = int(request.json['num1'])
#         num2 = int(request.json['num2'])
#         if ops == 'add':
#             r = num1+num2
#             result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'subtract':
#             r = num1-num2
#             result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'multiply':
#             r = num1*num2
#             result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'divide':
#             r = num1/num2
#             result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
#         return jsonify(result)


# @app.route('/input_url')
# def request_input():
#     data = request.args.get('x')
#     return "this is my input from url {}".format(data)


random_number=int(random.randint(1111,9999))

# list_random_number = list(str(random_number))

@app.route("/guess_number",methods=['POST','GET'])
def hello_world():
    if request.method=='POST':
        # tries = int(request.form['tries'])
        user_number = int(request.form['user_number'])    
        # list_user_number = list(str(user_number))
        if user_number==random_number:
            result = 'You WIN'
            
        elif user_number>random_number:
            result = 'Your guess is too  HIGH'
        elif user_number<random_number:
            result = 'Your guess is too LOW'
        
             
 
    else:
        result=""
    return render_template('guess_number.html', result = result)














if __name__=="__main__":
    app.run(host="0.0.0.0")