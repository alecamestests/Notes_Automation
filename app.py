# app.py
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Store forms in memory (for demo purposes)
saved_forms = []

def format_form_data(form_data):
    """Format form data with proper HTML structure"""
    html = []
    
    # Title section
    html.append('<div class="note-section"><h3>### Installer Support ###</h3>')
    
    # Contact section
    html.append('<div class="note-section"><h4>Contact with</h4>')
    html.append(f'<ul><li><strong>Contact with:</strong> {form_data.get("contact_with", "N/A")}</li>')
    html.append(f'<li><strong>Company:</strong> {form_data.get("company", "N/A")}</li>')
    html.append(f'<li><strong>Phone number:</strong> {form_data.get("phone", "N/A")}</li>')
    html.append(f'<li><strong>Email:</strong> {form_data.get("email", "N/A")}</li></ul>')
    html.append('<div class="spacer"></div>')
    
    # Controller info
    html.append('<div class="note-section"><h4>Site Controller DIN</h4>')
    html.append(f'<ul><li><strong>Site Controller DIN:</strong> {form_data.get("din", "N/A")}</li>')
    html.append(f'<li><strong>Product DIN (if different):</strong> {form_data.get("product_din", "N/A")}</li></ul>')
    html.append('<div class="spacer"></div>')
    
    # Steps taken (numerical list)
    html.append('<div class="note-section"><h4>Steps Taken</h4>')
    html.append('<ol>')
    steps = form_data.get('steps', '').split('\n')
    for step in steps:
        if step.strip():
            html.append(f'<li>{step.strip()}</li>')
    html.append('</ol><div class="spacer"></div>')
    
    # Information gathered
    html.append('<div class="note-section"><h4>Information Gathered</h4>')
    html.append('<ul>')
    html.append(f'<li><strong>Periscope:</strong> {form_data.get("periscope", "N/A")}</li>')
    html.append(f'<li><strong>Toolbox:</strong> {form_data.get("toolbox", "N/A")}</li>')
    html.append(f'<li><strong>Photos:</strong> {form_data.get("photos", "N/A")}</li>')
    html.append(f'<li><strong>SCA link:</strong> {form_data.get("sca_link", "N/A")}</li>')
    html.append(f'<li><strong>TCC Link:</strong> {form_data.get("tcc_link", "N/A")}</li></ul>')
    html.append('<div class="spacer"></div>')
    
    # Results section
    html.append('<div class="note-section"><h4>Results of Troubleshooting</h4>')
    html.append('<ol>')
    results = form_data.get('results', '').split('\n')
    for result in results:
        if result.strip():
            html.append(f'<li>{result.strip()}</li>')
    html.append('</ol><div class="spacer"></div>')
    
    # Submitting to T2
    html.append('<div class="note-section"><h4>Submitting to T2</h4>')
    html.append(f'<ul><li><strong>What Action are you requesting from Tier-2:</strong> {form_data.get("t2_request", "N/A")}</li></ul>')
    html.append('</div>')
    
    return ''.join(html)