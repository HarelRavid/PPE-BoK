# PPE-BoK — מבנה הספר / Working Book Architecture

**Status:** ACTIVE WORKING ARCHITECTURE — DO NOT FREEZE FINAL TOC  
**Change class:** B — Structural  
**Last architecture recovery:** 2026-08-12  
**Last production-status sync:** 2026-08-14  
**Governing principle:** היקף הידע קובע את מספר הפרקים; מספר הפרקים אינו יעד בפני עצמו.

> מסמך זה הוא חוזה הארכיטקטורה הפעיל של הספר. הוא מרכז את מבנה העבודה, את ה־knowledge scope שחובה לשמר, את מצב הכתיבה ואת גבולות אי־הוודאות. מספור הפרקים, שמות ה־Parts והחלוקה לכרכים יוקפאו רק לאחר השלמת התוכן, Topic-to-Chapter Coverage Audit, Technical Review ו־Editorial Review.

---

## 1. מטרת הספר

ליצור Body of Knowledge הנדסי מקיף למערכות צנרת פלסטיות ותרמופלסטיות בתעשייה — מהפיזיקה, הכימיה והמדע הפולימרי, דרך בחירת חומר, qualification, joining, תכן מכני והידראולי, התקנה, בדיקות והפעלה, ועד תחזוקה, Remaining Life, חקירת כשלים, בטיחות תהליכית וטכנולוגיות עתידיות.

הספר אינו מיועד להיות רק Textbook, Handbook או Engineering Report. הזהות המכוונת שלו היא שילוב של שלושתם:

`Engineering Question → Why → Physics / Mechanism → Standards / Evidence → Calculation → Verification → Engineering Decision → Workflow / Checklist → Common Mistakes`

יחידת העבודה המרכזית היא **Engineering Decision**. כל Investigation צריכה לאפשר למהנדס להבין מה לעשות, לפי איזה בסיס, איך לחשב או לאמת, מה מגבלות השיטה, מה דורש escalation ומה לתעד.

---

## 2. כללי ארכיטקטורה מחייבים

### 2.1 Topic-driven, not chapter-count-driven

הספר עבר לאורך הפיתוח מספר ארכיטקטורות: תוכנית מוקדמת קצרה, תוכנית היסטורית שהגיעה בוודאות לפחות עד Chapter 78 וככל הנראה לכ־91 פרקים, וה־redevelopment הנוכחי שמתחיל ב־Chapters 000–013.

לכן:

- אין יעד מלאכותי של 91, 100 או 110 פרקים.
- שום נושא היסטורי אינו נמחק רק כדי להתאים למספור חדש.
- נושא שהיה מיועד לטיפול עמוק אינו נחשב “מכוסה” רק משום שהוא מוזכר בפסקה בפרק אחר.
- אם נושא דורש פרק עצמאי כדי להשיג engineering-use depth — ייפתח פרק נוסף.
- אם מספר נושאים ניתנים לאיחוד ללא אובדן עומק — ניתן לאחד אותם.
- המספור הסופי הוא תוצאה של הארכיטקטורה, לא דרישה.

### 2.2 מקור אמת

`main` הוא ה־repository baseline הרשמי. תוכן ב־branch, PR, שיחה או טיוטה אינו baseline עד review, author approval ו־merge.

### 2.3 Knowledge hierarchy

`Book → Part → Chapter → Investigation → Engineering Asset`

Engineering Assets כוללים לפחות:

- Equations (`EQ-xxx-xxx`)
- Figures (`FIG-xxx-xxx`)
- Tables (`TAB-xxx-xxx`)
- Workflows (`WF-xxx-xxx`)
- Worked Examples (`EX-xxx-xxx`)
- Decision Trees (`DT-xxx-xxx`)
- Checklists (`CL-xxx-xxx`)

### 2.4 Working numbering

עד Design Freeze, מספרי 014 ואילך הם **Working Chapter Numbers** בלבד. אין לפרש אותם כשחזור מוכח של המספור ההיסטורי.

---

## 3. Scope floor — תחומים שאסור לאבד

המסגרת ההיסטורית המוקדמת הגדירה עשרה domains שהם minimum scope floor:

1. Plastic Piping Fundamentals
2. Materials Science
3. International Standards
4. Engineering Design
5. Joining & Welding Technologies
6. Equipment & Process Systems
7. Quality, Inspection & Qualification
8. Failure Analysis
9. Industrial Case Studies
10. Future Technologies

