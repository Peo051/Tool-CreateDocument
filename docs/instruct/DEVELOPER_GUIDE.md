# 👨‍💻 Developer Guide

> Hướng dẫn cho developers muốn mở rộng hoặc tùy chỉnh tool

## 🏗️ Kiến trúc

### Tổng quan
```
User Input (config.json)
    ↓
auto_report_pro_main.py (Orchestrator)
    ↓
    ├─→ algorithm_content.py (Data)
    ├─→ diagram_generator.py (Visualization)
    └─→ python-docx (Output)
```

### Modules

#### 1. auto_report_pro_main.py
**Vai trò**: Orchestrator chính, điều phối toàn bộ quy trình

**Classes**:
- `ProReportGenerator`: Class chính
  - `__init__()`: Khởi tạo, load config
  - `setup_document()`: Setup Word document
  - `add_cover_page()`: Tạo trang bìa
  - `add_chapter()`: Thêm chương
  - `add_algorithm_section()`: Thêm phần thuật toán
  - `generate()`: Tạo báo cáo hoàn chỉnh

**Flow**:
```python
1. Load config từ JSON
2. Khởi tạo Document
3. Tạo trang bìa
4. Tạo mục lục
5. Thêm phần mở đầu
6. Loop qua các thuật toán:
   - Lấy content từ algorithm_content
   - Tạo biểu đồ từ diagram_generator
   - Thêm vào document
7. Thêm kết luận
8. Save file
```

#### 2. algorithm_content.py
**Vai trò**: Database chứa nội dung chi tiết của tất cả thuật toán

**Structure**:
```python
ALGORITHMS = {
    "DFS": {
        "name": str,
        "title": str,
        "category": str,
        "purpose": str,
        "theory": str,
        "complexity": str,
        "pseudocode": str,
        "role": str,
        "advantages": list,
        "limitations": list,
        "solution": str,
        "application": str
    },
    # ... 8 thuật toán khác
}
```

**Functions**:
- `get_algorithm_content(name)`: Lấy nội dung thuật toán
- `get_all_algorithm_names()`: Lấy danh sách tên

#### 3. diagram_generator.py
**Vai trò**: Tạo biểu đồ minh họa tự động

**Class**: `DiagramGenerator`

**Methods**:
- `create_maze_example()`: Mê cung DFS
- `create_bfs_visualization()`: BFS distance map
- `create_astar_comparison()`: So sánh BFS vs A*
- `create_dijkstra_cost_map()`: Dijkstra cost map
- `create_csp_example()`: CSP constraint graph
- `create_graph_coloring()`: Graph coloring
- `create_tarjan_example()`: Tarjan articulation points
- `create_influence_map()`: Influence map
- `create_minimax_tree()`: Minimax tree

## 🔧 Thêm thuật toán mới

### Bước 1: Thêm vào algorithm_content.py

```python
ALGORITHMS["NewAlgo"] = {
    "name": "New Algorithm",
    "title": "NewAlgo - Mô tả ngắn",
    "category": "Loại thuật toán",
    "purpose": "Mục tiêu của thuật toán...",
    "theory": """
    Lý thuyết chi tiết...
    
    **Nguyên lý:**
    1. Bước 1
    2. Bước 2
    """,
    "complexity": "O(n log n) với giải thích...",
    "pseudocode": """
function newAlgo():
    // Code here
    """,
    "role": "Vai trò trong game...",
    "advantages": [
        "Ưu điểm 1",
        "Ưu điểm 2"
    ],
    "limitations": [
        "Hạn chế 1",
        "Hạn chế 2"
    ],
    "solution": "Cách khắc phục...",
    "application": "Ứng dụng cụ thể..."
}
```

### Bước 2: Thêm biểu đồ vào diagram_generator.py

```python
def create_newalgo_diagram(self):
    """Tạo biểu đồ cho thuật toán mới"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Vẽ biểu đồ
    # ...
    
    ax.set_title('Tiêu đề biểu đồ', fontweight='bold')
    plt.tight_layout()
    return self._fig_to_bytes(fig)
```

### Bước 3: Cập nhật config

```json
{
  "algorithms": [
    "DFS", "BFS", "A*", "NewAlgo"
  ]
}
```

### Bước 4: Test

```bash
python auto_report_pro_main.py --mode full
```

## 🎨 Tùy chỉnh format

### Thay đổi font

