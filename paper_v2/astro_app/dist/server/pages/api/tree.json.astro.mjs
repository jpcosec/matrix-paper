import { l as listDocs } from '../../chunks/fs_BAuakhth.mjs';
export { renderers } from '../../renderers.mjs';

const GET = async () => {
  const docs = await listDocs();
  return new Response(JSON.stringify({ docs }, null, 2), {
    headers: { "content-type": "application/json; charset=utf-8" }
  });
};

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  GET
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
