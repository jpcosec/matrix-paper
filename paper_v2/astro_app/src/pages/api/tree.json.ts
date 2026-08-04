import type { APIRoute } from 'astro';
import { listDocs } from '../../lib/fs';

export const GET: APIRoute = async () => {
  const docs = await listDocs();
  return new Response(JSON.stringify({ docs }, null, 2), {
    headers: { 'content-type': 'application/json; charset=utf-8' },
  });
};
