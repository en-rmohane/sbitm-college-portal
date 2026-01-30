
import os

style_path = r"c:\Users\ravik\.gemini\antigravity\scratch\sbitm_college\static\css\style.css"

# New CSS to append
new_css = """
/* Professional Faculty Redesign 2.0 (Strict Scope) */

/* 1. Scoped HOD Container */
.prof-hod-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 50px;
}

.prof-hod-wrapper .prof-faculty-card {
    max-width: 360px;
    width: 100%;
    border-color: var(--primary);
    box-shadow: 0 0 25px rgba(14, 165, 233, 0.15);
    transform: scale(1.02);
}

/* 2. Scoped Grid */
.prof-faculty-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(280px, 1fr)); /* Desktop */
    gap: 30px;
    margin-bottom: 80px;
}

/* 3. Scoped Card */
.prof-faculty-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 30px;
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

/* 4. Strict Image Sizing */
.prof-faculty-img-box {
    width: 100px; /* STRICT 100px */
    height: 100px; /* STRICT 100px */
    flex-shrink: 0;
    margin-bottom: 20px;
    position: relative;
}

.prof-faculty-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid var(--primary);
    padding: 3px;
    background: transparent;
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
    flex-grow: 1; /* Pushes button down */
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

/* 7. Department Divider (Clean) */
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
        grid-template-columns: repeat(2, 1fr); /* 2 Cols Tablet */
    }
}

@media (max-width: 768px) {
    .prof-faculty-grid {
        grid-template-columns: 1fr; /* 1 Col Mobile */
    }
    
    .prof-hod-wrapper .prof-faculty-card {
        max-width: 100%;
    }
}
"""

# Read and clean
clean_lines = []
with open(style_path, 'rb') as f:
    content = f.read()
    # Decode ignoring errors to find the good part, then strip garbage
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        # If utf-8 fails, try to salvage
        text = content.decode('utf-8', errors='ignore')

    # Remove the spaced out characters (which look like " . p r o f " etc)
    # Finding the last valid CSS closing brace } before the garbage starts.
    # We know the garbage starts with "/ *   P r o f"
    
    last_valid_idx = text.rfind(".prof-hod-wrapper")
    if last_valid_idx == -1:
        # If we can't find the garbage start easily, let's look for the end of the previous known good block
        # The previous block ended with mobile breakpoint closing brace
        pass

    # Better approach: Read lines, discard lines that appear to be spaced-out garbage
    lines = text.splitlines()
    for line in lines:
        if "/ *   P r o f" in line or " . p r o f" in line:
            continue # Skip garbage
        if line.strip() == "":
            clean_lines.append(line)
        else:
            clean_lines.append(line)

# Write back clean content + new CSS
with open(style_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(clean_lines))
    f.write('\n' + new_css)

print("Fixed style.css encoding and appended new styles.")
