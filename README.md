# 🚀 Công cụ Tự động Tạo Báo cáo Đồ án - PRO VERSION

> Tự động tạo báo cáo đồ án HOÀN CHỈNH với nội dung chi tiết, biểu đồ chuyên nghiệp và format chuẩn

## ✨ Tính năng nổi bật

- ✅ **9 thuật toán đầy đủ**: DFS, BFS, A*, Dijkstra, CSP, Graph Coloring, Tarjan, Influence Map, Minimax
- ✅ **Tự động sinh nội dung**: Lý thuyết, độ phức tạp, giả mã, ưu/nhược điểm
- ✅ **9+ biểu đồ chất lượng cao**: DPI 150, tự động chèn vào báo cáo
- ✅ **Export Word + PDF**: Format chuẩn, sẵn sàng nộp
- ✅ **6 Skills AI**: Hỗ trợ viết tài liệu học thuật chuyên nghiệp

## 🚀 Cài đặt nhanh (3 phút)

### Bước 1: Cài Python
Tải Python từ https://python.org (phiên bản 3.8+)

### Bước 2: Cài thư viện
```bash
pip install -r requirements_pro.txt
```

### Bước 3: Chạy tool
```bash
# Windows
.\run_pro.bat

# Linux/Mac
python source/auto_report_pro_main.py --mode full
```

## ⚙️ Cấu hình

### Cách 1: Sử dụng config hiện tại (Legacy format)

Sửa file `report_config.json`:

```json
{
  "title": "Tên đề tài của bạn",
  "students": [
    {"name": "Tên bạn", "id": "MSSV"}
  ],
  "advisor": "Tên giảng viên",
  "algorithms": ["DFS", "BFS", "A*", "Dijkstra", "CSP"]
}
```

### Cách 2: Sử dụng config mới (Pydantic format - Khuyến nghị)

Tạo file config với cấu trúc rõ ràng hơn:

```json
{
  "project_info": {
    "title": "Tên đề tài của bạn",
    "description": "Mô tả chi tiết về đề tài",
    "students": [
      {"name": "Tên bạn", "id": "MSSV"}
    ],
    "advisor": "Tên giảng viên",
    "university": "Tên trường"
  },
  "report_profile": {
    "report_type": "project_report",
    "language": "vi"
  },
  "technical_data": {
    "algorithms": ["DFS", "BFS", "A*", "Dijkstra", "CSP"],
    "technologies": ["Python", "NetworkX"]
  }
}
```

**Lợi ích của format mới:**
- ✅ Kiểm tra lỗi tự động (type checking)
- ✅ Validation đầy đủ
- ✅ Cấu trúc rõ ràng, dễ bảo trì
- ✅ Hỗ trợ 4 loại báo cáo: thesis, technical_report, project_report, business_report

### Chuyển đổi config cũ sang mới

```bash
python migrate_config.py report_config.json
# Tạo file report_config.new.json
```

