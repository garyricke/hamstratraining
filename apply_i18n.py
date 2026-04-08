#!/usr/bin/env python3
"""Apply all remaining i18n HTML changes and add JS implementation to lift-training.html"""
import re

with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── QUIZ RESULT LABELS ────────────────────────────────────────────────────────
for i in range(1, 5):
    html = html.replace(
        f'      <p>Module {i} Score</p>',
        f'      <p data-i18n="m{i}_result">Module {i} Score</p>'
    )

# ── MODULE 2 DRAG LABELS ──────────────────────────────────────────────────────
html = html.replace('">Drag these →</p>', '" data-i18n="drag_label">Drag these →</p>')
html = html.replace('">→ Drop into the correct description</p>',
                    '" data-i18n="drop_label">→ Drop into the correct description</p>')

# ── MODULE 4 SECTION ──────────────────────────────────────────────────────────
html = html.replace(
    '  <div class="sec-label">Module 4</div>',
    '  <div class="sec-label" data-i18n="m4_label">Module 4</div>'
)
html = html.replace(
    '  <h2 class="sec-title">QUICK FIXES &amp;<br>TROUBLESHOOTING</h2>',
    '  <h2 class="sec-title" data-i18n-html="m4_title">QUICK FIXES &amp;<br>TROUBLESHOOTING</h2>'
)
html = html.replace(
    '  <p class="sec-desc">The machine will test you. These three videos cover',
    '  <p class="sec-desc" data-i18n="m4_desc">The machine will test you. These three videos cover'
)

# Video captions 9-11
html = html.replace(
    '    <div class="video-caption"><strong>Video 9 of 11 \u2014</strong>',
    '    <div class="video-caption" data-i18n-html="v9_cap"><strong>Video 9 of 11 \u2014</strong>'
)
html = html.replace(
    '    <div class="video-caption"><strong>Video 10 of 11 \u2014</strong>',
    '    <div class="video-caption" data-i18n-html="v10_cap"><strong>Video 10 of 11 \u2014</strong>'
)
html = html.replace(
    '    <div class="video-caption"><strong>Video 11 of 11 \u2014</strong>',
    '    <div class="video-caption" data-i18n-html="v11_cap"><strong>Video 11 of 11 \u2014</strong>'
)

# Accordion triggers 9-11
html = html.replace(
    "    <button class=\"acc-trigger\" aria-expanded=\"false\">Machine Won't Start \u2014 Three Things to Check <span class=\"icon\">+</span></button>",
    "    <button class=\"acc-trigger\" aria-expanded=\"false\"><span data-i18n=\"acc_start_fix\">Machine Won't Start \u2014 Three Things to Check</span> <span class=\"icon\">+</span></button>"
)
html = html.replace(
    '    <button class="acc-trigger" aria-expanded="false">Outrigger Pressure Error \u2014 How to Reset <span class="icon">+</span></button>',
    '    <button class="acc-trigger" aria-expanded="false"><span data-i18n="acc_outrigger">Outrigger Pressure Error \u2014 How to Reset</span> <span class="icon">+</span></button>'
)
html = html.replace(
    "    <button class=\"acc-trigger\" aria-expanded=\"false\">Boom Won't Lift \u2014 Two Common Causes <span class=\"icon\">+</span></button>",
    "    <button class=\"acc-trigger\" aria-expanded=\"false\"><span data-i18n=\"acc_boom\">Boom Won't Lift \u2014 Two Common Causes</span> <span class=\"icon\">+</span></button>"
)

# Module 4 quiz q1
html = html.replace(
    "      <div class=\"q-num\">Question 1 of 4</div>\n      <h4>If the machine shows absolutely no battery power and will not start, what is the most likely cause?</h4>",
    "      <div class=\"q-num\" data-i18n=\"q_1of4\">Question 1 of 4</div>\n      <h4 data-i18n=\"m4q1_q\">If the machine shows absolutely no battery power and will not start, what is the most likely cause?</h4>"
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q1',false,'A dead diesel engine would not affect battery power readings \u2014 no battery power at all points to something cutting off the battery itself.')\"",
    "onclick=\"mcAnswer(this,'m4q1',false,'m4q1_A')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q1',true,'Correct! No battery power at all is the telltale sign of the battery cutoff switch in the shut-off position. Check it first before anything else.')\"",
    "onclick=\"mcAnswer(this,'m4q1',true,'m4q1_B')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q1',false,'A remote control failure would prevent sending commands, but the machine would still show battery power.')\"",
    "onclick=\"mcAnswer(this,'m4q1',false,'m4q1_C')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q1',false,'A blown outrigger fuse would prevent outrigger function, not total battery power loss.')\"",
    "onclick=\"mcAnswer(this,'m4q1',false,'m4q1_D')\""
)

# Module 4 quiz q2
html = html.replace(
    "      <div class=\"q-num\">Question 2 of 4</div>\n      <h4>Emergency kill switches on the machine require what specific action to fully reset them after being pushed in?</h4>",
    "      <div class=\"q-num\" data-i18n=\"q_2of4\">Question 2 of 4</div>\n      <h4 data-i18n=\"m4q2_q\">Emergency kill switches on the machine require what specific action to fully reset them after being pushed in?</h4>"
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q2',false,'Holding for 3 seconds does nothing \u2014 the switch requires a physical twist to disengage the latching mechanism.')\"",
    "onclick=\"mcAnswer(this,'m4q2',false,'m4q2_A')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q2',false,'Pressing twice does not reset the switch \u2014 it latches in when pushed and requires a twist to release.')\"",
    "onclick=\"mcAnswer(this,'m4q2',false,'m4q2_B')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q2',true,'Correct! Emergency shutoffs latch when pushed. Even when they appear to have popped back out, a twist is required to fully disengage them.')\"",
    "onclick=\"mcAnswer(this,'m4q2',true,'m4q2_C')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q2',false,'Replacing the switch is unnecessary \u2014 it is a reusable emergency stop that simply needs to be twisted to reset.')\"",
    "onclick=\"mcAnswer(this,'m4q2',false,'m4q2_D')\""
)

