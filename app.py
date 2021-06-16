from flask import Flask , render_template , request
from flask.globals import session


app = Flask(__name__)



@app.route('/', methods=['GET','POST'])




def test():

	
    p1 = request.form.get('pass1')
    p2 = request.form.get('pass2')
    p3 = request.form.get('pass3')



    if p1 == '314' and p2 == '12' and p3 == '36':

        
        return render_template('clear.html')


    return render_template('index.html')



@app.route('/impressions' , methods = ['GET','POST'])

def impressions():

    return render_template('impressions.html')

@app.route('/rule')

def rule():
    return render_template('rule.html')


@app.route('/clear')

def clear():
    return render_template('clear.html')





    


if __name__ == '__main__':
    app.run()