ה־recovery המאוחר הרחיב אותם לצירי הידע הבאים, שכולם חייבים לקבל טיפול מתאים בארכיטקטורה הסופית:

1. Physical and chemical foundations.
2. Polymer molecular architecture and morphology.
3. Thermal and viscoelastic behaviour.
4. Mechanical behaviour, fracture and degradation science.
5. Material families and formulations.
6. Material characterization and laboratory methods.
7. Long-term strength, classification and engineering evidence.
8. Pipe and system mechanical design.
9. Hydraulics and process transport phenomena.
10. Joining, welding and connection engineering.
11. Installation, construction, testing, commissioning and reinstatement.
12. Quality, inspection, qualification and documentation.
13. Failure analysis and root-cause investigation.
14. Standards navigation and cross-framework engineering.
15. Equipment and process-system integration.
16. Industrial case studies and lessons learned.
17. Future technologies and digital engineering.
18. Process safety and special hazards.
19. Human factors, operations and lifecycle integrity.
20. Engineering tables, equations, decision tools and checklists.

ה־canonical atomic topic inventory נמצא גם ב־`docs/MASTER-KNOWLEDGE-SCOPE-MAP.md` וב־`docs/HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md`. מסמך זה ממפה את אותו scope לארכיטקטורת העבודה של הספר.

---

## 4. מצב ה־redevelopment הנוכחי

### 4.1 Chapters 000–012 — existing redevelopment baseline

ה־redevelopment הנוכחי בנה שכבת פתיחה חזקה סביב:

- Chapter 000 — How to Use This Book
- Chapter 001 — Understanding Industrial Plastic Piping Systems
- Chapter 002 — Engineering Decision Process
- Chapter 003 — Understanding Industrial Processes
- Chapter 004 — Defining Engineering Requirements
- Chapter 005 — Establishing the Design Basis
- Chapter 006 — Service Conditions and Design Envelope
- Chapter 007 — Engineering Risk and Uncertainty
- Chapter 008 — Understanding Process Fluids
- Chapter 009 — Polymer Fundamentals
- Chapter 010 — Material Selection Methodology
- Chapter 011 — Common Plastic Piping Materials
- Chapter 012 — Long-Term Strength, MRS, SDR and Pressure Rating

פרקים אלה מהווים foundation ואינם מחליפים את ה־historical depth blocks המתועדים בהמשך.

### 4.2 Chapter 013 — Polyethylene (PE)

Chapter 013 הוא pilot ה־PDS הראשון וה־reference implementation הפעיל.

מצב ה־baseline לאחר PR #8:

- הפרק וה־review package המשויך אליו מוזגו ל־`main` כ־**active standards-validation candidate**.
- Investigations 1–10 integrated and complete for the approved CDB scope.
- Long-term evidence → regression → MRS → design coefficient → design stress → SDR → reference pressure chain integrated.
- Worked Example A and Worked Example B integrated.
- Failure Lens integrated.
- Chapter Design Review Checklist integrated.
- Technical Review: **PASS**.
- Physics / equations / units / worked-example verification: **PASS**.
- Academic/Evidence Review: **PASS for the current core non-normative claim set** with explicit applicability limits.
- Editorial/Style Review: **CONDITIONAL PASS — no structural rewrite required**.
- Public authoritative ISO identity / edition lifecycle / public scope navigation was rechecked on 2026-08-14.
- **Authoritative full-text Standards Validation remains OPEN** under Issue #9 (`SVH-013-01` through `SVH-013-05`).
- Chapter 013 is **not publication-frozen**; Design Freeze remains blocked until the source-dependent standards holds and bounded final publication actions close.
- Historical PR #2 was closed without merge and remains provenance only.

The remaining Chapter 013 blocker is controlled external source access, not unfinished Engineering Development. Author-approved planning/CDB work for Working Chapter 014 may therefore proceed in parallel while Issue #9 remains open. This does not waive any Chapter 013 Definition-of-Done requirement and does not authorize Chapter 014 Engineering Development before its own Definition of Ready is approved.

---

# 5. Working continuation architecture — Chapters 014 onward

> כל המספרים בפרק זה הם Working Numbers. ה־scope מחייב; המספור אינו מחייב עד Final Architecture Freeze.

---

## PART III — Polymer Science for Piping Engineers

### Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers

Scope:

