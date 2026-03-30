#!/usr/bin/env python3
"""
References Integration Demo
Shows how references are integrated into report generation
"""

import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from config_models import ReportConfig, Reference
from references import BibliographyGenerator, ReferenceEntry


def demo_config_with_references():
    """Demo: Create config with references"""
    print("=" * 60)
    print("Demo: Config with References")
    print("=" * 60)
    
    config_dict = {
        'project_info': {
            'title': 'AI Search Algorithms Study',
            'description': 'A comprehensive study of search algorithms in AI',
            'students': [{'name': 'John Doe', 'id': '123456'}],
            'university': 'Test University'
        },
        'report_profile': {
            'report_type': 'project_report',
            'language': 'en'
        },
        'technical_data': {
            'algorithms': ['BFS', 'DFS', 'A*']
        },
        'evidence': {
            'references': [
                {
                    'id': '1',
                    'authors': ['Stuart Russell', 'Peter Norvig'],
                    'title': 'Artificial Intelligence: A Modern Approach',
                    'year': 2020,
                    'source': 'Pearson'
                },
                {
                    'id': '2',
                    'authors': ['Edsger Dijkstra'],
                    'title': 'A Note on Two Problems in Connexion with Graphs',
                    'year': 1959,
                    'source': 'Numerische Mathematik'
                }
            ]
        },
        'format_rules': {
            'citation_style': 'IEEE'
        }
    }
    
    # Validate config
    config = ReportConfig(**config_dict)
    print(f"\n✓ Config validated")
    print(f"  References: {len(config.evidence.references)}")
    print(f"  Citation style: {config.format_rules.citation_style}")
    
    # Generate bibliography
    ref_entries = [
        ReferenceEntry.from_config_model(ref)
        for ref in config.evidence.references
    ]
    
    gen = BibliographyGenerator(style=config.format_rules.citation_style)
    bib = gen.generate(ref_entries)
    
    print(f"\n✓ Generated bibliography:")
    print("-" * 60)
    print(bib)
    print()


def demo_inline_citations():
    """Demo: Using inline citations in text"""
    print("=" * 60)
    print("Demo: Inline Citations")
    print("=" * 60)
    
    ref1 = ReferenceEntry(
        id="1",
        authors=["Stuart Russell", "Peter Norvig"],
        title="Artificial Intelligence: A Modern Approach",
        year=2020,
        type="book"
    )
    
    ref2 = ReferenceEntry(
        id="2",
        authors=["Edsger Dijkstra"],
        title="A Note on Two Problems in Connexion with Graphs",
        year=1959,
        type="article"
    )
    
    ieee_gen = BibliographyGenerator(style='IEEE')
    apa_gen = BibliographyGenerator(style='APA')
    
    # Example text with citations
    text_ieee = f"""
Search algorithms are fundamental to AI {ieee_gen.get_inline_citation(ref1)}.
The Dijkstra algorithm {ieee_gen.get_inline_citation(ref2)} is widely used
for finding shortest paths in graphs.
"""
    
    text_apa = f"""
Search algorithms are fundamental to AI {apa_gen.get_inline_citation(ref1)}.
The Dijkstra algorithm {apa_gen.get_inline_citation(ref2)} is widely used
for finding shortest paths in graphs.
"""
    
    print("\nIEEE style text:")
    print(text_ieee)
    
    print("\nAPA style text:")
    print(text_apa)
    print()


def demo_bibliography_section():
    """Demo: Generate complete bibliography section"""
    print("=" * 60)
    print("Demo: Bibliography Section for Report")
    print("=" * 60)
    
    references = [
        ReferenceEntry(
            id="1",
            authors=["Stuart Russell", "Peter Norvig"],
            title="Artificial Intelligence: A Modern Approach",
            year=2020,
            publisher="Pearson",
            type="book"
        ),
        ReferenceEntry(
            id="2",
            authors=["Ian Goodfellow", "Yoshua Bengio", "Aaron Courville"],
            title="Deep Learning",
            year=2016,
            publisher="MIT Press",
            type="book"
        ),
        ReferenceEntry(
            id="3",
            authors=["Yann LeCun", "Yoshua Bengio", "Geoffrey Hinton"],
            title="Deep learning",
            year=2015,
            source="Nature",
            volume="521",
            pages="436-444",
            type="article"
        )
    ]
    
    gen = BibliographyGenerator(style='IEEE')
    section = gen.generate_section(references)
    
    print(f"\nSection type: {section['type']}")
    print(f"Section title: {section['title']}")
    print(f"Reference count: {section['metadata']['count']}")
    print(f"Citation style: {section['metadata']['style']}")
    print(f"\nFormatted content:")
    print("-" * 60)
    print(section['content'])
    print()


if __name__ == '__main__':
    print("\nReferences Integration Demo\n")
    
    demo_config_with_references()
    demo_inline_citations()
    demo_bibliography_section()
    
    print("=" * 60)
    print("✅ All demos completed!")
    print("=" * 60)
    print()
