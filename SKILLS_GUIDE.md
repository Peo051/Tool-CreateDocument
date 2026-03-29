# 🎓 Hướng dẫn Sử dụng Skills - Viết Báo cáo Học thuật

> 6 Skills AI chuyên nghiệp hỗ trợ viết đồ án, luận văn, báo cáo nghiên cứu

## 📚 Danh sách Skills

Trong thư mục `.kiro/skills/` có 6 skills chuyên biệt:

### 1. 📝 academic-writing.md
**Chuyên gia viết tài liệu học thuật tổng quát**

**Khi nào dùng:**
- Viết đồ án, luận văn, báo cáo nghiên cứu
- Cần hỗ trợ cấu trúc và format
- Viết phần mở đầu, kết luận
- Cần ngôn ngữ học thuật chuyên nghiệp

**Ví dụ sử dụng:**
```
@academic-writing Hãy giúp tôi viết phần mở đầu cho đồ án về 
"Ứng dụng AI trong game". Đề tài tập trung vào thuật toán tìm 
kiếm và CSP.
```

### 2. 📖 literature-review.md
**Chuyên gia viết tổng quan tài liệu**

**Khi nào dùng:**
- Viết chương tổng quan (Literature Review)
- Phân tích các nghiên cứu liên quan
- So sánh các phương pháp
- Tìm khoảng trống nghiên cứu

**Ví dụ sử dụng:**
```
@literature-review Tôi có 15 papers về thuật toán A*. Hãy giúp 
tôi tổ chức và viết phần tổng quan, so sánh các cải tiến của A*.
```

### 3. 📊 data-analysis.md
**Chuyên gia phân tích dữ liệu**

**Khi nào dùng:**
- Phân tích kết quả thực nghiệm
- Tạo biểu đồ, bảng số liệu
- Viết phần kết quả (Results)
- So sánh hiệu năng thuật toán

**Ví dụ sử dụng:**
```
@data-analysis Tôi có dữ liệu thời gian chạy của 3 thuật toán 
trên 100 test cases. Hãy giúp phân tích và tạo biểu đồ so sánh.
```

### 4. 🔬 methodology-design.md
**Chuyên gia thiết kế phương pháp nghiên cứu**

**Khi nào dùng:**
- Viết chương phương pháp (Methodology)
- Thiết kế thực nghiệm
- Giải thích thuật toán chi tiết
- Mô tả kiến trúc hệ thống

**Ví dụ sử dụng:**
```
@methodology-design Hãy giúp tôi viết phần mô tả thuật toán DFS 
để sinh mê cung, bao gồm giả mã và giải thích từng bước.
```

### 5. 📚 citation-manager.md
**Chuyên gia quản lý trích dẫn**

**Khi nào dùng:**
- Format trích dẫn (APA, IEEE, ACM)
- Tạo danh mục tài liệu tham khảo
- Kiểm tra trích dẫn đầy đủ
- Sửa lỗi format trích dẫn

**Ví dụ sử dụng:**
```
@citation-manager Hãy format danh sách tài liệu tham khảo này 
theo chuẩn IEEE. [Danh sách tài liệu]
```

### 6. ✅ academic-reviewer.md
**Chuyên gia review báo cáo**

**Khi nào dùng:**
- Review toàn bộ báo cáo trước khi nộp
- Kiểm tra logic, ngôn ngữ, format
- Tìm lỗi chính tả, ngữ pháp
- Đề xuất cải thiện

**Ví dụ sử dụng:**
```
@academic-reviewer Hãy review chương 2 của báo cáo này và đưa 
ra nhận xét về cấu trúc, nội dung và ngôn ngữ.
```

## 🚀 Cách sử dụng Skills

### Cách 1: Sử dụng @ mention (Khuyến nghị)

Trong Kiro IDE, gõ `@` và chọn skill:

```
@academic-writing [câu hỏi của bạn]
```

### Cách 2: Kích hoạt thủ công

Nếu không có @ mention, bạn có thể nói rõ:

```
Sử dụng skill academic-writing để giúp tôi viết phần mở đầu.
```

### Cách 3: Tự động kích hoạt

Skills sẽ tự động kích hoạt khi bạn đề cập từ khóa liên quan:

- "viết đồ án" → academic-writing
- "literature review" → literature-review
- "phân tích dữ liệu" → data-analysis
- "trích dẫn" → citation-manager