- matter, atoms, elements and molecules;
- electron structure and why it matters to bonding;
- ionic, covalent, metallic, hydrogen and van der Waals interactions;
- material classes: metals, ceramics and polymers;
- carbon chemistry;
- orbitals and hybridization: sp, sp2, sp3;
- ethylene structure;
- bridge from molecular bonding to piping-material behaviour.

Engineering question: why do different thermoplastics behave differently even when they are all called “plastics”?

### Chapter 015 — From Monomer to Polymer: Polymerization, Catalysts and Process–Structure Relationships

Scope:

- monomers and polymer formation;
- chain-growth / addition polymerization;
- step-growth / condensation concepts;
- radical polymerization;
- Ziegler–Natta catalysis;
- metallocene catalysis;
- process history and resulting molecular architecture;
- processing → structure → properties → piping performance.

### Chapter 016 — Polymer Chain Architecture: Molecular Weight, Branching and Crosslinking

Scope:

- chain length;
- molecular weight and molecular-weight distribution;
- branching;
- crosslinking;
- molecular connectivity;
- chain architecture effects on stiffness, toughness, diffusion, creep, SCG resistance and fusion behaviour.

### Chapter 017 — Crystallinity, Lamellae, Spherulites and Molecular Mobility

Scope:

- amorphous versus semicrystalline behaviour;
- crystallinity;
- lamellae;
- spherulites;
- amorphous regions;
- tie molecules where applicable;
- molecular mobility;
- morphology effects on mechanical response, diffusion, ageing and welding/fusion.

### Chapter 018 — Thermal Transitions and Thermophysical Behaviour

Scope:

- glass-transition temperature (Tg);
- melting temperature (Tm);
- softening behaviour;
- heat capacity;
- thermal conductivity;
- coefficient of thermal expansion;
- temperature-dependent modulus and mobility;
- engineering consequences for supports, joining, pressure capability and operation.

### Chapter 019 — Viscoelasticity, Creep, Stress Relaxation and Time–Temperature Behaviour

Scope:

- viscoelastic response;
- creep;
- stress relaxation;
- loading-rate effects;
- time-temperature dependence;
- Arrhenius concepts;
- WLF concepts;
- time-temperature superposition;
- shift factors and master curves;
- extrapolation limits and validation.

### Chapter 020 — Fracture, Crack Growth, Fatigue, ESC and Polymer Ageing

Scope:

- stress and strain;
- elastic/plastic response;
- yield and toughness;
- ductile and brittle fracture;
- fracture mechanics fundamentals;
- stress concentration and crack-tip behaviour;
- SCG;
- RCP;
- fatigue;
- creep-fatigue interaction;
- environmental stress cracking (ESC);
- oxidation and thermal ageing;
- antioxidant systems;
- UV degradation and weathering;
- carbon black, HALS and pigments;
- diffusion and permeation;
- chemical interaction mechanisms;
- lifetime implications.

---

## PART IV — Engineering Material Families

### Chapter 021 — Polypropylene Family and Engineering Selection

Scope: PP family, morphology, strengths/limits, joining implications and system-level comparison to PE.

### Chapter 022 — PP-H

### Chapter 023 — PP-B

### Chapter 024 — PP-R and PP-RCT

Scope across Chapters 022–024:

- structure and formulation differences;
- pressure/temperature behaviour;
- chemical service;
- creep and long-term performance;
- joining routes;
- relevant product/application frameworks;
- practical selection limits.

### Chapter 025 — PVC Family

### Chapter 026 — PVC-U

### Chapter 027 — PVC-C / CPVC

### Chapter 028 — ABS

### Chapter 029 — Fluoropolymers and Specialty Thermoplastics

Mandatory family coverage within this block:

- PVDF;
- ECTFE;
- FEP;
- PFA;
- PTFE where relevant to piping/lining;
- PA / polyamide / nylon;
- PB / polybutylene;
- PEX;
- specialty fluoropolymers;
- reinforced, lined and multilayer thermoplastic architectures;
- GRP / FRP / RTRP interfaces where retained within final scope.

**Architecture hold:** final decision whether PVDF, ECTFE, FEP/PFA/PTFE, PA/PB/PEX and composite/lining systems remain grouped or become dedicated chapters will be made during CDB development. Historical depth must not be lost through grouping.

---

## PART V — Material Characterization and Testing

