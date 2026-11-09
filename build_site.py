"""Faculty proposal site (GitHub Pages repo junnynoh-tech/lab-proposals). Built 2026-11-09.

Daniel: one link for the Spanish faculty, one for the French faculty, instead of emailing HTML files.
The late-lab policy is left out (it goes to faculty separately).

    python3 labs/lab-proposals/build_site.py

1. Rebuilds the four faculty proposals with PROPOSAL_NO_LATE=1 (lab-builder/make_proposal.py).
2. Copies them to spanish/ and french/.
3. Writes the landing pages from the SUMMARY data below: a one-minute summary, what stays the same,
   the questions for faculty, and a card per course that opens the full proposal.
Public site: no names, rosters, grades or schedules. The only address is the Lab's shared inbox.
"""
import html, os, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LABS = HERE.parent
ENGINE = LABS / "lab-builder"
COURSES = {  # code: (source folder, site folder)
    "span1001": ("span1001/labs-regular-2026", "spanish"),
    "span1002": ("span1002/labs-2026", "spanish"),
    "fren1001": ("fren1001/labs-2026", "french"),
    "fren1002": ("fren1002/labs-2026", "french"),
}
e = lambda s: html.escape(s, quote=True)

SITES = {
 "spanish": dict(
  lang="Spanish", title="Language Lab proposal: SPAN 1001 and SPAN 1002",
  lead="The same six labs and Bongo recordings, organized so students find everything in one place, test their setup in week one, and are graded on one speaking rubric.",
  changes=[
   ("One LAB folder", "Everything students need sits in one folder per course: a tabbed description, Lab 0, then each lab's mini-quiz and Bongo recording. No Start Here module, no subfolders."),
   ("Lab 0 in week one", "The Guidelines Quiz plus a one-minute Bongo camera and screen check, both 0%. Recording problems show up in week one instead of on a due date."),
   ("One due time: 5:00 PM", "Both courses. SPAN 1001 labs were due Fridays at 3:00 PM; 5:00 PM is still during Lab hours, so students can get help before it closes."),
   ("One speaking rubric, still 25 points", "Fluency &amp; Discourse 10 · Comprehensibility &amp; Accuracy 5 · Vocabulary 5 · Task 5. Course weights don't change."),
   ("Better tech help", "Troubleshooting for video labs and slide labs, each with one backup students can finish before the deadline: a phone recording, or a PowerPoint or Canva MP4."),
   ("SPAN 1002: one video per lab", "One recording per lab with every question written on the Bongo page, instead of Question &amp; Answer prompts heard one at a time."),
   ("No face or no audio = 0", "In both courses, with no resubmission, as SPAN 1002 does now. Lab 0 has already tested the student's setup."),
  ],
  same=["Six labs (four in summer), 25 points each, graded by Language Lab staff.",
        "Each lab is a mini-quiz plus a Bongo recording: 1.5–2 minutes, face visible, Spanish only.",
        "The Guidelines Quiz (75%) still unlocks the labs, now together with Lab 0."],
  ask=["Does the new rubric work for your course?",
       "SPAN 1001: is moving the due time from 3:00 PM to 5:00 PM all right?",
       "When you copy your course next semester, could you leave the lab items out? The Lab sets up a fresh LAB folder. The steps, with pictures, are in the <b>Course copy</b> tab of each proposal.",
       "Is anything students see unclear? Every tab shows the real student page."],
  cards=[("span1001", "SPAN 1001", "Elementary Spanish I", "Six labs. Lab 5 is now one video: a North Georgia tour for a visitor, using Chapters 1–4."),
         ("span1002", "SPAN 1002", "Elementary Spanish II", "Six labs, one video each. Stone sections keep their own Lab 2 (La niñez).")],
 ),
 "french": dict(
  lang="French", title="Language Lab proposal: FREN 1001 and FREN 1002",
  lead="The French labs keep their content and platforms (Bongo for FREN 1001, TalkAbroad for FREN 1002). What changes is how students find the instructions, a setup check in week one, and a set of fixes where the current pages disagree with each other.",
  changes=[
   ("One LAB folder", "One folder per course with a tabbed description, so the rules, labs, accents and contact are in one place."),
   ("Lab 0 in week one", "A Guidelines Quiz that unlocks the labs. FREN 1001 adds a one-minute Bongo camera and screen check; FREN 1002 adds TalkAbroad setup. Both 0%."),
   ("Typing French", "A keyboard demo for Windows and Mac, with typing practice and three typed accent questions in the quiz."),
   ("FREN 1001: requirements in plain sight", "On each Bongo page, always visible and with counts, instead of hidden in drop-downs. Lab 4 and Lab 5 work for Gainesville, Dahlonega or the student's own town."),
   ("FREN 1001 Lab 6: 10 recorded questions", "A Bongo Question &amp; Answer with 10 questions recorded by a French professor, 2–3 minutes in all, in place of picking 5 of 47."),
   ("FREN 1002: vocabulary from Top Hat", "Lists rebuilt from the Top Hat chapter lists, with 18 Top Hat errors corrected and listed for you to confirm. Each word links to Forvo for audio."),
   ("FREN 1002: due Fridays at 5:00 PM", "Was 3:00 PM; now the same time as SPAN 1001 and SPAN 1002."),
   ("FREN 1002: workshops in person or online", "Lab assistants run every workshop. Online sections get online workshops, so Gainesville and Dahlonega can share lab assistants."),
   ("Consistent pages", "Fixes where pages disagreed: video length, points (FREN 1001: 20, scored with the rubric), resources, Lab 5's title and grading in FREN 1002."),
  ],
  same=["FREN 1001: six labs, individual Bongo videos, no mini-quizzes, the five-row rubric, due Wednesdays at 11:59 PM.",
        "FREN 1002: TalkAbroad conversations with a preparation document and an mp3, the TalkAbroad rubric (25 points per lab).",
        "FREN 1002 summer sections: due Wednesdays at 11:59 PM."],
  ask=["FREN 1001 Lab 6: is the 10-question Bongo Question &amp; Answer all right?",
       "FREN 1002 Top Hat corrections: could you confirm them? They're listed by chapter in the <b>Top Hat corrections</b> tab.",
       "FREN 1002 summer: should summer sections add workshops, or stay without them?",
       "Due times: FREN 1001 stays Wednesday 11:59 PM and FREN 1002 moves to Friday 5:00 PM. Keep them different, or align them?",
       "When you copy your course next semester, could you leave the lab items out? The steps are in the <b>Course copy</b> tab."],
  cards=[("fren1001", "FREN 1001", "Elementary French I", "Six labs in Bongo. New Lab 0, clearer Labs 4–5, and a recorded-question Lab 6."),
         ("fren1002", "FREN 1002", "Elementary French II", "Five TalkAbroad labs with workshops. New vocabulary lists and an optional reflection page.")],
 ),
}

