"""
Module tự động tạo biểu đồ và sơ đồ cho báo cáo
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from io import BytesIO
import networkx as nx

class DiagramGenerator:
    """Tạo các loại biểu đồ tự động"""
    
    def __init__(self):
        plt.rcParams['font.size'] = 10
        plt.rcParams['figure.dpi'] = 150
    
    def create_maze_example(self, size=10):
        """Tạo ví dụ mê cung DFS"""
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Tạo mê cung mẫu
        maze = np.random.choice([0, 1], size=(size, size), p=[0.3, 0.7])
        maze[0, 0] = 1  # Start
        maze[size-1, size-1] = 1  # End
        
        # Vẽ
        ax.imshow(maze, cmap='binary', interpolation='nearest')
        ax.set_title('Ví dụ mê cung sinh bằng DFS', fontweight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Đánh dấu start/end
        ax.text(0, 0, 'S', ha='center', va='center', color='green', fontsize=16, fontweight='bold')
        ax.text(size-1, size-1, 'E', ha='center', va='center', color='red', fontsize=16, fontweight='bold')
        
        return self._fig_to_bytes(fig)
    
    def create_bfs_visualization(self):
        """Tạo visualization BFS"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Grid
        size = 8
        grid = np.ones((size, size))
        grid[2:6, 3:5] = 0  # Walls
        
        # BFS distance map
        start = (0, 0)
        distances = np.full((size, size), -1)
        distances[start] = 0
        
        # Simple BFS simulation
        queue = [start]
        visited = {start}
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid[nx, ny] == 1:
                    distances[nx, ny] = distances[x, y] + 1
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        # Plot grid
        ax1.imshow(grid, cmap='binary', interpolation='nearest')
        ax1.set_title('Bản đồ (0=tường, 1=đường)', fontweight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])
        
        # Plot distance map
        masked_dist = np.ma.masked_where(distances == -1, distances)
        im = ax2.imshow(masked_dist, cmap='YlOrRd', interpolation='nearest')
        ax2.set_title('Distance Map từ (0,0)', fontweight='bold')
        ax2.set_xticks([])
        ax2.set_yticks([])
        plt.colorbar(im, ax=ax2, label='Khoảng cách')
        
        # Add numbers
        for i in range(size):
            for j in range(size):
                if distances[i, j] >= 0:
                    ax2.text(j, i, str(int(distances[i, j])), 
                            ha='center', va='center', color='black', fontsize=8)
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_astar_comparison(self):
        """So sánh BFS vs A*"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        size = 10
        
        # BFS - mở nhiều nút
        bfs_explored = np.random.rand(size, size) < 0.7
        ax1.imshow(bfs_explored, cmap='Blues', alpha=0.6)
        ax1.set_title('BFS - Mở nhiều nút', fontweight='bold')
        ax1.plot([0, size-1], [0, size-1], 'r-', linewidth=2, label='Đường đi')
        ax1.legend()
        ax1.set_xticks([])
        ax1.set_yticks([])
        
        # A* - mở ít nút hơn
        astar_explored = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                if abs(i - j) <= 2:  # Chỉ mở gần đường đi
                    astar_explored[i, j] = 1
        
        ax2.imshow(astar_explored, cmap='Greens', alpha=0.6)
        ax2.set_title('A* - Mở ít nút hơn nhờ heuristic', fontweight='bold')
        ax2.plot([0, size-1], [0, size-1], 'r-', linewidth=2, label='Đường đi')
        ax2.legend()
        ax2.set_xticks([])
        ax2.set_yticks([])
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_dijkstra_cost_map(self):
        """Tạo cost map cho Dijkstra"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        size = 10
        
        # Base cost map
        cost_map = np.ones((size, size))
        
        # Add dangers
        cost_map[3:5, 3:7] = 5  # Trap zone
        cost_map[7, 2:8] = 4    # Monster zone
        cost_map[2, 5] = 6      # High danger
        
        # Plot cost map
        im1 = ax1.imshow(cost_map, cmap='YlOrRd', interpolation='nearest')
        ax1.set_title('Cost Map (1=an toàn, 6=nguy hiểm)', fontweight='bold')
        plt.colorbar(im1, ax=ax1, label='Chi phí')
        ax1.set_xticks([])
        ax1.set_yticks([])
        
        # Add labels
        ax1.text(5, 4, 'TRAP', ha='center', va='center', fontweight='bold')
        ax1.text(5, 7, 'MONSTER', ha='center', va='center', fontweight='bold')
        
        # Show two paths
        ax2.imshow(cost_map, cmap='YlOrRd', alpha=0.3, interpolation='nearest')
        
        # Shortest path (goes through danger)
        ax2.plot([0, 5, 9], [0, 4, 9], 'b--', linewidth=2, label='Đường ngắn (nguy hiểm)', marker='o')
        
        # Safe path (longer but safer)
        ax2.plot([0, 1, 1, 8, 9], [0, 1, 8, 8, 9], 'g-', linewidth=2, label='Đường an toàn (Dijkstra)', marker='s')
        
        ax2.set_title('So sánh đường đi', fontweight='bold')
        ax2.legend()
        ax2.set_xticks([])
        ax2.set_yticks([])
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_csp_example(self):
        """Tạo ví dụ CSP"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Variables
        variables = ['Treasure', 'Monster1', 'Monster2', 'Quiz1', 'Quiz2']
        
        # Create constraint graph
        G = nx.Graph()
        G.add_nodes_from(variables)
        
        # Add constraints (edges)
        constraints = [
            ('Treasure', 'Monster1'),
            ('Treasure', 'Monster2'),
            ('Monster1', 'Monster2'),
            ('Quiz1', 'Quiz2'),
            ('Treasure', 'Quiz1')
        ]
        G.add_edges_from(constraints)
        
        # Draw
        pos = nx.spring_layout(G, seed=42)
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', ax=ax)
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, ax=ax)
        
        ax.set_title('Constraint Graph - CSP\n(Cạnh = ràng buộc giữa 2 biến)', fontweight='bold')
        ax.axis('off')
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_graph_coloring(self):
        """Tạo ví dụ Graph Coloring"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Create map regions
        size = 10
        regions = np.zeros((size, size))
        
        # Define regions
        regions[0:4, 0:4] = 1
        regions[0:4, 4:7] = 2
        regions[0:4, 7:10] = 3
        regions[4:7, 0:5] = 4
        regions[4:7, 5:10] = 5
        regions[7:10, 0:6] = 6
        regions[7:10, 6:10] = 7
        
        # Before coloring
        ax1.imshow(regions, cmap='tab10', interpolation='nearest')
        ax1.set_title('Bản đồ chia vùng', fontweight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])
        
        # After coloring
        colors = {1: 'red', 2: 'blue', 3: 'green', 4: 'blue', 5: 'red', 6: 'green', 7: 'blue'}
        colored_map = np.zeros((size, size, 3))
        color_rgb = {'red': [1,0,0], 'blue': [0,0,1], 'green': [0,1,0]}
        
        for i in range(size):
            for j in range(size):
                region = int(regions[i, j])
                if region > 0:
                    colored_map[i, j] = color_rgb[colors[region]]
        
        ax2.imshow(colored_map, interpolation='nearest')
        ax2.set_title('Sau Graph Coloring (3 màu)', fontweight='bold')
        ax2.set_xticks([])
        ax2.set_yticks([])
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_tarjan_example(self):
        """Tạo ví dụ Tarjan - Articulation Points"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Create graph
        G = nx.Graph()
        edges = [
            (1, 2), (2, 3), (3, 4), (4, 5),
            (2, 6), (6, 7), (7, 8),
            (3, 9), (9, 10)
        ]
        G.add_edges_from(edges)
        
        # Find articulation points (manually for demo)
        articulation_points = [2, 3, 6, 9]
        
        # Draw
        pos = nx.spring_layout(G, seed=42)
        
        # Draw normal nodes
        normal_nodes = [n for n in G.nodes() if n not in articulation_points]
        nx.draw_networkx_nodes(G, pos, nodelist=normal_nodes, 
                              node_color='lightblue', node_size=500, ax=ax)
        
        # Draw articulation points
        nx.draw_networkx_nodes(G, pos, nodelist=articulation_points,
                              node_color='red', node_size=700, ax=ax)
        
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, ax=ax)
        
        ax.set_title('Tarjan - Articulation Points (đỏ)\nNếu xóa nút đỏ, đồ thị bị tách rời', 
                    fontweight='bold')
        ax.axis('off')
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_influence_map(self):
        """Tạo Influence Map"""
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        
        size = 10
        
        # Enemy influence
        enemy_pos = (7, 7)
        enemy_influence = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                dist = np.sqrt((i - enemy_pos[0])**2 + (j - enemy_pos[1])**2)
                enemy_influence[i, j] = max(0, 5 - dist)
        
        im1 = ax1.imshow(enemy_influence, cmap='Reds', interpolation='bilinear')
        ax1.plot(enemy_pos[1], enemy_pos[0], 'ko', markersize=15, label='Enemy')
        ax1.set_title('Danger Map\n(Ảnh hưởng từ enemy)', fontweight='bold')
        ax1.legend()
        plt.colorbar(im1, ax=ax1)
        ax1.set_xticks([])
        ax1.set_yticks([])
        
        # Treasure opportunity
        treasure_pos = (2, 2)
        treasure_influence = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                dist = np.sqrt((i - treasure_pos[0])**2 + (j - treasure_pos[1])**2)
                treasure_influence[i, j] = max(0, 4 - dist)
        
        im2 = ax2.imshow(treasure_influence, cmap='Greens', interpolation='bilinear')
        ax2.plot(treasure_pos[1], treasure_pos[0], 'y*', markersize=20, label='Treasure')
        ax2.set_title('Opportunity Map\n(Ảnh hưởng từ treasure)', fontweight='bold')
        ax2.legend()
        plt.colorbar(im2, ax=ax2)
        ax2.set_xticks([])
        ax2.set_yticks([])
        
        # Combined
        combined = treasure_influence - enemy_influence
        im3 = ax3.imshow(combined, cmap='RdYlGn', interpolation='bilinear', vmin=-5, vmax=5)
        ax3.plot(enemy_pos[1], enemy_pos[0], 'ko', markersize=15)
        ax3.plot(treasure_pos[1], treasure_pos[0], 'y*', markersize=20)
        ax3.set_title('Combined Influence\n(Xanh=tốt, Đỏ=nguy hiểm)', fontweight='bold')
        plt.colorbar(im3, ax=ax3)
        ax3.set_xticks([])
        ax3.set_yticks([])
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def create_minimax_tree(self):
        """Tạo cây Minimax"""
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Create tree
        G = nx.DiGraph()
        
        # Add nodes with values
        nodes = {
            'root': 3,
            'A': 3, 'B': 5,
            'A1': 3, 'A2': 5, 'B1': 5, 'B2': 7,
            'A1a': 3, 'A1b': 5, 'A2a': 5, 'A2b': 9,
            'B1a': 5, 'B1b': 7, 'B2a': 7, 'B2b': 9
        }
        
        G.add_nodes_from(nodes.keys())
        
        # Add edges
        edges = [
            ('root', 'A'), ('root', 'B'),
            ('A', 'A1'), ('A', 'A2'), ('B', 'B1'), ('B', 'B2'),
            ('A1', 'A1a'), ('A1', 'A1b'), ('A2', 'A2a'), ('A2', 'A2b'),
            ('B1', 'B1a'), ('B1', 'B1b'), ('B2', 'B2a'), ('B2', 'B2b')
        ]
        G.add_edges_from(edges)
        
        # Layout
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot') if hasattr(nx, 'nx_agraph') else nx.spring_layout(G)
        
        # Draw
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800, ax=ax)
        
        # Draw labels with values
        labels = {node: f"{node}\n{val}" for node, val in nodes.items()}
        nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)
        nx.draw_networkx_edges(G, pos, arrows=True, ax=ax)
        
        ax.set_title('Cây Minimax (depth=3)\nMAX chọn giá trị lớn nhất, MIN chọn nhỏ nhất', 
                    fontweight='bold')
        ax.axis('off')
        
        plt.tight_layout()
        return self._fig_to_bytes(fig)
    
    def _fig_to_bytes(self, fig):
        """Convert matplotlib figure to bytes"""
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        buf.seek(0)
        plt.close(fig)
        return buf

# Test
if __name__ == '__main__':
    gen = DiagramGenerator()
    print("Testing diagram generation...")
    
    diagrams = [
        ('maze', gen.create_maze_example()),
        ('bfs', gen.create_bfs_visualization()),
        ('astar', gen.create_astar_comparison()),
        ('dijkstra', gen.create_dijkstra_cost_map()),
        ('csp', gen.create_csp_example()),
        ('coloring', gen.create_graph_coloring()),
        ('tarjan', gen.create_tarjan_example()),
        ('influence', gen.create_influence_map()),
        ('minimax', gen.create_minimax_tree())
    ]
    
    for name, buf in diagrams:
        with open(f'test_{name}.png', 'wb') as f:
            f.write(buf.read())
        print(f"✓ Created test_{name}.png")
    
    print("\nAll diagrams generated successfully!")