### Chapter 030 — Differential Scanning Calorimetry (DSC)
### Chapter 031 — Dynamic Mechanical Analysis (DMA)
### Chapter 032 — Thermogravimetric Analysis (TGA)
### Chapter 033 — Fourier Transform Infrared Spectroscopy (FTIR)
### Chapter 034 — Optical Microscopy
### Chapter 035 — SEM and EDS
### Chapter 036 — Oxidation Induction Time (OIT)
### Chapter 037 — Melt Flow Rate / Melt Flow Index and Density
### Chapter 038 — Tensile, Flexural, Impact and Hardness Testing
### Chapter 039 — Hydrostatic Pressure Testing
### Chapter 040 — Slow Crack Growth and Rapid Crack Propagation Testing
### Chapter 041 — Fatigue, Fracture and Environmental Stress-Cracking Testing

Cross-block requirements:

- specimen definition and conditioning;
- what the test measures;
- what the test does not prove;
- equipment and measurement principles;
- data interpretation;
- repeatability/uncertainty where relevant;
- standards path;
- acceptance versus characterization;
- destructive testing of joints where applicable;
- qualified NDT interfaces;
- use of test evidence in qualification and failure investigation.

---

## PART VI — Long-Term Performance and Engineering Evidence

### Chapter 042 — Fracture Mechanics for Plastic Piping

Scope:

- crack-tip fields;
- fracture toughness concepts;
- defect stability;
- local versus nominal stress;
- defect assessment boundaries.

### Chapter 043 — Creep and Stress Relaxation in Piping Components and Joints

Scope includes pipe wall, joints, gaskets, bolting interfaces, supports and load redistribution.

### Chapter 044 — Lifetime Prediction, Arrhenius/WLF and Time–Temperature Superposition

Scope:

- acceleration methods;
- shift factors;
- master curves;
- extrapolation limits;
- physical-mechanism validation;
- when lifetime extrapolation is not defensible.

### Chapter 045 — Qualification, Validation, Certification and Engineering Evidence

Scope:

- material qualification;
- product qualification;
- component qualification;
- system verification;
- certification;
- qualification matrices;
- evidence hierarchy;
- evidence maturity;
- acceptance boundaries.

### Chapter 046 — Technical Files, Change Control and Requalification

Scope:

- controlled technical file;
- configuration management;
- traceability;
- design-change classification;
- requalification triggers;
- standards change;
- material/supplier/process changes;
- MOC interfaces.

---

## PART VII — Joining and Connection Engineering

### Chapter 047 — Joining Method Selection as a System-Level Decision

Scope:

- geometry;
- material family;
- installation environment;
- pressure/service state;
- inspectability;
- maintainability;
- cleanliness;
- repair strategy;
- lifecycle risk.

### Chapter 048 — Heat-Fusion Fundamentals

Scope:

- interdiffusion and molecular healing;
- temperature/time/pressure interfaces;
- surface preparation;
- alignment;
- contamination;
- thermal history;
- essential variables.

### Chapter 049 — PE Butt Fusion
### Chapter 050 — PE Electrofusion
### Chapter 051 — PP Butt and Socket Fusion
### Chapter 052 — Infrared, BCF, Beadless and High-Purity Fusion
### Chapter 053 — Extrusion and Hot-Gas Welding
### Chapter 054 — Solvent Cementing for Applicable Material Families
### Chapter 055 — Flanges, Mechanical Joints, Plastic-to-Metal Transitions and Saddles
### Chapter 056 — Joining Qualification, Inspection, Traceability and Repair

Chapter 056 mandatory scope:

- WPS / joining-procedure control;
- procedure qualification;
- operator qualification;
- first-off joints;
- machine and heater calibration;
- fusion data logging;
- weld maps;
- traceability;
- visual/dimensional inspection;
- destructive sectioning;
- tensile/bend/peel/shear/crush tests as applicable;
- pressure/creep qualification;
- qualified NDT such as PAUT where applicable;
- defect taxonomy;
- acceptance criteria;
- repair limitations;
- approved repair procedures.

---

## PART VIII — Pipe and System Mechanical Design

### Chapter 057 — Internal Pressure Design, Hoop Stress and SDR/DR Geometry

Scope:

- hoop stress;
- axial pressure stress;
- thin/thick wall boundaries where relevant;
- SDR/DR relations;
- pressure classifications;
- end-cap loading;
- local stress intensification awareness.

### Chapter 058 — Axial Loads, End Thrust, Anchors and Guides

Scope:

- pressure forces at ends, bends and tees;
- anchors;
- guides;
- thrust blocks;
- restraint load paths;
- equipment/nozzle reactions.

