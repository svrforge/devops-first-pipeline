"""Offline course navigator. Shows commands; never executes lesson commands."""
import argparse
import json
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent


def catalog():
    return json.loads((ROOT / 'course/catalog.json').read_text(encoding='utf-8'))


def progress_file():
    return Path(os.environ.get('DEVOPS_PROGRESS_FILE', str(ROOT / '.learning-progress.json')))


def read_progress():
    path = progress_file()
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding='utf-8'))
    ids = {lesson['id'] for lesson in catalog()['lessons']}
    if not isinstance(data, list) or any(not isinstance(item, str) or item not in ids for item in data):
        raise ValueError('Invalid progress file; back it up and repair its list of lesson IDs.')
    return sorted(set(data))


def save_progress(done):
    path = progress_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(sorted(set(done))) + '\n', encoding='utf-8')
    temporary.replace(path)


def main(argv=None):
    data = catalog()
    parser = argparse.ArgumentParser(description='SVR Forge | DevOps Zero to Hero — offline learning companion')
    parser.add_argument('--lang', choices=data['languages'], default='en', help='Concept language (default: English)')
    sub = parser.add_subparsers(dest='command')
    for command in ['list', 'status', 'next', 'doctor']:
        sub.add_parser(command)
    for command in ['lesson', 'quiz', 'complete']:
        child = sub.add_parser(command)
        child.add_argument('id', choices=[x['id'] for x in data['lessons']])
        if command == 'quiz':
            child.add_argument('--answer', type=int, choices=[1, 2, 3], help='Optional non-interactive answer')
    args = parser.parse_args(argv)
    try:
        done = read_progress()
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Cannot read progress: {exc}\n')
    if args.command in (None, 'list', 'status', 'next'):
        print('\nSVR FORGE / DEVOPS ZERO TO HERO\nLearn. Build. Verify. Recover.\n')
        print(f'Progress: {len(done)}/{len(data["lessons"])} modules (self-reported, not a certification)\n')
        for lesson in data['lessons']:
            if args.command == 'next' and lesson['id'] in done:
                continue
            print(f'{"[x]" if lesson["id"] in done else "[ ]"} {lesson["id"]}  {lesson["title"][args.lang]}')
            if args.command == 'next':
                print(f'Next: python learn.py --lang {args.lang} lesson {lesson["id"]}')
                break
        print('\nStart: python learn.py lesson 01 | Help: python learn.py --help')
        return 0
    if args.command == 'doctor':
        print(f'Python: {sys.version.split()[0]} ({"OK" if sys.version_info >= (3, 11) else "upgrade to 3.11+"})')
        for tool in ['git', 'docker', 'bash', 'kubectl', 'kind', 'terraform']:
            print(f'{tool}: {"found" if shutil.which(tool) else "not on PATH"}')
        print('PATH checks only; this does not verify Docker daemon or cloud/cluster access.')
        print('Git + Python are enough to begin. Other tools are needed only for their labs.')
        return 0
    lesson = next(x for x in data['lessons'] if x['id'] == args.id)
    if args.command == 'lesson':
        print(f'\n{lesson["id"]} / {lesson["title"][args.lang]}\n')
        for heading, value in [('UNDERSTAND', lesson['concept'][args.lang]), ('TRY (run yourself)', lesson['commands']), ('VERIFY', lesson['expected'][args.lang]), ('BREAK / RECOVER', lesson['challenge'][args.lang])]:
            print(f'{heading}\n{value}\n')
        print(f'Quiz: python learn.py quiz {args.id}')
        return 0
    if args.command == 'quiz':
        quiz = lesson['quiz']
        print(quiz['question'])
        for index, option in enumerate(quiz['options'], 1):
            print(f'{index}. {option}')
        answer = args.answer
        if answer is None:
            try:
                answer = int(input('Your answer (1-3): '))
            except (ValueError, EOFError):
                print('Please enter 1, 2 or 3.'); return 2
        correct = answer == quiz['answer'] + 1
        print(('Correct. ' if correct else 'Try again. ') + quiz['explanation'])
        return 0 if correct else 1
    if args.command == 'complete':
        save_progress(done + [args.id])
        print(f'Module {args.id} recorded locally. Keep your lab evidence; this is self-reported progress.')
        return 0
    return 2


if __name__ == '__main__':
    sys.exit(main())
