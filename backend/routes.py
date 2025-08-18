from flask import Blueprint, render_template, request
from utils.text_extractor import extract_text_from_resume
from utils.text_preprocessor import preprocess_text
from models.skill_extractor import skill_extractor, extract_skills
from utils.text_similarity import calculate_tfid_similarity
import os
from datetime import datetime
import json
from tracker.tracker import add_application, view_applications, update_status

views = Blueprint('routes', __name__)
UPLOAD_FOLDER = "uploads"
@views.route('/health', methods = ["GET"])
def health():
    return {"status" : "Server is running"}, 200

@views.route("/")
def index():
    return render_template("index.html", current_year=datetime.now().year)

@views.route("/upload_resume_jd", methods=["GET", "POST"])
def analyze():
    # print("Analyze route hit with method:", request.method)
    if request.method == "POST":
        resume = request.files.get("resume")
        jd_text = request.form.get("job_description")

        if resume and jd_text:
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            save_path = os.path.join("uploads", resume.filename)
            resume.save(save_path)

            resume_text= extract_text_from_resume(save_path)
            clean_resume_text = preprocess_text(resume_text)
            clean_jd_text = preprocess_text(jd_text)

            resume_skills= extract_skills(clean_resume_text)
            jd_skills = extract_skills(clean_jd_text)

            common_skills = set(resume_skills) & set(jd_skills)
            skill_match_percentage = round((len(common_skills) / len(jd_skills)) *100, 2) if jd_skills else 0

            match_percentage = calculate_tfid_similarity(clean_resume_text, clean_jd_text)

            return render_template(
                "analyze.html",
                resume_skills=resume_skills,
                jd_skills=jd_skills,
                common_skills=list(common_skills),
                skill_match_percentage=skill_match_percentage,
                match_percentage=match_percentage
                )
        else:
            return f"Please provide both resume and jd text."
        
    return render_template("analyze.html")
    
@views.route("/tracker/add", methods=["POST"])
def tracker_add():
    company = request.form.get("company_name")
    job_title = request.form.get("job_title")
    status = request.form.get("status", "Applied")
    applied_date = request.form.get("applied_date") 
    result = add_application(company, job_title, status, applied_date)
    return result["message"]

@views.route("/tracker/view", methods=["GET"])
def tracker_view():
        applications = view_applications()
        return render_template("tracker.html", applications=applications)
    
@views.route("/tracker/update", methods=["POST"])
def tracker_update():
        application_id = request.form.get("id")
        new_status = request.form.get("status")
        update_status(application_id, new_status)
        return "Status updated successfully!"