# Module 4 quiz q3
html = html.replace(
    "      <div class=\"q-num\">Question 3 of 4</div>\n      <h4>After performing multiple operations, the boom stops functioning. What display indicator should you check?</h4>",
    "      <div class=\"q-num\" data-i18n=\"q_3of4\">Question 3 of 4</div>\n      <h4 data-i18n=\"m4q3_q\">After performing multiple operations, the boom stops functioning. What display indicator should you check?</h4>"
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',false,'The fuel gauge won\u2019t cause the boom to stop after multiple operations \u2014 this is a common boom-specific issue with a different cause.')\"",
    "onclick=\"mcAnswer(this,'m4q3',false,'m4q3_A')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',false,'Track width setting is a ground-level function and does not affect boom operation after multiple boom functions.')\"",
    "onclick=\"mcAnswer(this,'m4q3',false,'m4q3_B')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',true,'Correct! After multiple operations the basket can drift out of level. The display has a specific LED for this condition \u2014 leveling the basket restores boom function.')\"",
    "onclick=\"mcAnswer(this,'m4q3',true,'m4q3_C')\""
)
# q3 D uses double quotes because of apostrophe in "wouldn't"
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q3',false,\"The radio remote battery wouldn\u2019t cause the boom to stop mid-operation \u2014 the connection would drop entirely rather than just stopping boom movement.\")\"",
    "onclick=\"mcAnswer(this,'m4q3',false,'m4q3_D')\""
)

# Module 4 quiz q4
html = html.replace(
    "      <div class=\"q-num\">Question 4 of 4</div>\n      <h4>To clear an outrigger pressure sensor error, you remove Allen bolts to access and manually work what component?</h4>",
    "      <div class=\"q-num\" data-i18n=\"q_4of4\">Question 4 of 4</div>\n      <h4 data-i18n=\"m4q4_q\">To clear an outrigger pressure sensor error, you remove Allen bolts to access and manually work what component?</h4>"
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q4',false,'The hydraulic valve is a separate system component \u2014 the outrigger pressure fix involves the sensor switch inside the housing.')\"",
    "onclick=\"mcAnswer(this,'m4q4',false,'m4q4_A')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q4',false,'The pressure gauge is a readout, not an active component you work to reset the sensor.')\"",
    "onclick=\"mcAnswer(this,'m4q4',false,'m4q4_B')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q4',true,'Correct! Under the cover is a spring-loaded switch. Manually working this switch a few times clears the warning and restores full machine function.')\"",
    "onclick=\"mcAnswer(this,'m4q4',true,'m4q4_C')\""
)
html = html.replace(
    "onclick=\"mcAnswer(this,'m4q4',false,'The LED indicator is a display component \u2014 the actual fix requires working the spring-loaded switch behind the cover.')\"",
    "onclick=\"mcAnswer(this,'m4q4',false,'m4q4_D')\""
)

# Module 4 quiz result p (already done via loop above)

# ── MODULE 5 SECTION ──────────────────────────────────────────────────────────
html = html.replace(
    '  <div class="sec-label">Module 5</div>',
    '  <div class="sec-label" data-i18n="m5_label">Module 5</div>'
)
html = html.replace(
    '  <h2 class="sec-title">JEOPARDY<br>EXAM PREP</h2>',
    '  <h2 class="sec-title" data-i18n-html="m5_title">JEOPARDY<br>EXAM PREP</h2>'
)
html = html.replace(
    '  <p class="sec-desc">Test your knowledge across all four modules before the final exam.',
    '  <p class="sec-desc" data-i18n="m5_desc">Test your knowledge across all four modules before the final exam.'
)
html = html.replace(
    '    Launch Jeopardy Challenge\n  </button>',
    '    <span data-i18n="launch_j">Launch Jeopardy Challenge</span>\n  </button>'
)

# ── MODULE 6 SECTION ──────────────────────────────────────────────────────────
html = html.replace(
    '  <div class="sec-label">Module 6</div>',
    '  <div class="sec-label" data-i18n="m6_label">Module 6</div>'
)
html = html.replace(
    '  <h2 class="sec-title">FINAL TIMED<br>EXAM</h2>',
    '  <h2 class="sec-title" data-i18n-html="m6_title">FINAL TIMED<br>EXAM</h2>'
)
html = html.replace(
    '  <p class="sec-desc">15 questions, 45 seconds each.',
    '  <p class="sec-desc" data-i18n="m6_desc">15 questions, 45 seconds each.'
)

# Exam info cards
html = html.replace('<h4>Questions</h4>', '<h4 data-i18n="exam_ic1_h4">Questions</h4>')
html = html.replace('<p>Covering all four training modules.</p>', '<p data-i18n="exam_ic1_p">Covering all four training modules.</p>')
html = html.replace('<h4>Per Question</h4>', '<h4 data-i18n="exam_ic2_h4">Per Question</h4>')
html = html.replace('<p>The clock resets on each new question.</p>', '<p data-i18n="exam_ic2_p">The clock resets on each new question.</p>')
html = html.replace('<h4>Points Each</h4>', '<h4 data-i18n="exam_ic3_h4">Points Each</h4>')
html = html.replace('<p>300 points total available on the final exam.</p>', '<p data-i18n="exam_ic3_p">300 points total available on the final exam.</p>')

# Start exam button
html = html.replace(
    '        Start Final Exam\n      </button>',
    '        <span data-i18n="start_exam">Start Final Exam</span>\n      </button>'
)

# Exam result label
html = html.replace(
    '        <p>Final Exam Score</p>',
    '        <p data-i18n="exam_result">Final Exam Score</p>'
)

