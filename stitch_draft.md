
<!-- Editorial Column Browser -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>paper_v2 Editor</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&amp;family=Source+Serif+4:wght@400&amp;family=Geist:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "inverse-on-surface": "#eef0ff",
                    "primary-fixed": "#d8e3fb",
                    "on-tertiary-container": "#8b9094",
                    "on-primary-fixed-variant": "#3c475a",
                    "surface": "#faf8ff",
                    "tertiary-fixed-dim": "#c3c7cb",
                    "surface-container-high": "#e2e7ff",
                    "on-secondary": "#ffffff",
                    "on-secondary-fixed": "#07006c",
                    "surface-container-low": "#f2f3ff",
                    "on-tertiary-fixed": "#171c1f",
                    "on-primary-fixed": "#111c2d",
                    "on-primary-container": "#8590a6",
                    "on-background": "#131b2e",
                    "background": "#faf8ff",
                    "secondary-fixed-dim": "#c0c1ff",
                    "inverse-surface": "#283044",
                    "on-error": "#ffffff",
                    "on-error-container": "#93000a",
                    "surface-container-lowest": "#ffffff",
                    "on-secondary-fixed-variant": "#2f2ebe",
                    "error-container": "#ffdad6",
                    "surface-container": "#eaedff",
                    "on-tertiary-fixed-variant": "#43474b",
                    "surface-bright": "#faf8ff",
                    "on-secondary-container": "#fffbff",
                    "outline": "#75777d",
                    "on-surface-variant": "#45474c",
                    "outline-variant": "#c5c6cd",
                    "surface-variant": "#dae2fd",
                    "secondary": "#4648d4",
                    "primary-container": "#1e293b",
                    "secondary-container": "#6063ee",
                    "secondary-fixed": "#e1e0ff",
                    "primary-fixed-dim": "#bcc7de",
                    "on-tertiary": "#ffffff",
                    "tertiary-container": "#24292c",
                    "on-surface": "#131b2e",
                    "tertiary": "#101517",
                    "surface-container-highest": "#dae2fd",
                    "error": "#ba1a1a",
                    "primary": "#091426",
                    "surface-tint": "#545f73",
                    "inverse-primary": "#bcc7de",
                    "surface-dim": "#d2d9f4",
                    "tertiary-fixed": "#dfe3e7",
                    "on-primary": "#ffffff"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "ui-padding-sm": "8px",
                    "ui-padding-md": "16px",
                    "max-width-reading": "720px",
                    "ui-padding-xs": "4px",
                    "column-gap": "1px",
                    "manuscript-margin": "80px"
            },
            "fontFamily": {
                    "h1-manuscript": [
                            "Playfair Display"
                    ],
                    "mono-ui": [
                            "Geist"
                    ],
                    "ui-label": [
                            "Geist"
                    ],
                    "display-manuscript": [
                            "Playfair Display"
                    ],
                    "ui-header": [
                            "Geist"
                    ],
                    "body-manuscript": [
                            "\"Source Serif 4\""
                    ],
                    "ui-body": [
                            "Geist"
                    ]
            },
            "fontSize": {
                    "h1-manuscript": [
                            "32px",
                            {
                                    "lineHeight": "40px",
                                    "fontWeight": "600"
                            }
                    ],
                    "mono-ui": [
                            "12px",
                            {
                                    "lineHeight": "16px",
                                    "fontWeight": "400"
                            }
                    ],
                    "ui-label": [
                            "11px",
                            {
                                    "lineHeight": "16px",
                                    "fontWeight": "500"
                            }
                    ],
                    "display-manuscript": [
                            "42px",
                            {
                                    "lineHeight": "52px",
                                    "letterSpacing": "-0.02em",
                                    "fontWeight": "700"
                            }
                    ],
                    "ui-header": [
                            "14px",
                            {
                                    "lineHeight": "20px",
                                    "letterSpacing": "0.05em",
                                    "fontWeight": "600"
                            }
                    ],
                    "body-manuscript": [
                            "18px",
                            {
                                    "lineHeight": "32px",
                                    "fontWeight": "400"
                            }
                    ],
                    "ui-body": [
                            "13px",
                            {
                                    "lineHeight": "18px",
                                    "fontWeight": "400"
                            }
                    ]
            }
    },
        },
      }
    </script>