### Chapter 059 — Thermal Expansion and Contraction

Scope:

- free and restrained movement;
- thermal strain;
- expansion loops and offsets;
- support friction;
- thermal cycling;
- imposed displacement.

### Chapter 060 — Pipe Supports, Support Spacing and Local Bearing

Scope:

- creep modulus;
- sag and deflection;
- support spacing;
- concentrated loads;
- local bearing;
- valves and heavy components;
- support fatigue and movement interfaces.

### Chapter 061 — Pressure Surge and Water Hammer

Scope:

- Joukowsky relation;
- wave speed;
- valve closure time;
- recurring and occasional surge;
- negative pressure;
- surge mitigation;
- limits of simplified methods.

### Chapter 062 — Vacuum, External Pressure and Buckling

Scope:

- vacuum;
- external pressure;
- ring buckling;
- ovality;
- submerged conditions;
- temporary construction states;
- draining and vacuum protection.

### Chapter 063 — Combined Loads and Stress Interaction

Scope:

- hoop/axial interaction;
- bending and torsion;
- equivalent/principal stress concepts where applicable;
- local hot spots;
- creep-fatigue interaction;
- sustained/occasional/cyclic combinations.

### Chapter 064 — Flexibility Analysis, Expansion Loops and Nozzle Loads

Scope:

- flexibility modelling;
- material model selection;
- model validation;
- nozzle-load vectors;
- support friction;
- expansion-joint pressure thrust;
- software-result sanity checks.

### Chapter 065 — Buried Pipe Design and Soil–Pipe Interaction

Scope:

- soil-pipe structural interaction;
- trench geometry;
- bedding/backfill;
- external loads;
- deflection;
- buckling;
- groundwater;
- traffic/construction loads;
- installation condition sensitivity.

### Chapter 066 — Above-Ground Systems, Mechanical Protection, Accessibility and Maintainability

Scope:

- above-ground routing;
- exposure;
- mechanical protection;
- impact and point-load protection;
- access to joints and components;
- inspection access;
- repair/replacement space;
- maintainability;
- support/component arrangement;
- inspection before concealment/insulation.

**Historical note:** Buried Pipe Design and Mechanical Protection/Accessibility/Maintainability are directly verified historical continuation topics. Exact historical titles of Chapters 76–77 remain unresolved and shall not be invented.

---

## PART IX — Construction, Pressure Testing and Commissioning

### Chapter 067 — Transport, Storage and Handling
### Chapter 068 — Buried Installation: Trenching, Bedding and Backfill
### Chapter 069 — Trenchless and Special Installation Methods
### Chapter 070 — Installation QA, Supports, Restraints and Pre-Concealment Inspection
### Chapter 071 — Hydrostatic and Pneumatic Pressure Testing
### Chapter 072 — Flushing, Drying, Purging, Reinstatement and Commissioning

Mandatory block scope:

- transport/storage damage prevention;
- handling limits;
- installation geometry;
- supports/restraints;
- independent support of valves, actuators, filters, meters and pumps;
- protection from impact and concentrated loads;
- test boundaries;
- temporary configurations and blinds;
- filling and air removal;
- venting;
- conditioning/stabilization;
- leak evaluation;
- temperature/elevation correction where applicable;
- pneumatic stored-energy risk;
- draining with vacuum protection;
- flushing;
- drying;
- purging;
- reinstatement of relief devices/instrumentation;
- commissioning records and checklists.

---

## PART X — Hydraulics and Process Transport

### Chapter 073 — Single-Phase Hydraulics for Plastic Piping Systems

Scope:

- continuity;
- velocity;
- Reynolds number;
- laminar/turbulent regimes;
- Darcy–Weisbach;
- friction factors;
- minor losses;
- pump/system curves;
- pressure drop and elevation;
- thermoplastic-specific design implications.

### Chapter 074 — Dimensionless Thinking and Scale Analysis

Scope:

- Reynolds, Froude, Weber, Euler and other relevant dimensionless groups;
- similarity;
- scale effects;
- limits of geometric similarity.

### Chapter 075 — Fundamentals of Multiphase Flow
### Chapter 076 — Gas–Liquid Flow
### Chapter 077 — Slurry and Liquid–Solid Transport
### Chapter 078 — Solids Suspension, Settling and Minimum Transport Conditions
### Chapter 079 — Gas–Liquid–Solid / Three-Phase Flow
### Chapter 080 — Rheology and Non-Newtonian Process Fluids
### Chapter 081 — Erosion, Deposition, Fouling and Plugging
### Chapter 082 — Shutdown, Settling and Restart Philosophy
### Chapter 083 — Electrolyte and Reactive Process Transport

