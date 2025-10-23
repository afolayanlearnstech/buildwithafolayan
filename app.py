# Import all necessary tools from Flask and the 'os' module
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# --- Production-Ready App Initialization ---
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Good for development

# --- DYNAMIC CASE STUDY DATA (UPDATED) ---
portfolio_projects = [
    {
        'title': 'The User-Centric UI/UX Design',
        'description': 'A clean, modern layout and color palette designed to build user trust and make navigation intuitive.',
        'image_url': 'https://placehold.co/600x400/5c9ead/ffffff?text=Intuitive+Design',
        'case_study_url': '#'
    },
    {
        'title': 'The High-Converting Landing Page',
        'description': 'An SEO-driven service page focused on clear communication and a strong call-to-action to increase conversions.',
        'image_url': 'https://placehold.co/600x400/343a40/ffffff?text=Landing+Page',
        'case_study_url': '#'
    },
    {
        'title': 'The Secure, Automated Data Form',
        'description': 'A demo of a secure data intake system that protects user information and reduces administrative workload.',
        'image_url': 'https://placehold.co/600x400/0b0b3b/ffffff?text=Secure+Forms',
        'case_study_url': '#'
    },
    {
        'title': 'The "Meet The Team" Profile Page',
        'description': 'A professional bio page that goes beyond credentials to build a personal connection and establish authority.',
        'image_url': 'https://placehold.co/600x400/6f42c1/ffffff?text=Team+Bio',
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        # REMOVED the 'practice_type' line
        challenges = request.form['challenges']

        print(f"--- New Consultation Request ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        # REMOVED the print statement for 'practice_type'
        print(f"Challenges: {challenges}")
        print(f"---------------------------------")

        flash('Thank you for your consultation request! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', body_class="contact-body-gradient")

if __name__ == '__main__':
    app.run(debug=True)