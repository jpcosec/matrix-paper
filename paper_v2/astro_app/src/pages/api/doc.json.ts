import type { APIRoute } from 'astro';
import { readDoc, writeDoc } from '../../lib/fs';

export const GET: APIRoute = async ({ request }) => {
  const url = new URL(request.url);
  const docPath = url.searchParams.get('path');
  if (!docPath) {
    return new Response(JSON.stringify({ error: 'Missing path' }), { status: 400 });
  }
  try {
    const content = await readDoc(docPath);
    return new Response(JSON.stringify({ path: docPath, content }, null, 2), {
      headers: { 'content-type': 'application/json; charset=utf-8' },
    });
  } catch (error) {
    return new Response(
      JSON.stringify({ error: error instanceof Error ? error.message : 'Read failed' }),
      { status: 400 },
    );
  }
};

export const POST: APIRoute = async ({ request }) => {
  const body = await request.json().catch(() => null);
  const docPath = body?.path;
  const content = body?.content;
  if (!docPath || typeof content !== 'string') {
    return new Response(JSON.stringify({ error: 'Missing path or content' }), { status: 400 });
  }
  try {
    await writeDoc(docPath, content);
    return new Response(JSON.stringify({ ok: true, path: docPath }), {
      headers: { 'content-type': 'application/json; charset=utf-8' },
    });
  } catch (error) {
    return new Response(
      JSON.stringify({ error: error instanceof Error ? error.message : 'Write failed' }),
      { status: 400 },
    );
  }
};