# ── EXAM QUESTIONS: ADD data-i18n TO h4 ──────────────────────────────────────
exam_q_map = {
    "What speed setting MUST always be used when loading or unloading the machine from the trailer?": "eq1_q",
    "How many security straps hold the machine on the trailer?": "eq2_q",
    "What happens if the trailer doors are not fully latched before tilting?": "eq3_q",
    "What is the minimum wire gauge required for the extension cord when running the machine on 110V electric power?": "eq4_q",
    "The emergency electro-pump is specifically designed for:": "eq5_q",
    "What color are the remote control icons that represent aerial boom and basket movement functions?": "eq6_q",
    "Before backing the machine out of the trailer, the jib must be in what position?": "eq7_q",
    "Before raising the jib in basket mode, what must you do with the step?": "eq8_q",
    "Track width should remain in what position during normal machine operation?": "eq9_q",
    "What is notable about Stage 3 outrigger extension compared to pressing the switch one more time beyond it?": "eq10_q",
    "Why must the lower boom be raised before rotating the turret?": "eq11_q",
    "How many squirts of grease should be applied to the turret at each service?": "eq12_q",
    "An outrigger pressure LED warning that causes the machine to quit can sometimes be caused by what mechanical issue?": "eq13_q",
    "An emergency shutoff switch appears to have popped back out. What is required to fully reset it?": "eq14_q",
    "When returning the boom to its stowed position, what is the LAST step in the correct sequence?": "eq15_q",
}
for q_text, key in exam_q_map.items():
    html = html.replace(
        f'<h4 style="font-size:17px;color:var(--white);margin-bottom:4px">{q_text}</h4>',
        f'<h4 style="font-size:17px;color:var(--white);margin-bottom:4px" data-i18n="{key}">{q_text}</h4>'
    )

# ── EXAM QUESTIONS: REPLACE INLINE MESSAGES WITH KEYS ───────────────────────
exam_msg_map = {
    # Q1
    "Rabbit speed is the highest setting \u2014 using it during trailer operations is a safety hazard.": "eq1_A",
    "Medium speed is not the required setting for trailer operations.": "eq1_B",
    "Correct! Turtle Mode (slow speed) is mandatory for all loading and unloading \u2014 no exceptions.": "eq1_C",
    "Speed choice is not optional for trailer operations \u2014 Turtle Mode is specifically required.": "eq1_D",
    # Q2
    "Three straps is not the correct number \u2014 there are more securing points.": "eq2_A",
    "Four straps is close but not right \u2014 one more is used on the exterior.": "eq2_B",
    "Correct! Five straps total \u2014 four on the inside and one on the exterior.": "eq2_C",
    "Six straps is more than the actual number used.": "eq2_D",
    # Q3
    "Nothing happening is not the case \u2014 unlatched doors create a real hazard when the trailer tilts.": "eq3_A",
    "Flying off is not the issue \u2014 the hinge holds them; the bottom digs into the ground as the trailer tilts.": "eq3_B",
    "Correct! Unlatched doors hang down and dig into the ground when the trailer tilts, potentially damaging the doors or creating a hazard.": "eq3_C",
    "Doors do not have a mechanism to lock the machine \u2014 they simply drag on the ground if not latched around the sides.": "eq3_D",
    # Q4
    "10-gauge would work but is not the specified minimum \u2014 the requirement is 12-gauge.": "eq4_A",
    "Correct! 12-gauge is the minimum. Anything smaller cannot carry enough current to power the machine on.": "eq4_B",
    "14-gauge is thinner than 12-gauge and does not provide enough power to operate the machine.": "eq4_C",
    "16-gauge is a light-duty cord \u2014 far too thin for this application.": "eq4_D",
    # Q5
    "Indoor daily use is the role of the 110V electric system \u2014 not the emergency pump.": "eq5_A",
    "Long-term operation will drain the machine battery \u2014 the pump is for emergencies only.": "eq5_B",
    "Correct! Its sole intended purpose is to safely lower a worker who is stuck in the air due to engine or power failure.": "eq5_C",
    "The pump runs off the machine battery \u2014 it does not charge the remote.": "eq5_D",
    # Q6
    "Orange icons represent ground-level functions like driving and track width \u2014 not aerial movements.": "eq6_A",
    "Green is the button used to connect the remote to the machine \u2014 not a category color for functions.": "eq6_B",
    "White icons represent leveling and swivel functions \u2014 not general boom and basket aerial operations.": "eq6_C",
    "Correct! Yellow icons indicate aerial functions \u2014 boom movements, basket operations, and height-related controls.": "eq6_D",
    # Q7
    "The jib must not be lowered \u2014 it must be as high as possible to clear the trailer structure overhead.": "eq7_A",
    "Correct! The jib must be raised to its highest position to clear the trailer. Use enable + start + joystick simultaneously to raise it.": "eq7_B",
    "The jib cannot be removed for trailer operations \u2014 it must be raised to clear the trailer overhead.": "eq7_C",
    "A 90-degree angle would not clear the trailer overhead \u2014 the jib must be fully raised.": "eq7_D",
    # Q8
    "Lowering the step would make the problem worse \u2014 you must raise and stow it to prevent it from bending.": "eq8_A",
    "Leaving it as-is while operating will cause the step to bend when the jib moves.": "eq8_B",
    "Correct! Manually pull the step up and stow it before raising the jib. A step left down will bend during operation.": "eq8_C",
    "Locking at 45 degrees still leaves it in a position where it can interfere with jib operation.": "eq8_D",
    # Q9
    "Retracted tracks reduce stability \u2014 they should only be retracted when navigating a narrow gate.": "eq9_A",
    "Half-extended is not a specified operating position \u2014 tracks should be fully extended for maximum stability.": "eq9_B",
    "Correct! Tracks should remain extended (out) at all times during normal operation for maximum stability. Only retract for narrow gates.": "eq9_C",
    "Track width must be manually set \u2014 there is no automatic adjustment feature.": "eq9_D",
    # Q10
    "Stage 3 is not the absolute maximum \u2014 pressing again extends further, but Stage 3 is special because it keeps the auto-level active.": "eq10_A",
    "Correct! Stage 3 is the maximum height while still maintaining the auto-level feature. Pressing beyond Stage 3 extends fully regardless of whether the machine is level.": "eq10_B",
    "Stage 3 does not disable the boom for safety \u2014 it is the last stage that keeps the auto-level system active.": "eq10_C",
    "Stages 3 and beyond are not identical \u2014 going beyond Stage 3 removes the auto-level feature.": "eq10_D",
    # Q11
    "A safety interlock prevents it electronically": "eq11_A",
    "If not raised enough, the lower boom limits the turret rotation range": "eq11_B",
    "It is a hydraulic pressure requirement": "eq11_C",
    "Auto-level requires a raised lower boom to function": "eq11_D",
    # Q12
    "Five to ten squirts is too much and risks blowing out the internal seal.": "eq12_A",
    "Applying until you feel resistance means overfilling \u2014 this will damage the internal seal.": "eq12_B",
    "One squirt alone may not be enough to properly lubricate \u2014 two or three is the correct amount.": "eq12_C",
    "Correct! Two or three squirts \u2014 no more. Overfilling blows out the internal seal and creates an expensive repair.": "eq12_D",
    # Q13
    "Low fuel causes the engine to stop, not an outrigger pressure LED warning.": "eq13_A",
    "Correct! The spring-loaded switch in the outrigger housing can fail mechanically. Accessing it with the Allen kit and working the switch manually clears the error.": "eq13_B",
    "Turret misalignment does not trigger outrigger pressure warnings.": "eq13_C",
    "A dead remote battery would cause loss of control signal, not an outrigger pressure warning.": "eq13_D",
    # Q14
    "Pressing again only pushes it back in \u2014 it needs a twist to physically release the latch mechanism.": "eq14_A",
    "Replacing the fuse has nothing to do with resetting an emergency shutoff switch.": "eq14_B",
    "Correct! Emergency shutoffs require a twist to fully release the latch. They can look reset while still engaged \u2014 always twist to verify.": "eq14_C",
    "Power cycling the machine does not reset a mechanically latched emergency shutoff \u2014 it needs to be manually twisted.": "eq14_D",
    # Q15
    "Retracting the telescope is the first step in the stowing sequence, not the last.": "eq15_A",
    "Lowering the upper boom is the second step \u2014 the lower boom and jib still need to come down after it.": "eq15_B",
    "Lowering the lower boom comes before lowering the jib in the stowing sequence.": "eq15_C",
    "Correct! The jib is the very last thing to lower. Sequence: retract telescope \u2192 lower upper boom \u2192 lower lower boom \u2192 center turret \u2192 lower jib.": "eq15_D",
}
for msg, key in exam_msg_map.items():
    html = html.replace(
        f"onclick=\"examAnswer(this,false,'{msg}')\"",
        f"onclick=\"examAnswer(this,false,'{key}')\""
    )
    html = html.replace(
        f"onclick=\"examAnswer(this,true,'{msg}')\"",
        f"onclick=\"examAnswer(this,true,'{key}')\""
    )

