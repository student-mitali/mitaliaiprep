from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    level = ""
    feedback = ""
    data = {}

    resume_link = ""
    github_link = ""
    skills = ""

    if request.method == "POST":

        # Ratings
        tech = int(request.form.get("tech", 0))
        comm = int(request.form.get("comm", 0))
        conf = int(request.form.get("conf", 0))
        resume_score = int(request.form.get("resume_score", 0))

        # Links & Skills
        resume_link = request.form.get("resume_link", "")
        github_link = request.form.get("github_link", "")
        skills = request.form.get("skills", "")

        # Store for chart
        data = {
            "Technical": tech,
            "Communication": comm,
            "Confidence": conf,
            "Resume": resume_score
        }

        # Calculate score
        total = tech + comm + conf + resume_score
        score = (total / 40) * 100

        # Level + Feedback
        if score >= 80:
            level = "Excellent"
            feedback = "You are interview-ready. Keep improving!"
        elif score >= 60:
            level = "Good"
            feedback = "Improve projects and communication."
        else:
            level = "Needs Improvement"
            feedback = "Focus on skills, resume, and confidence."

    return render_template(
        "index.html",
        score=score,
        level=level,
        feedback=feedback,
        data=data,
        resume_link=resume_link,
        github_link=github_link,
        skills=skills
    )


if __name__ == "__main__":
    app.run(debug=True)
