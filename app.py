# Import all necessary tools from Flask and the 'os' module
from flask import Flask, render_template, request, redirect, url_for, flash
import os
# Import Flask-Mail
from flask_mail import Mail, Message

# --- Production-Ready App Initialization ---
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Good for development


# --- Flask-Mail Configuration ---
# ... existing code ...
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587)) # Port must be an integer
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True' # Converts string "True" to boolean True
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL') == 'True' # Converts string "False" to boolean False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
# Initialize the Mail object
mail = Mail(app)


# --- DYNAMIC CASE STUDY DATA (with Icons) ---
portfolio_projects = [
    # --- NEW PROJECT ADDED AT THE TOP ---
    {
        'title': 'Distributed Uptime Monitoring System',
        'description': 'A full-stack, distributed application built to monitor website reliability. This project demonstrates a hybrid-cloud architecture, combining Vercel (for the app) and Supabase (for the database).',
        # Icon: Activity/Pulse (for Monitoring)
        'icon_svg': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-activity"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
        'tech_tags': ['Python', 'Flask', 'PostgreSQL', 'Supabase', 'Vercel', 'SRE', 'Cloud Networking', 'Debugging'],
        'status': 'Live Demo',
        'live_url': 'https://uptime-monitor-drab-chi.vercel.app/',
        'github_url': 'https://github.com/buildwithafolayan/uptime-monitor'
    },
    # --- YOUR EXISTING PROJECTS ---
    {
        'title': 'The Secure Client Document Intake Portal',
# ... existing code ...
        'description': 'A private portal allowing firms (Law, Accounting) to securely receive sensitive client files via direct cloud upload, bypassing insecure email. Features multi-file selection with preview.',
        # Icon: Shield Check (Security)
# ... existing code ...
        'icon_svg': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-shield-check"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
        # UPDATED Tech Tags
        'tech_tags': ['Flask', 'SQLAlchemy', 'JavaScript', 'Vercel Blob', 'Security', 'Automation'],
# ... existing code ...
        'status': 'Live Demo',
        # NEW Links - *** REMEMBER TO REPLACE THE vercel.app URL ***
        'live_url': 'https://secure-client-portal.vercel.app/', # <-- *** REPLACE with your Secure Portal Vercel URL ***
        'github_url': 'https://github.com/buildwithafolayan/secure-client-portal'
    },
# ... existing code ...
    {
        'title': 'The Automated Patient Nurture Sequence',
        'description': 'Automated email system for cosmetic surgeons. Nurtures leads from web forms with a timed sequence of helpful emails, increasing consultations and saving staff time.',
# ... existing code ...
        'icon_svg': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail-check"><path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h8"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/><path d="m16 19 2 2 4-4"/></svg>',
        'tech_tags': ['Flask', 'Google Sheets', 'Email (SMTP)', 'Scheduling'],
# ... existing code ...
        'status': 'Concept',
        'case_study_url': '#', # Keep these for concept projects if needed
        'link_text': 'Learn More (Coming Soon)'
# ... existing code ...
    },
    {
        'title': 'The Market Intelligence Briefing',
# ... existing code ...
        'description': 'Automated daily email report delivering customized market data (stocks, crypto, commodities) directly to financial professionals, saving significant research time.',
        # Icon: Line Chart (Data/Finance)
        'icon_svg': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-line-chart"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>',
# ... existing code ...
        'tech_tags': ['Python Script', 'yfinance', 'Email (SMTP)', 'Scheduling'],
        'status': 'Concept',
# ... existing code ...
        'case_study_url': '#',
        'link_text': 'Learn More (Coming Soon)'
    },
    {
# ... existing code ...
        'title': 'The VIP Stock & Wishlist Notifier',
        'description': 'E-commerce feature for luxury goods. Captures emails for sold-out items and automatically notifies customers upon restock, recovering lost sales and driving urgency.',
# ... existing code ...
        'icon_svg': '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-bell-ring"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/><path d="M4 2C2.8 3.7 2 5.7 2 8"/><path d="M22 8c0-2.3-.8-4.3-2-6"/></svg>',
        'tech_tags': ['Flask', 'SQLAlchemy', 'Database', 'Email (SMTP)', 'Admin Panel'],
# ... existing code ...
        'status': 'Concept',
        'case_study_url': '#',
        'link_text': 'Learn More (Coming Soon)'
    }
]

