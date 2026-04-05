#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from html import unescape
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


MACOS_DEFAULT_ROOT = Path('/Users/choeyeongseo/Documents/code/pre-coding-test/Backjoon')
WSL2_DEFAULT_ROOT = Path.home() / 'Documents/code/pre-coding-test/Backjoon'
PROBLEM_URL_TEMPLATE = 'https://www.acmicpc.net/problem/{problem_id}'


def candidate_roots() -> list[Path]:
    script_dir = Path(__file__).resolve().parent
    candidates = [
        MACOS_DEFAULT_ROOT,
        script_dir / 'Backjoon',
        script_dir.parent / 'Backjoon',
        WSL2_DEFAULT_ROOT,
        Path.cwd() / 'Backjoon',
    ]

    unique_candidates: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_candidates.append(resolved)
    return unique_candidates


def get_default_root() -> Path:
    for candidate in candidate_roots():
        if candidate.exists():
            return candidate
    return candidate_roots()[0]


def find_problem_dirs(root: Path, problem_id: str) -> list[Path]:
    prefix = f"{problem_id} - "
    return sorted(
        path for path in root.rglob(f"{prefix}*")
        if path.is_dir() and path.name.startswith(prefix)
    )


def prompt_for_parent_dir(base_root: Path) -> Path | None:
    while True:
        raw = input(
            'Problem folder not found. Enter parent directory to create it under '
            '(absolute or relative path, blank to cancel): '
        ).strip()
        if not raw:
            return None

        parent = Path(raw).expanduser()
        if not parent.is_absolute():
            parent = (base_root / parent).resolve()
        else:
            parent = parent.resolve()

        if not parent.exists():
            print(f'Parent directory does not exist: {parent}', file=sys.stderr)
            continue
        if not parent.is_dir():
            print(f'Not a directory: {parent}', file=sys.stderr)
            continue
        return parent


def fetch_problem_name(problem_id: str) -> str | None:
    problem_url = PROBLEM_URL_TEMPLATE.format(problem_id=problem_id)
    request = Request(
        problem_url,
        headers={
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/122.0.0.0 Safari/537.36'
            )
        },
    )

    try:
        with urlopen(request, timeout=10) as response:
            html = response.read().decode('utf-8', errors='replace')
    except HTTPError as exc:
        print(f'Failed to fetch problem title from {problem_url}: HTTP {exc.code}', file=sys.stderr)
        return None
    except URLError as exc:
        print(f'Failed to fetch problem title from {problem_url}: {exc.reason}', file=sys.stderr)
        return None

    match = re.search(r'<span[^>]*id=["\']problem_title["\'][^>]*>(.*?)</span>', html, re.DOTALL)
    if match:
        normalized = normalize_problem_name(match.group(1))
        if normalized:
            return normalized

    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    if title_match:
        title = unescape(title_match.group(1)).strip()
        prefix = f'{problem_id}번:'
        suffix = ' - Baekjoon Online Judge'
        if title.startswith(prefix):
            title = title[len(prefix):].strip()
        if title.endswith(suffix):
            title = title[:-len(suffix)].strip()
        normalized = normalize_problem_name(title)
        if normalized:
            return normalized

    print(f'Could not parse problem title from {problem_url}', file=sys.stderr)
    return None


def normalize_problem_name(raw_name: str) -> str:
    name = unescape(re.sub(r'<[^>]+>', '', raw_name))
    name = re.sub(r'\s+', ' ', name).strip()
    # Preserve spaces in the title while avoiding path separators.
    return name.replace('/', '_')


def ensure_problem_dir(root: Path, problem_id: str) -> tuple[Path, bool] | None:
    search_roots = [root]
    if root == get_default_root():
        for candidate in candidate_roots():
            if candidate not in search_roots and candidate.exists():
                search_roots.append(candidate)

    matches: list[Path] = []
    for search_root in search_roots:
        matches.extend(find_problem_dirs(search_root, problem_id))
    matches = sorted(set(matches))

    if len(matches) == 1:
        return matches[0], False
    if len(matches) > 1:
        print('Multiple problem directories found. Narrow the root or resolve duplicates:', file=sys.stderr)
        for match in matches:
            print(match, file=sys.stderr)
        return None

    parent_dir = prompt_for_parent_dir(search_roots[0])
    if parent_dir is None:
        print('Creation cancelled.', file=sys.stderr)
        return None

    problem_name = fetch_problem_name(problem_id)
    if problem_name is None:
        print('Problem directory creation cancelled.', file=sys.stderr)
        return None

    problem_dir = parent_dir / f'{problem_id} - {problem_name}'
    if problem_dir.exists():
        if not problem_dir.is_dir():
            print(f'Path already exists and is not a directory: {problem_dir}', file=sys.stderr)
            return None
    else:
        problem_dir.mkdir(parents=True)

    main_file = problem_dir / 'main.py'
    if not main_file.exists():
        main_file.write_text('', encoding='utf-8')

    return problem_dir, True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Create a dated review file inside a problem directory, creating the directory if needed.'
    )
    parser.add_argument('problem_id', help='Problem number, e.g. 14501')
    parser.add_argument(
        '--date',
        default=datetime.now().strftime('%Y-%m-%d'),
        help='Review filename date. Default: today in YYYY-MM-DD format.',
    )
    parser.add_argument(
        '--root',
        default=str(get_default_root()),
        help='Base root directory used for search and relative parent-directory input. '
        'Defaults to the macOS path when present, otherwise the WSL2 path.',
    )
    parser.add_argument(
        '--copy-main',
        action='store_true',
        help='Copy main.py into the new review file instead of creating an empty file.',
    )
    parser.add_argument(
        '--stdout',
        action='store_true',
        help='Print only the created file path on success.',
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()

    ensured = ensure_problem_dir(root, args.problem_id)
    if ensured is None:
        return 1
    problem_dir, created_problem_dir = ensured

    main_file = problem_dir / 'main.py'
    if not main_file.exists():
        print(f'main.py is missing in {problem_dir}', file=sys.stderr)
        return 1

    if created_problem_dir:
        if args.stdout:
            print(main_file)
        else:
            print(f'Created problem directory and main.py: {main_file}')
        return 0

    target = problem_dir / f'{args.date}.py'
    if target.exists():
        print(f'Review file already exists: {target}', file=sys.stderr)
        return 1

    if args.copy_main:
        target.write_text(main_file.read_text(encoding='utf-8'), encoding='utf-8')
    else:
        target.write_text('', encoding='utf-8')

    if args.stdout:
        print(target)
    else:
        print(f'Created: {target}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
