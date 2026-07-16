#!/usr/bin/env python3
"""Extract NIST AI 600-1 GenAI Profile action table from pdftotext -layout output.

Row-based parse. Within each per-page table segment (delimited by the repeated
'Action ID ... GAI Risks' header, which also fixes the risk column start), rows are
groups of consecutive lines separated by FULLY-BLANK lines. A row that contains an
action id (strict XX-N.NN-NNN) is one action: its text = the text column joined, its
risks = the risk column joined then split on ';'. Rows with no id (subcategory
statements, 'AI Actor Tasks' lines, footnotes, page numbers) are pollution and drop
out. Ligatures normalised.
"""
import re, json, os

_HERE = os.path.dirname(os.path.abspath(__file__))
LINES = open(os.path.join(_HERE, 'nist-ai-600-1.layout.txt')).read().split('\n')
FN = {'GV': 'GOVERN', 'MP': 'MAP', 'MS': 'MEASURE', 'MG': 'MANAGE'}
IDRE = re.compile(r'^\s*([A-Z]{2})-?(\d+\.\d+)-+(\d+)\b')  # tolerant: source has 'GV4.3--001'


def canon_id(m):
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
LIG = {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi',
       '\ufb04': 'ffl', '\u2019': "'", '\u201c': '"', '\u201d': '"',
       '\u2013': '-', '\u2014': '-', '\u2018': "'", '\u00ad': ''}

CANON = [
    "CBRN Information or Capabilities", "Confabulation",
    "Dangerous, Violent, or Hateful Content", "Data Privacy", "Environmental",
    "Harmful Bias and Homogenization", "Human-AI Configuration",
    "Information Integrity", "Information Security", "Intellectual Property",
    "Obscene, Degrading, and/or Abusive Content",
    "Value Chain and Component Integration",
]
CANON_KEY = [
    ("cbrn", CANON[0]), ("confabulation", CANON[1]), ("dangerous", CANON[2]),
    ("data privacy", CANON[3]), ("environmental", CANON[4]),
    ("harmful bias", CANON[5]), ("human-ai", CANON[6]), ("human ai", CANON[6]),
    ("information integrity", CANON[7]), ("information security", CANON[8]),
    ("intellectual property", CANON[9]), ("obscene", CANON[10]),
    ("value chain", CANON[11]),
]
# first word(s) of each risk phrase — used to locate the risk column per row.
# ligatures pre-normalised in the raw line before matching (Conﬁguration -> Configuration)
RISK_STARTERS = [
    "CBRN", "Confabulation", "Dangerous", "Data Privacy", "Environmental",
    "Harmful Bias", "Human-AI", "Human AI", "Information Integrity",
    "Information Security", "Intellectual Property", "Obscene", "Value Chain",
]
NUM_ONLY = re.compile(r'^\d{1,3}$')


def norm(s: str) -> str:
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r'\s+', ' ', s).strip()


def split_line(raw: str, rs: int):
    """Split one layout line into (text, risk). Text and risk columns are separated by
    a LARGE whitespace gap (4+ spaces); the risk cell sits near column ``rs``. Prose
    text never has a 4+ space run, so this cleanly adapts per line to the actual gap
    (robust to +/-column jitter and to long text lines that reach near the risk column).
    """
    if raw.strip() == '':
        return '', ''
    lead = len(raw) - len(raw.lstrip(' '))
    if lead >= rs - 8:                      # line indented to the risk column = risk-only
        return '', raw.strip()
    for mt in re.finditer(r' {3,}', raw):   # a wide gap delimits the risk column
        j = mt.end()
        if j >= rs - 8 and raw[j:].strip():
            return raw[:j].strip(), raw[j:].strip()
    # abutting case (text touches risk, <3 space gap): fall back to a risk phrase that
    # begins near the risk column (e.g. "...property and Intellectual Property; ...")
    best = None
    for st in RISK_STARTERS:
        idx = raw.find(st)
        while idx != -1:
            if idx >= rs - 8 and (idx == 0 or raw[idx - 1] == ' '):
                best = idx if best is None else min(best, idx)
                break
            idx = raw.find(st, idx + 1)
    if best is not None:
        return raw[:best].strip(), raw[best:].strip()
    return raw.strip(), ''                   # no risk on this line


def canon_risks(blob: str):
    blob = norm(blob)
    out = []
    for frag in blob.split(';'):
        fl = frag.strip().lower()
        if not fl:
            continue
        for key, canon in CANON_KEY:
            if key in fl and canon not in out:
                out.append(canon)
                break
    return out


def main():
    headers = [i for i, l in enumerate(LINES)
               if 'Action ID' in l and 'GAI Risks' in l]
    actions = []
    multi_id_rows = []
    for k, h in enumerate(headers):
        start, end = h + 1, headers[k + 1] if k + 1 < len(headers) else len(LINES)
        rs = LINES[h].find('GAI Risks') - 2
        # group into rows separated by fully-blank lines
        rows, cur = [], []
        for i in range(start, end):
            if LINES[i].strip() == '':
                if cur:
                    rows.append(cur)
                    cur = []
            else:
                cur.append(i)
        if cur:
            rows.append(cur)
        for row in rows:
            ids, texts, risks = [], [], []
            for i in row:
                raw = LINES[i]                   # ORIGINAL line (ligatures = 1 char)
                if NUM_ONLY.match(raw.strip()):
                    continue                     # bare page-number line
                left, r = split_line(raw, rs)
                m = IDRE.match(left) or IDRE.match(raw)
                if m:
                    ids.append(canon_id(m))
                    left = left.replace(m.group(0).strip(), '', 1)
                if left.strip():
                    texts.append(left.strip())
                if r:
                    risks.append(r)
            if not ids:
                continue                       # pollution row
            if len(ids) > 1:
                multi_id_rows.append((ids, ' '.join(texts)[:60]))
            aid = ids[0]
            actions.append({
                'id': aid,
                'subcat': f"{FN[aid[:2]]} {aid.split('-')[1]}",
                'text': norm(' '.join(texts)),
                'risks': canon_risks(' '.join(risks)),
            })

    # diagnostics
    print(f"actions: {len(actions)}")
    ids = [a['id'] for a in actions]
    dups = sorted({x for x in ids if ids.count(x) > 1})
    print(f"duplicate ids: {dups}")
    print(f"short text (<25): {[a['id'] for a in actions if len(a['text'])<25]}")
    print(f"lowercase-start: {[a['id'] for a in actions if a['text'] and a['text'][0].islower()]}")
    from collections import Counter
    rc = Counter(r for a in actions for r in a['risks'])
    print("risk coverage:")
    for r in CANON:
        print(f"  {rc.get(r,0):3d}  {r}")
    print(f"empty-risk actions: {len([a for a in actions if not a['risks']])}")
    if multi_id_rows:
        print("MULTI-ID ROWS:")
        for ids_, t in multi_id_rows:
            print("  ", ids_, t)
    # subcat counts
    sc = Counter(a['subcat'] for a in actions)
    print(f"subcategories: {len(sc)}")
    json.dump(actions, open(os.path.join(_HERE, 'actions.json'), 'w'),
              indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
