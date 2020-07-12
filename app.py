from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/admin')
def admin_login_page():
    return render_template('admin_login.html')
@app.route('/validate_admin',methods=['post'])
def validateAdmin():

    return render_template('validate_Admin.html')

if__name__=='__main__':
    app.run(debug=True)