Chapter 083 mandatory application scope:

- KOH transport;
- Ni(OH)2 suspension service;
- hydrogen-generation interfaces;
- oxygen-generation interfaces;
- gas accumulation/release;
- local process-state changes along piping;
- shutdown/restart implications.

### Chapter 084 — Heat Transfer, Mass Transfer, Scale-Up and CFD

Scope:

- heat transfer in plastic piping;
- wall thermal resistance;
- convective transport;
- mass transfer where relevant;
- process scale-up;
- CFD use and misuse;
- model verification and validation;
- experimental correlation.

**Historical recovery rule:** multiphase flow, slurry transport, gas-liquid-solid systems, restart philosophy, erosion, deposition and electrolyte transport are verified mandatory post-78 historical intent regardless of final numbering.

---

## PART XI — Equipment and Process-System Integration

### Chapter 085 — Pumps and Pump Interfaces
### Chapter 086 — Valves and Actuators
### Chapter 087 — Filters, Strainers, Flowmeters and Instrument Interfaces
### Chapter 088 — Tanks, Vessels, Vents, Drains and Relief-System Interfaces
### Chapter 089 — Process Skids, Utilities, Vibration and Equipment Integration
### Chapter 090 — Gas-Generation and Electrolyzer Piping Systems

Mandatory block scope:

- equipment nozzle loads;
- rotating-equipment vibration/pulsation;
- component support;
- isolation philosophy;
- drains/vents;
- relief interfaces;
- utility interfaces;
- alkaline-electrolyzer context;
- maintenance and safe isolation at equipment boundaries.

---

## PART XII — Quality, Inspection and Asset Integrity

### Chapter 091 — QA/QC Philosophy and Inspection/Test Planning
### Chapter 092 — Material/Product Traceability, Conformity and NCR Control
### Chapter 093 — Inspection, Destructive Examination and Qualified NDT
### Chapter 094 — Maintenance Strategy and Inspection Planning
### Chapter 095 — Remaining Life Assessment and Fitness for Continued Service
### Chapter 096 — Supports, Anchors, Bolts and Lifecycle Mechanical Integrity

Mandatory scope:

- ITP;
- hold/witness points;
- lot boundaries;
- record retention;
- joining records;
- equipment calibration;
- acceptance criteria;
- qualified NDT boundaries;
- evidence maturity;
- inspection intervals;
- degradation trending;
- support/anchor/bolt fatigue;
- lifecycle decision criteria.

---

## PART XIII — Failure Analysis and Root-Cause Investigation

### Chapter 097 — Failure Investigation Strategy and Evidence Preservation
### Chapter 098 — Fractography and Laboratory Evidence for Plastic Piping
### Chapter 099 — Joint, Fusion, Flange and Connection Failures
### Chapter 100 — Root-Cause Analysis Methods and Hypothesis Testing
### Chapter 101 — Extent of Condition, CAPA, Verification of Effectiveness and MOC

Mandatory mechanisms and evidence scope:

- ductile overload;
- SCG;
- fatigue;
- RCP;
- butt-fusion interface failure;
- electrofusion lack of fusion / decohesion;
- flange leakage;
- mechanical pullout;
- vacuum collapse;
- chemical degradation;
- oxidative degradation;
- ESC;
- external and installation damage;
- support-induced failure;
- branch/concentrated-load failures;
- wall-thickness mapping;
- optical microscopy;
- SEM/EDS;
- FTIR;
- DSC/OIT;
- MFR and density;
- tensile/bend/peel/crush/SCG investigation testing;
- reference samples;
- process historian data;
- weld logs;
- as-built/support review;
- Five Whys;
- Fishbone;
- Fault Tree;
- Barrier Analysis;
- Hypothesis Matrix;
- evidence grading: possible / probable / confirmed / unlikely;
- corrective versus preventive action;
- extent of condition;
- effectiveness verification;
- post-failure MOC.

---

## PART XIV — Process Safety and Special Hazards

### Chapter 102 — Process Safety Interfaces and HAZOP for Plastic Piping
### Chapter 103 — Flow-Induced and Mechanical Vibration
### Chapter 104 — Cavitation and Transient Damage
### Chapter 105 — Electrostatic Hazards, Fire and Hazardous Gas Interfaces
### Chapter 106 — Gas Permeation, Hydrogen Service and Metallic-Interface Concerns

