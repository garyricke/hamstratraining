#!/usr/bin/env python3
"""Fix remaining i18n replacements that failed due to apostrophe character mismatch"""

with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── ACCORDION TRIGGERS (straight apostrophe, not curly) ──────────────────────
html = html.replace(
    "    <button class=\"acc-trigger\" aria-expanded=\"false\">Machine Won't Start \u2014 Three Things to Check <span class=\"icon\">+</span></button>",
    "    <button class=\"acc-trigger\" aria-expanded=\"false\"><span data-i18n=\"acc_start_fix\">Machine Won't Start \u2014 Three Things to Check</span> <span class=\"icon\">+</span></button>"
)
html = html.replace(
    "    <button class=\"acc-trigger\" aria-expanded=\"false\">Boom Won't Lift \u2014 Two Common Causes <span class=\"icon\">+</span></button>",
    "    <button class=\"acc-trigger\" aria-expanded=\"false\"><span data-i18n=\"acc_boom\">Boom Won't Lift \u2014 Two Common Causes</span> <span class=\"icon\">+</span></button>"
)

# ── M4Q3_A (fuel gauge won't — straight apostrophe) ───────────────────────────
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',false,'The fuel gauge won't cause the boom to stop after multiple operations \u2014 this is a common boom-specific issue with a different cause.')\"",
    "onclick=\"mcAnswer(this,'m4q3',false,'m4q3_A')\""
)

# ── M4Q3_D (wouldn't — double-quoted string in onclick) ──────────────────────
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',false,\"The radio remote battery wouldn't cause the boom to stop mid-operation \u2014 the connection would drop entirely rather than just stopping boom movement.\")\"",
    "onclick=\"mcAnswer(this,'m4q3',false,'m4q3_D')\""
)

with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✓ Fixes applied')

# Verify
checks = [
    ('data-i18n="acc_start_fix"', 'Accordion start fix'),
    ('data-i18n="acc_boom"', 'Accordion boom'),
    ("onclick=\"mcAnswer(this,'m4q3',false,'m4q3_A')\"", 'M4 q3 A key'),
    ("onclick=\"mcAnswer(this,'m4q3',false,'m4q3_D')\"", 'M4 q3 D key'),
]
for needle, label in checks:
    found = needle in html
    print(f'  {"✓" if found else "✗ MISSING"}: {label}')