# --- ROUTES ---

@app.route('/')
# ... existing code ...
def home():
    # Pass 'home-page' as the body_class
    return render_template('index.html', body_class='home-page')

@app.route('/about')
# ... existing code ...
def about():
    # Pass 'about-page' as the body_class
    return render_template('about.html', body_class='about-page')

@app.route('/solutions')
# ... existing code ...
def solutions():
    # Pass 'solutions-page' as the body_class
    return render_template('solutions.html', body_class='solutions-page')

@app.route('/portfolio')
# ... existing code ...
def portfolio():
    # Pass 'portfolio-page' as the body_class
    return render_template('portfolio.html', projects=portfolio_projects, body_class='portfolio-page')

@app.route('/contact', methods=['GET', 'POST'])
# ... existing code ...
def contact():
    # This page needs the body_class in all return statements
    active_body_class = 'contact-page'

    # ==== MODIFICATION ====
# ... existing code ...
    # On a GET request, check for a 'service' parameter in the URL
    # We set this as a default, which will be used when rendering
    selected_service = request.args.get('service', '')
    # ==== END MODIFICATION ====

    # Check if mail configuration is missing
# ... existing code ...
    if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
        # Only flash this message if the server config is wrong, on POST attempt
        if request.method == 'POST':
# ... existing code ...
            flash('The server is not configured for mail. Please contact the administrator.', 'error')
        # ==== MODIFICATION ====
        # Pass 'selected_service' even on the error page
        return render_template('contact.html', body_class=active_body_class, selected_service=selected_service)

    try:
# ... existing code ...
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
# ... existing code ...
            service = request.form['service_needed']
            challenges = request.form['challenges']

            # Basic validation (can be expanded)
# ... existing code ...
            if not name or not email or not service or not challenges:
                 flash('Please fill out all required fields.', 'error')
                 # Return, not redirect, so user doesn't lose their data
# ... existing code ...
                 # Pass the user's *submitted* data back to the form
                 return render_template('contact.html', name=name, email=email, service=service, challenges=challenges, body_class=active_body_class)

            # --- Create the Email ---
# ... existing code ...
            subject = f"New Portfolio Contact Request from: {name}"
            # Send the email TO yourself
            recipients = ['favour.afolayan.dev@gmail.com']
# ... existing code ...

            # Build a nice-looking email body
            msg_body = f"""
# ... existing code ...
            You have a new consultation request:

            Name: {name}
            Email: {email}

            Service Needed:
            {service}

            Project Details / Challenges:
            {challenges}
            """

            # Create the message object
# ... existing code ...
            msg = Message(subject=subject,
                          recipients=recipients,
                          body=msg_body)
# ... existing code ...

            # Set the reply-to to be the user's email
            msg.reply_to = email

            # --- Send the Email ---
# ... existing code ...
            mail.send(msg)

            # --- END Email Logic ---

# ... existing code ...
            flash('Thank you for your consultation request! I will get back to you soon.', 'success')
            return redirect(url_for('contact')) # Redirect to clear the form

    except Exception as e:
# ... existing code ...
        print(f"Form submission or email error: {e}")
        # Log the error properly in a real application
        # import logging
# ... existing code ...
        # logging.exception("Form submission error")
        flash('An unexpected server error occurred. Please try again later.', 'error')
        # Don't redirect, let user see the page and their data

    # Render the template for GET requests or if POST fails and throws exception
# ... existing code ...
    # ==== MODIFICATION ====
    # Pass 'selected_service' to the template
    return render_template('contact.html', body_class=active_body_class, selected_service=selected_service)


if __name__ == '__main__':
# ... existing code ...
    # Use environment variable for port if available (e.g., for deployment)
    port = int(os.environ.get('PORT', 5000))
    # Turn off debug mode for production (Important: set to False before final deployment)
# ... existing code ...
    # For local testing, you might temporarily set debug=True
    app.run(debug=False, host='0.0.0.0', port=port)