<style>
        /* Custom ultra-thin scrollbar for editorial columns */
        .editorial-scroll::-webkit-scrollbar {
            width: 4px;
            height: 4px;
            background-color: transparent;
        }
        .editorial-scroll:hover::-webkit-scrollbar {
            background-color: transparent;
        }
        .editorial-scroll::-webkit-scrollbar-thumb {
            background-color: transparent;
            border-radius: 4px;
        }
        .editorial-scroll:hover::-webkit-scrollbar-thumb {
            background-color: rgba(203, 213, 225, 0.5); /* Slate 300, 50% */
        }
        .editorial-scroll {
            scrollbar-width: thin;
            scrollbar-color: transparent transparent;
            transition: scrollbar-color 0.3s ease;
        }
        .editorial-scroll:hover {
            scrollbar-color: rgba(203, 213, 225, 0.5) transparent;
        }
    </style>
</head>
<body class="bg-surface text-on-surface h-screen w-screen overflow-hidden flex flex-col font-ui-body text-ui-body">
<!-- TopAppBar (from JSON) -->
<header class="bg-primary text-on-primary font-ui-header text-ui-header docked full-width top-0 bg-primary flat no shadows flex justify-between items-center w-full px-ui-padding-md h-16 z-50">
<div class="flex items-center gap-6">
<div class="font-h1-manuscript text-h1-manuscript text-on-primary tracking-tight">paper_v2</div>
<nav class="hidden md:flex gap-4 items-center h-full">
<a class="text-secondary-fixed font-bold border-b-2 border-secondary-fixed pb-1 h-full flex items-center hover:text-primary-fixed transition-colors opacity-80" href="#">Manuscript</a>
<a class="text-on-primary-fixed-variant h-full flex items-center hover:text-primary-fixed transition-colors" href="#">Archive</a>
<a class="text-on-primary-fixed-variant h-full flex items-center hover:text-primary-fixed transition-colors" href="#">Library</a>
<a class="text-on-primary-fixed-variant h-full flex items-center hover:text-primary-fixed transition-colors" href="#">Sources</a>
</nav>
</div>
<div class="flex items-center gap-4">
<button class="text-on-primary hover:text-primary-fixed transition-colors">
<span class="material-symbols-outlined">account_circle</span>
</button>
<button class="text-on-primary hover:text-primary-fixed transition-colors">
<span class="material-symbols-outlined">settings</span>
</button>
</div>
</header>
<div class="flex flex-1 h-[calc(100vh-64px)] overflow-hidden">
<!-- SideNavBar (from JSON) -->
<nav class="bg-primary text-on-primary font-ui-label text-ui-label docked full-height left-0 w-20 border-r border-outline-variant flat no shadows fixed left-0 top-16 bottom-0 flex flex-col items-center py-ui-padding-md z-40">
<!-- Active Tab: Sections (Semantic Match for Editorial Browser) -->
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">edit_note</span>
                Drafts
            </a>
<a class="flex flex-col items-center justify-center bg-primary-container text-on-primary-container border-l-4 border-secondary-container w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all scale-95 opacity-80" href="#">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 1;">segment</span>
                Sections
            </a>
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">subject</span>
                Paragraphs
            </a>
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">description</span>
                Notes
            </a>
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">menu_book</span>
                Sources
            </a>
<div class="mt-auto w-full flex flex-col items-center gap-2">
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-2 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">help</span>
                    Help
                </a>
<a class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-2 hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
<span class="material-symbols-outlined mb-1">feedback</span>
                    Feedback
                </a>
</div>
</nav>
<!-- Main Workspace Area -->
<main class="flex flex-1 ml-20 h-full overflow-hidden">
<!-- Left Pane: Reader View -->
<section class="w-2/5 h-full bg-surface-container-lowest overflow-y-auto border-r border-outline-variant editorial-scroll">
<div class="max-w-reading mx-auto px-8 py-manuscript-margin">
<h1 class="font-display-manuscript text-display-manuscript text-on-surface mb-8">Logical and Semantic Guarantees in LLMs Require More Than Continuous Embeddings</h1>
<h2 class="font-h1-manuscript text-h1-manuscript text-on-surface mt-12 mb-4">Abstract</h2>
<p class="font-body-manuscript text-body-manuscript text-on-surface-variant mb-6 text-justify">
                        This position paper argues that continuous embeddings are insufficient as the sole semantic substrate for reliable LLM-based systems. Embeddings support similarity, generalization, and retrieval, but they do not by themselves define what counts as a valid proposition, a category error, a contextual truth, or a recoverable explanation. We argue that future AI systems need an additional representational layer: locally scoped logical spaces in which linguistic signs are separated from logical structure, and propositions are compiled into typed, auditable, context-bound coordinates. To support this position, we define a representational and operational framework for world-local semantic validation. In this framework, each local world specifies its own universe of concepts, admissible relations, rules of sense, signatures, masks, and denotation functions. LLMs or human operators may assist with semantic disambiguation, but candidate propositions must pass through symbolic validation before being asserted as knowledge. Mathematically, the framework is grounded in a contextualized boolean algebra over typed binary signatures, with XOR-based contrasts, boolean operations for semantic filtering, matrix indices over the boolean semiring, and partition refinements induced by discriminative dimensions. Our central claim is that hallucination mitigation should not be treated only as a retrieval or calibration problem. It should also be treated as a representability problem: systems should reject propositions that cannot be expressed within the local grammar of sense.
                    </p>
