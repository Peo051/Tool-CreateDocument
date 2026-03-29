# 🚀 Công cụ Tự động Tạo Báo cáo Đồ án - PRO VERSION

> Tự động tạo báo cáo đồ án HOÀN CHỈNH với nội dung chi tiết, biểu đồ chuyên nghiệp và format chuẩn

## ✨ Tính năng nổi bật

### 📝 Tự động sinh nội dung chi tiết
- ✅ **9 thuật toán đầy đủ**: DFS, BFS, A*, Dijkstra, CSP, Graph Coloring, Tarjan, Influence Map, Minimax
- ✅ Mỗi thuật toán có: Lý thuyết, độ phức tạp, giả mã, ưu/nhược điểm, ứng dụng
- ✅ Phần mở đầu, tổng quan, kết luận tự động

### 📊 Tự động tạo biểu đồ
- ✅ 9+ biểu đồ minh họa chất lượng cao (DPI 150)
- ✅ Ví dụ mê cung, distance map, cost map, constraint graph...
- ✅ Tự động chèn vào đúng vị trí trong báo cáo

### 📄 Export nhiều định dạng
- ✅ Word (.docx) - Dễ chỉnh sửa
- ✅ PDF (.pdf) - Sẵn sàng nộp
- ✅ Format chuẩn theo quy định trường

## 🚀 Cài đặt nhanh

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
python auto_report_pro_main.py --mode full
```

## ⚙️ Cấu hình

Sửa file `report_config.json`:

```json
{
  "title": "Tên đề tài của bạn",
  "students": [
    {"name": "Tên bạn", "id": "MSSV"}
  ],
  "advisor": "Tên giảng viên",
  "class": "Lớp của bạn",
  "github_repo": "Link GitHub",
  "demo_url": "Link demo"
}
```

## 📁 Cấu trúc project

```
📦 Project
├── 📄 auto_report_pro_main.py      # Tool chính
├── 📄 algorithm_content.py         # Database 9 thuật toán
├── 📄 diagram_generator.py         # Tạo biểu đồ tự động
├── 📄 report_config.json           # Cấu hình (SỬA FILE NÀY)
├── 📄 requirements_pro.txt         # Thư viện
├── 📄 run_pro.bat                  # Script chạy nhanh
├── 📄 README.md                    # File này
├── 📄 README_PRO.md                # Hướng dẫn chi tiết
│
├── 📁 diagrams/                    # Biểu đồ tự động tạo
│   ├── dfs_diagram.png
│   ├── bfs_diagram.png
│   ├── astar_diagram.png
│   └── ...
│
├── 📁 output/                      # Kết quả
│   ├── Bao_Cao_Full_Pro.docx
│   └── Bao_Cao_Full_Pro.pdf
│
└── 📁 .kiro/skills/                # Skills hỗ trợ viết
    ├── academic-writing.md
    ├── literature-review.md
    ├── data-analysis.md
    └── ...
```

## 🎯 Sử dụng

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
python diagram_generator.py
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

## 💡 Tips

1. **Kiểm tra config** - Đảm bảo thông tin trong `report_config.json` đúng
2. **Mở file Word** - Kiểm tra nội dung và format
3. **Bổ sung hình ảnh** - Thêm screenshot từ demo
4. **Chỉnh sửa nội dung** - Điều chỉnh cho phù hợp đề tài

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

- [README_PRO.md](README_PRO.md) - Hướng dẫn chi tiết đầy đủ
- [report_config.json](report_config.json) - File cấu hình
- [algorithm_content.py](algorithm_content.py) - Xem nội dung thuật toán

## 🎓 Skills hỗ trợ viết

Trong thư mục `.kiro/skills/` có 6 skills AI hỗ trợ:

1. **academic-writing** - Viết tài liệu học thuật
2. **literature-review** - Viết tổng quan tài liệu
3. **data-analysis** - Phân tích dữ liệu
4. **methodology-design** - Thiết kế phương pháp
5. **citation-manager** - Quản lý trích dẫn
6. **academic-reviewer** - Review báo cáo

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra Python: `python --version`
2. Kiểm tra thư viện: `pip list`
3. Xem log lỗi trong terminal
4. Đọc [README_PRO.md](README_PRO.md) để biết thêm chi tiết

## 📜 License

MIT License - Sử dụng tự do cho mục đích học tập

---

**Made with ❤️ for students** | Version 1.0 PRO
