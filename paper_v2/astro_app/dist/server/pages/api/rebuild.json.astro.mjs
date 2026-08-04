import { a as runRebuild } from '../../chunks/fs_BAuakhth.mjs';
export { renderers } from '../../renderers.mjs';

const POST = async () => {
  const result = await runRebuild();
  const status = result.code === 0 ? 200 : 500;
  return new Response(JSON.stringify(result, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" }
  });
};

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  POST
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
