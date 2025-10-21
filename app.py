# Import all necessary tools from Flask and the 'os' module
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# --- Production-Ready App Initialization ---
# This is a more robust way to initialize the app for production.
# It explicitly tells Flask where to find the templates and static files.
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Good for development

# --- DYNAMIC CASE STUDY DATA ---
portfolio_projects = [
    {
        'title': 'The Calming & Trustworthy Design',
        'description': 'A strategic color palette and layout designed to reduce patient anxiety and build immediate trust.',
        'image_url': 'https://placehold.co/600x400/5c9ead/ffffff?text=Calm+Design',
        'case_study_url': '#'
    },
    {
        'title': 'The High-Converting Service Page',
        'description': 'An SEO-driven page for "Dental Implants" that answers patient questions and drives high-value bookings.',
        'image_url': 'https://placehold.co/600x400/343a40/ffffff?text=Service+Page',
        'case_study_url': '#'
    },
    {
        'title': 'The Secure, Automated New Patient Form',
        'description': 'A demo of our HIPAA-compliant intake system that reduces front-desk workload and eliminates errors.',
        'image_url': 'https://placehold.co/600x400/0b0b3b/ffffff?text=Secure+Forms',
        'case_study_url': '#'
    },
    {
        'title': 'The "Meet The Doctor" Trust-Builder',
        'description': 'A bio page that goes beyond credentials to build a personal connection with prospective patients.',
        'image_url': 'https://placehold.co/600x400/6f42c1/ffffff?text=Doctor+Bio',
        'case_study_url': '#'
    }
]

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=portfolio_projects)

@app.route('/hipaa')
def hipaa():
    return render_template('hipaa.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        practice_type = request.form['practice_type']
        challenges = request.form['challenges']

        print(f"--- New Consultation Request ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Practice Type: {practice_type}")
        print(f"Challenges: {challenges}")
        print(f"---------------------------------")

        flash('Thank you for your consultation request! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', body_class="contact-body-gradient")

if __name__ == '__main__':
    app.run(debug=True)