<!-- Highlighted Active Section -->
<div class="bg-surface-container-low border-l-4 border-secondary-container p-6 -mx-6 my-8 rounded-r-lg">
<h2 class="font-h1-manuscript text-h1-manuscript text-on-surface mb-4">Introduction</h2>
<p class="font-body-manuscript text-body-manuscript text-on-surface-variant text-justify">
                            The rapid advancement of Large Language Models (LLMs) has demonstrated an unprecedented capacity for fluent text generation and complex pattern matching. However, these systems remain plagued by a fundamental instability that predates them and is the cause of drift, unpredictable behaviour and hallucinations , the symbol grounding problem [@harnad1990symbolgrounding]. Current research efforts primarily address this issue through epistemic improvements, such as Retrieval-Augmented Generation or Reinforcement Learning from Human Feedback. We argue, however, that the root of this instability is representational rather than purely informational. The reliance on continuous vector spaces as the sole substrate for semantic encoding excels at capturing fuzzy similarities but lacks the discrete primitives necessary to define the rigorous boundaries of logical sense. Consequently, current architectures often conflate falsehood with fundamental inapplicability. To address this representational gap, this paper argues for the necessity of a discrete, locally scoped representational layer that explicitly separates the stochastic nature of linguistic signs from their underlying deterministic logical structure. Drawing upon the logical atomism of Ludwig Wittgenstein's Tractatus Logico-Philosophicus—specifically the premise that the logical structure of the world is determined by facts rather than isolated things — **we propose a transition from probabilistic distances to verifiable, algebraic logical coordinates.** Under this framework, propositions must be evaluated not only by their truth value but by their state of meaning: Sinnvoll (meaningful), Sinnlos (tautological or contradictory), and Unsinnig (absurd or structurally inapplicable) . By treating the validity of assertions as a problem of representability within a strict grammar of sense, we propose decoupling language
                        </p>
</div>
</div>
</section>
<!-- Right Pane: Editorial Browser (Horizontally Scrolling Columns) -->
<section class="w-3/5 h-full bg-surface flex overflow-x-auto editorial-scroll">
<!-- Column 1: Section Details -->
<div class="w-80 flex-shrink-0 border-r border-outline-variant h-full flex flex-col bg-surface-bright">
<div class="p-4 border-b border-outline-variant bg-surface flex items-center justify-between sticky top-0 z-10">
<span class="font-ui-header text-ui-header text-on-surface">section</span>
</div>
<div class="p-4 flex-1 overflow-y-auto editorial-scroll">
<h3 class="font-ui-header text-ui-header text-on-surface mb-2">Introduction</h3>
<div class="font-mono-ui text-mono-ui text-on-surface-variant mb-6 pb-2 border-b border-outline-variant">sections/01_introduction.md</div>
<!-- Missing Data Pill -->
<div class="mb-6 flex flex-col gap-1">
<span class="font-ui-label text-ui-label text-on-surface font-semibold">Missing</span>
<div class="inline-flex">
<span class="bg-surface-variant text-on-surface-variant px-2 py-1 rounded-DEFAULT font-mono-ui text-mono-ui">none</span>
</div>
</div>
<!-- Editable Fields -->
<div class="space-y-4">
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">title</label>
<input class="w-full bg-surface-container-lowest border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-ui-body text-ui-body text-on-surface transition-all" type="text" value="Introduction"/>
</div>
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">section_id</label>
<input class="w-full bg-surface-container-lowest border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-mono-ui text-mono-ui text-on-surface transition-all" type="text" value="01_introduction"/>
</div>
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">source_section_file</label>
<input class="w-full bg-surface-container-lowest border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-mono-ui text-mono-ui text-on-surface transition-all" type="text" value="sections/01_introduction.md"/>
</div>
</div>
<!-- Child List (Paragraphs) -->
<div class="mt-8">
<span class="block font-ui-label text-ui-label text-on-surface-variant mb-2">Paragraphs</span>
<div class="flex flex-col gap-1">
<button class="text-left px-3 py-2 bg-surface hover:bg-surface-container-low text-on-surface text-ui-body rounded transition-colors border border-transparent">Introduction paragraph 01</button>
<!-- Active Item -->
<button class="text-left px-3 py-2 bg-surface-container-low text-secondary-fixed-variant font-medium text-ui-body rounded border-l-4 border-secondary-container flex justify-between items-center group">
                                    Introduction paragraph 02
                                    <span class="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity">chevron_right</span>
