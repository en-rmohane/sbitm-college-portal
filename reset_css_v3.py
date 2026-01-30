
import os
import re

style_path = r"c:\Users\ravik\.gemini\antigravity\scratch\sbitm_college\static\css\style.css"

# The Fresh v3 CSS
v3_css = """
/* =========================================
   FACULTY PAGE V3 (CLEAN SLATE)
   ========================================= */

/* Department Section Header */
.fac-v3-dept-section {
    border-left: 5px solid var(--primary);
    padding-left: 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 15px;
}

.fac-v3-dept-title {
    font-size: 1.8rem;
    color: var(--text-light);
    margin: 0;
}

/* HOD Wrapper - Centered Top */
.fac-v3-hod-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 60px;
}

/* Grid Layout - Strict 3 Columns */
.fac-v3-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Force 3 columns */
    gap: 30px;
    margin-bottom: 60px;
}

/* Card Styling */
.fac-v3-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
}

.hod-card {
    max-width: 350px;
    width: 100%;
    background: rgba(0, 0, 0, 0.4); /* Slightly darker for distinction */
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border-color: var(--primary);
}

.fac-v3-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--primary);
}

/* Image Styling - Fixed 120px */
.fac-v3-img-box {
    width: 120px;
    height: 120px;
    margin-bottom: 20px;
    border-radius: 50%;
    overflow: hidden;
    flex-shrink: 0;
}

.fac-v3-img-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border: 3px solid var(--primary);
    border-radius: 50%;
}

/* Typography */
.fac-v3-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-light);
    margin-bottom: 5px;
    line-height: 1.3;
}

.fac-v3-role {
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}

.fac-v3-spec {
    font-size: 0.85rem;
    color: var(--text-dim);
    margin-bottom: 20px;
    flex-grow: 1; /* Pushes button down */
}

/* Button */
.fac-v3-btn {
    display: inline-block;
    padding: 8px 25px;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    color: var(--text-dim);
    text-decoration: none;
    font-size: 0.85rem;
    transition: 0.3s;
    width: 100%;
    box-sizing: border-box;
}

.fac-v3-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

/* Badge */
.fac-v3-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    padding: 4px 10px;
    border-radius: 20px;
    color: white;
    font-size: 0.7rem;
    font-weight: bold;
    text-transform: uppercase;
}

/* RESPONSIVENESS */
@media (max-width: 1024px) {
    .fac-v3-grid {
        grid-template-columns: repeat(2, 1fr); /* 2 cols on Tablet */
    }
}

@media (max-width: 600px) {
    .fac-v3-grid {
        grid-template-columns: 1fr; /* 1 col on Mobile */
    }
    
    .fac-v3-hod-wrapper .hod-card {
        max-width: 100%;
    }
}
"""

# Read file
with open(style_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Filter out OLD faculty CSS (prof-, faculty-, etc to be safe)
clean_lines = []
skip = False
for line in lines:
    # Basic filtering of known old blocks
    if "Professional Faculty Redesign" in line:
        continue
    if ".prof-" in line or ".faculty-" in line:
        continue
    # Filter specific old blocks if they span multiple lines and aren't caught above, 
    # but the above line-by-line check is safer for "messy" files than regex block replacement if indentation varies.
    clean_lines.append(line)

# Reassemble
final_content = "".join(clean_lines).rstrip() + "\n\n" + v3_css

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Faculty CSS completely reset to v3.")
