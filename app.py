# Import all necessary tools from Flask and the 'os' module
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# --- Production-Ready App Initialization ---
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Good for development

# --- MODIFIED: DYNAMIC CASE STUDY DATA ---
portfolio_projects = [
    {
        'title': 'The Secure Client Document Intake Portal',
        'description': 'A private portal allowing firms (Law, Accounting) to securely receive sensitive client files, bypassing insecure email. Automates renaming and organization, saving admin time and reducing breach risks.',
        'image_url': 'https://placehold.co/600x400/8B5CF6/ffffff?text=Secure+Client+Intake+Portal+(Concept)', # Purple theme
        'tech_tags': ['Flask', 'File Handling', 'Security', 'Automation'],
        'status': 'Concept',
        'case_study_url': '#', # Keep '#' until you have a detailed page
        'link_text': 'Learn More (Coming Soon)'
    },
    {
        'title': 'The Automated Patient Nurture Sequence',
        'description': 'Automated email system for cosmetic surgeons. Nurtures leads from web forms with a timed sequence of helpful emails, increasing consultations and saving staff time.',
        'image_url': 'https://placehold.co/600x400/10B981/ffffff?text=Automated+Patient+Nurturing+(Concept)', # Green theme
        'tech_tags': ['Flask', 'Google Sheets', 'Email (SMTP)', 'Scheduling'],
        'status': 'Concept',
        'case_study_url': '#',
        'link_text': 'Learn More (Coming Soon)'
    },
    {
        'title': 'The Market Intelligence Briefing',
        'description': 'Automated daily email report delivering customized market data (stocks, crypto, commodities) directly to financial professionals, saving significant research time.',
        'image_url': 'https://placehold.co/600x400/3B82F6/ffffff?text=Market+Intelligence+Briefing+(Concept)', # Blue theme
        'tech_tags': ['Python Script', 'yfinance', 'Email (SMTP)', 'Scheduling'],
        'status': 'Concept',
        'case_study_url': '#',
        'link_text': 'Learn More (Coming Soon)'
    },
    {
        'title': 'The VIP Stock & Wishlist Notifier',
        'description': 'E-commerce feature for luxury goods. Captures emails for sold-out items and automatically notifies customers upon restock, recovering lost sales and driving urgency.',
        'image_url': 'https://placehold.co/600x400/F59E0B/ffffff?text=VIP+Wishlist+Notifier+(Concept)', # Amber theme
        'tech_tags': ['Flask', 'SQLAlchemy', 'Database', 'Email (SMTP)', 'Admin Panel'],
        'status': 'Concept',
        'case_study_url': '#',
        'link_text': 'Learn More (Coming Soon)'
    }
]
# --- END MODIFIED DATA ---


# --- ROUTES ---

@app.route('/')
def home():
    # Pass projects to home if needed, otherwise remove if not used there
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/portfolio')
def portfolio():
    # This now uses the detailed project data
    return render_template('portfolio.html', projects=portfolio_projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            service = request.form['service_needed']
            challenges = request.form['challenges']

            print(f"--- New Consultation Request ---")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Service Needed: {service}")
            print(f"Challenges: {challenges}")
            print(f"---------------------------------")

            flash('Thank you for your consultation request! I will get back to you soon.', 'success')
            return redirect(url_for('contact'))
    except Exception as e:
        print(f"Form submission error: {e}")
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)