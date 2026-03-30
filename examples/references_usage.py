#!/usr/bin/env python3
"""
References Engine Usage Examples
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from references import ReferenceEntry, APAFormatter, IEEEFormatter, BibliographyGenerator


def example_basic_formatting():
    """Example 1: Basic citation formatting"""
    print("=" * 60)
    print("Example 1: Basic Citation Formatting")
    print("=" * 60)
    
    # Create a reference
    ref = ReferenceEntry(
        id="Russell2020",
        authors=["Stuart Russell", "Peter Norvig"],
        title="Artificial Intelligence: A Modern Approach",
        year=2020,
        publisher="Pearson",
        type="book"
    )
    
    # APA format
    apa = APAFormatter()
    print("\nAPA Format:")
    print(f"Full: {apa.format_citation(ref)}")
    print(f"Inline: {apa.format_inline(ref)}")
    
    # IEEE format
    ieee = IEEEFormatter()
    print("\nIEEE Format:")
    print(f"Full: {ieee.format_citation(ref)}")
    print(f"Inline: {ieee.format_inline(ref)}")
    print()


def example_journal_article():
    """Example 2: Journal article"""
    print("=" * 60)
    print("Example 2: Journal Article")
    print("=" * 60)
    
    ref = ReferenceEntry(
        id="Smith2019",
        authors=["John Smith", "Alice Doe"],
        title="Deep Learning for Natural Language Processing",
        year=2019,
        source="Journal of Machine Learning Research",
        volume="20",
        issue="3",
        pages="123-145",
        type="article"
    )
    
    apa = APAFormatter()
    ieee = IEEEFormatter()
    
    print("\nAPA:", apa.format_citation(ref))
    print("\nIEEE:", ieee.format_citation(ref))
    print()


def example_bibliography_generation():
    """Example 3: Generate bibliography"""
    print("=" * 60)
    print("Example 3: Bibliography Generation")
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
    
    # IEEE style
    print("\nIEEE Style Bibliography:")
    print("-" * 60)
    ieee_gen = BibliographyGenerator(style='IEEE')
    print(ieee_gen.generate(references))
    
    # APA style
    print("\n\nAPA Style Bibliography:")
    print("-" * 60)
    apa_gen = BibliographyGenerator(style='APA')
    print(apa_gen.generate(references))
    print()


def example_inline_citations():
    """Example 4: Inline citations"""
    print("=" * 60)
    print("Example 4: Inline Citations")
    print("=" * 60)
    
    ref1 = ReferenceEntry(
        id="1",
        authors=["John Smith"],
        title="Example Paper",
        year=2020,
        type="article"
    )
    
    ref2 = ReferenceEntry(
        id="2",
        authors=["Alice Doe", "Bob Johnson"],
        title="Another Paper",
        year=2021,
        type="article"
    )
    
    ref3 = ReferenceEntry(
        id="3",
        authors=["Tom Lee", "Sarah Chen", "Mike Brown"],
        title="Third Paper",
        year=2022,
        type="article"
    )
    
    ieee_gen = BibliographyGenerator(style='IEEE')
    apa_gen = BibliographyGenerator(style='APA')
    
    print("\nIEEE inline citations:")
    print(f"Single author: {ieee_gen.get_inline_citation(ref1)}")
    print(f"Two authors: {ieee_gen.get_inline_citation(ref2)}")
    print(f"Three+ authors: {ieee_gen.get_inline_citation(ref3)}")
    
    print("\nAPA inline citations:")
    print(f"Single author: {apa_gen.get_inline_citation(ref1)}")
    print(f"Two authors: {apa_gen.get_inline_citation(ref2)}")
    print(f"Three+ authors: {apa_gen.get_inline_citation(ref3)}")
    print()


def example_section_generation():
    """Example 5: Generate section data"""
    print("=" * 60)
    print("Example 5: Section Data Generation")
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
        )
    ]
    
    gen = BibliographyGenerator(style='IEEE')
    section = gen.generate_section(references)
    
    print(f"\nSection type: {section['type']}")
    print(f"Section title: {section['title']}")
    print(f"Reference count: {section['metadata']['count']}")
    print(f"Citation style: {section['metadata']['style']}")
    print(f"\nContent preview:")
    print(section['content'][:200] + "...")
    print()


if __name__ == '__main__':
    print("\nReferences Engine Usage Examples\n")
    
    example_basic_formatting()
    example_journal_article()
    example_bibliography_generation()
    example_inline_citations()
    example_section_generation()
    
    print("=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)
    print()