CSS = """
:root{--navy:#002147;--blue:#005fa3;--gold:#7a5d14;--gold-bar:#b8952a;--ink:#0d1525;--muted:#4a5f75;--bg:#f7f9fc;--card:#fff;--line:#d5e0ee;--chip:#fdf6e3;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--navy:#cfe0f5;--blue:#8cc4f2;--gold:#e2c26a;--gold-bar:#b8952a;--ink:#e6ecf4;--muted:#a9b7c8;--bg:#0f1724;--card:#17223a;--line:#2b3a55;--chip:#2a2414;}}
:root[data-theme="dark"]{--navy:#cfe0f5;--blue:#8cc4f2;--gold:#e2c26a;--gold-bar:#b8952a;--ink:#e6ecf4;--muted:#a9b7c8;--bg:#0f1724;--card:#17223a;--line:#2b3a55;--chip:#2a2414;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1.02rem/1.6 'DM Sans',system-ui,sans-serif;}
main{max-width:980px;margin:0 auto;padding:40px 16px 64px;}
.kicker{font-weight:700;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 6px;}
h1{font-family:'Fraunces',Georgia,serif;font-weight:900;color:var(--navy);font-size:clamp(1.7rem,4vw,2.5rem);line-height:1.15;margin:0 0 12px;}
h2{font-family:'Fraunces',Georgia,serif;font-weight:700;color:var(--navy);font-size:1.45rem;margin:44px 0 14px;}
.lead{font-size:1.15rem;color:var(--muted);max-width:760px;margin:0;}
.bar{width:64px;height:4px;background:var(--gold-bar);border-radius:2px;margin:18px 0 0;}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;}
.card{background:var(--card);border:1px solid var(--line);border-top:5px solid var(--navy);border-radius:14px;padding:20px 20px 22px;display:flex;flex-direction:column;gap:6px;}
.card h2,.card h3{margin:0;font-family:'Fraunces',Georgia,serif;font-size:1.5rem;color:var(--navy);}
.card .sub{margin:0;color:var(--muted);font-weight:600;}
.card p{margin:0;}
.btn{display:inline-block;margin-top:12px;align-self:flex-start;background:var(--navy);color:var(--bg);text-decoration:none;font-weight:700;padding:10px 18px;border-radius:999px;}
.btn:hover,.btn:focus-visible{background:var(--blue);}
.btn:focus-visible{outline:3px solid var(--gold-bar);outline-offset:2px;}
.hint{font-size:.92rem;color:var(--muted);}
ol.changes{list-style:none;counter-reset:c;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;}
ol.changes li{counter-increment:c;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px 14px 56px;position:relative;}
ol.changes li::before{content:counter(c);position:absolute;left:16px;top:13px;width:28px;height:28px;border-radius:50%;background:var(--chip);color:var(--gold);font-weight:700;display:grid;place-items:center;font-size:.95rem;}
ol.changes b{display:block;color:var(--navy);margin-bottom:2px;}
ul.plain{margin:0;padding-left:20px;} ul.plain li{margin:0 0 6px;}
.ask{background:var(--chip);border-left:4px solid var(--gold-bar);border-radius:0 12px 12px 0;padding:18px 22px;}
.ask ol{margin:8px 0 0;padding-left:22px;} .ask li{margin:0 0 8px;}
.ask p{margin:0;}
.how{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:0;padding:0;list-style:none;}
.how li{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;}
.how b{color:var(--navy);}
footer{margin-top:48px;color:var(--muted);font-size:.9rem;border-top:1px solid var(--line);padding-top:16px;}
a{color:var(--blue);}
@media (max-width:760px){.cards,ol.changes,.how{grid-template-columns:minmax(0,1fr);}}
"""