</button>
<button class="text-left px-3 py-2 bg-surface hover:bg-surface-container-low text-on-surface text-ui-body rounded transition-colors border border-transparent">Introduction paragraph 03</button>
<button class="text-left px-3 py-2 bg-surface hover:bg-surface-container-low text-on-surface text-ui-body rounded transition-colors border border-transparent">Introduction paragraph 04</button>
</div>
</div>
</div>
</div>
<!-- Column 2: Paragraph Details -->
<div class="w-80 flex-shrink-0 border-r border-outline-variant h-full flex flex-col bg-surface-container-lowest">
<div class="p-4 border-b border-outline-variant bg-surface-bright flex items-center justify-between sticky top-0 z-10">
<span class="font-ui-header text-ui-header text-on-surface">paragraph</span>
</div>
<div class="p-4 flex-1 overflow-y-auto editorial-scroll">
<h3 class="font-ui-header text-ui-header text-on-surface mb-2">Introduction paragraph 02</h3>
<div class="font-mono-ui text-mono-ui text-on-surface-variant mb-6 pb-2 border-b border-outline-variant">paragraphs/01_introduction-p02.md</div>
<!-- Missing Data Pill (Warning) -->
<div class="mb-6 flex flex-col gap-1">
<span class="font-ui-label text-ui-label text-on-surface font-semibold">Missing</span>
<div class="inline-flex">
<span class="bg-error-container text-on-error-container px-2 py-1 rounded-DEFAULT font-mono-ui text-mono-ui border border-error/20 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">warning</span>
                                    notes_refs
                                </span>
</div>
</div>
<!-- Editable Fields -->
<div class="space-y-4">
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">title</label>
<input class="w-full bg-surface border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-ui-body text-ui-body text-on-surface transition-all" type="text" value="Introduction paragraph 02"/>
</div>
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">section_id</label>
<input class="w-full bg-surface border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-mono-ui text-mono-ui text-on-surface transition-all" readonly="" type="text" value="01_introduction"/>
</div>
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">paragraph_index</label>
<input class="w-full bg-surface border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-mono-ui text-mono-ui text-on-surface transition-all" type="text" value="2"/>
</div>
<div>
<label class="block font-ui-label text-ui-label text-on-surface-variant mb-1">paragraph_text</label>
<textarea class="w-full bg-surface border-0 border-b border-outline hover:border-outline-variant focus:border-secondary-container focus:border-b-2 focus:ring-0 px-2 py-1 font-ui-body text-ui-body text-on-surface transition-all resize-none" rows="4">To address this representational gap, this paper argues for the necessity of a discrete...</textarea>
</div>
</div>
<!-- Child List (Notes) -->
<div class="mt-8">
<span class="block font-ui-label text-ui-label text-on-surface-variant mb-2">Notes</span>
<div class="flex flex-col gap-1">
<button class="text-left px-3 py-2 bg-surface-bright hover:bg-surface-container-low text-on-surface text-ui-body rounded transition-colors border border-transparent flex items-center justify-between group">
                                    Introduction note 02
                                    <span class="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity">open_in_new</span>
</button>
</div>
</div>
</div>
</div>
<!-- Ghost space to allow scrolling past last column -->
<div class="w-16 flex-shrink-0"></div>
</section>
</main>
</div>
</body></html>

