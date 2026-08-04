const s={graph:null,selectedSectionPath:"",selectedParagraphPath:"",selectedNotePath:"",selectedSourcePath:""},w=document.querySelector("#status"),_=document.querySelector("#paper-view"),N=document.querySelector("#sections-list"),m=document.querySelector("#paragraph-pane"),o=document.querySelector("#notes-pane"),i=document.querySelector("#sources-pane"),C=document.querySelector("#selected-section-label"),x=document.querySelector("#selected-paragraph-label"),S=document.querySelector("#selected-note-label"),b=document.querySelector("#selected-source-label"),E={supported:"ok","evidence-pending":"warn","missing-source":"warn","missing-note":"danger",incomplete:"danger"},T={supported:"Supported","evidence-pending":"Evidence pending","missing-source":"Missing source","missing-note":"Missing note",incomplete:"Incomplete"},u=t=>{w.textContent=typeof t=="string"?t:JSON.stringify(t,null,2)},P=()=>s.graph?.sections.find(t=>t.path===s.selectedSectionPath)||null,v=()=>P()?.paragraphs.find(t=>t.path===s.selectedParagraphPath)||null,h=()=>v()?.notes.find(t=>t.path===s.selectedNotePath)||null,q=()=>h()?.sources.find(t=>t.path===s.selectedSourcePath)||null,L=t=>{s.selectedSectionPath=t;const e=P();s.selectedParagraphPath=e?.paragraphs?.[0]?.path||"",s.selectedNotePath=e?.paragraphs?.[0]?.notes?.[0]?.path||"",s.selectedSourcePath=e?.paragraphs?.[0]?.notes?.[0]?.sources?.[0]?.path||"",g()},M=t=>{s.selectedParagraphPath=t;const e=v();s.selectedNotePath=e?.notes?.[0]?.path||"",s.selectedSourcePath=e?.notes?.[0]?.sources?.[0]?.path||"",g()},H=t=>{s.selectedNotePath=t;const e=h();s.selectedSourcePath=e?.sources?.[0]?.path||"",g()},j=t=>{s.selectedSourcePath=t,g()},n=t=>String(t??"").replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;"),l=t=>`
      <span class="status-pill ${E[t]||"muted"}">${n(T[t]||t)}</span>
    `,f=t=>t?.length?t.map(e=>`<div class="reason-line">${n(e)}</div>`).join(""):'<div class="reason-line ok">Trace complete</div>',A=()=>{const t=s.graph;if(!t)return;const{manuscript:e,sections:c}=t;_.innerHTML=`
        <h1 class="paper-title">${n(e.data.title)}</h1>
        <div class="paper-summary-strip">
          ${l(e.derived.support_status)}
          <span class="summary-pill">${e.derived.section_count} sections</span>
          <span class="summary-pill">${e.derived.paragraph_count} paragraphs</span>
          <span class="summary-pill ok">${e.derived.supported_count} supported</span>
          <span class="summary-pill danger">${e.derived.unsupported_count} need attention</span>
        </div>
        <div class="trace-reasons manuscript-reasons">${f(e.derived.status_reasons)}</div>
        <div class="paper-abstract">
          <h2>Abstract</h2>
          <div class="prose">${e.rendered?.abstract_html||""}</div>
        </div>
      `,c.forEach(a=>{const d=document.createElement("section");d.className="section-block",a.path===s.selectedSectionPath&&(d.dataset.active="true"),d.innerHTML=`
          <div class="section-head">
            <div>
              <h2>${n(a.data.title)}</h2>
              <div class="section-summary">
                ${l(a.derived.support_status)}
                <span class="summary-pill">${a.derived.paragraph_count} paragraphs</span>
                <span class="summary-pill ok">${a.derived.supported_count} supported</span>
                <span class="summary-pill danger">${a.derived.unsupported_count} gaps</span>
              </div>
            </div>
          </div>
        `,d.addEventListener("click",r=>{r.target.closest(".paragraph-trace")||L(a.path)});const $=document.createElement("div");$.className="section-body",a.paragraphs.forEach(r=>{const p=document.createElement("article");p.className="paragraph-trace",r.path===s.selectedParagraphPath&&(p.dataset.active="true"),p.innerHTML=`
            <div class="trace-bar ${E[r.derived.support_status]||"muted"}"></div>
            <div class="trace-main">
              <div class="trace-head">
                ${l(r.derived.support_status)}
                <div class="trace-metrics">
                  <span>${r.derived.note_count} note${r.derived.note_count===1?"":"s"}</span>
                  <span>${r.derived.source_count} source${r.derived.source_count===1?"":"s"}</span>
                </div>
              </div>
              <div class="prose trace-prose">${r.rendered?.paragraph_html||""}</div>
              <div class="trace-reasons">${f(r.derived.status_reasons)}</div>
            </div>
          `,p.addEventListener("click",k=>{k.stopPropagation(),s.selectedSectionPath!==a.path&&(s.selectedSectionPath=a.path),M(r.path)}),$.appendChild(p)}),d.appendChild($),_.appendChild(d)})},R=()=>{const t=s.graph?.sections||[];N.innerHTML="",t.forEach(c=>{const a=document.createElement("button");a.className="section-row",c.path===s.selectedSectionPath&&(a.dataset.active="true"),a.innerHTML=`
          <div class="row-title">${n(c.data.title)}</div>
          <div class="row-meta compact">
            ${l(c.derived.support_status)}
            <span>${c.derived.paragraph_count} paragraphs</span>
            <span>${c.derived.unsupported_count} gaps</span>
          </div>
          <div class="mini-bars">
            <span class="mini-bar ok" style="flex:${Math.max(c.derived.supported_count,1)}"></span>
            <span class="mini-bar danger" style="flex:${Math.max(c.derived.unsupported_count,1)}"></span>
          </div>
        `,a.addEventListener("click",()=>L(c.path)),N.appendChild(a)});const e=P();C.textContent=e?e.data.title:"Nothing selected"},O=()=>{const t=P(),e=v();if(!t||!e){m.className="detail-scroll empty-state",m.textContent="Select a paragraph from the manuscript or section list.",x.textContent="Select one";return}m.className="detail-scroll",x.textContent=e.data.title||`Paragraph ${e.data.paragraph_index}`,m.innerHTML=`
        <div class="focus-card claim-card">
          <div class="focus-head stack">
            <div>
              <div class="focus-title">${n(e.data.title||`Paragraph ${e.data.paragraph_index}`)}</div>
              <div class="focus-subtitle">Section: ${n(t.data.title)}</div>
            </div>
            ${l(e.derived.support_status)}
          </div>

          <div class="support-strip">
            <div class="support-metric">
              <span class="metric-label">Notes</span>
              <strong>${e.derived.note_count}</strong>
            </div>
            <div class="support-metric">
              <span class="metric-label">Sources</span>
              <strong>${e.derived.source_count}</strong>
            </div>
            <div class="support-metric wide">
              <span class="metric-label">Open gaps</span>
              <strong>${e.derived.status_reasons.length||0}</strong>
            </div>
          </div>

          <section>
            <div class="section-label">Reading model</div>
            <div class="read-box">The paragraph text stays on the left. Use this panel to inspect structure, coverage, and linked support without duplicating the prose.</div>
          </section>

          <section>
            <div class="section-label">Trace diagnosis</div>
            <div class="trace-reasons card-reasons">${f(e.derived.status_reasons)}</div>
          </section>
        </div>
      `},G=()=>{const t=v(),e=t?.notes||[];if(!t){o.className="detail-scroll empty-state",o.textContent="Select a paragraph first.",S.textContent="Waiting";return}if(o.className="detail-scroll",!e.length){o.innerHTML='<div class="empty-state inner">No warrant note linked to this paragraph.</div>',S.textContent="No note";return}const c=h()||e[0];s.selectedNotePath=c.path,S.textContent=c.data.title,o.innerHTML=e.map(a=>`
        <section class="note-card ${a.path===s.selectedNotePath?"active":""}" data-note-path="${a.path}">
          <div class="note-card-head">
            <div>
              <div class="row-title">${n(a.data.title)}</div>
              <div class="row-meta compact">
                ${l(a.derived.support_status)}
                <span>${a.derived.source_count} source${a.derived.source_count===1?"":"s"}</span>
              </div>
            </div>
          </div>
          <div class="trace-block">
            <div class="section-label">Intent</div>
            <div class="read-box">${n(a.data.intent||"—")}</div>
          </div>
          <div class="trace-block">
            <div class="section-label">Claim</div>
            <div class="read-box">${n(a.data.claim||"—")}</div>
          </div>
          <div class="trace-block">
            <div class="section-label">Reasoning note</div>
            <div class="read-box note-body">${n(a.data.notes||"—")}</div>
          </div>
        </section>
      `).join(""),o.querySelectorAll("[data-note-path]").forEach(a=>{a.addEventListener("click",()=>H(a.dataset.notePath))})},I=()=>{const t=h(),e=t?.sources||[];if(!t){i.className="detail-scroll empty-state",i.textContent="Select a note first.",b.textContent="Waiting";return}if(i.className="detail-scroll",!e.length){i.innerHTML='<div class="empty-state inner">No evidence linked to this warrant.</div>',b.textContent="No source";return}const c=q()||e[0];s.selectedSourcePath=c.path,b.textContent=c.data.title,i.innerHTML=e.map(a=>`
        <section class="source-card ${a.path===s.selectedSourcePath?"active":""}" data-source-path="${a.path}">
          <div class="row-title">${n(a.data.title)}</div>
          <div class="row-meta compact">
            <span>${n(a.data.kind||"source")}</span>
            <span>${n(a.data.anchor||"")}</span>
          </div>
          <div class="trace-block">
            <div class="section-label">Relevance</div>
            <div class="read-box">${n(a.data.relevance||"—")}</div>
          </div>
          <div class="trace-block">
            <div class="section-label">Excerpt</div>
            <div class="read-box note-body">${n(a.data.excerpt||"—")}</div>
          </div>
          <div class="trace-block">
            <div class="section-label">Origin</div>
            <div class="read-box">${n(a.data.origin||"—")}</div>
          </div>
        </section>
      `).join(""),i.querySelectorAll("[data-source-path]").forEach(a=>{a.addEventListener("click",()=>j(a.dataset.sourcePath))})},g=()=>{A(),R(),O(),G(),I()},y=async()=>{u("Loading graph...");const t=await fetch("/api/graph.json"),e=await t.json();if(!t.ok){u(e);return}s.graph=e,s.selectedSectionPath||(s.selectedSectionPath=e.sections?.[0]?.path||""),s.selectedParagraphPath||(s.selectedParagraphPath=e.sections?.[0]?.paragraphs?.[0]?.path||"");const c=v();s.selectedNotePath||(s.selectedNotePath=c?.notes?.[0]?.path||"");const a=h();s.selectedSourcePath||(s.selectedSourcePath=a?.sources?.[0]?.path||""),u("Graph loaded"),g()},W=async()=>{u("Rebuilding pipeline...");const e=await(await fetch("/api/rebuild.json",{method:"POST"})).json();u(e),s.selectedSectionPath="",s.selectedParagraphPath="",s.selectedNotePath="",s.selectedSourcePath="",await y()};document.querySelector("#refresh-graph").addEventListener("click",y);document.querySelector("#rebuild").addEventListener("click",W);y();