def page(title, body, desc):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=DM+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><main>
{body}
<footer>UNG Language Lab · Questions: reply to the email this link came in, or write to <a href="mailto:languagelab-gvl@ung.edu">languagelab-gvl@ung.edu</a>. This is a proposal: nothing changes in your course until it's agreed.</footer>
</main></body></html>
"""

def lang_page(key, S):
    cards = "".join(f"""<article class="card"><h3>{code_l}</h3><p class="sub">{e(name)}</p><p>{blurb}</p>
<a class="btn" href="{code}.html">Open the {code_l} proposal</a></article>""" for code, code_l, name, blurb in S["cards"])
    body = f"""<p class="kicker">UNG Language Lab · Proposal for {S['lang']} faculty</p>
<h1>{e(S['title'])}</h1>
<p class="lead">{S['lead']}</p><div class="bar" aria-hidden="true"></div>

<h2>What changes, in one minute</h2>
<ol class="changes">{"".join(f"<li><b>{t}</b>{d}</li>" for t, d in S["changes"])}</ol>

<h2>What stays the same</h2>
<ul class="plain">{"".join(f"<li>{x}</li>" for x in S["same"])}</ul>

<h2>What we'd like from you</h2>
<div class="ask"><p>A short reply to the email is plenty. These are the questions we most need answered:</p>
<ol>{"".join(f"<li>{x}</li>" for x in S["ask"])}</ol></div>

<h2>See exactly what students would see</h2>
<ul class="how">
<li><b>1. Start with “What changes.”</b> Each tile shows before and after. Click a tile to see why.</li>
<li><b>2. Click through the tabs.</b> Every tab is the real student page: the announcement, the LAB folder, Lab 0, each lab.</li>
<li><b>3. Use the switches.</b> Buttons at the top of a tab switch between in-person and online sections, or between labs.</li>
</ul>
<p class="hint">Works best on a laptop or desktop. Dates in the previews are this semester's, as an example.</p>
<div class="cards" style="margin-top:18px">{cards}</div>"""
    return page(S["title"], body, S["lead"])

def index_page():
    body = """<p class="kicker">UNG Language Lab</p>
<h1>Language Lab proposals</h1>
<p class="lead">Proposed updates to the language labs, for faculty review. Pick your language.</p><div class="bar" aria-hidden="true"></div>
<div class="cards" style="margin-top:28px">
<article class="card"><h2>Spanish</h2><p class="sub">SPAN 1001 · SPAN 1002</p><p>One LAB folder, a week-one setup check, a 5:00 PM due time and one speaking rubric.</p><a class="btn" href="spanish/">Open the Spanish proposal</a></article>
<article class="card"><h2>French</h2><p class="sub">FREN 1001 · FREN 1002</p><p>One LAB folder, a week-one setup check, French typing help, and fixes where the pages disagreed.</p><a class="btn" href="french/">Open the French proposal</a></article>
</div>"""
    return page("Language Lab proposals", body, "Proposed Language Lab updates for Spanish and French faculty.")

def main():
    if "--no-rebuild" not in sys.argv:
        for code, (src, _) in COURSES.items():
            env = dict(os.environ, LABS_COURSE=str(LABS / src / "source"), PROPOSAL_NO_LATE="1")
            subprocess.run([sys.executable, "make_proposal.py"], cwd=ENGINE, env=env, check=True)
    for code, (src, site) in COURSES.items():
        (HERE / site).mkdir(exist_ok=True)
        shutil.copyfile(LABS / src / f"{code}-lab-proposal-faculty.html", HERE / site / f"{code}.html")
    for key, S in SITES.items():
        (HERE / key / "index.html").write_text(lang_page(key, S), encoding="utf8")
    (HERE / "index.html").write_text(index_page(), encoding="utf8")
    (HERE / ".nojekyll").write_text("", encoding="utf8")
    print("site written:", HERE)

if __name__ == "__main__":
    main()
