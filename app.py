from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
  },
  {
    "id": 2,
    "title": "AI Developer",
    "location": "Chennai, India",
    "salary": "Rs. 15,00,000"
  },
  {
    "id": 3,
    "title": "Software Developer",
    "location": "Hyderabad, India",
    "salary": "Rs. 20,00,000"
  },
  {
    "id": 4,
    "title": "Network Engineer",  
    "location": "Delhi, India",
    "salary": "Rs. 25,00,000"
  },
]

@app.route("/")
def hello_jasim():
  return render_template('home.html',
                         jobs = JOBS,
                         company_name = 'Jovian')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
