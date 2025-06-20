
from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf, match_resume_with_jd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    match_score = None
    top_keywords = []
    if request.method == 'POST':
        file = request.files['resume']
        if file.filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(file)
            with open('jd.txt', 'r', encoding='utf-8') as f:
                jd_text = f.read()
            match_score, top_keywords = match_resume_with_jd(resume_text, jd_text)
    return render_template('index.html', score=match_score, keywords=top_keywords)

if __name__ == '__main__':
    app.run(debug=True)