## 📋 Quy trình Viết Báo cáo với Skills

### Bước 1: Lên outline (academic-writing)
```
@academic-writing Đề tài của tôi là "Maze Duel - Game AI". 
Hãy đề xuất cấu trúc báo cáo đồ án CNTT.
```

### Bước 2: Viết phần mở đầu (academic-writing)
```
@academic-writing Viết phần mở đầu với:
- Lý do chọn đề tài
- Mục tiêu: Áp dụng 5 thuật toán AI
- Phạm vi: Game 2D multiplayer
```

### Bước 3: Viết tổng quan (literature-review)
```
@literature-review Tôi có 20 papers về game AI và pathfinding. 
Hãy giúp tổ chức theo nhóm: Search algorithms, CSP, Decision making.
```

### Bước 4: Viết phương pháp (methodology-design)
```
@methodology-design Giải thích thuật toán A* trong game:
- Input: start, goal, cost map
- Output: optimal path
- Pseudocode
```

### Bước 5: Phân tích kết quả (data-analysis)
```
@data-analysis Dữ liệu benchmark:
- DFS: 50ms, BFS: 80ms, A*: 30ms
Tạo biểu đồ so sánh và phân tích.
```

### Bước 6: Format trích dẫn (citation-manager)
```
@citation-manager Format theo IEEE:
1. Russell, Norvig. AI: A Modern Approach. 2020.
2. GitHub repo: https://github.com/...
```

### Bước 7: Review toàn bộ (academic-reviewer)
```
@academic-reviewer Review chương 2 về thuật toán. 
Kiểm tra: logic, ngôn ngữ, format, trích dẫn.
```

## 💡 Tips Sử dụng Hiệu quả

### 1. Cung cấp context đầy đủ

❌ Không tốt:
```
Viết phần mở đầu.
```

✅ Tốt:
```
@academic-writing Viết phần mở đầu cho đồ án CNTT về "Game AI":
- Đề tài: Maze Duel
- Mục tiêu: Áp dụng DFS, BFS, A*, Dijkstra, CSP
- Công nghệ: HTML5, JavaScript
- Đối tượng: Sinh viên năm 3
```

### 2. Làm việc từng phần nhỏ

Thay vì:
```
Viết toàn bộ chương 2.
```

Nên:
```
@methodology-design Viết phần 2.1 về thuật toán DFS.
[Sau khi xong] → Viết phần 2.2 về BFS.
```

### 3. Cung cấp dữ liệu thực tế

Thay vì:
```
Tạo biểu đồ so sánh thuật toán.
```

Nên:
```
@data-analysis Dữ liệu thực tế:
Test 1: DFS=45ms, BFS=78ms, A*=32ms
Test 2: DFS=48ms, BFS=82ms, A*=35ms
...
Tạo biểu đồ box plot và phân tích.
```

### 4. Review nhiều lần

```
# Lần 1: Review cấu trúc
@academic-reviewer Kiểm tra cấu trúc chương 2.

# Lần 2: Review nội dung
@academic-reviewer Kiểm tra logic và độ đầy đủ.

# Lần 3: Review ngôn ngữ
@academic-reviewer Kiểm tra ngữ pháp và từ vựng.
```

### 5. Kết hợp nhiều skills

```
# Bước 1: Viết nội dung
@methodology-design Viết phần thuật toán A*.

# Bước 2: Thêm trích dẫn
@citation-manager Thêm trích dẫn cho phần A*.

# Bước 3: Review
@academic-reviewer Review phần A* vừa viết.
```

## 🎯 Ví dụ Thực tế

### Ví dụ 1: Viết phần giới thiệu thuật toán

```
@methodology-design 

Đề tài: Maze Duel Game
Thuật toán: A* (A-Star)

Hãy viết phần giới thiệu A* bao gồm:
1. Mục đích sử dụng trong game
2. Cơ sở lý thuyết (f = g + h)
3. Giả mã
4. Độ phức tạp
5. Ưu/nhược điểm
6. Ví dụ minh họa

Ngôn ngữ: Tiếng Việt, học thuật
Độ dài: 2-3 trang
```

### Ví dụ 2: Phân tích kết quả benchmark

