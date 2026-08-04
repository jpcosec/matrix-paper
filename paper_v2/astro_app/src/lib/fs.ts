import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const appRoot = path.dirname(fileURLToPath(import.meta.url));
export const paperRoot = path.resolve(appRoot, '../../..');

const ALLOWED_ROOTS = ['sources', 'notes', 'paragraphs', 'sections', 'manuscript', 'build'];

export type DocNode = {
  group: string;
  path: string;
  name: string;
};

export function resolveDocPath(relativePath: string): string {
  const normalized = relativePath.replace(/\\/g, '/').replace(/^\/+/, '');
  const first = normalized.split('/')[0];
  if (!ALLOWED_ROOTS.includes(first)) {
    throw new Error('Path outside allowed roots');
  }
  const absolute = path.resolve(paperRoot, normalized);
  if (!absolute.startsWith(paperRoot)) {
    throw new Error('Invalid path');
  }
  return absolute;
}

export async function listDocs(): Promise<DocNode[]> {
  const nodes: DocNode[] = [];
  for (const group of ALLOWED_ROOTS) {
    const dir = path.join(paperRoot, group);
    let entries: string[] = [];
    try {
      entries = await fs.readdir(dir);
    } catch {
      continue;
    }
    for (const name of entries.sort()) {
      if (!name.endsWith('.md') && !name.endsWith('.json')) continue;
      nodes.push({ group, name, path: `${group}/${name}` });
    }
  }
  return nodes;
}

export async function readDoc(relativePath: string): Promise<string> {
  const fullPath = resolveDocPath(relativePath);
  return fs.readFile(fullPath, 'utf-8');
}

export async function writeDoc(relativePath: string, content: string): Promise<void> {
  const fullPath = resolveDocPath(relativePath);
  await fs.writeFile(fullPath, content, 'utf-8');
}

export async function runRebuild(): Promise<{ code: number | null; stdout: string; stderr: string }> {
  return new Promise((resolve) => {
    const child = spawn('python3', ['build_pipeline.py'], {
      cwd: paperRoot,
      env: process.env,
    });
    let stdout = '';
    let stderr = '';
    child.stdout.on('data', (chunk) => {
      stdout += String(chunk);
    });
    child.stderr.on('data', (chunk) => {
      stderr += String(chunk);
    });
    child.on('close', (code) => resolve({ code, stdout, stderr }));
  });
}
