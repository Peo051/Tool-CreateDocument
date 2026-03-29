#!/usr/bin/env python3
"""Quick Generators Demo"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from generators import (
    IntroductionGenerator,
    MethodologyGenerator,
    ConclusionGenerator
)

# 1. Introduction
print("1. Introduction")
print("-" * 40)
gen = IntroductionGenerator()
section = gen.generate({
    'title': 'AI Maze Game',
    'domain': 'AI',
    'objectives': ['Implement pathfinding', 'Create AI agents']
})
print(f"Title: {section.title}")
print(f"Subsections: {len(section.subsections)}")

# 2. Methodology
print("\n2. Methodology")
print("-" * 40)
gen = MethodologyGenerator()
section = gen.generate({
    'approach': 'Multi-algorithm approach',
    'algorithms': ['A*', 'Dijkstra', 'BFS'],
    'tools': ['Python', 'NetworkX']
})
print(f"Title: {section.title}")
print(f"Algorithms: {section.metadata['algorithms_count']}")

# 3. Conclusion
print("\n3. Conclusion")
print("-" * 40)
gen = ConclusionGenerator()
section = gen.generate({
    'summary': 'Successfully implemented AI algorithms',
    'achievements': ['5 algorithms', 'Real-time performance'],
    'future_work': ['Add ML', 'Mobile support']
})
print(f"Title: {section.title}")
print(f"Achievements: {section.metadata['achievements_count']}")

# 4. Export
print("\n4. Export to Dict")
print("-" * 40)
data = section.to_dict()
print(f"Keys: {list(data.keys())}")
print(f"Subsections: {len(data['subsections'])}")

print("\n✅ Done!")
