
import os

style_path = r"c:\Users\ravik\.gemini\antigravity\scratch\sbitm_college\static\css\style.css"

# Read content
with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Grid to Strict 3 Columns (remove minmax)
if "grid-template-columns: repeat(3, minmax(280px, 1fr));" in content:
    content = content.replace(
        "grid-template-columns: repeat(3, minmax(280px, 1fr));",
        "grid-template-columns: repeat(3, 1fr); /* STRICT 3 Columns */"
    )

# 2. Update Breakpoints (Tablet at 992px, Mobile at 576px)
# Find the responsiveness block to replace carefully
if "@media (max-width: 900px)" in content:
    # We replace the entire responsive block to be safe
    old_responsive_block = """/* 8. Responsiveness */
    @media (max-width: 900px) {
        .prof-faculty-grid {
            grid-template-columns: repeat(2, 1fr);
            /* 2 Cols for Tablet */
        }
    }

    @media (max-width: 600px) {
        .prof-faculty-grid {
            grid-template-columns: 1fr;
            /* 1 Col Mobile */
        }

        .prof-hod-wrapper .prof-faculty-card {
            max-width: 100%;
        }
    }"""
    
    # Normalizing potential whitespace differences for search isn't easy with simple replace.
    # So we will search for the start of the block and truncate/append.
    start_idx = content.find("/* 8. Responsiveness */")
    if start_idx != -1:
        content = content[:start_idx] + """/* 8. Responsiveness */
@media (max-width: 992px) {
    .prof-faculty-grid {
        grid-template-columns: repeat(2, 1fr); /* 2 Cols Tablet (<992px) */
    }
}

@media (max-width: 576px) {
    .prof-faculty-grid {
        grid-template-columns: 1fr; /* 1 Col Mobile (<576px) */
    }
    
    .prof-hod-wrapper .prof-faculty-card {
        max-width: 100%;
    }
}"""

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated Grid to Strict 3-Col and adjusted breakpoints.")
