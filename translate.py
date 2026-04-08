#!/usr/bin/env python3
"""
Generate Spanish translations for lift-training.html via DeepL API.
Usage: python3 translate.py YOUR_DEEPL_API_KEY

Outputs: translations-es.js  (load this in the page)
Free tier: 500,000 chars/month — this script uses ~15,000 chars total.
"""

import requests, json, sys, time

def translate(texts, api_key, is_html=False):
    """Translate a list of strings via DeepL Free API."""
    url = "https://api-free.deepl.com/v2/translate"
    headers = {"Authorization": f"DeepL-Auth-Key {api_key}"}

    results = []
    BATCH = 40
    for i in range(0, len(texts), BATCH):
        batch = texts[i:i+BATCH]
        payload = {
            "source_lang": "EN",
            "target_lang": "ES",
            "text": batch,
        }
        if is_html:
            payload["tag_handling"] = "html"
        resp = requests.post(url, json=payload, headers=headers)
        if resp.status_code != 200:
            print(f"DeepL error {resp.status_code}: {resp.text}")
            sys.exit(1)
        results += [t["text"] for t in resp.json()["translations"]]
        if i + BATCH < len(texts):
            time.sleep(0.3)
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate.py YOUR_DEEPL_API_KEY")
        sys.exit(1)
    key = sys.argv[1]

    # ── UI STRINGS ──────────────────────────────────────────────────────────
    ui = {
        "lock_title":    "Lift Operation Training",
        "lock_desc":     "Enter your name and password to begin.",
        "name_ph":       "Your Full Name",
        "pw_ph":         "Password",
        "lock_btn":      "Enter",
        "nav_title":     "Lift Operation",
        "score_label":   "Score: ",
        "mnav_1":        "1. Pre-Op & Startup",
        "mnav_2":        "2. Operating the Machine",
        "mnav_3":        "3. Systems & Maintenance",
        "mnav_4":        "4. Troubleshooting",
        "mnav_5":        "5. Exam Prep",
        "mnav_6":        "6. Final Exam",
        "mnav_cert":     "Certificate",
        "hero_eyebrow":  "Hamstra Roofing Training Program",
        "hero_desc":     "From safe unloading to flying the boom — master every aspect of aerial lift operation, maintenance, and troubleshooting.",
        "badge_1":       "4 Modules",
        "badge_2":       "11 Training Videos",
        "badge_3":       "Jeopardy Challenge",
        "badge_4":       "Timed Final Exam",
        "badge_5":       "Certificate",
        "m1_label":      "Module 1",
        "m2_label":      "Module 2",
        "m3_label":      "Module 3",
        "m4_label":      "Module 4",
        "m5_label":      "Module 5",
        "m6_label":      "Module 6",
        "m1_desc":       "Before the boom moves an inch, you need to safely unload the machine, know your power options, start the engine correctly, and understand the remote in your hand. These four videos cover everything that happens before you go up.",
        "m2_desc":       "Three ways to control the machine, and how to fly it from the basket. Understand which control method to use and when — including the backup systems if electronics fail.",
        "m3_desc":       "The machine can supply power, air, and water to the basket — and it requires regular greasing to keep the turret healthy. Small mistakes in either area create big problems.",
        "m4_desc":       "The machine will test you. These three videos cover the most common field problems — engine won't start, boom won't lift, and outrigger pressure errors. Know these cold before your first job.",
        "m5_desc":       "Test your knowledge across all four modules before the final exam. Earn bonus points — jeopardy scores are added on top of your regular total.",
        "m6_desc":       "15 questions, 45 seconds each. All four modules covered. 20 points per correct answer — 300 points total. This triggers your certificate of completion.",
        # Info cards — Module 1
        "m1_ic1_h4":    "Security Straps",
        "m1_ic1_p":     "Remove all five straps before tilting the trailer — four inside, one exterior.",
        "m1_ic2_h4":    "Radio Remote Value",
        "m1_ic2_p":     "The remote is a $7,000 component. Keep it in its case whenever it's not in active use.",
        "m1_ic3_h4":    "Outrigger Stages",
        "m1_ic3_p":     "Stage 3 is the maximum height that still maintains the machine's auto-level feature.",
        "m1_ic4_h4":    "Min Extension Cord",
        "m1_ic4_p":     "Running on 110V indoors? You must use at least 12-gauge cord — smaller won't provide enough power.",
        # Info cards — Module 2
        "m2_ic1_h4":    "Radio Remote",
        "m2_ic1_p":     "Standard operation from the ground. Runs off an internal battery — a spare is kept charged in a dedicated box. If both batteries die, plug the remote directly into the machine via a tether cord.",
        "m2_ic2_h4":    "Basket Controls",
        "m2_ic2_p":     "Nearly identical to the ground remote but activates from inside the basket. Switching to basket controls disconnects the ground radio. Follow the startup procedure to ensure proper connection.",
        "m2_ic3_h4":    "Emergency Controls",
        "m2_ic3_p":     "Ground controls allow a ground operator to bypass all electronics and manually push valves. In total power failure, a lever can manually pump the hydraulics — instructions are in the owner's manual.",
        # Info cards — Exam start
        "exam_ic1_h4":  "Questions",
        "exam_ic1_p":   "Covering all four training modules.",
        "exam_ic2_h4":  "Per Question",
        "exam_ic2_p":   "The clock resets on each new question.",
        "exam_ic3_h4":  "Points Each",
        "exam_ic3_p":   "300 points total available on the final exam.",
        # Accordion triggers
        "acc_unload":       "Unloading Procedure — Step by Step",
        "acc_power":        "Three Power Sources Explained",
        "acc_startup":      "Startup Sequence & Outrigger Setup",
        "acc_remote":       "Color-Coded Remote Reference",
        "acc_basket_op":    "Basket Operation Sequence",
        "acc_basket_power": "Basket Power & Air/Water System Details",
        "acc_grease":       "Turret Greasing Procedure",
        "acc_start_fix":    "Machine Won't Start — Three Things to Check",
        "acc_outrigger":    "Outrigger Pressure Error — How to Reset",
        "acc_boom":         "Boom Won't Lift — Two Common Causes",
        # Video captions
        "v1_cap":   "Video 1 of 4 — Getting the Machine Off the Trailer",
        "v2_cap":   "Video 2 of 4 — Types of Power (Diesel / Electric / Emergency)",
        "v3_cap":   "Video 3 of 4 — Starting Instructions, Outrigger Setup & Machine Anatomy",
        "v4_cap":   "Video 4 of 4 — Radio Remote Functions & Color-Coded Controls",
        "v5_cap":   "Video 5 of 11 — Ways to Operate (Radio / Basket / Emergency Controls)",
        "v6_cap":   "Video 6 of 11 — Aerial Functions — Flying from the Basket",
        "v7_cap":   "Video 7 of 11 — Air, Water & Power in the Basket",
        "v8_cap":   "Video 8 of 11 — Maintenance: Greasing the Turret",
        "v9_cap":   "Video 9 of 11 — Quick Fix: Machine Won't Start",
        "v10_cap":  "Video 10 of 11 — Quick Fix: Outrigger Pressure Error",
        "v11_cap":  "Video 11 of 11 — Quick Fix: Boom Won't Lift",
        # Drag & drop
        "chip_radio":   "Radio Remote",
        "chip_basket":  "Basket Controls",
        "chip_ground":  "Ground Emergency",
        "chip_pump":    "Emergency Electro-Pump",
        "drag_label":   "Drag these →",
        "drop_label":   "→ Drop into the correct description",
        "check_drag":   "Check Answers",
        # Quiz numbering
        "q_1of4": "Question 1 of 4", "q_2of4": "Question 2 of 4",
        "q_3of4": "Question 3 of 4", "q_4of4": "Question 4 of 4",
        "q_1of5": "Question 1 of 5", "q_2of5": "Question 2 of 5",
        "q_3of5": "Question 3 of 5", "q_4of5": "Question 4 of 5", "q_5of5": "Question 5 of 5",
        "tf_true": "True", "tf_false": "False",
        # Quiz result labels
        "m1_result": "Module 1 Score", "m2_result": "Module 2 Score",
        "m3_result": "Module 3 Score", "m4_result": "Module 4 Score",
        "exam_result": "Final Exam Score",
        # Cert
        "cert_complete":  "Course Complete",
        "cert_title":     "YOUR CERTIFICATE",
        "cert_total":     "Total Points Earned",
        "cert_desc":      "Enter your name to generate your certificate of completion.",
        "cert_name_ph":   "Your Full Name",
        "cert_print":     "Print Certificate",
        # History
        "hist_label":     "Your Progress",
        "hist_title":     "SESSION HISTORY",
        "hist_loading":   "Loading history...",
        # Jeopardy
        "j_title":     "LIFT JEOPARDY",
        "j_bonus":     "Bonus: $",
        "j_close":     "Close",
        "j_type":      "Type your answer...",
        "j_submit":    "Submit",
        "j_skip":      "Skip",
        "j_back":      "Back to Board",
        "launch_j":    "Launch Jeopardy Challenge",
        "jcat_0":      "Machine Basics",
        "jcat_1":      "Power & Starting",
        "jcat_2":      "Controls & Remote",
        "jcat_3":      "Maintenance",
        "jcat_4":      "Troubleshooting",
        # Exam
        "start_exam":  "Start Final Exam",
        "next_q":      "Next Question →",
        "see_results": "See Results →",
        "times_up":    "Time's up! Moving on...",
        "exam_great":  "Outstanding — you are certified!",
        "exam_ok":     "Good work — review any missed topics and retry.",
        "exam_keep":   "Keep studying — you've got this!",
    }

    # ── QUIZ QUESTIONS ───────────────────────────────────────────────────────
    questions = {
        # Module 1 T/F
        "m1q1_q": "The machine should be set to \"Turtle Mode\" (slow speed) when loading or unloading from the trailer.",
        "m1q2_q": "Before tilting the trailer, you must first remove all five security straps from the machine.",
        "m1q3_q": "A standard 10-gauge extension cord is the minimum requirement when running the machine on 110V electric power.",
        "m1q4_q": "When traveling on a hilly job site, the outriggers should be kept fully retracted to improve the machine's mobility.",
        # Module 3 MC
        "m3q1_q": "What powers the basket in the power-in-the-basket system?",
        "m3q2_q": "Where can a generator be placed so that it travels with the machine while powering the basket?",
        "m3q3_q": "If liquid was used in the boom's air/water system, what must be done at the end of the day?",
        "m3q4_q": "When greasing the turret, how much grease should be applied at each service?",
        "m3q5_q": "What boom position is needed to access the turret grease circuit?",
        # Module 4 MC
        "m4q1_q": "If the machine shows absolutely no battery power and will not start, what is the most likely cause?",
        "m4q2_q": "Emergency kill switches on the machine require what specific action to fully reset them after being pushed in?",
        "m4q3_q": "After performing multiple operations, the boom stops functioning. What display indicator should you check?",
        "m4q4_q": "To clear an outrigger pressure sensor error, you remove Allen bolts to access and manually work what component?",
        # Exam Q1–15
        "eq1_q":  "What speed setting MUST always be used when loading or unloading the machine from the trailer?",
        "eq2_q":  "How many security straps hold the machine on the trailer?",
        "eq3_q":  "What happens if the trailer doors are not fully latched before tilting?",
        "eq4_q":  "What is the minimum wire gauge required for the extension cord when running the machine on 110V electric power?",
        "eq5_q":  "The emergency electro-pump is specifically designed for:",
        "eq6_q":  "What color are the remote control icons that represent aerial boom and basket movement functions?",
        "eq7_q":  "Before backing the machine out of the trailer, the jib must be in what position?",
        "eq8_q":  "Before raising the jib in basket mode, what must you do with the step?",
        "eq9_q":  "Track width should remain in what position during normal machine operation?",
        "eq10_q": "What is notable about Stage 3 outrigger extension compared to pressing the switch one more time beyond it?",
        "eq11_q": "Why must the lower boom be raised before rotating the turret?",
        "eq12_q": "How many squirts of grease should be applied to the turret at each service?",
        "eq13_q": "An outrigger pressure LED warning that causes the machine to quit can sometimes be caused by what mechanical issue?",
        "eq14_q": "An emergency shutoff switch appears to have popped back out. What is required to fully reset it?",
        "eq15_q": "When returning the boom to its stowed position, what is the LAST step in the correct sequence?",
    }

    # ── ANSWER OPTIONS ───────────────────────────────────────────────────────
    options = {
        # Module 3
        "m3q1_A": "The diesel engine directly",
        "m3q1_B": "An extension cord running through the boom",
        "m3q1_C": "A separate battery stored in the basket",
        "m3q1_D": "The outrigger hydraulic system",
        "m3q2_A": "On the boom arm",
        "m3q2_B": "On the trailer hitch",
        "m3q2_C": "On the custom platform on the opposite side of the machine",
        "m3q2_D": "Inside the basket alongside the worker",
        "m3q3_A": "Add more fluid to maintain pressure in the line",
        "m3q3_B": "Open the valves at both top and bottom to drain the line",
        "m3q3_C": "Seal all connections tightly",
        "m3q3_D": "Flush with compressed air only",
        "m3q4_A": "Fill completely until you feel resistance",
        "m3q4_B": "10 to 15 squirts for full coverage",
        "m3q4_C": "Only two or three squirts",
        "m3q4_D": "Grease is only needed once per season",
        "m3q5_A": "When the boom is fully extended",
        "m3q5_B": "When the boom is twisted at a 90-degree angle",
        "m3q5_C": "Only when the machine is completely powered off",
        "m3q5_D": "After lowering the boom to the home position",
        # Module 4
        "m4q1_A": "The diesel engine has failed",
        "m4q1_B": "The battery cutoff switch is in the \"shut off\" position",
        "m4q1_C": "The remote control has failed completely",
        "m4q1_D": "A blown outrigger fuse",
        "m4q2_A": "Hold the switch for 3 seconds",
        "m4q2_B": "Press the switch twice rapidly",
        "m4q2_C": "A twist to physically release the latch",
        "m4q2_D": "Replace the switch entirely",
        "m4q3_A": "The fuel level gauge",
        "m4q3_B": "The track width setting",
        "m4q3_C": "The basket leveling LED indicator",
        "m4q3_D": "The radio remote battery indicator",
        "m4q4_A": "A hydraulic valve",
        "m4q4_B": "A pressure gauge",
        "m4q4_C": "A spring-loaded switch",
        "m4q4_D": "The LED indicator housing",
        # Exam options
        "eq1_A": "Rabbit (fast)", "eq1_B": "Medium", "eq1_C": "Turtle (slow)", "eq1_D": "Any speed works fine",
        "eq2_A": "Three", "eq2_B": "Four", "eq2_C": "Five", "eq2_D": "Six",
        "eq3_A": "Nothing — they just swing freely", "eq3_B": "They fly off the trailer",
        "eq3_C": "They dig into the ground as the trailer tilts", "eq3_D": "They lock the machine from moving",
        "eq4_A": "10-gauge", "eq4_B": "12-gauge", "eq4_C": "14-gauge", "eq4_D": "16-gauge",
        "eq5_A": "Indoor daily use when diesel is unavailable",
        "eq5_B": "Long-term operation during power outages",
        "eq5_C": "Safely lowering a worker who is stranded in the air",
        "eq5_D": "Charging the radio remote batteries",
        "eq6_A": "Orange", "eq6_B": "Green", "eq6_C": "White", "eq6_D": "Yellow",
        "eq7_A": "Lowered all the way down", "eq7_B": "Raised to its highest position",
        "eq7_C": "Removed from the machine", "eq7_D": "At a 90-degree angle",
        "eq8_A": "Lower it fully", "eq8_B": "Leave it as-is",
        "eq8_C": "Manually pull it up and put it away", "eq8_D": "Lock it at a 45-degree angle",
        "eq9_A": "Retracted (in)", "eq9_B": "Half-extended",
        "eq9_C": "Extended (out)", "eq9_D": "Automatically adjusts as needed",
        "eq10_A": "Stage 3 is the maximum possible extension",
        "eq10_B": "Stage 3 maintains auto-level; beyond Stage 3 extends regardless of level",
        "eq10_C": "Stage 3 disables the boom for safety",
        "eq10_D": "They are identical — no difference",
        "eq11_A": "A safety interlock prevents it electronically",
        "eq11_B": "If not raised enough, the lower boom limits the turret rotation range",
        "eq11_C": "It is a hydraulic pressure requirement",
        "eq11_D": "Auto-level requires a raised lower boom to function",
        "eq12_A": "Five to ten squirts", "eq12_B": "Until you feel resistance",
        "eq12_C": "One squirt only", "eq12_D": "Two or three squirts",
        "eq13_A": "Low fuel level",
        "eq13_B": "A failed spring-loaded switch in the outrigger housing",
        "eq13_C": "Turret misalignment", "eq13_D": "Dead remote battery",
        "eq14_A": "Press it again firmly", "eq14_B": "Replace the fuse",
        "eq14_C": "A twist to release the latching mechanism", "eq14_D": "Power cycle the machine",
        "eq15_A": "Retract the telescope", "eq15_B": "Lower the upper boom",
        "eq15_C": "Lower the lower boom", "eq15_D": "Lower the jib",
    }

    # ── FEEDBACK MESSAGES ────────────────────────────────────────────────────
    feedback = {
        # Module 1 T/F
        "m1q1_T": "Correct! Turtle Mode is required for all loading and unloading — no exceptions.",
        "m1q1_F": "Incorrect. Turtle Mode is mandatory for all trailer loading and unloading to prevent accidents.",
        "m1q2_T": "Correct! Start the machine, remove all five straps, then pull the locking pin and tilt. Straps must come off before tilting.",
        "m1q2_F": "Incorrect. The straps must be removed before tilting — otherwise the machine remains bound to the tilting trailer.",
        "m1q3_T": "Incorrect. The minimum is 12-gauge — not 10. Smaller cords cannot provide enough power to turn the machine on.",
        "m1q3_F": "Correct! The minimum is 12-gauge. A 10-gauge cord would work, but smaller than 12-gauge will not provide enough power.",
        "m1q4_T": "Incorrect. On hilly terrain, keep outriggers partially extended — if the machine tips, it lands on the outriggers instead of the booms.",
        "m1q4_F": "Correct! On slopes, keep outriggers partially extended. If the machine tips, it falls on the outriggers rather than damaging the booms.",
        # Module 3 MC
        "m3q1_A": "The diesel engine powers the machine, but power to the basket comes through a cord in the boom — not directly from the engine.",
        "m3q1_B": "Correct! An extension cord runs through the boom itself. A generator on the platform plugs into this cord and travels with the machine.",
        "m3q1_C": "There is no separate battery in the basket — power comes via the cord system through the boom.",
        "m3q1_D": "The outrigger hydraulic system is for stability, not for providing electrical power to the basket.",
        "m3q2_A": "Placing a generator on the boom arm would create a dangerous imbalance and is not a built-in feature.",
        "m3q2_B": "The trailer hitch is a connection point for the trailer, not a generator platform.",
        "m3q2_C": "Correct! There is a custom platform on the opposite side of the machine designed specifically for a generator to travel along during operation.",
        "m3q2_D": "A generator cannot fit safely inside the basket alongside a worker — it belongs on the dedicated platform.",
        "m3q3_A": "Adding more fluid would make the problem worse — the liquid needs to be removed, not topped off.",
        "m3q3_B": "Correct! Both the top and bottom valves must be opened to drain the line completely. Skipping this leaves liquid in the system that causes damage next time air is used.",
        "m3q3_C": "Sealing connections traps the liquid — the opposite of what you want. The line needs to drain.",
        "m3q3_D": "The line must be physically drained by opening both end valves — compressed air alone does not drain standing liquid.",
        "m3q4_A": "Filling until resistance is felt means overfilling — this will blow out the internal seal and cause expensive damage.",
        "m3q4_B": "10 to 15 squirts is far too much — it will blow out the internal seal.",
        "m3q4_C": "Correct! Only two or three squirts. More than that can blow out the internal seal, which is an expensive repair.",
        "m3q4_D": "The turret needs frequent greasing — waiting a full season is far too long and will cause premature wear.",
        "m3q5_A": "When the boom is fully extended it moves away from the turret base — access to the grease circuit requires the boom to be twisted sideways.",
        "m3q5_B": "Correct! The boom must be twisted at a 90-degree angle to expose the turret base and allow access to the grease circuit.",
        "m3q5_C": "The machine does not need to be powered off to grease the turret — positioning the boom correctly is what matters.",
        "m3q5_D": "Lowering to home position keeps the boom forward — it needs to be twisted 90 degrees sideways to access the base.",
        # Module 4 MC
        "m4q1_A": "A dead diesel engine would not affect battery power readings — no battery power at all points to something cutting off the battery itself.",
        "m4q1_B": "Correct! No battery power at all is the telltale sign of the battery cutoff switch in the shut-off position. Check it first before anything else.",
        "m4q1_C": "A remote control failure would prevent sending commands, but the machine would still show battery power.",
        "m4q1_D": "A blown outrigger fuse would prevent outrigger function, not total battery power loss.",
        "m4q2_A": "Holding for 3 seconds does nothing — the switch requires a physical twist to disengage the latching mechanism.",
        "m4q2_B": "Pressing twice does not reset the switch — it latches in when pushed and requires a twist to release.",
        "m4q2_C": "Correct! Emergency shutoffs latch when pushed. Even when they appear to have popped back out, a twist is required to fully disengage them.",
        "m4q2_D": "Replacing the switch is unnecessary — it is a reusable emergency stop that simply needs to be twisted to reset.",
        "m4q3_A": "The fuel gauge won't cause the boom to stop after multiple operations — this is a common boom-specific issue with a different cause.",
        "m4q3_B": "Track width setting is a ground-level function and does not affect boom operation after multiple boom functions.",
        "m4q3_C": "Correct! After multiple operations the basket can drift out of level. The display has a specific LED for this condition — leveling the basket restores boom function.",
        "m4q3_D": "The radio remote battery wouldn't cause the boom to stop mid-operation — the connection would drop entirely rather than just stopping boom movement.",
        "m4q4_A": "The hydraulic valve is a separate system component — the outrigger pressure fix involves the sensor switch inside the housing.",
        "m4q4_B": "The pressure gauge is a readout, not an active component you work to reset the sensor.",
        "m4q4_C": "Correct! Under the cover is a spring-loaded switch. Manually working this switch a few times clears the warning and restores full machine function.",
        "m4q4_D": "The LED indicator is a display component — the actual fix requires working the spring-loaded switch behind the cover.",
        # Exam feedback
        "eq1_A": "Rabbit speed is the highest setting — using it during trailer operations is a safety hazard.",
        "eq1_B": "Medium speed is not the required setting for trailer operations.",
        "eq1_C": "Correct! Turtle Mode (slow speed) is mandatory for all loading and unloading — no exceptions.",
        "eq1_D": "Speed choice is not optional for trailer operations — Turtle Mode is specifically required.",
        "eq2_A": "Three straps is not the correct number — there are more securing points.",
        "eq2_B": "Four straps is close but not right — one more is used on the exterior.",
        "eq2_C": "Correct! Five straps total — four on the inside and one on the exterior.",
        "eq2_D": "Six straps is more than the actual number used.",
        "eq3_A": "Nothing happening is not the case — unlatched doors create a real hazard when the trailer tilts.",
        "eq3_B": "Flying off is not the issue — the hinge holds them; the bottom digs into the ground as the trailer tilts.",
        "eq3_C": "Correct! Unlatched doors hang down and dig into the ground when the trailer tilts, potentially damaging the doors or creating a hazard.",
        "eq3_D": "Doors do not have a mechanism to lock the machine — they simply drag on the ground if not latched.",
        "eq4_A": "10-gauge would work but is not the specified minimum — the requirement is 12-gauge.",
        "eq4_B": "Correct! 12-gauge is the minimum. Anything smaller cannot carry enough current to power the machine on.",
        "eq4_C": "14-gauge is thinner than 12-gauge and does not provide enough power to operate the machine.",
        "eq4_D": "16-gauge is a light-duty cord — far too thin for this application.",
        "eq5_A": "Indoor daily use is the role of the 110V electric system — not the emergency pump.",
        "eq5_B": "Long-term operation will drain the machine battery — the pump is for emergencies only.",
        "eq5_C": "Correct! Its sole intended purpose is to safely lower a worker who is stuck in the air due to engine or power failure.",
        "eq5_D": "The pump runs off the machine battery — it does not charge the remote.",
        "eq6_A": "Orange icons represent ground-level functions like driving and track width — not aerial movements.",
        "eq6_B": "Green is the button used to connect the remote to the machine — not a category color for functions.",
        "eq6_C": "White icons represent leveling and swivel functions — not general boom and basket aerial operations.",
        "eq6_D": "Correct! Yellow icons indicate aerial functions — boom movements, basket operations, and height-related controls.",
        "eq7_A": "The jib must not be lowered — it must be as high as possible to clear the trailer structure overhead.",
        "eq7_B": "Correct! The jib must be raised to its highest position to clear the trailer. Use enable + start + joystick simultaneously to raise it.",
        "eq7_C": "The jib cannot be removed for trailer operations — it must be raised to clear the trailer overhead.",
        "eq7_D": "A 90-degree angle would not clear the trailer overhead — the jib must be fully raised.",
        "eq8_A": "Lowering the step would make the problem worse — you must raise and stow it to prevent it from bending.",
        "eq8_B": "Leaving it as-is while operating will cause the step to bend when the jib moves.",
        "eq8_C": "Correct! Manually pull the step up and stow it before raising the jib. A step left down will bend during operation.",
        "eq8_D": "Locking at 45 degrees still leaves it in a position where it can interfere with jib operation.",
        "eq9_A": "Retracted tracks reduce stability — they should only be retracted when navigating a narrow gate.",
        "eq9_B": "Half-extended is not a specified operating position — tracks should be fully extended for maximum stability.",
        "eq9_C": "Correct! Tracks should remain extended (out) at all times during normal operation. Only retract for narrow gates.",
        "eq9_D": "Track width must be manually set — there is no automatic adjustment feature.",
        "eq10_A": "Stage 3 is not the absolute maximum — pressing again extends further, but Stage 3 keeps the auto-level active.",
        "eq10_B": "Correct! Stage 3 is the maximum height while still maintaining the auto-level feature. Pressing beyond Stage 3 extends fully regardless of level.",
        "eq10_C": "Stage 3 does not disable the boom — it is the last stage that keeps the auto-level system active.",
        "eq10_D": "They are not identical — going beyond Stage 3 removes the auto-level feature.",
        "eq11_A": "There is no electronic interlock that prevents rotation — the issue is mechanical, not a safety lockout.",
        "eq11_B": "Correct! If the lower boom is not raised high enough, it physically limits the range of turret rotation. Raise the lower boom first to allow full rotation.",
        "eq11_C": "This is not a hydraulic pressure requirement — it is about physical clearance for rotation.",
        "eq11_D": "Auto-level does not require lower boom height — the rotation limit is the reason.",
        "eq12_A": "Five to ten squirts is too much and risks blowing out the internal seal.",
        "eq12_B": "Applying until you feel resistance means overfilling — this will damage the internal seal.",
        "eq12_C": "One squirt alone may not be enough to properly lubricate — two or three is the correct amount.",
        "eq12_D": "Correct! Two or three squirts — no more. Overfilling blows out the internal seal and creates an expensive repair.",
        "eq13_A": "Low fuel causes the engine to stop, not an outrigger pressure LED warning.",
        "eq13_B": "Correct! The spring-loaded switch in the outrigger housing can fail mechanically. Accessing it with the Allen kit and working the switch manually clears the error.",
        "eq13_C": "Turret misalignment does not trigger outrigger pressure warnings.",
        "eq13_D": "A dead remote battery would cause loss of control signal, not an outrigger pressure warning.",
        "eq14_A": "Pressing again only pushes it back in — it needs a twist to physically release the latch mechanism.",
        "eq14_B": "Replacing the fuse has nothing to do with resetting an emergency shutoff switch.",
        "eq14_C": "Correct! Emergency shutoffs require a twist to fully release the latch. They can look reset while still engaged — always twist to verify.",
        "eq14_D": "Power cycling the machine does not reset a mechanically latched emergency shutoff — it needs to be manually twisted.",
        "eq15_A": "Retracting the telescope is the first step in the stowing sequence, not the last.",
        "eq15_B": "Lowering the upper boom is the second step — the lower boom and jib still need to come down after it.",
        "eq15_C": "Lowering the lower boom comes before lowering the jib in the stowing sequence.",
        "eq15_D": "Correct! The jib is the very last thing to lower. Sequence: retract telescope → lower upper boom → lower lower boom → center turret → lower jib.",
    }

    # ── JEOPARDY CLUES & ANSWERS ─────────────────────────────────────────────
    jeopardy_clues = [
        "The number of security straps used to hold the machine on the trailer.",
        "These boards are placed on the ground to protect the tracks during trailer descent.",
        "These paint markings on the turret show you the boom is perfectly centered for stowing.",
        "This is the cost of the radio remote — the reason it must always be kept in its case.",
        "The primary power source for all normal machine operations.",
        "The minimum wire gauge required for the extension cord when running on 110V electric.",
        "Key #1 on the machine selects this — either radio or basket.",
        "For a cold start, you wait for this colored light to turn off before firing the engine.",
        "The color of remote icons representing ground-level functions like driving and track width.",
        "The color of remote icons representing aerial boom and basket movements.",
        "To use aerial functions while outriggers are up, hold enable and press this button.",
        "The one function on the basket remote that is NOT found on the ground remote.",
        "The exact number of grease squirts to apply to the turret at each service.",
        "The boom position needed to access the turret grease circuit.",
        "Applying too much grease can blow out this internal turret component.",
        "If liquid was used in the boom plumbing, you open valves at top and bottom to do this at end of day.",
        "If the machine has absolutely no battery power, check this switch first.",
        "This tool, included with the remote, is needed to open the outrigger housing to reset the sensor.",
        "If the boom will not lift, physically check that these are all the way down before anything else.",
        "After multiple boom operations, this display indicator tells you the basket has drifted and needs correction.",
    ]
    jeopardy_answers = [
        "five", "2x6 boards", "white paint strips", "$7,000",
        "diesel engine", "12 gauge", "control mode", "orange",
        "orange", "yellow", "park button", "swivel",
        "two or three", "90 degrees", "seal", "drain the line",
        "battery cutoff switch", "allen kit", "locking pins", "basket leveling led",
    ]

    # ── TRANSLATE ALL GROUPS ─────────────────────────────────────────────────
    print("Translating UI strings...")
    ui_keys = list(ui.keys())
    ui_es = translate(list(ui.values()), key)

    print("Translating questions...")
    q_keys = list(questions.keys())
    q_es = translate(list(questions.values()), key)

    print("Translating options...")
    opt_keys = list(options.keys())
    opt_es = translate(list(options.values()), key)

    print("Translating feedback messages...")
    fb_keys = list(feedback.keys())
    fb_es = translate(list(feedback.values()), key)

    print("Translating jeopardy clues...")
    clue_es = translate(jeopardy_clues, key)
    answer_es = translate(jeopardy_answers, key)

    # ── BUILD OUTPUT ─────────────────────────────────────────────────────────
    T_ES = {}
    for k, v in zip(ui_keys, ui_es):     T_ES[k] = v
    for k, v in zip(q_keys, q_es):       T_ES[k] = v
    for k, v in zip(opt_keys, opt_es):   T_ES[k] = v
    for k, v in zip(fb_keys, fb_es):     T_ES[k] = v

    # Jeopardy data array
    jdata_es = []
    cats = [
        [0,1,2,3], [4,5,6,7], [8,9,10,11],
        [12,13,14,15], [16,17,18,19]
    ]
    pts = [100, 200, 300, 400]
    for cat_idxs in cats:
        cat = []
        for i, idx in enumerate(cat_idxs):
            cat.append({
                "pts": pts[i],
                "clue": clue_es[idx],
                "answer": answer_es[idx]
            })
        jdata_es.append(cat)

    # ── WRITE OUTPUT FILE ────────────────────────────────────────────────────
    out = "// Auto-generated by translate.py — do not edit manually\n"
    out += "// DeepL translation: EN → ES\n\n"
    out += "const T_ES = " + json.dumps(T_ES, ensure_ascii=False, indent=2) + ";\n\n"
    out += "const jData_es = " + json.dumps(jdata_es, ensure_ascii=False, indent=2) + ";\n"

    with open("translations-es.js", "w", encoding="utf-8") as f:
        f.write(out)

    total = len(T_ES)
    print(f"\n✓ Done — {total} strings translated")
    print("✓ Output: translations-es.js")
    print("\nNext: open lift-training.html and test the ES toggle.")

if __name__ == "__main__":
    main()