<!-- Editorial Column Browser V2 (Desktop) -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Editorial Column Browser V2</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&amp;family=Playfair+Display:wght@600;700&amp;family=Source+Serif+4:wght@400&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              "colors": {
                      "tertiary-fixed-dim": "#c3c7cb",
                      "surface-dim": "#d2d9f4",
                      "on-primary-fixed": "#111c2d",
                      "surface-container-highest": "#dae2fd",
                      "outline-variant": "#c5c6cd",
                      "on-tertiary": "#ffffff",
                      "primary-container": "#1e293b",
                      "tertiary-container": "#24292c",
                      "tertiary": "#101517",
                      "on-primary-fixed-variant": "#3c475a",
                      "surface": "#faf8ff",
                      "surface-container-lowest": "#ffffff",
                      "inverse-on-surface": "#eef0ff",
                      "surface-bright": "#faf8ff",
                      "inverse-primary": "#bcc7de",
                      "error": "#ba1a1a",
                      "on-error-container": "#93000a",
                      "surface-container": "#eaedff",
                      "on-secondary-fixed": "#07006c",
                      "primary-fixed-dim": "#bcc7de",
                      "on-tertiary-container": "#8b9094",
                      "on-secondary-container": "#fffbff",
                      "on-surface": "#131b2e",
                      "secondary-container": "#6063ee",
                      "tertiary-fixed": "#dfe3e7",
                      "outline": "#75777d",
                      "error-container": "#ffdad6",
                      "on-primary-container": "#8590a6",
                      "secondary-fixed": "#e1e0ff",
                      "surface-variant": "#dae2fd",
                      "on-tertiary-fixed-variant": "#43474b",
                      "primary-fixed": "#d8e3fb",
                      "on-secondary-fixed-variant": "#2f2ebe",
                      "primary": "#091426",
                      "surface-tint": "#545f73",
                      "secondary": "#4648d4",
                      "on-tertiary-fixed": "#171c1f",
                      "on-primary": "#ffffff",
                      "on-error": "#ffffff",
                      "background": "#faf8ff",
                      "surface-container-high": "#e2e7ff",
                      "on-secondary": "#ffffff",
                      "secondary-fixed-dim": "#c0c1ff",
                      "on-surface-variant": "#45474c",
                      "inverse-surface": "#283044",
                      "on-background": "#131b2e",
                      "surface-container-low": "#f2f3ff"
              },
              "borderRadius": {
                      "DEFAULT": "0.125rem",
                      "lg": "0.25rem",
                      "xl": "0.5rem",
                      "full": "0.75rem"
              },
              "spacing": {
                      "manuscript-margin": "80px",
                      "ui-padding-sm": "8px",
                      "ui-padding-xs": "4px",
                      "column-gap": "1px",
                      "ui-padding-md": "16px",
                      "max-width-reading": "720px"
              },
              "fontFamily": {
                      "ui-label": ["Geist"],
                      "body-manuscript": ["\"Source Serif 4\""],
                      "display-manuscript": ["Playfair Display"],
                      "ui-body": ["Geist"],
                      "h1-manuscript": ["Playfair Display"],
                      "mono-ui": ["Geist"],
                      "ui-header": ["Geist"]
              },
              "fontSize": {
                      "ui-label": ["11px", {"lineHeight": "16px", "fontWeight": "500"}],
                      "body-manuscript": ["18px", {"lineHeight": "32px", "fontWeight": "400"}],
                      "display-manuscript": ["42px", {"lineHeight": "52px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                      "ui-body": ["13px", {"lineHeight": "18px", "fontWeight": "400"}],
                      "h1-manuscript": ["32px", {"lineHeight": "40px", "fontWeight": "600"}],
                      "mono-ui": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                      "ui-header": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}]
              }
            }
          }
        }
    </script>
<style>
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background-color: transparent;
            border-radius: 4px;
        }
        .custom-scrollbar:hover::-webkit-scrollbar-thumb {
            background-color: #c5c6cd; /* outline-variant */
        }
        .pane-divider {
            border-right: 1px solid #e2e7ff; /* surface-container-high */
        }
    </style>
