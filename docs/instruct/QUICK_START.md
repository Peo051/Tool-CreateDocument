# ⚡ Quick Start - Bắt đầu trong 3 phút

## 🎯 Mục tiêu
Tạo báo cáo đồ án 50-60 trang hoàn chỉnh chỉ trong vài phút!

## 📋 Yêu cầu
- Python 3.8+ đã cài đặt
- 5 phút thời gian
- Thông tin đề tài của bạn

## 🚀 3 bước đơn giản

### Bước 1: Cài thư viện (1 phút)
```bash
pip install -r requirements_pro.txt
```

### Bước 2: Sửa thông tin (2 phút)
Mở file `report_config.json` và sửa:

```json
{
  "title": "Maze Duel - BO3",           ← Đổi tên đề tài
  "students": [
    {"name": "Tên bạn", "id": "MSSV"}  ← Đổi tên và MSSV
  ],
  "advisor": "TS. Tên GV",              ← Đổi tên giảng viên
  "class": "DHCN01",                    ← Đổi lớp
  "github_repo": "https://...",         ← Link GitHub
  "demo_url": "https://..."             ← Link demo
}
```

### Bước 3: Chạy tool (30 giây)
```bash
.\run_pro.bat
```

Chọn `[1]` và đợi 30 giây!

## ✅ Kết quả

File `output/Bao_Cao_Full_Pro.docx` đã sẵn sàng với:

✅ 50-60 trang nội dung chi tiết
✅ 9 thuật toán được phân tích đầy đủ
✅ 9+ biểu đồ chất lượng cao
✅ Format chuẩn, sẵn sàng nộp

## 🎨 Tùy chỉnh (Optional)

### Thêm/bớt thuật toán
```json
{
  "algorithms": ["DFS", "BFS", "A*", "Dijkstra", "CSP"]
}
```

### Thay đổi công nghệ
```json
{
  "technologies": ["HTML5", "JavaScript", "React", "Node.js"]
}
```

### Thêm sinh viên
```json
{
  "students": [
    {"name": "SV 1", "id": "001"},
    {"name": "SV 2", "id": "002"}
  ]
}
```

## 💡 Tips nhanh

1. **Kiểm tra file Word** ngay sau khi tạo
2. **Bổ sung hình ảnh** từ demo của bạn
3. **Chỉnh sửa nội dung** cho phù hợp
4. **Export PDF** trước khi nộp

## 🔧 Lỗi thường gặp

### Lỗi: python không tìm thấy
```bash
# Cài Python từ python.org
# Tick "Add Python to PATH" khi cài
```

### Lỗi: pip không hoạt động
```bash
python -m pip install -r requirements_pro.txt
```

### Lỗi: File đang mở
```bash
# Đóng file Word, chạy lại
```

## 📞 Cần trợ giúp?

1. Đọc [README.md](README.md) - Hướng dẫn cơ bản
2. Đọc [README_PRO.md](README_PRO.md) - Hướng dẫn chi tiết
3. Kiểm tra [CHANGELOG.md](CHANGELOG.md) - Lịch sử phiên bản

## 🎉 Xong!

Chỉ 3 bước đơn giản, bạn đã có báo cáo hoàn chỉnh!

**Tiết kiệm 90% thời gian viết báo cáo** 🚀

---

**Next steps:**
- Mở file Word và kiểm tra
- Thêm hình ảnh từ demo
- Bổ sung kết quả thực nghiệm
- Nộp báo cáo! 📝
