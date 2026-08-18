function checkReviewGate(text) {
  if (!text.startsWith('---')) return 'no front matter';
  const end = text.indexOf('\n---', 3);
  if (end === -1) return 'unclosed';
  const front = text.slice(3, end);
  if (/^\s*reviewed_by_human\s*:\s*true\s*$/im.test(front)) return null;
  if (/^\s*reviewed_by_human\s*:\s*false\s*$/im.test(front)) return 'still false';
  return 'missing field';
}

const cases = [
  ['approved',        "---\nrole: operations\nreviewed_by_human: true\n---\n\n# Interview", null],
  ['unreviewed',      "---\nrole: operations\nreviewed_by_human: false\n---\n\n# Interview", 'still false'],
  ['field absent',    "---\nrole: operations\n---\n\n# Interview", 'missing field'],
  ['no frontmatter',  "# Interview\n\nsome text", 'no front matter'],
  ['unclosed',        "---\nreviewed_by_human: true", 'unclosed'],
  ['true w/ spacing', "---\n  reviewed_by_human :  true  \n---\nx", null],
  ['sneaky in body',  "---\nrole: x\n---\nreviewed_by_human: true", 'missing field'],
];

let pass = 0;
for (const [name, input, want] of cases) {
  const got = checkReviewGate(input);
  const ok = got === want;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${name.padEnd(16)} -> ${got === null ? 'accepted' : got}`);
  if (ok) pass++;
}
console.log(`\n${pass}/${cases.length} passed`);