</head>
<body class="bg-surface text-on-surface h-screen w-full flex overflow-hidden">
<!-- SideNavBar -->
<nav class="bg-primary dark:bg-primary text-on-primary dark:text-on-primary font-ui-label text-ui-label font-ui-header text-ui-header text-on-primary docked full-height left-0 w-20 border-r border-outline-variant flat no shadows fixed left-0 top-16 bottom-0 flex flex-col items-center py-ui-padding-md z-40">
<div class="flex flex-col gap-2 w-full mt-4">
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">edit_note</span>
<span>Drafts</span>
</button>
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">segment</span>
<span>Sections</span>
</button>
<button class="flex flex-col items-center justify-center bg-primary-container text-on-primary-container border-l-4 border-secondary-container w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 1;">subject</span>
<span>Paragraphs</span>
</button>
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">description</span>
<span>Notes</span>
</button>
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">menu_book</span>
<span>Sources</span>
</button>
</div>
<div class="mt-auto flex flex-col w-full">
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">help</span>
<span>Help</span>
</button>
<button class="flex flex-col items-center justify-center text-on-primary-fixed-variant w-full py-4 hover:bg-primary-container hover:text-on-primary-container transition-all">
<span class="material-symbols-outlined mb-1" style="font-variation-settings: 'FILL' 0;">feedback</span>
<span>Feedback</span>
</button>
</div>
</nav>
<!-- Main Content Area -->
<div class="flex-1 flex flex-col ml-20 h-full overflow-hidden">
<!-- TopAppBar -->
<header class="bg-primary dark:bg-primary text-on-primary dark:text-on-primary font-ui-header text-ui-header font-h1-manuscript text-h1-manuscript text-on-primary docked full-width top-0 bg-primary flat no shadows flex justify-between items-center w-full px-ui-padding-md h-16 z-50">
<div class="flex items-center gap-6">
<span class="font-h1-manuscript text-h1-manuscript">paper_v2</span>
<nav class="flex gap-4">
<button class="text-on-primary-fixed-variant hover:text-primary-fixed transition-colors">Manuscript</button>
<button class="text-on-primary-fixed-variant hover:text-primary-fixed transition-colors">Archive</button>
<button class="text-secondary-fixed font-bold border-b-2 border-secondary-fixed pb-1 hover:text-primary-fixed transition-colors">Library</button>
<button class="text-on-primary-fixed-variant hover:text-primary-fixed transition-colors">Sources</button>
</nav>
</div>
<div class="flex items-center gap-4">
<span class="material-symbols-outlined text-on-primary hover:text-primary-fixed transition-colors cursor-pointer" style="font-variation-settings: 'FILL' 0;">account_circle</span>
<span class="material-symbols-outlined text-on-primary hover:text-primary-fixed transition-colors cursor-pointer" style="font-variation-settings: 'FILL' 0;">settings</span>
</div>
</header>
<!-- Column Browser Layout -->
<main class="flex-1 flex overflow-x-auto overflow-y-hidden custom-scrollbar bg-surface-container-lowest">
<!-- Column 1: Manuscript Reader -->
<section class="min-w-[400px] max-w-[600px] flex-shrink-0 pane-divider h-full overflow-y-auto custom-scrollbar px-10 py-manuscript-margin bg-surface-container-lowest relative">
<div class="max-w-[720px] mx-auto">
<h1 class="font-display-manuscript text-display-manuscript text-on-surface mb-8">The Nature of Digital Archives</h1>
<p class="font-body-manuscript text-body-manuscript text-on-surface mb-6 opacity-80">
                        In the shift from physical to digital, the fundamental concept of an archive undergoes a transformation. It is no longer a static repository of documents, but a dynamic, interconnected web of information.
                    </p>
<div class="relative bg-surface-container-low -mx-4 px-4 py-2 rounded">
<div class="absolute left-0 top-0 bottom-0 w-1 bg-secondary-container rounded-l"></div>
<p class="font-body-manuscript text-body-manuscript text-on-surface">
                            This transition challenges traditional notions of permanence and provenance. Where a physical manuscript carries the literal marks of its creator, a digital file is endlessly reproducible, demanding new systems for verification and authenticity.
                        </p>
</div>
<p class="font-body-manuscript text-body-manuscript text-on-surface mt-6 opacity-80">
                        Furthermore, the architecture of digital systems imposes its own logic on the data it holds. Categorization becomes algorithmic, and search replaces serendipitous discovery.
                    </p>
