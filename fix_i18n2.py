#!/usr/bin/env python3
"""Fix remaining exam message replacements"""

with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Q10_C: HTML has no "for safety"
html = html.replace(
    "examAnswer(this,false,'Stage 3 does not disable the boom \u2014 it is the last stage that keeps the auto-level system active.')",
    "examAnswer(this,false,'eq10_C')"
)

# Q11_A
html = html.replace(
    "examAnswer(this,false,'There is no electronic interlock that prevents rotation \u2014 the issue is mechanical, not a safety lockout.')",
    "examAnswer(this,false,'eq11_A')"
)

# Q11_B
html = html.replace(
    "examAnswer(this,true,'Correct! If the lower boom is not raised high enough, it physically limits the range of turret rotation. Raise the lower boom first to allow full rotation.')",
    "examAnswer(this,true,'eq11_B')"
)

# Q11_C
html = html.replace(
    "examAnswer(this,false,'This is not a hydraulic pressure requirement \u2014 it is about physical clearance for rotation.')",
    "examAnswer(this,false,'eq11_C')"
)

# Q11_D
html = html.replace(
    "examAnswer(this,false,'Auto-level does not require lower boom height \u2014 the rotation limit is the reason.')",
    "examAnswer(this,false,'eq11_D')"
)

with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re
remaining = re.findall(r"examAnswer\(this,(?:true|false),'[A-Z][^']{10,}'\)", html)
if remaining:
    print(f'Still {len(remaining)} remaining inline exam messages:')
    for r in remaining[:3]:
        print(' ', r[:80])
else:
    print('✓ All exam messages replaced with keys')
