# AI Disclosure

## Academic Integrity Statement

This project is conducted in accordance with:

- CU Boulder Honor Code
- Coursera Honor Code
- Course AI Usage Policy

AI tools are used as assistants for brainstorming,
project planning, technical discussion, and review.

The student remains responsible for all submitted work,
including analysis, implementation decisions,
interpretation of results, writing, and attribution.

---

## AI Usage Log

### 2026-07-11

Tool:
- Microsoft Copilot

Purpose:
- Data mining project planning.

Representative Activities:
- Evaluation of candidate datasets.
- Discussion of project scope and feasibility.
- Review of grading policy.
- Review of AI disclosure requirements.
- Review of project proposal lectures.
- Review of project proposal review lectures.
- Discussion of anomaly detection project ideas.
- Evaluation of Online Retail II dataset.
- Evaluation of NASA IMS Bearings dataset.
- Review of initial EDA findings.

Outcome:
- Identified Online Retail II as the preferred dataset.
- Rejected NASA IMS Bearings due to project scope concerns.
- Defined preliminary project direction focused on unusual customer purchasing behavior.
- Established workflow for proposal development.

Use in Project:
- Project planning and brainstorming only.

### 2026-07-18

Tool:
- Microsoft Copilot

Purpose:
- Visualization refinement for DBSCAN stability analysis.

Representative Prompt:
- "I found something really beautiful. Please review the results of my min_samples sensitivity test while keeping eps fixed.
I observed a clear trend: over the range [5, 30], as min_samples increases, the number of clusters decreases, the number of noise points increases slightly, and the silhouette score decreases slightly.
Now I want to improve the plot presentation. Noise points are much larger in magnitude than silhouette score and cluster count. I tried log(noise points), but trend visibility is still limited. Please suggest plotting strategies and an example implementation."

Representative Activities:
- Reviewed visualization challenges caused by mixed metric scales.
- Suggested multi-panel plotting to separate absolute levels from small trend changes.
- Proposed plotting first differences and normalized index views to improve interpretability.
- Provided example plotting implementation approach for min_samples stability results.

Outcome:
- Clarified a plotting strategy that preserves both magnitude and trend visibility across metrics.
- Established a more interpretable way to communicate DBSCAN stability findings for research reporting.

Use in Project:
- Technical review and plotting guidance only; final interpretation and implementation decisions remain student-authored.

Reference:
- notebooks/04_CustomerSegmentation.ipynb
- Stability analysis section for min_samples sweep visualization.

### 2026-07-20

Tool:
- Claude Code

Purpose:
- Convert the project proposition draft into a slide-deck presentation (PPTX), matching the same content in a different format.

Representative Prompt:
- "I need to create a presentation in addition to the project proposition. Same content, different format (PowerPoint/PDF). How to do this fast without compromising academic integrity?"

Representative Activities:
- Recommended pandoc (already installed locally) for Markdown-to-PPTX conversion as the fastest compliant path.
- Drafted `docs/presentation.md`: condensed each section of `docs/project_proposition_draft.md` (Abstract, Introduction, Related Work, Proposed Work, Evaluation) into slide-level bullet points.
- Added a dedicated "AI Acknowledgement" slide in the deck pointing back to this log entry.
- Ran `pandoc docs/presentation.md -o docs/presentation.pptx --slide-level=1` to generate the deck.

Outcome:
- Produced `docs/presentation.pptx`, structurally mirroring the approved proposition draft in slide form.

Use in Project:
- Slide wording was AI-condensed from the student's own already-authored/approved proposal text (no new analysis, interpretation, or claims introduced). Student is responsible for reviewing and editing final slide wording/design before submission.

Reference:
- docs/project_proposition_draft.md (source content)
- docs/presentation.md (generated slide markdown)
- docs/presentation.pptx (generated deck)

---

## AI Usage Template

### YYYY-MM-DD

Tool:
- <Tool name>

Purpose:
- <Why AI was used>

Representative Prompt:
- "<Prompt text or concise paraphrase>"

Representative Activities:
- <Activity 1>
- <Activity 2>

Outcome:
- <What was produced or clarified>

Use in Project:
- <How output was used; confirm student ownership of final decisions>

Reference:
- <File path(s)>
- <Notebook section/cell purpose>