import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path('tmp/lesson-review-tools').resolve()))
import pymupdf as fitz

stage = sys.argv[1]
out = Path('tmp/lesson-review') / stage
out.mkdir(parents=True, exist_ok=True)
reports = []
source_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('static/lessons')
for pdf in sorted(source_dir.glob('T[0-6]-*.pdf')):
    doc = fitz.open(pdf)
    pages = []
    for number, page in enumerate(doc, 1):
        page.get_pixmap(dpi=110).save(out / f'{pdf.stem[:2]}-{number:02}.png')
        if stage != 'before':
            page.get_pixmap(dpi=110, colorspace=fitz.csGRAY).save(out / f'{pdf.stem[:2]}-{number:02}-gray.png')
        body = [b for b in page.get_text('blocks') if b[1] < 795]
        bottom = max((b[3] for b in body), default=0)
        pages.append({'page': number, 'body_bottom': round(bottom, 1),
                      'text': page.get_text(), 'links': page.get_links()})
    reports.append({'file': pdf.name, 'pages': len(doc), 'detail': pages})
(out / 'report.json').write_text(json.dumps(reports, ensure_ascii=False, indent=2, default=str), encoding='utf8')
print([(r['file'], r['pages'], [p['body_bottom'] for p in r['detail']]) for r in reports])
