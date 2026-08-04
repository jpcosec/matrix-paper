import { renderers } from './renderers.mjs';
import { c as createExports, s as serverEntrypointModule } from './chunks/_@astrojs-ssr-adapter_B4fXvQ4N.mjs';
import { manifest } from './manifest_KMK0lAfJ.mjs';

const _page0 = () => import('./pages/_image.astro.mjs');
const _page1 = () => import('./pages/api/doc.json.astro.mjs');
const _page2 = () => import('./pages/api/graph.json.astro.mjs');
const _page3 = () => import('./pages/api/rebuild.json.astro.mjs');
const _page4 = () => import('./pages/api/tree.json.astro.mjs');
const _page5 = () => import('./pages/index.astro.mjs');

const pageMap = new Map([
    ["node_modules/astro/dist/assets/endpoint/node.js", _page0],
    ["src/pages/api/doc.json.ts", _page1],
    ["src/pages/api/graph.json.ts", _page2],
    ["src/pages/api/rebuild.json.ts", _page3],
    ["src/pages/api/tree.json.ts", _page4],
    ["src/pages/index.astro", _page5]
]);
const serverIslandMap = new Map();
const _manifest = Object.assign(manifest, {
    pageMap,
    serverIslandMap,
    renderers,
    middleware: () => import('./_noop-middleware.mjs')
});
const _args = {
    "mode": "standalone",
    "client": "file:///home/jp/proyectos/Matrix/paper_v2/astro_app/dist/client/",
    "server": "file:///home/jp/proyectos/Matrix/paper_v2/astro_app/dist/server/",
    "host": true,
    "port": 4321,
    "assets": "_astro"
};
const _exports = createExports(_manifest, _args);
const handler = _exports['handler'];
const startServer = _exports['startServer'];
const options = _exports['options'];
const _start = 'start';
{
	serverEntrypointModule[_start](_manifest, _args);
}

export { handler, options, pageMap, startServer };
