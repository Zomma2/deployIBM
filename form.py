from flask import Flask, request, render_template 
import requests
# Flask constructor
app = Flask(__name__,instance_relative_config=True)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 



       return ''' 
       <style>
       h1, input::-webkit-input-placeholder, button {
  font-family: "roboto", sans-serif;
  -webkit-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

h1 {
  height: 100px;
  width: 100%;
  font-size: 18px;
  background: #18aa8d;
  color: white;
  line-height: 150%;
  border-radius: 3px 3px 0 0;
  box-shadow: 0 2px 5px 1px rgba(0, 0, 0, 0.2);
}

form {
  box-sizing: border-box;
  width: 260px;
  margin: 100px auto 0;
  box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.2);
  padding-bottom: 40px;
  border-radius: 3px;
}
form h1 {
  box-sizing: border-box;
  padding: 20px;
}

input {
  margin: 40px 25px;
  width: 200px;
  display: block;
  border: none;
  padding: 10px 0;
  border-bottom: solid 1px #1abc9c;
  transition: all 0.3s cubic-bezier(0.64, 0.09, 0.08, 1);
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 96%, #1abc9c 4%);
  background-position: -200px 0;
  background-size: 200px 100%;
  background-repeat: no-repeat;
  color: #0e6252;
}
input:focus, input:valid {
  box-shadow: none;
  outline: none;
  background-position: 0 0;
}
input:focus::-webkit-input-placeholder, input:valid::-webkit-input-placeholder {
  color: #1abc9c;
  font-size: 11px;
  transform: translateY(-20px);
  visibility: visible !important;
}

button {
  border: none;
  background: #1abc9c;
  cursor: pointer;
  border-radius: 3px;
  padding: 6px;
  width: 200px;
  color: white;
  margin-left: 25px;
  box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.2);
}
button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 6px 0 rgba(0, 0, 0, 0.2);
}

.follow {
  width: 42px;
  height: 42px;
  border-radius: 50px;
  background: #03A9F4;
  display: inline-block;
  margin: 50px calc(50% - 21px);
  white-space: nowrap;
  padding: 13px;
  box-sizing: border-box;
  color: white;
  transition: all 0.2s ease;
  font-family: Roboto, sans-serif;
  text-decoration: none;
  box-shadow: 0 5px 6px 0 rgba(0, 0, 0, 0.2);
}
.follow i {
  margin-right: 20px;
  transition: margin-right 0.2s ease;
}
.follow:hover {
  width: 134px;
  transform: translateX(-50px);
}
.follow:hover i {
  margin-right: 10px;
}
       </style>
       <form>
  <h1>Material Design Text Input With No Extra Markup</h1>


</form> 
       <form>
  <h1>Material Design Text Input With No Extra Markup</h1>


</form> 
       <form>
  <h1>Material Design Text Input With No Extra Markup</h1>


</form> 
       <form>
  <h1>Material Design Text Input With No Extra Markup</h1>

</form> 



<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">

<link href='https://fonts.googleapis.com/css?family=Roboto:400' rel='stylesheet' type='text/css'>
       
       
       
       '''
    return render_template("form.html")
  
if __name__=='__main__':
   app.run()