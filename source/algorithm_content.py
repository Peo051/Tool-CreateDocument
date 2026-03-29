"""
Database đầy đủ nội dung cho TẤT CẢ thuật toán
"""

ALGORITHMS = {
    "DFS": {
        "name": "DFS",
        "title": "DFS - Sinh mê cung procedural",
        "category": "Tìm kiếm",
        "purpose": "Tạo ra mê cung ngẫu nhiên cho mỗi ván đấu với chi phí thấp nhưng vẫn đủ đa dạng.",
        "theory": "DFS (Depth-First Search) là thuật toán duyệt đồ thị theo chiều sâu, sử dụng recursive backtracking để tạo mê cung.",
        "complexity": "O(V + E) với V là số ô, E là số cạnh.",
        "pseudocode": "function generateMaze(grid):\n    stack = []\n    start = randomCell()\n    mark start as visited\n    stack.push(start)\n    while stack not empty:\n        current = stack.top()\n        neighbors = unvisitedNeighbors(current)\n        if neighbors not empty:\n            next = random(neighbors)\n            removeWall(current, next)\n            stack.push(next)\n        else:\n            stack.pop()",
        "role": "Tạo nền móng cho gameplay với bản đồ mới mỗi ván.",
        "advantages": ["Cực kỳ nhanh O(V)", "Đơn giản dễ cài đặt", "Tạo mê cung đa dạng"],
        "limitations": ["Nhiều ngõ cụt", "Ít loops", "Cần hậu xử lý"],
        "solution": "Thêm post-processing để mở loops.",
        "application": "Map generation pipeline."
    },
    "BFS": {
        "name": "BFS",
        "title": "BFS - Distance map và fairness check",
        "category": "Tìm kiếm",
        "purpose": "Xây bản đồ khoảng cách để kiểm tra tính công bằng và tìm đường ngắn nhất.",
        "theory": "BFS duyệt đồ thị theo chiều rộng, đảm bảo tìm được đường ngắn nhất trên đồ thị không trọng số.",
        "complexity": "O(V + E). Với lưới 2D, E ≈ 4V nên gần như tuyến tính.",
        "pseudocode": "function BFS(start):\n    queue = []\n    dist[start] = 0\n    queue.enqueue(start)\n    while queue not empty:\n        current = queue.dequeue()\n        for neighbor in neighbors(current):\n            if dist[neighbor] == INFINITY:\n                dist[neighbor] = dist[current] + 1\n                parent[neighbor] = current\n                queue.enqueue(neighbor)",
        "role": "Fairness check và baseline pathfinding.",
        "advantages": ["Đảm bảo optimal", "Đơn giản", "Hiệu quả O(V+E)", "Tạo distance map"],
        "limitations": ["Chỉ cho chi phí đồng nhất", "Không xét danger", "Không có heuristic"],
        "solution": "Dùng Dijkstra khi có danger, A* khi biết mục tiêu.",
        "application": "Map quality check và fallback pathfinding."
    },
    "A*": {
        "name": "A*",
        "title": "A* - Tìm đường tối ưu với heuristic",
        "category": "Tìm kiếm",
        "purpose": "Tìm đường nhanh đến mục tiêu bằng heuristic dẫn hướng.",
        "theory": "A* kết hợp Dijkstra và Greedy: f(n) = g(n) + h(n). Heuristic h(n) ước lượng chi phí đến goal.",
        "complexity": "O(E log V) nhưng nhanh hơn nhiều nhờ heuristic.",
        "pseudocode": "function AStar(start, goal):\n    openSet = PriorityQueue()\n    g[start] = 0\n    f[start] = h(start, goal)\n    openSet.push(start, f[start])\n    while openSet not empty:\n        current = openSet.pop()\n        if current == goal:\n            return reconstructPath()\n        for neighbor in neighbors(current):\n            tentative_g = g[current] + cost(current, neighbor)\n            if tentative_g < g[neighbor]:\n                g[neighbor] = tentative_g\n                f[neighbor] = g[neighbor] + h(neighbor, goal)\n                openSet.push(neighbor, f[neighbor])",
        "role": "Primary pathfinding cho AI di chuyển đến mục tiêu cụ thể.",
        "advantages": ["Nhanh nhờ heuristic", "Tối ưu", "Linh hoạt", "Phổ biến"],
        "limitations": ["Cần biết goal", "Phụ thuộc heuristic", "Không cho exploration"],
        "solution": "Kết hợp với cost map khi cần tránh nguy hiểm.",
        "application": "AI di chuyển đến treasure, base, enemy."
    },
    "Dijkstra": {
        "name": "Dijkstra",
        "title": "Dijkstra - Đường đi an toàn theo chi phí rủi ro",
        "category": "Tìm kiếm có trọng số",
        "purpose": "Tìm đường có tổng chi phí nhỏ nhất khi các ô có mức độ nguy hiểm khác nhau. Giúp AI biết tránh trap, monster, choke-point thay vì lao vào đường ngắn nhất.",
        "theory": """Dijkstra là thuật toán tìm đường ngắn nhất trên đồ thị có trọng số không âm. Khác với BFS (mọi cạnh = 1), Dijkstra xử lý được chi phí khác nhau cho mỗi ô.

**Mô hình chi phí trong Maze Duel:**
cost(cell) = 1 + dangerPenalty + trapPenalty + monsterPenalty + chokePenalty

Ví dụ:
- Ô trống: cost = 1
- Ô có trap: cost = 1 + 5 = 6
- Ô gần monster: cost = 1 + 3 = 4
- Ô choke-point: cost = 1 + 2 = 3

**Thuật toán:**
1. Khởi tạo: dist[start] = 0, các ô khác = ∞
2. Dùng priority queue, lấy ô có dist nhỏ nhất
3. Với mỗi láng giềng, tính dist mới = dist[current] + cost(neighbor)
4. Nếu dist mới < dist cũ, cập nhật và thêm vào queue
5. Lặp đến khi queue rỗng hoặc đến đích

**Khi nào dùng Dijkstra:**
- AI đang cầm treasure, cần về base an toàn
- AI thấp máu/năng lượng
- Cần vòng ra sau để tránh contest
- Muốn né vùng monster pressure""",
        "complexity": "O(E log V) với priority queue (heap). Trên lưới 50x50: V=2500, E≈10000, cần ~130000 operations.",
        "pseudocode": """function Dijkstra(start, costMap):
    dist = {}
    parent = {}
    pq = PriorityQueue()
    
    for each cell:
        dist[cell] = INFINITY
    
    dist[start] = 0
    pq.push(start, 0)
    
    while pq not empty:
        current = pq.pop()
        
        if visited[current]:
            continue
        visited[current] = true
        
        for neighbor in walkableNeighbors(current):
            // Chi phí = chi phí cơ bản + penalty
            edgeCost = 1 + costMap[neighbor]
            newDist = dist[current] + edgeCost
            
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                parent[neighbor] = current
                pq.push(neighbor, newDist)
    
    return dist, parent

function buildCostMap(state):
    costMap = {}
    
    for each cell:
        cost = 0
        
        // Trap penalty
        if hasTrap(cell):
            cost += 5
        
        // Monster proximity
        for monster in monsters:
            d = distance(cell, monster)
            if d < 3:
                cost += (3 - d) * 2
        
        // Enemy proximity
        d = distance(cell, enemy)
        if d < 4:
            cost += (4 - d) * 1.5
        
        // Choke point
        if isChokePoint(cell):
            cost += 2
        
        costMap[cell] = cost
    
    return costMap""",
        "role": "Dijkstra làm AI thông minh hơn bằng cách xét đến nguy hiểm. Thay vì đi đường ngắn nhất, AI chọn đường an toàn nhất.",
        "advantages": [
            "Xét đến chi phí thực tế của từng ô",
            "Tìm đường tối ưu theo weighted cost",
            "Linh hoạt với nhiều loại penalty",
            "Phù hợp cho survival gameplay"
        ],
        "limitations": [
            "Chậm hơn BFS (O(E log V) vs O(V+E))",
            "Không có heuristic nên mở nhiều nút",
            "Phụ thuộc vào chất lượng cost map",
            "Cost model phải được tune cẩn thận"
        ],
        "solution": "Chỉ dùng Dijkstra khi cần thiết (AI cầm treasure, low HP). Các tình huống khác dùng A* hoặc BFS để tiết kiệm.",
        "application": "Safe pathfinding khi AI cần ưu tiên sống sót hơn tốc độ."
    },
    
    "A*": {
        "name": "A* (A-Star)",
        "title": "A* - Tìm đường nhanh tới mục tiêu cụ thể",
        "category": "Tìm kiếm có heuristic",
        "purpose": "Tìm đường tối ưu đến mục tiêu đã biết với tốc độ nhanh hơn BFS/Dijkstra nhờ heuristic dẫn hướng.",
        "theory": """A* kết hợp ưu điểm của Dijkstra (tối ưu) và Greedy (nhanh) bằng hàm đánh giá:

f(n) = g(n) + h(n)

Trong đó:
- g(n): Chi phí thực tế từ start đến n
- h(n): Chi phí ước lượng từ n đến goal (heuristic)
- f(n): Tổng chi phí ước lượng

**Heuristic phổ biến:**
1. Manhattan distance (lưới 4 hướng):
   h(n) = |n.x - goal.x| + |n.y - goal.y|

2. Euclidean distance (lưới 8 hướng):
   h(n) = sqrt((n.x - goal.x)² + (n.y - goal.y)²)

3. Diagonal distance:
   h(n) = max(|dx|, |dy|) + (√2 - 1) * min(|dx|, |dy|)

**Tính chất heuristic:**
- Admissible: h(n) ≤ actual cost (không overestimate)
- Consistent: h(n) ≤ cost(n,n') + h(n')
- Nếu admissible → A* tìm được đường tối ưu

**Ưu điểm so với Dijkstra:**
- Heuristic "kéo" tìm kiếm về phía goal
- Mở ít nút hơn → nhanh hơn
- Vẫn đảm bảo optimal nếu h admissible""",
        "complexity": "O(E log V) nhưng thực tế nhanh hơn nhiều nhờ heuristic. Với h tốt, chỉ mở ~30% số nút so với Dijkstra.",
        "pseudocode": """function AStar(start, goal):
    openSet = PriorityQueue()
    closedSet = Set()
    g = {}
    parent = {}
    
    g[start] = 0
    f = g[start] + heuristic(start, goal)
    openSet.push(start, f)
    
    while openSet not empty:
        current = openSet.pop()
        
        if current == goal:
            return reconstructPath(parent, goal)
        
        closedSet.add(current)
        
        for neighbor in walkableNeighbors(current):
            if neighbor in closedSet:
                continue
            
            tentative_g = g[current] + cost(current, neighbor)
            
            if neighbor not in openSet or tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                f = g[neighbor] + heuristic(neighbor, goal)
                
                if neighbor not in openSet:
                    openSet.push(neighbor, f)
                else:
                    openSet.update(neighbor, f)
    
    return null  // No path found

function heuristic(node, goal):
    // Manhattan distance cho lưới 4 hướng
    return abs(node.x - goal.x) + abs(node.y - goal.y)

// A* với cost map (safe A*)
function SafeAStar(start, goal, costMap):
    // Tương tự nhưng cost(current, neighbor) xét costMap
    edgeCost = 1 + costMap[neighbor]
    tentative_g = g[current] + edgeCost
    ...""",
        "role": "A* là công cụ chính cho AI di chuyển: đến treasure, về base, đuổi enemy. Nhanh hơn BFS, tối ưu hơn Greedy.",
        "advantages": [
            "Nhanh - heuristic giảm không gian tìm kiếm",
            "Tối ưu - đảm bảo đường ngắn nhất",
            "Linh hoạt - dễ kết hợp với cost map",
            "Phổ biến - có sẵn nhiều implementation"
        ],
        "limitations": [
            "Cần biết trước goal",
            "Hiệu quả phụ thuộc heuristic",
            "Không phù hợp cho exploration",
            "Vẫn chậm hơn Greedy (nhưng đúng hơn)"
        ],
        "solution": "Dùng A* cho point-to-point navigation. Kết hợp với Dijkstra cost map khi cần tránh nguy hiểm.",
        "application": "Primary pathfinding cho AI Normal và Hard. CPU Easy dùng BFS để dễ đánh bại hơn."
    },
    
    "CSP": {
        "name": "CSP (Constraint Satisfaction Problem)",
        "title": "CSP - Đặt nội dung bản đồ theo ràng buộc",
        "category": "Giải bài toán ràng buộc",
        "purpose": "Biến việc đặt treasure, quiz, monster từ random thành bài toán có điều kiện: hợp lệ, công bằng, không chồng lấn, phân tán đều.",
        "theory": """CSP là framework để giải bài toán thỏa mãn ràng buộc. Gồm 3 thành phần:

**1. Variables (Biến):**
- treasure_position
- monster_positions[1..n]
- quiz_positions[1..m]
- zone_centers[1..k]

**2. Domains (Miền giá trị):**
- Tập các ô floor hợp lệ
- Ví dụ: treasure_domain = {tất cả ô floor, không phải wall, không phải base}

**3. Constraints (Ràng buộc):**
a) Unary: Ràng buộc 1 biến
   - treasure không ở trên wall
   - monster không ở base

b) Binary: Ràng buộc 2 biến
   - treasure và monster không trùng ô
   - 2 monster cách nhau ít nhất 5 ô

c) Global: Ràng buộc nhiều biến
   - Tất cả objects phân bố đều theo zone
   - Fairness: |dist(baseA, treasure) - dist(baseB, treasure)| ≤ 2

**Thuật toán giải:**
1. Backtracking: Thử từng giá trị, quay lui nếu vi phạm
2. Forward Checking: Loại bỏ giá trị không hợp lệ sớm
3. Arc Consistency: Đảm bảo mọi giá trị đều có giá trị tương thích
4. Heuristics:
   - MRV (Minimum Remaining Values): Chọn biến khó nhất trước
   - Degree: Chọn biến ràng buộc nhiều biến khác
   - LCV (Least Constraining Value): Thử giá trị ít ràng buộc nhất""",
        "complexity": "Worst case: O(d^n) với d = domain size, n = số biến. Nhưng với heuristics + pruning, thực tế chấp nhận được.",
        "pseudocode": """function solveCSP(variables, domains, constraints):
    assignment = {}
    return backtrack(assignment, variables, domains, constraints)

function backtrack(assignment, variables, domains, constraints):
    if assignment complete:
        return assignment
    
    // MRV: Chọn biến có domain nhỏ nhất
    var = selectUnassignedVariable(variables, domains)
    
    // LCV: Sắp xếp giá trị theo thứ tự ít ràng buộc nhất
    for value in orderDomainValues(var, domains):
        if consistent(var, value, assignment, constraints):
            assignment[var] = value
            
            // Forward checking: Prune domains
            inferences = inference(var, value, domains, constraints)
            
            if inferences != failure:
                result = backtrack(assignment, variables, domains, constraints)
                if result != failure:
                    return result
            
            // Undo
            remove(var, assignment)
            restore(domains, inferences)
    
    return failure

function selectUnassignedVariable(variables, domains):
    // MRV + Degree heuristic
    unassigned = variables not in assignment
    return min(unassigned, key=lambda v: (len(domains[v]), -degree(v)))

function orderDomainValues(var, domains):
    // LCV: Sắp xếp theo số ràng buộc
    return sorted(domains[var], key=lambda val: countConflicts(var, val))

function inference(var, value, domains, constraints):
    // Forward checking
    inferences = {}
    for neighbor in neighbors(var):
        for val in domains[neighbor]:
            if conflicts(var, value, neighbor, val, constraints):
                remove val from domains[neighbor]
                inferences[neighbor].add(val)
        if domains[neighbor] empty:
            return failure
    return inferences""",
        "role": "CSP là lá chắn chống 'random xấu'. Đảm bảo bản đồ không thiên vị, objects không chồng lấn, phân bố hợp lý.",
        "advantages": [
            "Đảm bảo thỏa mãn tất cả ràng buộc",
            "Linh hoạt - dễ thêm/bớt constraints",
            "Có thể kiểm tra feasibility trước khi generate",
            "Framework chung cho nhiều bài toán"
        ],
        "limitations": [
            "Có thể chậm nếu quá nhiều ràng buộc",
            "Worst case exponential",
            "Cần tune heuristics cho từng bài toán",
            "Có thể không tìm được solution"
        ],
        "solution": "Thiết kế constraints theo mức ưu tiên: hard (bắt buộc) và soft (nên có). Nếu không tìm được solution, nới soft constraints hoặc reroll map.",
        "application": "Dùng sau khi DFS sinh mê cung, trước khi chạy quality gate. Đảm bảo content placement hợp lý."
    }
}

def get_algorithm_content(algo_name):
    """Lấy nội dung chi tiết của thuật toán"""
    return ALGORITHMS.get(algo_name, None)

def get_all_algorithm_names():
    """Lấy danh sách tên tất cả thuật toán"""
    return list(ALGORITHMS.keys())