# ── EXAM NEXT / SEE RESULTS BUTTONS ──────────────────────────────────────────
# Wrap next button text in span (14 of them say "Next Question →")
html = html.replace(
    '>Next Question \u2192</button>',
    '><span data-i18n="next_q">Next Question \u2192</span></button>'
)
# See results button (last)
html = html.replace(
    '>See Results \u2192</button>',
    '><span data-i18n="see_results">See Results \u2192</span></button>'
)

# ── CERTIFICATE SECTION ───────────────────────────────────────────────────────
html = html.replace(
    '    <div class="sec-label" style="justify-content:center">Course Complete</div>',
    '    <div class="sec-label" style="justify-content:center" data-i18n="cert_complete">Course Complete</div>'
)
html = html.replace(
    '    <h2 class="sec-title" style="font-size:clamp(36px,5vw,64px)">YOUR CERTIFICATE</h2>',
    '    <h2 class="sec-title" style="font-size:clamp(36px,5vw,64px)" data-i18n="cert_title">YOUR CERTIFICATE</h2>'
)
html = html.replace(
    '      <p>Total Points Earned</p>',
    '      <p data-i18n="cert_total">Total Points Earned</p>'
)
html = html.replace(
    '    <p style="color:var(--gray);margin-bottom:24px">Enter your name to generate your certificate of completion.</p>',
    '    <p style="color:var(--gray);margin-bottom:24px" data-i18n="cert_desc">Enter your name to generate your certificate of completion.</p>'
)
html = html.replace(
    'placeholder="Your Full Name" oninput="updateCertName()">',
    'placeholder="Your Full Name" data-i18n-ph="cert_name_ph" oninput="updateCertName()">'
)
html = html.replace(
    '></svg> Print Certificate</button>',
    '></svg> <span data-i18n="cert_print">Print Certificate</span></button>'
)

# ── HISTORY SECTION ───────────────────────────────────────────────────────────
html = html.replace(
    '    <div class="sec-label">Your Progress</div>',
    '    <div class="sec-label" data-i18n="hist_label">Your Progress</div>'
)
html = html.replace(
    '    <h2 class="sec-title" style="font-size:clamp(28px,4vw,44px);margin-bottom:24px">SESSION HISTORY</h2>',
    '    <h2 class="sec-title" style="font-size:clamp(28px,4vw,44px);margin-bottom:24px" data-i18n="hist_title">SESSION HISTORY</h2>'
)
html = html.replace(
    '"><p class="history-empty">Loading history...</p></div>',
    '"><p class="history-empty" data-i18n="hist_loading">Loading history...</p></div>'
)

