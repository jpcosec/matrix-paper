import { promises } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const appRoot = path.dirname(fileURLToPath(import.meta.url));
const paperRoot = path.resolve(appRoot, "../../..");
const ALLOWED_ROOTS = ["sources", "notes", "paragraphs", "sections", "manuscript", "build"];
function resolveDocPath(relativePath) {
  const normalized = relativePath.replace(/\\/g, "/").replace(/^\/+/, "");
  const first = normalized.split("/")[0];
  if (!ALLOWED_ROOTS.includes(first)) {
    throw new Error("Path outside allowed roots");
  }
  const absolute = path.resolve(paperRoot, normalized);
  if (!absolute.startsWith(paperRoot)) {
    throw new Error("Invalid path");
  }
  return absolute;
}
async function listDocs() {
  const nodes = [];
  for (const group of ALLOWED_ROOTS) {
    const dir = path.join(paperRoot, group);
    let entries = [];
    try {
      entries = await promises.readdir(dir);
    } catch {
      continue;
    }
    for (const name of entries.sort()) {
      if (!name.endsWith(".md") && !name.endsWith(".json")) continue;
      nodes.push({ group, name, path: `${group}/${name}` });
    }
  }
  return nodes;
}
async function readDoc(relativePath) {
  const fullPath = resolveDocPath(relativePath);
  return promises.readFile(fullPath, "utf-8");
}
async function writeDoc(relativePath, content) {
  const fullPath = resolveDocPath(relativePath);
  await promises.writeFile(fullPath, content, "utf-8");
}
async function runRebuild() {
  return new Promise((resolve) => {
    const child = spawn("python3", ["build_pipeline.py"], {
      cwd: paperRoot,
      env: process.env
    });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (chunk) => {
      stdout += String(chunk);
    });
    child.stderr.on("data", (chunk) => {
      stderr += String(chunk);
    });
    child.on("close", (code) => resolve({ code, stdout, stderr }));
  });
}

export { runRebuild as a, listDocs as l, readDoc as r, writeDoc as w };
