"""
Test references engine
"""

import pytest
from source.references import ReferenceEntry, APAFormatter, IEEEFormatter, BibliographyGenerator


def test_reference_entry_creation():
    """Test creating reference entry"""
    ref = ReferenceEntry(
        id="test1",
        authors=["John Doe"],
        title="Test Article",
        year=2020
    )
    
    assert ref.id == "test1"
    assert ref.authors == ["John Doe"]
    assert ref.year == 2020


def test_reference_entry_validation():
    """Test reference validation"""
    # Empty authors should fail
    with pytest.raises(ValueError):
        ReferenceEntry(
            id="test",
            authors=[],
            title="Test",
            year=2020
        )
    
    # Invalid year should fail
    with pytest.raises(ValueError):
        ReferenceEntry(
            id="test",
            authors=["John Doe"],
            title="Test",
            year=1800
        )


def test_apa_single_author():
    """Test APA format with single author"""
    ref = ReferenceEntry(
        id="test1",
        authors=["John Smith"],
        title="Example Article",
        year=2020,
        type="article"
    )
    
    formatter = APAFormatter()
    citation = formatter.format_citation(ref)
    inline = formatter.format_inline(ref)
    
    assert "Smith" in citation
    assert "2020" in citation
    assert "Example Article" in citation
    assert "(Smith, 2020)" == inline


def test_apa_multiple_authors():
    """Test APA format with multiple authors"""
    ref = ReferenceEntry(
        id="test2",
        authors=["John Smith", "Alice Doe", "Bob Johnson"],
        title="Example Article",
        year=2021,
        type="article"
    )
    
    formatter = APAFormatter()
    inline = formatter.format_inline(ref)
    
    # Three+ authors should use "et al."
    assert "et al." in inline
    assert "2021" in inline


def test_ieee_single_author():
    """Test IEEE format with single author"""
    ref = ReferenceEntry(
        id="1",
        authors=["John Smith"],
        title="Example Article",
        year=2020,
        type="article"
    )
    
    formatter = IEEEFormatter()
    citation = formatter.format_citation(ref)
    inline = formatter.format_inline(ref)
    
    assert "Smith" in citation
    assert "2020" in citation
    assert "Example Article" in citation  # Without quotes check
    assert "[1]" == inline


def test_ieee_journal_article():
    """Test IEEE format for journal article"""
    ref = ReferenceEntry(
        id="2",
        authors=["John Smith", "Alice Doe"],
        title="Deep Learning Methods",
        year=2019,
        source="IEEE Transactions on Neural Networks",
        volume="30",
        issue="5",
        pages="123-145",
        type="article"
    )
    
    formatter = IEEEFormatter()
    citation = formatter.format_citation(ref)
    
    assert "vol. 30" in citation
    assert "no. 5" in citation
    assert "pp. 123-145" in citation
    assert "2019" in citation


def test_apa_book():
    """Test APA format for book"""
    ref = ReferenceEntry(
        id="book1",
        authors=["Stuart Russell", "Peter Norvig"],
        title="Artificial Intelligence: A Modern Approach",
        year=2020,
        publisher="Pearson",
        type="book"
    )
    
    formatter = APAFormatter()
    citation = formatter.format_citation(ref)
    
    assert "Russell" in citation
    assert "Norvig" in citation
    assert "2020" in citation
    assert "Pearson" in citation


def test_bibliography_ieee():
    """Test IEEE bibliography generation"""
    references = [
        ReferenceEntry(
            id="1",
            authors=["John Smith"],
            title="First Article",
            year=2020,
            type="article"
        ),
        ReferenceEntry(
            id="2",
            authors=["Alice Doe"],
            title="Second Article",
            year=2021,
            type="article"
        )
    ]
    
    gen = BibliographyGenerator(style='IEEE')
    bib = gen.generate(references)
    
    assert "[1]" in bib
    assert "[2]" in bib
    assert "First Article" in bib
    assert "Second Article" in bib


def test_bibliography_apa():
    """Test APA bibliography generation"""
    references = [
        ReferenceEntry(
            id="ref1",
            authors=["John Smith"],
            title="First Article",
            year=2020,
            type="article"
        ),
        ReferenceEntry(
            id="ref2",
            authors=["Alice Doe"],
            title="Second Article",
            year=2021,
            type="article"
        )
    ]
    
    gen = BibliographyGenerator(style='APA')
    bib = gen.generate(references)
    
    # APA doesn't use numbers by default
    assert "[1]" not in bib
    assert "Smith" in bib
    assert "Doe" in bib
    assert "2020" in bib
    assert "2021" in bib


def test_bibliography_section_generation():
    """Test section data generation"""
    references = [
        ReferenceEntry(
            id="1",
            authors=["John Smith"],
            title="Test Article",
            year=2020,
            type="article"
        )
    ]
    
    gen = BibliographyGenerator(style='IEEE')
    section = gen.generate_section(references)
    
    assert section['type'] == 'references'
    assert section['title'] == 'REFERENCES'
    assert section['metadata']['count'] == 1
    assert section['metadata']['style'] == 'IEEE'
    assert len(section['references']) == 1


def test_inline_citation_ieee():
    """Test IEEE inline citations"""
    ref = ReferenceEntry(
        id="5",
        authors=["John Smith"],
        title="Test",
        year=2020,
        type="article"
    )
    
    gen = BibliographyGenerator(style='IEEE')
    inline = gen.get_inline_citation(ref)
    
    assert inline == "[5]"


def test_inline_citation_apa():
    """Test APA inline citations"""
    ref = ReferenceEntry(
        id="test",
        authors=["John Smith", "Alice Doe"],
        title="Test",
        year=2020,
        type="article"
    )
    
    gen = BibliographyGenerator(style='APA')
    inline = gen.get_inline_citation(ref)
    
    assert "Smith" in inline
    assert "Doe" in inline
    assert "2020" in inline


def test_empty_bibliography():
    """Test empty bibliography"""
    gen = BibliographyGenerator(style='IEEE')
    bib = gen.generate([])
    
    assert bib == ""


def test_reference_with_url():
    """Test reference with URL"""
    ref = ReferenceEntry(
        id="web1",
        authors=["John Doe"],
        title="Online Article",
        year=2022,
        url="https://example.com/article",
        type="website"
    )
    
    ieee = IEEEFormatter()
    citation = ieee.format_citation(ref)
    
    assert "example.com" in citation


def test_reference_with_doi():
    """Test reference with DOI"""
    ref = ReferenceEntry(
        id="doi1",
        authors=["Jane Smith"],
        title="Research Paper",
        year=2021,
        doi="10.1234/example.doi",
        type="article"
    )
    
    apa = APAFormatter()
    citation = apa.format_citation(ref)
    
    assert "10.1234/example.doi" in citation