Mandatory scope:

- HAZOP preparation interfaces;
- credible failure scenarios;
- stored energy;
- ignition/static charging;
- venting and gas accumulation;
- permeation;
- hydrogen/oxygen service;
- metallic-component concerns including hydrogen-related degradation where relevant;
- interface between plastic piping and process-safety layers.

---

## PART XV — Human, Digital and Future Engineering

### Chapter 107 — Human Factors and Operational Error in Plastic Piping Systems
### Chapter 108 — Sensors, Condition Monitoring and Digital Twin
### Chapter 109 — Predictive Maintenance and Data-Driven Asset Integrity
### Chapter 110 — AI, Emerging Materials, Advanced Joining/NDT and Future Technologies

Rules for Future Technologies:

- historical intent is verified at domain level;
- exact historical subtopics are not yet fully recovered;
- candidates may include emerging materials, advanced joining, monitoring, NDT, digital engineering and advanced piping architectures;
- no candidate shall be represented as historical fact without source evidence;
- new developments must be clearly separated from historical recovery.

---

## PART XVI — Industrial Case Studies and Lessons Learned

Case studies may be integrated throughout technical chapters and/or collected in a dedicated final Part.

Mandatory case-study method:

1. select only educationally useful cases;
2. separate verified facts, official findings and PPE-BoK interpretation;
3. verify material facts through reliable independent evidence;
4. connect the case to a mechanism and an engineering decision;
5. use failures and near misses as feedback into Design Basis, qualification, installation, inspection or operation;
6. avoid anecdotal or vendor-marketing examples presented as evidence.

Potential case-study families include:

- pressure-pipe failures;
- fusion/joint failures;
- installation/support failures;
- cyclic-pressure and transient cases;
- chemical/environmental degradation;
- buried-pipe failures;
- vacuum/buckling cases;
- slurry/deposition/restart cases;
- process-plant and electrolyzer piping cases.

**Numbering hold:** dedicated case-study chapter numbers will be assigned only after the technical architecture is mature.

---

# 6. Standards and cross-framework layer — applies book-wide

The book shall not treat standards as a bibliography. Standards are engineering navigation tools.

Every applicable technical chapter shall identify the relevant standards path, potentially including:

- ISO;
- EN / European frameworks;
- ASTM / PPI;
- DVS;
- AWWA;
- API;
- ASME;
- product standards;
- design standards;
- test standards;
- application-specific standards;
- regulatory/project requirements.

Book-wide requirements:

- edition control;
- applicability and precedence;
- product vs design vs test standard distinction;
- clause-level verification for normative claims;
- terminology crosswalks;
- no silent mixing of incompatible frameworks;
- standards-derived equations, coefficients, limits and interpretations remain subject to Standards Validation.

---

# 7. Engineering workflow layer — applies to every chapter

Where technically meaningful, chapters should follow the PPE-BoK engineering-use sequence:

`Question → Applicable Standards / Evidence → Required Inputs → Engineering Logic → Physics / Mechanism → Calculation → Verification → Decision → Documentation → Failure Modes / Common Mistakes`

A chapter should enable a competent engineer to answer:

- What is the engineering question?
- Why does the mechanism matter?
- Which inputs are required?
- Which standards/evidence govern?
- Which equations or methods apply?
- What assumptions and validity limits exist?
- How is the result independently checked?
- What engineering decision follows?
- What remains project-specific?
- What evidence should be retained?
- What common mistakes invalidate the conclusion?

---

# 8. Mandatory appendices

## Appendix A — Engineering Tables

Centralized tables may include:

- SDR / DR;
- pipe dimensional series;
- Schedule cross-reference where relevant;
- PE, PP, PVC, CPVC, PVDF, ECTFE, FEP, PFA, PTFE and specialty materials;
- modulus;
- density;
- Poisson ratio;
- thermal expansion;
- thermal conductivity;
- temperature ranges;
- UV/environmental considerations;
- chemical compatibility;
- pressure derating / temperature treatment where appropriately sourced;
- selected fluid and slurry properties;
- support/design reference values where justified.

## Appendix B — Industrial Equations Handbook

Target: approximately 300–500 equations collected from the book, organized by topic.

Mandatory families include:

