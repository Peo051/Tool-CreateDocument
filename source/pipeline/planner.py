from typing import List, Dict, Any
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models import Section, SectionType, Report, ReportMetadata

class OutlinePlanner:
    """Plan report outline structure"""
    
    def plan(self, config: Dict[str, Any]) -> Report:
        """Create report structure from config"""
        
        # Create metadata
        metadata = ReportMetadata(
            title=config['title'],
            subtitle=config.get('subtitle'),
            authors=config.get('students', []),
            advisor=config.get('advisor'),
            organization=config.get('university', config.get('organization', '')),
            faculty=config.get('faculty', ''),
            class_name=config.get('class', ''),
            github_repo=config.get('github_repo'),
            demo_url=config.get('demo_url')
        )
        
        # Create report
        report = Report(metadata=metadata, config=config)
        
        # Add sections
        report.add_section(self._create_cover_section(config))
        report.add_section(self._create_acknowledgment_section(config))
        report.add_section(self._create_commitment_section(config))
        report.add_section(self._create_toc_section())
        report.add_section(self._create_introduction_section(config))
        
        # Add algorithm chapters
        algorithms = config.get('algorithms', [])
        if algorithms:
            report.add_section(self._create_algorithm_chapter(algorithms, config))
        
        report.add_section(self._create_conclusion_section(config))
        report.add_section(self._create_references_section(config))
        
        return report
    
    def _create_cover_section(self, config: Dict[str, Any]) -> Section:
        return Section(
            id="cover",
            title="Cover Page",
            type=SectionType.COVER,
            metadata=config
        )
    
    def _create_acknowledgment_section(self, config: Dict[str, Any]) -> Section:
        return Section(
            id="acknowledgment",
            title="LỜI CẢM ƠN",
            type=SectionType.ACKNOWLEDGMENT,
            level=1
        )
    
    def _create_commitment_section(self, config: Dict[str, Any]) -> Section:
        return Section(
            id="commitment",
            title="LỜI CAM ĐOAN",
            type=SectionType.COMMITMENT,
            level=1
        )
    
    def _create_toc_section(self) -> Section:
        return Section(
            id="toc",
            title="MỤC LỤC",
            type=SectionType.TOC,
            level=1
        )
    
    def _create_introduction_section(self, config: Dict[str, Any]) -> Section:
        intro = Section(
            id="introduction",
            title="PHẦN MỞ ĐẦU",
            type=SectionType.INTRODUCTION,
            level=1
        )
        
        intro.add_subsection(Section(
            id="intro_reason",
            title="Lý do chọn đề tài",
            type=SectionType.INTRODUCTION,
            level=2
        ))
        
        intro.add_subsection(Section(
            id="intro_objectives",
            title="Mục tiêu nghiên cứu",
            type=SectionType.INTRODUCTION,
            level=2
        ))
        
        return intro
    
    def _create_algorithm_chapter(self, algorithms: List[str], config: Dict[str, Any]) -> Section:
        chapter = Section(
            id="chapter_algorithms",
            title="CÁC THUẬT TOÁN TÌM KIẾM",
            type=SectionType.CHAPTER,
            level=1
        )
        
        for i, algo_name in enumerate(algorithms[:4], 1):  # First 4 for search algorithms
            algo_section = Section(
                id=f"algo_{algo_name.lower().replace('*', 'star')}",
                title=f"2.{i}. {algo_name}",
                type=SectionType.ALGORITHM,
                level=2,
                metadata={'algorithm': algo_name}
            )
            chapter.add_subsection(algo_section)
        
        return chapter
    
    def _create_conclusion_section(self, config: Dict[str, Any]) -> Section:
        return Section(
            id="conclusion",
            title="KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN",
            type=SectionType.CONCLUSION,
            level=1
        )
    
    def _create_references_section(self, config: Dict[str, Any]) -> Section:
        return Section(
            id="references",
            title="TÀI LIỆU THAM KHẢO",
            type=SectionType.REFERENCES,
            level=1
        )
