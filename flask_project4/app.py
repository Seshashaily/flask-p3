from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/static_files')

def static_files():
   return  render_template('static_file.html')

@FAI.route('/new_file')
def new_file():
   return render_template('new.html')

FAI.run(debug=True)

