from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,'title': "Data Analyst", 'location':' Kathmandu, Nepal', 'salary': ' RS 20,00,000'
    },
    {
        'id':2,'title': "Fullstack Engineer", 'location':' Nepalgunj, Nepal', 'salary': ' RS 30,00,000'
    },
    {
        'id':3,'title': "Front end Engineer", 'location':' Remote'
    },
    {
        'id':4,'title': "React JS Engineer", 'location':' Seattle, USA', 'salary': ' $120,000'
    }
]

@app.route('/')
def main():
    return render_template('home.html', jobs = JOBS,
                           company_name = 'Pratik')

@app.route('/about/jobs')
def about_jobs():
    return jsonify(JOBS)

@app.route('/user/<username>')
def dynamic(username):
    return f"Welcome {username}"

if __name__ == '__main__':
    app.run(debug=True, port=7000)