# ── JEOPARDY MODAL ────────────────────────────────────────────────────────────
html = html.replace('<h2>LIFT JEOPARDY</h2>', '<h2 data-i18n="j_title">LIFT JEOPARDY</h2>')
html = html.replace(
    '<div class="j-score-display">Bonus: $<span id="j-score">0</span></div>',
    '<div class="j-score-display"><span data-i18n="j_bonus">Bonus: $</span><span id="j-score">0</span></div>'
)
html = html.replace(
    '">Close</button>',
    '" data-i18n="j_close">Close</button>'
)
html = html.replace(
    '<div class="j-cat-header">Machine Basics</div>',
    '<div class="j-cat-header" data-i18n="jcat_0">Machine Basics</div>'
)
html = html.replace(
    '<div class="j-cat-header">Power &amp; Starting</div>',
    '<div class="j-cat-header" data-i18n="jcat_1">Power &amp; Starting</div>'
)
html = html.replace(
    '<div class="j-cat-header">Controls &amp; Remote</div>',
    '<div class="j-cat-header" data-i18n="jcat_2">Controls &amp; Remote</div>'
)
html = html.replace(
    '<div class="j-cat-header">Maintenance</div>',
    '<div class="j-cat-header" data-i18n="jcat_3">Maintenance</div>'
)
html = html.replace(
    '<div class="j-cat-header">Troubleshooting</div>',
    '<div class="j-cat-header" data-i18n="jcat_4">Troubleshooting</div>'
)
html = html.replace(
    'placeholder="Type your answer..." onkeydown',
    'placeholder="Type your answer..." data-i18n-ph="j_type" onkeydown'
)
html = html.replace(
    '" onclick="submitJAnswer()">Submit</button>',
    '" onclick="submitJAnswer()" data-i18n="j_submit">Submit</button>'
)
html = html.replace(
    '" onclick="skipJAnswer()">Skip</button>',
    '" onclick="skipJAnswer()" data-i18n="j_skip">Skip</button>'
)
html = html.replace(
    '" id="j-next-btn" onclick="closeJQ()" style="margin-top:12px;display:none">Back to Board</button>',
    '" id="j-next-btn" onclick="closeJQ()" style="margin-top:12px;display:none" data-i18n="j_back">Back to Board</button>'
)

# ── ADD TRANSLATIONS SCRIPT TAG ───────────────────────────────────────────────
html = html.replace(
    '<script>\n// ═══ SCORE SYSTEM ═══',
    '<script src="./translations-es.js"></script>\n\n<script>\n// ═══ SCORE SYSTEM ═══'
)