</div>
</section>
<!-- Column 2: Sections List -->
<section class="w-80 flex-shrink-0 pane-divider h-full flex flex-col bg-surface-bright">
<div class="px-4 py-3 border-b border-surface-container-high bg-surface-container-lowest sticky top-0">
<h2 class="font-ui-header text-ui-header text-on-surface">Sections</h2>
</div>
<div class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-1">
<div class="p-3 rounded hover:bg-surface-container-low cursor-pointer transition-colors">
<div class="font-ui-body text-ui-body font-medium text-on-surface mb-1 truncate">Introduction: The Shift</div>
<div class="flex justify-between items-center text-on-surface-variant font-mono-ui text-mono-ui">
<span>4 Paragraphs</span>
<span>1200w</span>
</div>
</div>
<div class="p-3 rounded bg-surface-container text-on-surface cursor-pointer border-l-2 border-secondary-container">
<div class="font-ui-body text-ui-body font-medium mb-1 truncate">Permanence and Provenance</div>
<div class="flex justify-between items-center text-on-surface-variant font-mono-ui text-mono-ui">
<span>6 Paragraphs</span>
<span>1850w</span>
</div>
</div>
<div class="p-3 rounded hover:bg-surface-container-low cursor-pointer transition-colors">
<div class="font-ui-body text-ui-body font-medium text-on-surface mb-1 truncate">Algorithmic Architectures</div>
<div class="flex justify-between items-center text-on-surface-variant font-mono-ui text-mono-ui">
<span>5 Paragraphs</span>
<span>1420w</span>
</div>
</div>
</div>
</section>
<!-- Column 3: Paragraph Focus -->
<section class="w-96 flex-shrink-0 pane-divider h-full flex flex-col bg-surface-container-lowest">
<div class="px-4 py-3 border-b border-surface-container-high sticky top-0 flex justify-between items-center">
<h2 class="font-ui-header text-ui-header text-on-surface">Paragraph</h2>
<span class="material-symbols-outlined text-outline-variant text-[18px] cursor-pointer hover:text-on-surface">open_in_full</span>
</div>
<div class="flex-1 overflow-y-auto custom-scrollbar p-4">
<textarea class="w-full h-48 resize-none bg-transparent border-0 border-b border-outline-variant focus:border-secondary focus:ring-0 font-ui-body text-ui-body text-on-surface p-0 pb-2 custom-scrollbar focus:border-b-2 transition-all">This transition challenges traditional notions of permanence and provenance. Where a physical manuscript carries the literal marks of its creator, a digital file is endlessly reproducible, demanding new systems for verification and authenticity.</textarea>
<div class="mt-6">
<h3 class="font-ui-label text-ui-label text-on-surface-variant mb-2 uppercase tracking-wider">Metadata</h3>
<div class="flex gap-2 mb-4">
<span class="inline-flex items-center px-2 py-1 rounded bg-error-container text-on-error-container font-ui-label text-ui-label">
<span class="material-symbols-outlined text-[14px] mr-1">warning</span>
                                Needs Citation
                            </span>
<span class="inline-flex items-center px-2 py-1 rounded bg-surface-container-high text-on-surface-variant font-ui-label text-ui-label">
                                Draft v3
                            </span>
</div>
</div>
</div>
</section>
<!-- Column 4: Notes -->
<section class="w-80 flex-shrink-0 h-full flex flex-col bg-surface-bright">
<div class="px-4 py-3 border-b border-surface-container-high sticky top-0 flex justify-between items-center bg-surface-container-lowest">
<h2 class="font-ui-header text-ui-header text-on-surface">Notes</h2>
<span class="material-symbols-outlined text-outline-variant text-[18px] cursor-pointer hover:text-on-surface">add</span>
</div>
<div class="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-3">
<div class="bg-surface-container-lowest p-3 rounded border border-surface-container-high shadow-sm">
<div class="font-ui-label text-ui-label text-on-surface-variant mb-1 uppercase">Intent</div>
<div class="font-ui-body text-ui-body text-on-surface">Establish the core tension between physical uniqueness and digital reproducibility.</div>
</div>
<div class="bg-surface-container-lowest p-3 rounded border border-surface-container-high shadow-sm relative overflow-hidden">
<div class="absolute left-0 top-0 bottom-0 w-1 bg-secondary-container"></div>
<div class="font-ui-label text-ui-label text-on-surface-variant mb-1 uppercase">Claim</div>
<div class="font-ui-body text-ui-body text-on-surface">Digital files lack inherent provenance markers compared to physical texts.</div>
<div class="mt-2 text-error font-ui-label text-ui-label flex items-center">
<span class="material-symbols-outlined text-[14px] mr-1">info</span>
                            Evidence pending
                        </div>
</div>
</div>
</section>
</main>
</div>
</body></html>

