from typing import Dict, Any, List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models import ReportMetadata

class ContentTemplates:
    """Content templates for report sections"""
    
    def acknowledgment(self, metadata: ReportMetadata, config: Dict[str, Any]) -> str:
        faculty = config.get('faculty', '')
        advisor = metadata.advisor or ''
        
        return f"""Nhóm chúng em xin chân thành cảm ơn quý Thầy/Cô Khoa {faculty}, đặc biệt là {advisor} đã tận tình hướng dẫn, giúp đỡ nhóm trong suốt quá trình thực hiện đồ án môn Trí tuệ nhân tạo.

Qua đồ án này, nhóm đã có cơ hội áp dụng các kiến thức lý thuyết vào thực tiễn, hiểu sâu hơn về các thuật toán AI và cách chúng hoạt động trong một hệ thống thực tế.

Mặc dù đã cố gắng hết sức, báo cáo vẫn không tránh khỏi những thiếu sót. Nhóm rất mong nhận được sự góp ý của quý Thầy/Cô để hoàn thiện hơn.

Nhóm xin chân thành cảm ơn!"""
    
    def commitment(self, metadata: ReportMetadata) -> str:
        return """Nhóm chúng em xin cam đoan đây là sản phẩm nghiên cứu của riêng nhóm. Các số liệu, kết quả nêu trong báo cáo là trung thực và chưa từng được ai công bố trong bất kỳ công trình nào khác.

Nhóm xin hoàn toàn chịu trách nhiệm về lời cam đoan này."""
    
    def introduction_reason(self, config: Dict[str, Any]) -> str:
        title = config.get('title', '')
        
        return f"""Trong bối cảnh công nghệ phát triển mạnh mẽ, Trí tuệ nhân tạo (AI) đã và đang trở thành một phần không thể thiếu trong nhiều lĩnh vực, đặc biệt là trong ngành công nghiệp game.

Đề tài "{title}" được nhóm lựa chọn xuất phát từ mong muốn tìm hiểu sâu về cách các thuật toán AI hoạt động trong một hệ thống thực tế. Thay vì chỉ nghiên cứu lý thuyết, nhóm muốn xây dựng một ứng dụng game hoàn chỉnh để minh họa cách các thuật toán phối hợp với nhau."""
    
    def introduction_objectives(self) -> str:
        objectives = [
            "Nghiên cứu và triển khai các thuật toán AI cơ bản",
            "Áp dụng thuật toán CSP và Graph Coloring",
            "Xây dựng hệ thống AI đa tầng",
            "Triển khai chế độ online",
            "Tạo công cụ debug và visualization"
        ]
        return "\n".join(f"- {obj}" for obj in objectives)
    
    def conclusion(self, config: Dict[str, Any]) -> str:
        title = config.get('title', '')
        
        return f"""Qua quá trình nghiên cứu và triển khai đồ án "{title}", nhóm đã đạt được các kết quả quan trọng trong việc áp dụng các thuật toán AI vào một hệ thống game hoàn chỉnh.

Đồ án đã thành công trong việc tích hợp nhiều thuật toán AI khác nhau, từ sinh môi trường (DFS, CSP) đến tìm đường (BFS, A*, Dijkstra) và ra quyết định (Minimax, Utility Scoring).

Hướng phát triển tiếp theo bao gồm: tối ưu hiệu năng, thêm machine learning, phát triển mobile app và tournament mode."""
    
    def references(self, config: Dict[str, Any]) -> str:
        refs = []
        
        if config.get('github_repo'):
            refs.append(f"[1] Repository: {config['github_repo']}")
        
        if config.get('demo_url'):
            refs.append(f"[2] Demo: {config['demo_url']}")
        
        refs.extend([
            "[3] Stuart Russell, Peter Norvig. Artificial Intelligence: A Modern Approach. 4th Edition, 2020.",
            "[4] Thomas H. Cormen et al. Introduction to Algorithms. 3rd Edition, MIT Press, 2009."
        ])
        
        return "\n".join(refs)