📖 **Xem hướng dẫn chi tiết:** [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

## 📁 Cấu trúc project

```
📦 Project
├── 📁 source/                      # Mã nguồn
│   ├── main.py                     # Pipeline mới (khuyến nghị)
│   ├── legacy_main.py              # Tool cũ (tương thích)
│   ├── config_models.py            # Pydantic models
│   ├── algorithm_content.py        # Database 9 thuật toán
│   ├── diagram_generator.py        # Tạo biểu đồ
│   ├── 📁 pipeline/                # Pipeline stages
│   ├── 📁 models/                  # Data models
│   ├── 📁 content/                 # Content generators
│   └── 📁 renderers/               # Output renderers
│
├── 📁 examples/                    # Ví dụ config
│   ├── config_minimal.json         # Config tối thiểu
│   ├── config_full.json            # Config đầy đủ
│   └── usage_example.py            # Ví dụ sử dụng
│
├── 📁 docs/                        # Tài liệu
│   └── instruct/                   # Hướng dẫn chi tiết
│       ├── README.md               # Hướng dẫn chính
│       ├── README_PRO.md           # Hướng dẫn đầy đủ
│       ├── QUICK_START.md          # Bắt đầu nhanh
│       ├── DEVELOPER_GUIDE.md      # Hướng dẫn developer
│       └── PROJECT_SUMMARY.md      # Tổng kết project
│
├── 📁 .kiro/skills/                # 6 Skills AI
│   ├── academic-writing.md         # Viết học thuật
│   ├── literature-review.md        # Tổng quan tài liệu
│   ├── data-analysis.md            # Phân tích dữ liệu
│   ├── methodology-design.md       # Thiết kế phương pháp
│   ├── citation-manager.md         # Quản lý trích dẫn
│   └── academic-reviewer.md        # Review báo cáo
│
├── 📁 diagrams/                    # Biểu đồ tự động tạo
├── 📁 output/                      # Kết quả
│   └── Bao_Cao_Full_Pro.docx
│
├── 📄 report_config.json           # Cấu hình (SỬA FILE NÀY)
├── 📄 migrate_config.py            # Script chuyển đổi config
├── 📄 requirements_pro.txt         # Thư viện
├── 📄 run_pro.bat                  # Script chạy nhanh
├── 📄 SKILLS_GUIDE.md              # Hướng dẫn sử dụng Skills
├── 📄 INTEGRATION_GUIDE.md         # Hướng dẫn Pydantic integration
└── 📄 README.md                    # File này
```

## 🎯 Sử dụng

### Pipeline mới (Khuyến nghị) - Orchestrator v2.0

```bash
# Sử dụng config hiện tại
python source/main.py --config report_config.json

# Sử dụng config mới
python source/main.py --config examples/config_minimal.json

# Chỉ định output
python source/main.py --config report_config.json --output output/my_report.docx

# Chế độ im lặng (cho scripts)
python source/main.py --quiet

# Xem trợ giúp
python source/main.py --help
```

**Tính năng mới:**
- ✅ 7 bước rõ ràng: Load → Validate → Plan → Generate → Bind → Render → Review
- ✅ Theo dõi tiến trình chi tiết với thời gian từng bước
- ✅ Xử lý lỗi tốt hơn với thông báo rõ ràng
- ✅ Chế độ quiet cho automation
- ✅ Tổng kết thực thi sau khi hoàn thành

### Tool cũ (Tương thích)

```bash
.\run_pro.bat
# Chọn [1] Tạo báo cáo HOÀN CHỈNH
```

### Tạo báo cáo hoàn chỉnh
```bash
.\run_pro.bat
# Chọn [1] Tạo báo cáo HOÀN CHỈNH
```

### Tạo báo cáo + PDF
```bash
.\run_pro.bat
# Chọn [2] Tạo báo cáo + Export PDF
```

### Chỉ tạo biểu đồ test
```bash
python source/diagram_generator.py
```

## 📊 Kết quả

Tool tạo báo cáo **50-60 trang** với:

✅ Trang bìa, lời cảm ơn, cam đoan  
✅ Mục lục chi tiết  
✅ Phần mở đầu (6 mục)  
✅ 5 chương với nội dung đầy đủ  
✅ Phân tích 9 thuật toán chi tiết  
✅ 9+ biểu đồ chất lượng cao  
✅ Kết luận và tài liệu tham khảo  
✅ Format chuẩn, sẵn sàng nộp  

**Tiết kiệm 90% thời gian viết báo cáo!** 🎉

## 🎓 Skills AI hỗ trợ viết

6 skills chuyên nghiệp trong `.kiro/skills/`:

1. **academic-writing** - Viết tài liệu học thuật tổng quát
2. **literature-review** - Viết tổng quan tài liệu, phân tích nghiên cứu
3. **data-analysis** - Phân tích dữ liệu, tạo biểu đồ
4. **methodology-design** - Thiết kế phương pháp, giải thích thuật toán
5. **citation-manager** - Quản lý trích dẫn, format chuẩn
6. **academic-reviewer** - Review báo cáo, đề xuất cải thiện

### Cách sử dụng Skills

```
# Trong Kiro IDE, gõ @ và chọn skill
@academic-writing Hãy giúp tôi viết phần mở đầu cho đồ án về AI.

@literature-review Tôi có 15 papers về A*. Hãy giúp viết tổng quan.

@data-analysis Phân tích dữ liệu benchmark: DFS=50ms, BFS=80ms, A*=30ms

@methodology-design Giải thích thuật toán Dijkstra với giả mã.

@citation-manager Format danh sách tài liệu theo chuẩn IEEE.

@academic-reviewer Review chương 2 và đưa ra nhận xét.
```

📖 **Xem hướng dẫn chi tiết:** [SKILLS_GUIDE.md](SKILLS_GUIDE.md)

## 💡 Tips

1. **Kiểm tra config** - Đảm bảo thông tin trong `report_config.json` đúng
2. **Mở file Word** - Kiểm tra nội dung và format
3. **Bổ sung hình ảnh** - Thêm screenshot từ demo
4. **Sử dụng Skills** - Để cải thiện nội dung và ngôn ngữ

## 🔧 Xử lý lỗi

### Lỗi: ModuleNotFoundError
```bash
pip install -r requirements_pro.txt
```

### Lỗi: Permission denied
Đóng file Word nếu đang mở, chạy lại

### Lỗi: matplotlib không hiển thị
```bash
pip install --upgrade matplotlib
```

## 📖 Tài liệu

- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Tham khảo nhanh các lệnh
- [ORCHESTRATOR_GUIDE.md](ORCHESTRATOR_GUIDE.md) - Hướng dẫn kiến trúc Orchestrator v2.0
- [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) - Hướng dẫn Pydantic config integration
- [SKILLS_GUIDE.md](SKILLS_GUIDE.md) - Hướng dẫn sử dụng 6 Skills AI
- [docs/instruct/README.md](docs/instruct/README.md) - Hướng dẫn chính
- [docs/instruct/README_PRO.md](docs/instruct/README_PRO.md) - Hướng dẫn chi tiết đầy đủ
- [docs/instruct/QUICK_START.md](docs/instruct/QUICK_START.md) - Bắt đầu trong 3 phút
- [docs/instruct/DEVELOPER_GUIDE.md](docs/instruct/DEVELOPER_GUIDE.md) - Hướng dẫn developer
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Hướng dẫn migration pipeline
- [REFACTOR_SUMMARY.md](REFACTOR_SUMMARY.md) - Tổng kết refactor
- [REFACTOR_ORCHESTRATOR.md](REFACTOR_ORCHESTRATOR.md) - Tổng kết Orchestrator refactoring
- [CHANGELOG.md](CHANGELOG.md) - Lịch sử phiên bản

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra Python: `python --version`
2. Kiểm tra thư viện: `pip list`
3. Xem log lỗi trong terminal
4. Đọc tài liệu trong `docs/instruct/`

## 📜 License

MIT License - Sử dụng tự do cho mục đích học tập

---

**Made with ❤️ for students** | Version 1.0 PRO

