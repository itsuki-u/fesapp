from flask import Flask , render_template , request
from flask.globals import session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'user'
app.permanent_session_lifetime = timedelta(days=2) # -> 5分 #(days=5) -> 5日保存

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
    session.permanent = True


    nickname = request.form.get('nickname')
    text = request.form.get('text')

    session['nickname'] = nickname
    session['text'] = text
    print(session['nickname'])
    print(session['text'])

    return render_template('impressions.html')

@app.route('/rule')

def rule():
    return render_template('rule.html')


@app.route('/clear')

def clear():
    return render_template('clear.html')





    


if __name__ == '__main__':
    app.run()