```python
# Trong setup_document()
normal = styles['Normal']
normal.font.name = 'Arial'  # Thay đổi font
normal.font.size = Pt(12)   # Thay đổi size
```

### Thay đổi margin

```python
# Trong setup_document()
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
```

### Thay đổi màu heading

```python
h1 = styles['Heading 1']
h1.font.color.rgb = RGBColor(0, 0, 255)  # Màu xanh
```

## 📊 Tùy chỉnh biểu đồ

### Thay đổi DPI

```python
# Trong __init__() của DiagramGenerator
plt.rcParams['figure.dpi'] = 300  # Tăng độ phân giải
```

### Thay đổi colormap

```python
# Trong các hàm create_*
ax.imshow(data, cmap='viridis')  # Thay đổi màu
```

### Thay đổi kích thước

```python
fig, ax = plt.subplots(figsize=(12, 8))  # Tăng kích thước
```

## 🔌 Tích hợp API

### Thêm GPT API

```python
import openai

def generate_content_with_gpt(prompt):
    """Sinh nội dung bằng GPT"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an academic writer"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

### Sử dụng

```python
# Trong add_introduction()
intro_text = generate_content_with_gpt(
    f"Write introduction for project: {self.config['title']}"
)
self.doc.add_paragraph(intro_text)
```

## 🧪 Testing

### Test từng module

```bash
# Test algorithm content
python -c "from algorithm_content import ALGORITHMS; print(len(ALGORITHMS))"

# Test diagram generator
python diagram_generator.py

# Test main tool
python auto_report_pro_main.py --mode diagrams
```

### Unit tests (TODO)

```python
import unittest

class TestAlgorithmContent(unittest.TestCase):
    def test_all_algorithms_have_required_fields(self):
        required = ['name', 'title', 'purpose', 'theory']
        for algo in ALGORITHMS.values():
            for field in required:
                self.assertIn(field, algo)
```

## 📦 Build & Deploy

### Tạo executable (PyInstaller)

```bash
pip install pyinstaller

pyinstaller --onefile \
    --add-data "algorithm_content.py:." \
    --add-data "diagram_generator.py:." \
    auto_report_pro_main.py
```

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements_pro.txt .
RUN pip install -r requirements_pro.txt

COPY . .

CMD ["python", "auto_report_pro_main.py", "--mode", "full"]
```

## 🐛 Debugging

### Enable verbose logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Trong code
logger.debug(f"Processing algorithm: {algo_name}")
```

### Common issues

**Issue**: Biểu đồ không hiển thị
```python
# Solution: Kiểm tra matplotlib backend
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
```

**Issue**: Font không đúng
```python
# Solution: Kiểm tra font có sẵn
from matplotlib import font_manager
print(font_manager.findSystemFonts())
```

## 📝 Code Style

### PEP 8 Compliance

```bash
# Check style
pip install flake8
flake8 *.py

# Auto format
pip install black
black *.py
```

### Docstrings

```python
def create_diagram(self, algo_name):
    """
    Tạo biểu đồ cho thuật toán.
    
    Args:
        algo_name (str): Tên thuật toán
        
    Returns:
        BytesIO: Buffer chứa ảnh PNG
        
    Raises:
        ValueError: Nếu algo_name không hợp lệ
    """
    pass
```

## 🚀 Performance

### Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
generator.generate()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumtime')
stats.print_stats(10)
```

### Optimization tips

1. **Cache biểu đồ**: Không tạo lại nếu đã có
2. **Lazy loading**: Chỉ load thuật toán cần dùng
3. **Parallel processing**: Tạo biểu đồ song song

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    diagrams = list(executor.map(create_diagram, algorithms))
```

## 📚 Resources

### Documentation
- [python-docx docs](https://python-docx.readthedocs.io/)
- [matplotlib docs](https://matplotlib.org/stable/contents.html)
- [networkx docs](https://networkx.org/documentation/stable/)

### Examples
- Xem code trong `auto_report_pro_main.py`
- Xem examples trong `diagram_generator.py`

## 🤝 Contributing

### Workflow

1. Fork repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Commit messages

```
feat: Add new algorithm XYZ
fix: Fix diagram generation bug
docs: Update README
refactor: Clean up code structure
```

## 📞 Support

- GitHub Issues: [Link]
- Email: [Email]
- Discord: [Link]

---

**Happy Coding!** 👨‍💻
