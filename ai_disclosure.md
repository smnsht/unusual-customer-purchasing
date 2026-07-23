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

### 2026-07-23

Tool:
- Claude Code

Purpose:
- Deciding which existing plots/markdown findings from the 4 analysis notebooks to include in a 10-slide conclusion for the final report/deck.

Representative Prompt:
- "If you are asking to add only 10 new pages to existing slides in order to conclude the research and prepare final report, what would you select from my existing 4 notebooks? You can select plots and markdown cells."

Representative Activities:
- Reviewed all 4 notebooks (01_EDA, 02_PreProcessing, 03_FeatureEngineering, 04_UnusualPurchasingBehavior) for conclusion-relevant content.
- Proposed a prioritized list of 10 slides (specific plots/markdown cells with source notebook references) and explicitly listed what was excluded and why.
- On follow-up approval ("yes, please go ahead"), extracted the 5 selected plot images directly from each notebook's cached cell output (base64 PNG data already stored in the .ipynb from prior runs - no re-execution or manual export needed) into `docs/assets/`.
- Wrote 10 new slides into `docs/slides/presentation.md` (bullets + embedded figures) covering PCA diagnostic, KMeans/DBSCAN model selection and tuning, the final locked DBSCAN result, outlier/cluster population breakdown, both Cohen's d comparisons with characterization, the cancellation-rate context stat, and a closing Conclusions slide.
- Rendered the updated deck to `docs/slides/project_proposition_slides_03.pptx` via pandoc (kept as a new version rather than overwriting the student's hand-edited `_02` deck).
- Wrote the same findings as full prose (adapted from the slide bullets into report-style paragraphs) into the Discussion (§6) and Conclusion (§7) sections of `docs/report/project_proposition_draft.md`, with the same 5 figures embedded, and regenerated `docs/report/project_proposition_draft.html`/`.pdf`.

Outcome:
- `docs/slides/project_proposition_slides_03.pptx` and `docs/report/project_proposition_draft.pdf` both now contain a completed Discussion/Conclusion built from the actual notebook results (DBSCAN: 2 clusters, 134 outliers from 41 customers, silhouette 0.65; Cohen's d characterizations for outliers-vs-clusters and cluster0-vs-cluster1).

Use in Project:
- Both the slide bullets and report prose were AI-drafted from the notebooks' own numeric results and existing markdown reflections (no new analysis or claims beyond what the notebooks already contain). Student is responsible for reviewing wording, verifying the numbers against the notebooks, and editing before submission.

Reference:
- notebooks/01_EDA.ipynb#4e28e1f7, notebooks/03_FeatureEngineering.ipynb#59e7c4e7, notebooks/04_UnusualPurchasingBehavior.ipynb#bfe884d7,#bdb58b8b,#384be797 (source plots)
- docs/assets/*.png (extracted figures)
- docs/slides/presentation.md, docs/slides/project_proposition_slides_03.pptx
- docs/report/project_proposition_draft.md, .html, .pdf (Discussion & Conclusion sections)

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