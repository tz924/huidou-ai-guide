"""Validate portable documentation links and bundled evidence; standard library only."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
errors = []
required = ['README.md', 'AGENTS.md', 'CLAUDE.md', 'docs/GUIDE.md',
            'docs/AI-ADAPTERS.md', 'docs/SECOND-COMPUTER.md',
            'progress/STATUS.md', 'progress/TODO.md', 'progress/FEATURE-MATRIX.csv']
for name in required:
    if not (root / name).is_file():
        errors.append(f'Missing required file: {name}')
for folder in ['docs', 'progress', 'prompts', 'templates']:
    for p in (root / folder).glob('*.md'):
        if not p.read_text(encoding='utf-8-sig').strip():
            errors.append(f'Empty document: {p.relative_to(root)}')
for p in [root / 'README.md', *root.glob('docs/*.md')]:
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8-sig')):
        if re.match(r'^[a-z]+://', target) or target.startswith('#'):
            continue
        target = unquote(target.split('#')[0].strip('<>'))
        if target and not (p.parent / target).exists():
            errors.append(f'Broken local link: {p.relative_to(root)} -> {target}')
if '@AGENTS.md' not in (root / 'CLAUDE.md').read_text(encoding='utf-8'):
    errors.append('Claude entry must import the shared AGENTS.md')
with (root / 'progress/FEATURE-MATRIX.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
if not rows or not {'功能', '状态', '验证内容及边界'}.issubset(rows[0]):
    errors.append('Feature matrix schema missing')
for row in rows:
    if not all(row.values()):
        errors.append(f'Incomplete feature row: {row}')
manifest = json.loads((root / 'evidence/manifest.json').read_text(encoding='utf-8'))
for entry in manifest:
    p = (root / entry['path']).resolve()
    if not p.is_relative_to(root) or not p.is_file():
        errors.append(f'Missing/invalid evidence: {entry["path"]}')
        continue
    if p.stat().st_size != entry['bytes']:
        errors.append(f'Size mismatch: {entry["path"]}')
    if hashlib.sha256(p.read_bytes()).hexdigest() != entry['sha256']:
        errors.append(f'Hash mismatch: {entry["path"]}')
actual = {p.relative_to(root).as_posix() for p in (root / 'evidence/media').iterdir() if p.is_file()}
if actual != {entry['path'] for entry in manifest}:
    errors.append('Evidence manifest does not match media directory')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(rows)} features; {len(manifest)} evidence files; local links and SHA256 verified.')
