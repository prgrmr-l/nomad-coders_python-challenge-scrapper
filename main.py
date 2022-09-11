from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.wwr2 import extract_wwr2_jobs
from file import save_to_file

db={}
app=Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="YGP")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        wwr2 = extract_wwr2_jobs(keyword)
        jobs=wwr+wwr2
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
         return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)
app.run("0.0.0.0")