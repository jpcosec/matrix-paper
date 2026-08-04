import MarkdownIt from 'markdown-it';
import { r as readDoc } from '../../chunks/fs_BAuakhth.mjs';
export { renderers } from '../../renderers.mjs';

const md = new MarkdownIt({ html: false, linkify: false, typographer: false });
function parseJson(text) {
  return JSON.parse(text);
}
function renderMarkdown(markdown) {
  return md.render(markdown || "");
}
function normalizeRef(ref) {
  return String(ref || "").replace(/^\.\.\//, "");
}
function missingFields(data) {
  return Object.entries(data || {}).filter(([, value]) => value === "" || value == null || Array.isArray(value) && value.length === 0).map(([key]) => key);
}
function deriveAggregateStatus(counts, total) {
  const reasons = [];
  const supportedCount = counts["supported"] || 0;
  const unsupportedCount = total - supportedCount;
  let supportStatus = "supported";
  if ((counts["missing-note"] || 0) > 0) {
    supportStatus = "missing-note";
    reasons.push(`${counts["missing-note"]} item${counts["missing-note"] === 1 ? "" : "s"} missing note coverage`);
  } else if ((counts["missing-source"] || 0) > 0) {
    supportStatus = "missing-source";
    reasons.push(`${counts["missing-source"]} item${counts["missing-source"] === 1 ? "" : "s"} missing source coverage`);
  } else if ((counts["evidence-pending"] || 0) > 0) {
    supportStatus = "evidence-pending";
    reasons.push(`${counts["evidence-pending"]} item${counts["evidence-pending"] === 1 ? "" : "s"} pending evidence linkage`);
  } else if ((counts["incomplete"] || 0) > 0) {
    supportStatus = "incomplete";
    reasons.push(`${counts["incomplete"]} item${counts["incomplete"] === 1 ? "" : "s"} incomplete`);
  }
  if (unsupportedCount > 0) {
    reasons.push(`${unsupportedCount} of ${total} item${total === 1 ? "" : "s"} not fully supported`);
  }
  return {
    supported_count: supportedCount,
    unsupported_count: unsupportedCount,
    support_status: supportStatus,
    status_reasons: reasons
  };
}
function deriveNoteStatus(note) {
  const sourceCount = note.sources.length;
  const missing = missingFields(note.data);
  const reasons = [];
  if (!sourceCount) reasons.push("missing source");
  if (missing.length) reasons.push(`${missing.length} empty field${missing.length === 1 ? "" : "s"}`);
  let supportStatus = "supported";
  if (missing.length > 0) {
    supportStatus = "incomplete";
  }
  if (!sourceCount) {
    supportStatus = "missing-source";
  }
  return {
    source_count: sourceCount,
    has_source: sourceCount > 0,
    missing_fields: missing,
    support_status: supportStatus,
    status_reasons: reasons
  };
}
function deriveParagraphStatus(paragraph) {
  const noteCount = paragraph.notes.length;
  const sourceCount = paragraph.notes.reduce(
    (total, note) => total + (note.sources?.length || 0),
    0
  );
  const notesWithoutSources = paragraph.notes.filter((note) => !(note.sources || []).length).length;
  const missing = missingFields(paragraph.data);
  const reasons = [];
  if (!paragraph.data.paragraph_text) reasons.push("missing paragraph text");
  if (!noteCount) reasons.push("missing note");
  if (noteCount && !sourceCount) reasons.push("missing source");
  if (notesWithoutSources > 0) reasons.push(`${notesWithoutSources} note${notesWithoutSources === 1 ? "" : "s"} without evidence`);
  if (missing.length) reasons.push(`${missing.length} empty field${missing.length === 1 ? "" : "s"}`);
  let supportStatus = "supported";
  if (!paragraph.data.paragraph_text || missing.length > 0) {
    supportStatus = "incomplete";
  }
  if (!noteCount) {
    supportStatus = "missing-note";
  } else if (!sourceCount) {
    supportStatus = "missing-source";
  } else if (notesWithoutSources > 0) {
    supportStatus = "evidence-pending";
  }
  return {
    note_count: noteCount,
    source_count: sourceCount,
    notes_without_sources: notesWithoutSources,
    has_note: noteCount > 0,
    has_source: sourceCount > 0,
    missing_fields: missing,
    support_status: supportStatus,
    status_reasons: reasons
  };
}
function deriveSectionStatus(section) {
  const paragraphStatuses = section.paragraphs.map((paragraph) => paragraph.derived);
  const counts = paragraphStatuses.reduce(
    (acc, status) => {
      acc[status.support_status] = (acc[status.support_status] || 0) + 1;
      return acc;
    },
    {}
  );
  const aggregate = deriveAggregateStatus(counts, section.paragraphs.length);
  return {
    paragraph_count: section.paragraphs.length,
    support_status_counts: counts,
    ...aggregate
  };
}
const GET = async () => {
  try {
    const reportRaw = await readDoc("build/validation_report.json");
    const report = parseJson(reportRaw);
    const byPath = new Map(
      (report.validation || []).map((entry) => [entry.path, entry])
    );
    const manuscript = byPath.get("manuscript/paper.md");
    if (!manuscript) {
      return new Response(JSON.stringify({ error: "Missing manuscript in validation report" }), {
        status: 500
      });
    }
    const sectionRefs = manuscript.input_data.section_refs || [];
    const sections = sectionRefs.map(normalizeRef).map((path) => byPath.get(path)).filter(Boolean).map((sectionEntry) => {
      const paragraphRefs = sectionEntry.input_data.paragraph_refs || [];
      const paragraphs = paragraphRefs.map(normalizeRef).map((path) => byPath.get(path)).filter(Boolean).map((paragraphEntry) => {
        const noteRefs = paragraphEntry.input_data.notes_refs || [];
        const notes = noteRefs.map(normalizeRef).map((path) => byPath.get(path)).filter(Boolean).map((noteEntry) => {
          const sourceRefs = noteEntry.input_data.sources || [];
          const sources = sourceRefs.map(normalizeRef).map((path) => byPath.get(path)).filter(Boolean).map((sourceEntry) => ({
            path: sourceEntry.path,
            model: sourceEntry.model,
            data: sourceEntry.input_data,
            derived: {
              missing_fields: missingFields(sourceEntry.input_data)
            }
          }));
          const note = {
            path: noteEntry.path,
            model: noteEntry.model,
            data: noteEntry.input_data,
            sources
          };
          return {
            ...note,
            derived: deriveNoteStatus(note)
          };
        });
        const paragraph = {
          path: paragraphEntry.path,
          model: paragraphEntry.model,
          data: paragraphEntry.input_data,
          notes,
          rendered: {
            paragraph_html: renderMarkdown(paragraphEntry.input_data.paragraph_text || "")
          }
        };
        return {
          ...paragraph,
          derived: deriveParagraphStatus(paragraph)
        };
      });
      const section = {
        path: sectionEntry.path,
        model: sectionEntry.model,
        data: sectionEntry.input_data,
        rendered: {
          section_html: renderMarkdown(sectionEntry.input_data.section_body || "")
        },
        paragraphs
      };
      return {
        ...section,
        derived: deriveSectionStatus(section)
      };
    });
    const manuscriptStatusCounts = sections.reduce(
      (acc, section) => {
        const status = section.derived.support_status;
        acc[status] = (acc[status] || 0) + 1;
        return acc;
      },
      {}
    );
    const manuscriptDerived = {
      section_count: sections.length,
      paragraph_count: sections.reduce((total, section) => total + section.paragraphs.length, 0),
      support_status_counts: manuscriptStatusCounts,
      ...deriveAggregateStatus(manuscriptStatusCounts, sections.length)
    };
    return new Response(
      JSON.stringify(
        {
          manuscript: {
            path: manuscript.path,
            model: manuscript.model,
            data: manuscript.input_data,
            rendered: {
              abstract_html: renderMarkdown(manuscript.input_data.abstract || "")
            },
            derived: manuscriptDerived
          },
          sections
        },
        null,
        2
      ),
      {
        headers: { "content-type": "application/json; charset=utf-8" }
      }
    );
  } catch (error) {
    return new Response(
      JSON.stringify({ error: error instanceof Error ? error.message : "Graph load failed" }),
      { status: 500 }
    );
  }
};

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  GET
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
