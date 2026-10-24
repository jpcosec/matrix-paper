# NeurIPS 2026 Position Paper Style Instructions

Use these instructions to prepare a NeurIPS 2026 paper in the **Position Paper track**. This paper is **not** in final (camera-ready) state, so the output must follow the anonymized submission style rather than the final version.

## 1. Required LaTeX setup

Use the official NeurIPS 2026 style file and load it with the `position` option only:

```latex
\usepackage[position]{neurips_2026}
```

Do **not** use:

- `final`
- `preprint`

For this stage, the paper must remain in submission mode.

## 2. Non-negotiable constraints

- Use the official `neurips_2026.sty` file without modifying it.
- Do not change margins, font sizes, line spacing, title spacing, or any formatting parameters defined by the style.
- The PDF must use **US Letter** paper size, not A4.
- Keep page numbers enabled as produced by the template.

Any manual formatting changes can lead to desk rejection.

## 3. Page limit

The main paper may contain at most **9 pages**, including figures.

The following do **not** count toward the 9-page content limit:

- acknowledgments
- references
- checklist
- optional technical appendices

Still, the main argument of the paper must stand on its own without depending on the appendix.

## 4. Base formatting rules

Follow these template-level rules:

- Text area: **5.5 inches wide** by **9 inches long**
- Left margin: **1.5 inches**
- Main text size: **10 pt**
- Leading: **11 pt**
- Font family: the template uses Times-style fonts by default
- Paragraphs are **not indented**
- Paragraphs are separated by about **half a line** of vertical space

Do not override these settings.

## 5. Title and section headings

- The title should use normal title capitalization (initial caps / lowercase, not all caps).
- First-level headings should be flush left, bold, and 12 pt.
- Second- and third-level headings should be flush left, bold, and 10 pt.
- Headings should be lowercase except for the first word and proper nouns.
- `\paragraph` may be used for inline bold paragraph headings.

## 6. Submission anonymity and self-citations

Because this is not the final version, write the paper in submission-safe style.

- Refer to the authors' prior work in the **third person**.
- Do **not** write phrases like "in our previous work".
- Instead write phrases like "in the previous work of Smith et al.".
- If citing work that is not publicly available, anonymize the author names where needed and provide anonymized supplementary material if appropriate.

Do not include identifying acknowledgments or author-revealing material in the submission version.

## 7. Figures

All figures must be neat, legible, and publication-quality.

- Put the **figure caption after the figure**.
- Leave one line of space before the caption and one line after the figure block.
- Use lowercase in captions except for the first word and proper nouns.
- Number figures consecutively.
- Color figures are allowed, but the content must remain understandable if printed in black and white.

## 8. Tables

All tables must be centered, clean, and legible.

- Put the **table title/caption before the table**.
- Leave one line before the title, one line after the title, and one line after the table.
- Use lowercase in table captions except for the first word and proper nouns.
- Number tables consecutively.
- Do **not** use vertical rules in tables.
- Prefer the `booktabs` package for professional table formatting.

## 9. Math

- Use standard LaTeX math environments.
- Do **not** use bare `$$ ... $$` display math.
- Prefer LaTeX or AMS environments such as `equation`, `align`, etc.

This matters because improper display math can interfere with correct line numbering in submission mode.

## 10. Citations and bibliography

- The template loads `natbib` by default.
- Citation style may be numeric or author-year, but it must be internally consistent.
- References should appear under an unnumbered first-level heading.
- The references may be set in `\small` (9 pt) if needed.
- The references section does not count toward the page limit.

## 11. Footnotes

- Use footnotes sparingly.
- Place footnote markers after punctuation.
- Keep footnotes short and only when necessary.

## 12. PDF production requirements

- Prefer compiling directly with `pdflatex`.
- The final PDF must contain only **Type 1** fonts or **embedded TrueType** fonts.
- Avoid workflows that introduce bitmap fonts.
- If graphics are included, prefer `\includegraphics` from `graphicx`.
- Size figures relative to `\linewidth` when possible.

## 13. Appendix, checklist, and back matter

- The checklist is required and must be included.
- The checklist should come after the references and after any optional supplemental/appendix material.
- Technical appendices are allowed and have no formal page limit.
- However, the main paper must remain self-contained for reviewers.

## 14. Acknowledgments rule for this stage

Do **not** include acknowledgments in the anonymized submission version.

Acknowledgments belong only in the final camera-ready version. The NeurIPS template provides an `ack` environment that stays hidden in anonymized submissions.

## 15. Minimal implementation checklist for the subagent

The generated paper should satisfy all of the following:

1. Load the template as `\usepackage[position]{neurips_2026}`.
2. Do not use `final`.
3. Do not use `preprint`.
4. Do not edit `neurips_2026.sty`.
5. Keep the main paper within 9 pages.
6. Preserve the template's default margins, spacing, and font sizing.
7. Use submission-safe anonymous writing conventions.
8. Omit acknowledgments from the submission version.
9. Include references, appendix if needed, and the required checklist after the main paper.
10. Produce a US Letter PDF with embedded fonts.

## 16. Suggested instruction block for a LaTeX-writing subagent

You can give the following instruction to a subagent:

```text
Write a NeurIPS 2026 submission in LaTeX for the Position Paper track.
Use the official template with \usepackage[position]{neurips_2026}.
This is not a final/camera-ready version, so do not use final or preprint.
Preserve all template formatting defaults and do not modify the style file.
Keep the main paper within 9 pages excluding references, checklist, acknowledgments, and optional appendix.
Write in anonymized submission style: use third-person self-citations and omit acknowledgments.
Place figure captions after figures and table captions before tables.
Avoid $$...$$ display math; use standard LaTeX/AMS math environments.
Ensure the output compiles to a US Letter PDF with proper embedded fonts.
Include the required checklist after references and any appendix material.
```
