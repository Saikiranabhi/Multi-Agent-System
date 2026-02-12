# def build_report(analysis_text):
#     return f"""
# ===============================
# 📘 PAGE 1 — EXECUTIVE SUMMARY
# ===============================

# {analysis_text}

# ===============================
# 📘 PAGE 2 — TECHNICAL ANALYSIS
# ===============================

# {analysis_text}

# ===============================
# 📘 PAGE 3 — INSIGHTS & IMPACT
# ===============================

# {analysis_text}
# """




def build_report(analysis_text):
    """
    Build a structured 3-page report with proper formatting
    """
    # Parse the analysis into sections
    sections = parse_analysis(analysis_text)
    
    return f"""
═══════════════════════════════════════════════════════════
📘 PAGE 1 — EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════

RESEARCH OBJECTIVE:
{sections.get('objective', 'Not specified')}

METHODOLOGY:
{sections.get('methodology', 'Not specified')}

CORE CONTRIBUTIONS:
{sections.get('contributions', 'Not specified')}

═══════════════════════════════════════════════════════════
📘 PAGE 2 — TECHNICAL ANALYSIS
═══════════════════════════════════════════════════════════

EXPERIMENTAL EVIDENCE:
{sections.get('evidence', 'Not specified')}

NOVELTY & INNOVATION:
{sections.get('novelty', 'Not specified')}

STRENGTHS:
{sections.get('strengths', 'Not specified')}

WEAKNESSES:
{sections.get('weaknesses', 'Not specified')}

═══════════════════════════════════════════════════════════
📘 PAGE 3 — INSIGHTS & IMPACT
═══════════════════════════════════════════════════════════

LIMITATIONS:
{sections.get('limitations', 'Not specified')}

PRACTICAL IMPACT:
{sections.get('impact', 'Not specified')}

RECOMMENDED FOLLOW-UP RESEARCH:
{sections.get('future_work', 'Based on the analysis, further research is recommended in the identified areas.')}
"""


def parse_analysis(analysis_text):
    """
    Parse the Gemini analysis into structured sections
    """
    sections = {}
    
    # Split by common section markers
    text_lower = analysis_text.lower()
    
    # Extract each section
    if '- research objective' in text_lower or 'research objective:' in text_lower:
        sections['objective'] = extract_section(analysis_text, 
            ['research objective', 'objective'], 
            ['methodology', 'method'])
    
    if '- methodology' in text_lower or 'methodology:' in text_lower:
        sections['methodology'] = extract_section(analysis_text, 
            ['methodology', 'method'], 
            ['core contributions', 'contributions', 'experimental'])
    
    if '- core contributions' in text_lower or 'core contributions:' in text_lower:
        sections['contributions'] = extract_section(analysis_text, 
            ['core contributions', 'contributions'], 
            ['experimental', 'evidence', 'novelty'])
    
    if '- experimental evidence' in text_lower or 'experimental evidence:' in text_lower:
        sections['evidence'] = extract_section(analysis_text, 
            ['experimental evidence', 'evidence'], 
            ['novelty', 'strengths'])
    
    if '- novelty' in text_lower or 'novelty:' in text_lower:
        sections['novelty'] = extract_section(analysis_text, 
            ['novelty', 'innovation'], 
            ['strengths', 'weakness'])
    
    if '- strengths' in text_lower or 'strengths:' in text_lower:
        sections['strengths'] = extract_section(analysis_text, 
            ['strengths'], 
            ['weaknesses', 'weakness', 'limitations'])
    
    if '- weaknesses' in text_lower or 'weaknesses:' in text_lower:
        sections['weaknesses'] = extract_section(analysis_text, 
            ['weaknesses', 'weakness'], 
            ['limitations', 'practical impact'])
    
    if '- limitations' in text_lower or 'limitations:' in text_lower:
        sections['limitations'] = extract_section(analysis_text, 
            ['limitations', 'limitation'], 
            ['practical impact', 'impact'])
    
    if '- practical impact' in text_lower or 'practical impact:' in text_lower:
        sections['impact'] = extract_section(analysis_text, 
            ['practical impact', 'impact'], 
            ['future', 'conclusion'])
    
    return sections


def extract_section(text, start_markers, end_markers):
    """
    Extract a section of text between start and end markers
    """
    text_lower = text.lower()
    
    # Find start position
    start_pos = -1
    for marker in start_markers:
        pos = text_lower.find(marker)
        if pos != -1:
            start_pos = pos
            break
    
    if start_pos == -1:
        return ""
    
    # Find end position
    end_pos = len(text)
    for marker in end_markers:
        pos = text_lower.find(marker, start_pos + 1)
        if pos != -1 and pos < end_pos:
            end_pos = pos
    
    # Extract and clean the section
    section = text[start_pos:end_pos].strip()
    
    # Remove the marker itself
    for marker in start_markers:
        section = section.replace(marker, '', 1)
        section = section.replace(marker.title(), '', 1)
        section = section.replace(marker.upper(), '', 1)
    
    # Remove leading symbols and whitespace
    section = section.lstrip('-:•● \n\t')
    
    return section.strip()