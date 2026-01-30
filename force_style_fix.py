
import os

style_path = r"c:\Users\ravik\.gemini\antigravity\scratch\sbitm_college\static\css\style.css"

# The correct CSS block (3 Columns, 120px Images, Top HOD)
final_css = """
/* Professional Faculty Redesign 2.0 (Departments Match) */

/* 1. Scoped HOD Container */
.prof-hod-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 50px;
}

.prof-hod-wrapper .prof-faculty-card {
    max-width: 350px; /* Standout size */
    width: 100%;
    border-color: var(--primary);
    box-shadow: 0 0 20px rgba(14, 165, 233, 0.15);
    background: rgba(0, 0, 0, 0.3);
    transform: scale(1.0);
}

/* 2. Scoped Grid */
.prof-faculty-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(280px, 1fr)); /* 3 Columns requested */
    gap: 30px;
    margin-bottom: 80px;
}

/* 3. Scoped Card */
.prof-faculty-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 25px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    height: 100%;
    position: relative;
    transition: all 0.3s ease;
}

.prof-faculty-card:hover {
    background: rgba(255, 255, 255, 0.06);
    transform: translateY(-5px);
    border-color: var(--primary);
}

/* 4. Strict Image Sizing (120px) */
.prof-faculty-img-box {
    width: 120px;
    height: 120px;
    flex-shrink: 0;
    margin-bottom: 20px;
    position: relative;
    border-radius: 50%;
}

.prof-faculty-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid var(--primary);
    padding: 0;
}

/* 5. Typography */
.prof-faculty-name {
    color: var(--text-light);
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 5px;
    line-height: 1.3;
}

.prof-faculty-role {
    color: var(--primary);
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.prof-faculty-spec {
    color: var(--text-dim);
    font-size: 0.85rem;
    margin-bottom: 20px;
    line-height: 1.5;
    flex-grow: 1; 
}

.prof-actions {
    width: 100%;
    margin-top: auto;
}

.prof-btn {
    display: block;
    width: 100%;
    padding: 10px 0;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    color: var(--text-dim);
    text-decoration: none;
    font-size: 0.85rem;
    transition: 0.3s;
}

.prof-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

/* 6. HOD Badge */
.prof-hod-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: var(--primary);
    color: white;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    text-transform: uppercase;
}

/* 7. Dept Divider */
.prof-dept-divider {
    display: flex;
    align-items: center;
    margin-bottom: 50px;
    padding-bottom: 15px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.prof-dept-title {
    color: var(--text-light);
    font-size: 1.8rem;
    margin: 0;
    padding-left: 15px;
    border-left: 5px solid var(--primary);
}

/* 8. Responsiveness */
@media (max-width: 1024px) {
    .prof-faculty-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .prof-faculty-grid {
        grid-template-columns: 1fr;
    }
    .prof-hod-wrapper .prof-faculty-card {
        max-width: 100%;
    }
}
"""

with open(style_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace the incorrect block we added earlier
if "/* Professional Faculty Redesign 2.0 (Compact Version) */" in content:
    # Find start
    start_idx = content.find("/* Professional Faculty Redesign 2.0 (Compact Version) */")
    # Finding end is tricky without specific anchor, lets assume it goes to end of file if it was appended last
    # Or strict replacement
    content = content[:start_idx] + final_css
elif "/* Professional Faculty Redesign 2.0 (Strict Scope) */" in content:
     start_idx = content.find("/* Professional Faculty Redesign 2.0 (Strict Scope) */")
     content = content[:start_idx] + final_css
else:
    # Just append if not found (fallback)
    content += "\n" + final_css

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forced update of style.css complete.")
