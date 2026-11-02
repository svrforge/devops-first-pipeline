"""Check lesson parity, quiz bounds and local Markdown links without network access."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    data = json.loads((root / 'course/catalog.json').read_text(encoding='utf-8'))
    assert data['default_language'] == 'en'
    assert set(data['languages']) == {'en'}
    lessons = data['lessons']
    assert [x['id'] for x in lessons] == [f'{i:02}' for i in range(1, 31)]
    for lesson in lessons:
        for field in ['title', 'concept', 'expected', 'challenge']:
            assert set(lesson[field]) == set(data['languages'])
            assert all(lesson[field].values())
        assert len(lesson['quiz']['options']) == 3
        assert 0 <= lesson['quiz']['answer'] < 3
        assert lesson['commands'].strip()
        assert len(lesson['steps']) == 4
        assert len(lesson['visual']) == 4
        assert len(lesson['concept']['en']) > 180
        assert all(len(s['text']) > 30 for s in lesson['steps'])
        for lang in data['languages']:
            assert (root / 'docs' / lang / (lesson['id'] + '.md')).is_file()
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if target.startswith(('https:', 'http:', '#', 'mailto:')):
                continue
            target = target.split('#')[0]
            assert (path.parent / target).exists(), f'{path.relative_to(root)}: broken link {target}'
    print(f'Course validated: {len(lessons)} days, {len(data["languages"])} languages, local links OK')


if __name__ == '__main__':
    validate()
