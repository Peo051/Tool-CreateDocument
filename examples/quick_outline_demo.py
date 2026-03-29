#!/usr/bin/env python3
"""Quick OutlinePlanner Demo"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from outline_planner import OutlinePlanner

# Initialize planner
planner = OutlinePlanner()

# Example 1: Simple thesis outline
print("1. Thesis Outline:")
outline = planner.plan('thesis')
print(f"   Sections: {len(outline.sections)}")

# Example 2: Project report with algorithms
print("\n2. Project Report with Algorithms:")
config = {'algorithms': ['DFS', 'BFS', 'A*']}
outline = planner.plan('project_report', config)
for section in outline.sections:
    print(f"   - {section.title}")
    if section.id == 'algorithms':
        for sub in section.subsections:
            print(f"     • {sub.title}")

# Example 3: Custom sections
print("\n3. Technical Report with Custom Section:")
config = {
    'custom_sections': [{
        'id': 'security',
        'title': 'Security Analysis',
        'level': 1,
        'position': 5
    }]
}
outline = planner.plan('technical_report', config)
for i, section in enumerate(outline.sections, 1):
    print(f"   {i}. {section.title}")

# Example 4: Export to dict
print("\n4. Export to Dictionary:")
outline = planner.plan('business_report')
data = outline.to_dict()
print(f"   Type: {data['report_type']}")
print(f"   Sections: {len(data['sections'])}")
print(f"   First section: {data['sections'][0]['title']}")

print("\n✅ Done!")
