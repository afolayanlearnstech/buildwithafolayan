# Import all necessary tools from Flask
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'

# --- DEVELOPMENT SETTING: PREVENT BROWSER CACHING OF STATIC FILES ---
# This ensures that any changes you make to your CSS file are reflected
# immediately in the browser without needing to hard-refresh every time.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# --- DYNAMIC CASE STUDY DATA ---
# This list now holds the data for our "Patient-First" demo
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

# CORRECTED: Route is now '/solutions' to match our strategy
@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/portfolio')
def portfolio():
    # We pass the project data to the template here
    return render_template('portfolio.html', projects=portfolio_projects)

# NEW: This route makes the HIPAA page live
@app.route('/hipaa')
def hipaa():
    return render_template('hipaa.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Updated to capture the new form fields
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        practice_type = request.form['practice_type']
        
        # Updated the print statement for better logging
        print(f"New Consultation Request: From {name} ({email}), Phone: {phone}, Practice Type: {practice_type}")
        
        # Updated the flash message to match the new context
        flash('Thank you for scheduling a consultation! I will be in touch shortly to confirm.', 'success')
        
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

