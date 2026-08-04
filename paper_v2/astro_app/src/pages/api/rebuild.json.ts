import type { APIRoute } from 'astro';
import { runRebuild } from '../../lib/fs';

export const POST: APIRoute = async () => {
  const result = await runRebuild();
  const status = result.code === 0 ? 200 : 500;
  return new Response(JSON.stringify(result, null, 2), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8' },
  });
};
