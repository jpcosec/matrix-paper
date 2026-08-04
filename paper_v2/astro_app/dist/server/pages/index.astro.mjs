import { c as createComponent, d as renderHead, e as renderSlot, r as renderTemplate, b as createAstro, f as renderComponent, m as maybeRenderHead } from '../chunks/astro/server_DMZIVyZi.mjs';
import 'kleur/colors';
import 'clsx';
/* empty css                                 */
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro();
const $$BaseLayout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$BaseLayout;
  const { title = "paper_v2 editor" } = Astro2.props;
  return renderTemplate`<html lang="en" data-astro-cid-37fxchfa> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>${title}</title>${renderHead()}</head> <body data-astro-cid-37fxchfa> <div class="app-shell" data-astro-cid-37fxchfa> ${renderSlot($$result, $$slots["default"])} </div> </body></html>`;
}, "/home/jp/proyectos/Matrix/paper_v2/astro_app/src/layouts/BaseLayout.astro", void 0);

const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": "paper_v2 editorial browser", "data-astro-cid-j7pv25f6": true }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<main class="app-shell" data-astro-cid-j7pv25f6> <section class="workspace" data-astro-cid-j7pv25f6> <header class="topbar" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>paper_v2</div> <h1 data-astro-cid-j7pv25f6>Rendered document + SLDB structure</h1> </div> <div class="toolbar" data-astro-cid-j7pv25f6> <button id="refresh-graph" data-astro-cid-j7pv25f6>Refresh</button> <button id="rebuild" data-astro-cid-j7pv25f6>Rebuild</button> </div> </header> <div class="split-view" data-astro-cid-j7pv25f6> <section class="manuscript-pane" data-astro-cid-j7pv25f6> <div class="pane-header" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>Document</div> <div class="pane-title" data-astro-cid-j7pv25f6>Read the paper, click a paragraph, inspect the structure on the right</div> </div> <div id="status" class="status" data-astro-cid-j7pv25f6>Loading...</div> </div> <article id="paper-view" class="paper-view" data-astro-cid-j7pv25f6></article> </section> <section class="inspector-pane" data-astro-cid-j7pv25f6> <div class="pane-header sticky inspector-topbar" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>SLDB structure</div> <div class="pane-title" data-astro-cid-j7pv25f6>Section → paragraph → note → source</div> </div> </div> <div class="inspector-grid" data-astro-cid-j7pv25f6> <section class="sections-pane" data-astro-cid-j7pv25f6> <div class="pane-header sticky" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>Sections</div> <div id="selected-section-label" class="pane-title" data-astro-cid-j7pv25f6>Nothing selected</div> </div> </div> <div id="sections-list" class="sections-list" data-astro-cid-j7pv25f6></div> </section> <section class="detail-pane paragraph-pane-shell" data-astro-cid-j7pv25f6> <div class="pane-header sticky" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>Paragraph</div> <div id="selected-paragraph-label" class="pane-title" data-astro-cid-j7pv25f6>Select one</div> </div> </div> <div id="paragraph-pane" class="detail-scroll empty-state" data-astro-cid-j7pv25f6>Select a paragraph from the manuscript or section list.</div> </section> <section class="detail-pane notes-pane" data-astro-cid-j7pv25f6> <div class="pane-header sticky" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>Notes</div> <div id="selected-note-label" class="pane-title" data-astro-cid-j7pv25f6>Waiting</div> </div> </div> <div id="notes-pane" class="detail-scroll empty-state" data-astro-cid-j7pv25f6>Select a paragraph first.</div> </section> <section class="detail-pane sources-pane" data-astro-cid-j7pv25f6> <div class="pane-header sticky" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <div class="eyebrow" data-astro-cid-j7pv25f6>Sources</div> <div id="selected-source-label" class="pane-title" data-astro-cid-j7pv25f6>Waiting</div> </div> </div> <div id="sources-pane" class="detail-scroll empty-state" data-astro-cid-j7pv25f6>Select a note first.</div> </section> </div> </section> </div> </section> </main>   ` })}`;
}, "/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro", void 0);

const $$file = "/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro";
const $$url = "";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
