#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path


DEFAULT_ROOT = Path('/Users/choeyeongseo/Documents/code/pre-coding-test/Backjoon')


def find_problem_dirs(root: Path, problem_id: str) -> list[Path]:
    prefix = f"{problem_id} - "
    return sorted(
        path for path in root.rglob(f"{prefix}*")
        if path.is_dir() and path.name.startswith(prefix)
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Create a dated review file inside an existing problem directory.'
    )
    parser.add_argument('problem_id', help='Problem number, e.g. 14501')
    parser.add_argument(
        '--date',
        default=datetime.now().strftime('%Y-%m-%d'),
        help='Review filename date. Default: today in YYYY-MM-DD format.',
    )
    parser.add_argument(
        '--root',
        default=str(DEFAULT_ROOT),
        help='Backjoon root directory to search.',
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

    matches = find_problem_dirs(root, args.problem_id)
    if not matches:
        print(f'No problem directory found for {args.problem_id} under {root}.', file=sys.stderr)
        return 1
    if len(matches) > 1:
        print('Multiple problem directories found. Narrow the root or resolve duplicates:', file=sys.stderr)
        for match in matches:
            print(match, file=sys.stderr)
        return 1

    problem_dir = matches[0]
    main_file = problem_dir / 'main.py'
    if not main_file.exists():
        print(f'main.py is missing in {problem_dir}', file=sys.stderr)
        return 1

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