```
@data-analysis

Dữ liệu benchmark 3 thuật toán trên 50 test cases:

DFS: [45, 48, 52, 47, 50, ...]
BFS: [78, 82, 85, 80, 83, ...]
A*:  [32, 35, 38, 33, 36, ...]

Yêu cầu:
1. Tính mean, median, std
2. Tạo box plot so sánh
3. Test thống kê (t-test)
4. Viết phần Results với:
   - Mô tả dữ liệu
   - Trình bày biểu đồ
   - Phân tích ý nghĩa
   - So sánh với nghiên cứu khác
```

### Ví dụ 3: Review toàn bộ báo cáo

```
@academic-reviewer

Hãy review toàn bộ báo cáo đồ án (file đính kèm).

Kiểm tra:
1. Cấu trúc: Đầy đủ các phần? Logic?
2. Nội dung: Đủ chi tiết? Có mâu thuẫn?
3. Ngôn ngữ: Học thuật? Ngữ pháp?
4. Format: Font, margin, heading?
5. Trích dẫn: Đầy đủ? Đúng format?
6. Hình/bảng: Có caption? Rõ ràng?

Đưa ra:
- Điểm mạnh (3-5 điểm)
- Điểm cần cải thiện (5-10 điểm)
- Checklist trước khi nộp
```

## 📊 So sánh Skills

| Skill | Dùng cho | Đầu vào | Đầu ra |
|-------|----------|---------|--------|
| academic-writing | Viết tổng quát | Đề tài, yêu cầu | Nội dung học thuật |
| literature-review | Tổng quan | Danh sách papers | Phần tổng quan |
| data-analysis | Phân tích | Dữ liệu số | Biểu đồ + phân tích |
| methodology-design | Phương pháp | Thuật toán, hệ thống | Mô tả chi tiết |
| citation-manager | Trích dẫn | Danh sách tài liệu | Format chuẩn |
| academic-reviewer | Review | Báo cáo hoàn chỉnh | Nhận xét + đề xuất |

## ⚠️ Lưu ý Quan trọng

### Skills KHÔNG thể:
- ❌ Bịa dữ liệu, số liệu
- ❌ Tạo trích dẫn giả
- ❌ Viết thay hoàn toàn
- ❌ Đảm bảo 100% đúng

### Skills CÓ THỂ:
- ✅ Hỗ trợ cấu trúc
- ✅ Đề xuất nội dung
- ✅ Cải thiện ngôn ngữ
- ✅ Phân tích dữ liệu
- ✅ Format trích dẫn
- ✅ Review và góp ý

### Trách nhiệm của bạn:
- ✅ Cung cấp dữ liệu thực tế
- ✅ Xác minh thông tin
- ✅ Hiểu và chịu trách nhiệm nội dung
- ✅ Chỉnh sửa cho phù hợp
- ✅ Kiểm tra lại trước khi nộp

## 🔧 Troubleshooting

### Skill không kích hoạt?
```
# Thử gọi trực tiếp
@academic-writing [câu hỏi]

# Hoặc nói rõ
Sử dụng skill academic-writing để...
```

### Kết quả không như mong đợi?
```
# Cung cấp thêm context
@academic-writing 

Context:
- Đề tài: [chi tiết]
- Đối tượng: [sinh viên/giảng viên]
- Yêu cầu: [cụ thể]
- Phong cách: [formal/technical]

Yêu cầu: [rõ ràng]
```

### Cần kết hợp nhiều skills?
```
# Làm từng bước
1. @methodology-design Viết phần thuật toán
2. @data-analysis Thêm phân tích kết quả
3. @citation-manager Format trích dẫn
4. @academic-reviewer Review toàn bộ
```

## 📚 Tài liệu Tham khảo

- Xem chi tiết từng skill trong `.kiro/skills/`
- Mỗi skill có hướng dẫn đầy đủ
- Có ví dụ và mẫu câu

## 🎉 Kết luận

6 skills này giúp bạn:
- ⏱️ Tiết kiệm 70-80% thời gian viết
- 📈 Nâng cao chất lượng báo cáo
- 🎯 Tập trung vào nội dung chính
- ✅ Đảm bảo format chuẩn

**Bắt đầu ngay:**
```
@academic-writing Hãy giúp tôi lên outline cho đồ án về [đề tài].
```

---

**Happy Writing!** 📝✨