# ── ADD LANGUAGE JS (after score system opening) ──────────────────────────────
lang_js = '''
// ═══ LANGUAGE ═══
let CLANG = 'en';

const T_EN = {
  "m1q1_T": "Correct! Turtle Mode is required for all loading and unloading \u2014 no exceptions.",
  "m1q1_F": "Incorrect. Turtle Mode is mandatory for all trailer loading and unloading to prevent accidents.",
  "m1q2_T": "Correct! Start the machine, remove all five straps, then pull the locking pin and tilt. Straps must come off before tilting.",
  "m1q2_F": "Incorrect. The straps must be removed before tilting \u2014 otherwise the machine remains bound to the tilting trailer.",
  "m1q3_T": "Incorrect. The minimum is 12-gauge \u2014 not 10. Smaller cords cannot provide enough power to turn the machine on.",
  "m1q3_F": "Correct! The minimum is 12-gauge. A 10-gauge cord would work, but smaller than 12-gauge will not provide enough power.",
  "m1q4_T": "Incorrect. On hilly terrain, keep outriggers partially extended \u2014 if the machine tips, it lands on the outriggers instead of the booms.",
  "m1q4_F": "Correct! On slopes, keep outriggers partially extended. If the machine tips, it falls on the outriggers rather than damaging the booms.",
  "m3q1_A": "The diesel engine powers the machine, but power to the basket comes through a cord in the boom \u2014 not directly from the engine.",
  "m3q1_B": "Correct! An extension cord runs through the boom itself. A generator on the platform plugs into this cord and travels with the machine.",
  "m3q1_C": "There is no separate battery in the basket \u2014 power comes via the cord system through the boom.",
  "m3q1_D": "The outrigger hydraulic system is for stability, not for providing electrical power to the basket.",
  "m3q2_A": "Placing a generator on the boom arm would create a dangerous imbalance and is not a built-in feature.",
  "m3q2_B": "The trailer hitch is a connection point for the trailer, not a generator platform.",
  "m3q2_C": "Correct! There is a custom platform on the opposite side of the machine designed specifically for a generator to travel along during operation.",
  "m3q2_D": "A generator cannot fit safely inside the basket alongside a worker \u2014 it belongs on the dedicated platform.",
  "m3q3_A": "Adding more fluid would make the problem worse \u2014 the liquid needs to be removed, not topped off.",
  "m3q3_B": "Correct! Both the top and bottom valves must be opened to drain the line completely. Skipping this leaves liquid in the system that causes damage next time air is used.",
  "m3q3_C": "Sealing connections traps the liquid \u2014 the opposite of what you want. The line needs to drain.",
  "m3q3_D": "The line must be physically drained by opening both end valves \u2014 compressed air alone does not drain standing liquid.",
  "m3q4_A": "Filling until resistance is felt means overfilling \u2014 this will blow out the internal seal and cause expensive damage.",
  "m3q4_B": "10 to 15 squirts is far too much \u2014 it will blow out the internal seal.",
  "m3q4_C": "Correct! Only two or three squirts. More than that can blow out the internal seal, which is an expensive repair.",
  "m3q4_D": "The turret needs frequent greasing \u2014 waiting a full season is far too long and will cause premature wear.",
  "m3q5_A": "When the boom is fully extended it moves away from the turret base \u2014 access to the grease circuit requires the boom to be twisted sideways.",
  "m3q5_B": "Correct! The boom must be twisted at a 90-degree angle to expose the turret base and allow access to the grease circuit.",
  "m3q5_C": "The machine does not need to be powered off to grease the turret \u2014 positioning the boom correctly is what matters.",
  "m3q5_D": "Lowering to home position keeps the boom forward \u2014 it needs to be twisted 90 degrees sideways to access the base.",
  "m4q1_A": "A dead diesel engine would not affect battery power readings \u2014 no battery power at all points to something cutting off the battery itself.",
  "m4q1_B": "Correct! No battery power at all is the telltale sign of the battery cutoff switch in the shut-off position. Check it first before anything else.",
  "m4q1_C": "A remote control failure would prevent sending commands, but the machine would still show battery power.",
  "m4q1_D": "A blown outrigger fuse would prevent outrigger function, not total battery power loss.",
  "m4q2_A": "Holding for 3 seconds does nothing \u2014 the switch requires a physical twist to disengage the latching mechanism.",
  "m4q2_B": "Pressing twice does not reset the switch \u2014 it latches in when pushed and requires a twist to release.",
  "m4q2_C": "Correct! Emergency shutoffs latch when pushed. Even when they appear to have popped back out, a twist is required to fully disengage them.",
  "m4q2_D": "Replacing the switch is unnecessary \u2014 it is a reusable emergency stop that simply needs to be twisted to reset.",
  "m4q3_A": "The fuel gauge won\u2019t cause the boom to stop after multiple operations \u2014 this is a common boom-specific issue with a different cause.",
  "m4q3_B": "Track width setting is a ground-level function and does not affect boom operation after multiple boom functions.",
  "m4q3_C": "Correct! After multiple operations the basket can drift out of level. The display has a specific LED for this condition \u2014 leveling the basket restores boom function.",
  "m4q3_D": "The radio remote battery wouldn\u2019t cause the boom to stop mid-operation \u2014 the connection would drop entirely rather than just stopping boom movement.",
  "m4q4_A": "The hydraulic valve is a separate system component \u2014 the outrigger pressure fix involves the sensor switch inside the housing.",
  "m4q4_B": "The pressure gauge is a readout, not an active component you work to reset the sensor.",
  "m4q4_C": "Correct! Under the cover is a spring-loaded switch. Manually working this switch a few times clears the warning and restores full machine function.",
  "m4q4_D": "The LED indicator is a display component \u2014 the actual fix requires working the spring-loaded switch behind the cover.",
  "eq1_A": "Rabbit speed is the highest setting \u2014 using it during trailer operations is a safety hazard.",
  "eq1_B": "Medium speed is not the required setting for trailer operations.",
  "eq1_C": "Correct! Turtle Mode (slow speed) is mandatory for all loading and unloading \u2014 no exceptions.",
  "eq1_D": "Speed choice is not optional for trailer operations \u2014 Turtle Mode is specifically required.",
  "eq2_A": "Three straps is not the correct number \u2014 there are more securing points.",
  "eq2_B": "Four straps is close but not right \u2014 one more is used on the exterior.",
  "eq2_C": "Correct! Five straps total \u2014 four on the inside and one on the exterior.",
  "eq2_D": "Six straps is more than the actual number used.",
  "eq3_A": "Nothing happening is not the case \u2014 unlatched doors create a real hazard when the trailer tilts.",
  "eq3_B": "Flying off is not the issue \u2014 the hinge holds them; the bottom digs into the ground as the trailer tilts.",
  "eq3_C": "Correct! Unlatched doors hang down and dig into the ground when the trailer tilts, potentially damaging the doors or creating a hazard.",
  "eq3_D": "Doors do not have a mechanism to lock the machine \u2014 they simply drag on the ground if not latched.",
  "eq4_A": "10-gauge would work but is not the specified minimum \u2014 the requirement is 12-gauge.",
  "eq4_B": "Correct! 12-gauge is the minimum. Anything smaller cannot carry enough current to power the machine on.",
  "eq4_C": "14-gauge is thinner than 12-gauge and does not provide enough power to operate the machine.",
  "eq4_D": "16-gauge is a light-duty cord \u2014 far too thin for this application.",
  "eq5_A": "Indoor daily use is the role of the 110V electric system \u2014 not the emergency pump.",
  "eq5_B": "Long-term operation will drain the machine battery \u2014 the pump is for emergencies only.",
  "eq5_C": "Correct! Its sole intended purpose is to safely lower a worker who is stuck in the air due to engine or power failure.",
  "eq5_D": "The pump runs off the machine battery \u2014 it does not charge the remote.",
  "eq6_A": "Orange icons represent ground-level functions like driving and track width \u2014 not aerial movements.",
  "eq6_B": "Green is the button used to connect the remote to the machine \u2014 not a category color for functions.",
  "eq6_C": "White icons represent leveling and swivel functions \u2014 not general boom and basket aerial operations.",
  "eq6_D": "Correct! Yellow icons indicate aerial functions \u2014 boom movements, basket operations, and height-related controls.",
  "eq7_A": "The jib must not be lowered \u2014 it must be as high as possible to clear the trailer structure overhead.",
  "eq7_B": "Correct! The jib must be raised to its highest position to clear the trailer. Use enable + start + joystick simultaneously to raise it.",
  "eq7_C": "The jib cannot be removed for trailer operations \u2014 it must be raised to clear the trailer overhead.",
  "eq7_D": "A 90-degree angle would not clear the trailer overhead \u2014 the jib must be fully raised.",
  "eq8_A": "Lowering the step would make the problem worse \u2014 you must raise and stow it to prevent it from bending.",
  "eq8_B": "Leaving it as-is while operating will cause the step to bend when the jib moves.",
  "eq8_C": "Correct! Manually pull the step up and stow it before raising the jib. A step left down will bend during operation.",
  "eq8_D": "Locking at 45 degrees still leaves it in a position where it can interfere with jib operation.",
  "eq9_A": "Retracted tracks reduce stability \u2014 they should only be retracted when navigating a narrow gate.",
  "eq9_B": "Half-extended is not a specified operating position \u2014 tracks should be fully extended for maximum stability.",
  "eq9_C": "Correct! Tracks should remain extended (out) at all times during normal operation. Only retract for narrow gates.",
  "eq9_D": "Track width must be manually set \u2014 there is no automatic adjustment feature.",
  "eq10_A": "Stage 3 is not the absolute maximum \u2014 pressing again extends further, but Stage 3 keeps the auto-level active.",
  "eq10_B": "Correct! Stage 3 is the maximum height while still maintaining the auto-level feature. Pressing beyond Stage 3 extends fully regardless of level.",
  "eq10_C": "Stage 3 does not disable the boom \u2014 it is the last stage that keeps the auto-level system active.",
  "eq10_D": "They are not identical \u2014 going beyond Stage 3 removes the auto-level feature.",
  "eq11_A": "There is no electronic interlock that prevents rotation \u2014 the issue is mechanical, not a safety lockout.",
  "eq11_B": "Correct! If the lower boom is not raised high enough, it physically limits the range of turret rotation. Raise the lower boom first to allow full rotation.",
  "eq11_C": "This is not a hydraulic pressure requirement \u2014 it is about physical clearance for rotation.",
  "eq11_D": "Auto-level does not require lower boom height \u2014 the rotation limit is the reason.",
  "eq12_A": "Five to ten squirts is too much and risks blowing out the internal seal.",
  "eq12_B": "Applying until you feel resistance means overfilling \u2014 this will damage the internal seal.",
  "eq12_C": "One squirt alone may not be enough to properly lubricate \u2014 two or three is the correct amount.",
  "eq12_D": "Correct! Two or three squirts \u2014 no more. Overfilling blows out the internal seal and creates an expensive repair.",
  "eq13_A": "Low fuel causes the engine to stop, not an outrigger pressure LED warning.",
  "eq13_B": "Correct! The spring-loaded switch in the outrigger housing can fail mechanically. Accessing it with the Allen kit and working the switch manually clears the error.",
  "eq13_C": "Turret misalignment does not trigger outrigger pressure warnings.",
  "eq13_D": "A dead remote battery would cause loss of control signal, not an outrigger pressure warning.",
  "eq14_A": "Pressing again only pushes it back in \u2014 it needs a twist to physically release the latch mechanism.",
  "eq14_B": "Replacing the fuse has nothing to do with resetting an emergency shutoff switch.",
  "eq14_C": "Correct! Emergency shutoffs require a twist to fully release the latch. They can look reset while still engaged \u2014 always twist to verify.",
  "eq14_D": "Power cycling the machine does not reset a mechanically latched emergency shutoff \u2014 it needs to be manually twisted.",
  "eq15_A": "Retracting the telescope is the first step in the stowing sequence, not the last.",
  "eq15_B": "Lowering the upper boom is the second step \u2014 the lower boom and jib still need to come down after it.",
  "eq15_C": "Lowering the lower boom comes before lowering the jib in the stowing sequence.",
  "eq15_D": "Correct! The jib is the very last thing to lower. Sequence: retract telescope \u2192 lower upper boom \u2192 lower lower boom \u2192 center turret \u2192 lower jib.",
  "times_up": "Time's up! Moving on...",
  "exam_great": "Outstanding \u2014 you are certified!",
  "exam_ok": "Good work \u2014 review any missed topics and retry.",
  "exam_keep": "Keep studying \u2014 you've got this!"
};

const SECTION_TITLES_ES = {
  "m1_title": "PRE-OP Y<br>ARRANQUE",
  "m2_title": "OPERANDO<br>LA M\\u00C1QUINA",
  "m3_title": "SISTEMAS Y<br>MANTENIMIENTO",
  "m4_title": "CORRECCIONES R\\u00C1PIDAS Y<br>RESOLUCI\\u00D3N",
  "m5_title": "JEOPARDY<br>PREPARACI\\u00D3N EXAMEN",
  "m6_title": "EXAMEN FINAL<br>CRONOMETRADO",
  "hero_h1": "OPERACI\\u00D3N<br>DE ELEVADORES<br><em>CERTIFICADO</em>"
};

const SECTION_TITLES_EN = {
  "m1_title": "PRE-OP &amp;<br>STARTUP",
  "m2_title": "OPERATING<br>THE MACHINE",
  "m3_title": "SYSTEMS &amp;<br>MAINTENANCE",
  "m4_title": "QUICK FIXES &amp;<br>TROUBLESHOOTING",
  "m5_title": "JEOPARDY<br>EXAM PREP",
  "m6_title": "FINAL TIMED<br>EXAM",
  "hero_h1": "LIFT OPERATION<br><em>CERTIFIED</em>"
};

function setLang(lang) {
  CLANG = lang;

  // Update plain-text [data-i18n] elements (skip option spans inside mc-options)
  document.querySelectorAll('[data-i18n]').forEach(el => {
    if (el.closest('.mc-options, .exam-mc-options')) return;
    const key = el.getAttribute('data-i18n');
    if (lang === 'es') {
      const val = T_ES[key];
      if (val === undefined) return;
      if (!el.dataset.orig) el.dataset.orig = el.textContent;
      el.textContent = val;
    } else {
      if (el.dataset.orig !== undefined) el.textContent = el.dataset.orig;
    }
  });

  // Update [data-i18n-ph] placeholders
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const key = el.getAttribute('data-i18n-ph');
    if (lang === 'es') {
      const val = T_ES[key];
      if (val === undefined) return;
      if (!el.dataset.origPh) el.dataset.origPh = el.placeholder;
      el.placeholder = val;
    } else {
      if (el.dataset.origPh) el.placeholder = el.dataset.origPh;
    }
  });

  // Update [data-i18n-html] elements — section titles + video captions
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const key = el.getAttribute('data-i18n-html');
    if (lang === 'es') {
      if (!el.getAttribute('data-orig-html')) el.setAttribute('data-orig-html', el.innerHTML);
      const val = (SECTION_TITLES_ES[key] !== undefined) ? SECTION_TITLES_ES[key] : T_ES[key];
      if (val !== undefined) el.innerHTML = val;
    } else {
      const orig = el.getAttribute('data-orig-html');
      if (orig) el.innerHTML = orig;
    }
  });
}

function toggleLang() {
  const newLang = CLANG === 'en' ? 'es' : 'en';
  setLang(newLang);
  const btn = document.getElementById('lang-toggle');
  if (newLang === 'es') {
    btn.textContent = 'EN';
    btn.classList.add('active');
  } else {
    btn.textContent = 'ES';
    btn.classList.remove('active');
  }
}

'''