- mechanics;
- pressure design;
- stress/strain;
- buckling;
- fatigue;
- creep;
- fracture;
- hydraulics;
- surge;
- multiphase flow;
- slurry transport;
- rheology;
- heat transfer;
- mass transfer;
- thermal expansion;
- settling;
- erosion/deposition correlations where justified;
- scale-up and dimensionless groups.

Every equation entry shall include variable definitions, units, assumptions, validity limits, source/derivation basis and misuse notes where needed.

## Appendix C — Engineering Checklists

Mandatory checklist families:

- Design Review;
- material-selection review;
- standards-path review;
- HAZOP preparation;
- joining/fusion readiness;
- FAT;
- SAT;
- hydrotest / pressure test;
- commissioning;
- shutdown;
- restart;
- maintenance;
- inspection planning;
- failure investigation;
- Root Cause Analysis;
- Remaining Life Assessment;
- reinstatement;
- MOC / requalification.

Additional appendices may be created for:

- symbols and nomenclature;
- glossary;
- standards register;
- bibliography;
- terminology crosswalks;
- worked-calculation index;
- engineering-asset index.

---

# 9. Controlled historical-recovery holds

The following are intentionally unresolved and shall not be filled by guesswork:

1. Exact historical titles and scope of Chapters 76–77 in the old architecture.
2. Exact numbering/title mapping of post-78 historical topics.
3. Confirmation of the complete old program through approximately Chapter 91.
4. Exact historical subtopics under Future Technologies.
5. Any additional Parts/Volumes planned beyond the recovered program.
6. Whether several specialty-material families should receive individual chapters or controlled grouped chapters.
7. Whether Industrial Case Studies are a dedicated Part, integrated chapter assets, or both.

Historical uncertainty does **not** permit removal of the verified knowledge scope.

---

# 10. Coverage states used during development

Every recovered atomic topic shall eventually receive one formal state:

- **FULLY COVERED** — current treatment preserves subject and intended depth.
- **PARTIALLY COVERED** — subject exists but depth or engineering utility is insufficient.
- **ABSORBED / DUPLICATED** — equivalent/better treatment exists elsewhere.
- **PLANNED BUT MISSING** — intended topic not yet developed.
- **NEEDS DEEPER TREATMENT** — currently summary/background only.
- **HISTORICAL INTENT NOT YET VERIFIED** — suspected historical topic without direct evidence.

No final TOC may be frozen until the Topic-to-Current-Chapter Coverage Audit is complete.

---

# 11. Final book completion sequence

## Stage 1 — Content Development

- complete all required domains;
- do not constrain the book to a chapter count;
- open new chapters where engineering depth requires them;
- retain standards/evidence hold points explicitly.

## Stage 2 — Technical Review

Review book-wide:

- every equation;
- every unit;
- every mathematical symbol;
- variable definitions;
- internal consistency;
- cross-chapter definitions;
- tables;
- worked examples;
- case-study factual basis;
- engineering decisions and applicability limits.

This stage is effectively a full engineering peer review.

## Stage 3 — Editorial / Architecture Review

Freeze only here:

- final Parts;
- final chapter numbering;
- chapter titles;
- Table of Contents;
- cross-references;
- glossary;
- index;
- list of symbols;
- standards list;
- bibliography;
- appendix structure.

## Stage 4 — Final Engineering Review

For every chapter ask:

> האם מהנדס בכיר באמת היה משתמש בפרק הזה בפרויקט אמיתי?

If the answer is not clearly yes, the chapter returns for improvement.

---

# 12. Immediate continuation checkpoint

Current practical sequence after the controlled Chapter 13 integration:

1. Keep Chapter 013 full-text Standards Validation controlled under Issue #9; do not represent it as publication-frozen.
2. Acquire or lawfully access the current authoritative standards needed to close `SVH-013-01` through `SVH-013-05`, then return Chapter 013 to final Standards Validation and Design Freeze.
3. In parallel with that external source-access hold, prepare the controlled Chapter Design Brief for Working Chapter 014.
4. Review the Chapter 014 CDB against `governance/Definition-of-Ready.md` and obtain explicit author approval.
5. Only after that approval, begin Chapter 014 Engineering Development using the recovered first-principles polymer-science scope.
6. Continue sequentially while maintaining the Master Knowledge-Scope coverage map and preserving Chapter 013’s unresolved publication gates until they are formally closed.

The current intended first new chapter is:

> **Working Chapter 014 — Atomic Structure, Chemical Bonding and Carbon Chemistry for Polymer Engineers**