html = html.replace(
    '// ═══ SCORE SYSTEM ═══',
    lang_js + '// ═══ SCORE SYSTEM ═══'
)

# ── MODIFY tfAnswer TO USE KEY LOOKUP ─────────────────────────────────────────
html = html.replace(
    '  fb.textContent = msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) m1Scores[qId] = 25;',
    '  fb.textContent = (CLANG===\'es\' ? T_ES : T_EN)[msg] || msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) m1Scores[qId] = 25;'
)

# ── MODIFY mcAnswer TO USE KEY LOOKUP ─────────────────────────────────────────
html = html.replace(
    '  fb.textContent = msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) mcEarned[mod]',
    '  fb.textContent = (CLANG===\'es\' ? T_ES : T_EN)[msg] || msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) mcEarned[mod]'
)

# ── MODIFY examAnswer TO USE KEY LOOKUP ───────────────────────────────────────
html = html.replace(
    '  fb.textContent = msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) examScore',
    '  fb.textContent = (CLANG===\'es\' ? T_ES : T_EN)[msg] || msg;\n  fb.className = \'q-feedback show \' + (isCorrect ? \'good\' : \'bad\');\n  if (isCorrect) examScore'
)

# ── MODIFY loadExamQ TIMER TIMEOUT ────────────────────────────────────────────
html = html.replace(
    "        fb.textContent = \"Time's up! Moving on...\";",
    "        fb.textContent = (CLANG==='es' ? T_ES : T_EN)['times_up'];"
)

# ── MODIFY finishExam RESULT MESSAGES ─────────────────────────────────────────
html = html.replace(
    "  document.getElementById('exam-msg').textContent = pct >= 80 ? 'Outstanding \u2014 you are certified!' : pct >= 60 ? 'Good work \u2014 review any missed topics and retry.' : 'Keep studying \u2014 you\\'ve got this!';",
    "  const T_fin = CLANG==='es' ? T_ES : T_EN;\n  document.getElementById('exam-msg').textContent = pct >= 80 ? T_fin['exam_great'] : pct >= 60 ? T_fin['exam_ok'] : T_fin['exam_keep'];"
)

# ── MODIFY openJQ TO USE CLANG-AWARE jData ────────────────────────────────────
html = html.replace(
    '  const q = jData[cat][row];',
    '  const q = (CLANG===\'es\' ? jData_es : jData)[cat][row];'
)

# ── MODIFY submitJAnswer TO USE CLANG-AWARE jData ────────────────────────────
html = html.replace(
    '  const q = jData[currentJCat][currentJRow];\n  const correct = q.answer.toLowerCase();',
    '  const q = (CLANG===\'es\' ? jData_es : jData)[currentJCat][currentJRow];\n  const correct = q.answer.toLowerCase();'
)

# ── MODIFY skipJAnswer TO USE CLANG-AWARE jData ──────────────────────────────
html = html.replace(
    '  const q = jData[currentJCat][currentJRow];\n  const rev = document.getElementById(\'j-reveal\');',
    '  const q = (CLANG===\'es\' ? jData_es : jData)[currentJCat][currentJRow];\n  const rev = document.getElementById(\'j-reveal\');'
)

# ── MODIFY loadHistory MODULE LABELS FOR CLANG ───────────────────────────────
html = html.replace(
    "  const modLabels = { m1: 'Pre-Op & Startup', m2: 'Operating the Machine', m3: 'Systems & Maintenance', m4: 'Troubleshooting', exam: 'Final Exam' };",
    "  const modLabels = CLANG==='es' ? { m1: T_ES['mnav_1']||'Pre-Op & Startup', m2: T_ES['mnav_2']||'Operating the Machine', m3: T_ES['mnav_3']||'Systems & Maintenance', m4: T_ES['mnav_4']||'Troubleshooting', exam: T_ES['mnav_6']||'Final Exam' } : { m1: 'Pre-Op & Startup', m2: 'Operating the Machine', m3: 'Systems & Maintenance', m4: 'Troubleshooting', exam: 'Final Exam' };"
)

# ── WRITE OUTPUT ──────────────────────────────────────────────────────────────
with open('/Users/garyricke/Documents/hamstra-training/lift-training.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✓ Done — all i18n changes applied')

# Verify key replacements
checks = [
    ('data-i18n="m4_label"', 'Module 4 sec-label'),
    ('data-i18n-html="m4_title"', 'Module 4 sec-title'),
    ('data-i18n-html="v9_cap"', 'Video 9 caption'),
    ('data-i18n-html="v10_cap"', 'Video 10 caption'),
    ('data-i18n-html="v11_cap"', 'Video 11 caption'),
    ("data-i18n=\"acc_start_fix\"", 'Accordion start fix'),
    ("data-i18n=\"acc_outrigger\"", 'Accordion outrigger'),
    ("data-i18n=\"acc_boom\"", 'Accordion boom'),
    ("data-i18n=\"m4q1_q\"", 'M4 q1 question'),
    ("onclick=\"mcAnswer(this,'m4q1',false,'m4q1_A')\"", 'M4 q1 A key'),
    ("data-i18n=\"m5_label\"", 'Module 5 sec-label'),
    ("data-i18n-html=\"m5_title\"", 'Module 5 sec-title'),
    ("data-i18n=\"launch_j\"", 'Launch Jeopardy button'),
    ("data-i18n=\"m6_label\"", 'Module 6 sec-label'),
    ("data-i18n-html=\"m6_title\"", 'Module 6 sec-title'),
    ("data-i18n=\"start_exam\"", 'Start exam button'),
    ("data-i18n=\"eq1_q\"", 'Exam q1 question'),
    ("onclick=\"examAnswer(this,false,'eq1_A')\"", 'Exam q1 A key'),
    ("data-i18n=\"next_q\"", 'Next question span'),
    ("data-i18n=\"see_results\"", 'See results span'),
    ("data-i18n=\"cert_complete\"", 'Cert sec-label'),
    ("data-i18n=\"cert_title\"", 'Cert h2'),
    ("data-i18n=\"hist_label\"", 'History sec-label'),
    ("data-i18n=\"j_title\"", 'Jeopardy title'),
    ("data-i18n=\"jcat_0\"", 'Jeopardy cat 0'),
    ("data-i18n=\"j_submit\"", 'Jeopardy submit'),
    ('let CLANG', 'CLANG variable'),
    ('const T_EN', 'T_EN object'),
    ('function setLang', 'setLang function'),
    ('function toggleLang', 'toggleLang function'),
    ('translations-es.js', 'translations script tag'),
    ("(CLANG==='es' ? T_ES : T_EN)[msg]", 'tfAnswer key lookup'),
    ("(CLANG==='es' ? jData_es : jData)[cat][row]", 'openJQ jData switch'),
]
print()
all_pass = True
for needle, label in checks:
    found = needle in html
    status = '✓' if found else '✗ MISSING'
    if not found:
        all_pass = False
    print(f'  {status}: {label}')
if all_pass:
    print('\n✓ All checks passed!')
else:
    print('\n✗ Some items missing — check script')
