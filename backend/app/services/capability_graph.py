import networkx as nnx
from typing import Dict, Any, List

class CapabilityGraph:
    def __init__(self):
        self.G = nnx.DiGraph()
        self._initialize_graph()

    def _initialize_graph(self):
        # 1. Define Nodes (Capabilities)
        # Category: UI / Editor
        self.G.add_node("rich_text_editor", label="Markdown & Rich Text Editor", category="UI/UX", description="Block-based WYSIWYG editing, e.g., Notion slash command editor")
        self.G.add_node("drawing_canvas", label="Vector Drawing Canvas", category="UI/UX", description="Drag and drop creative workspace with canvas nodes, e.g., Canva/Figma")
        self.G.add_node("sidebar_navigation", label="Collapsible Sidebar Directory", category="UI/UX", description="Nested folder structure explorer for documents/files")
        self.G.add_node("tabbed_navigation", label="Tabbed Developer Hub", category="UI/UX", description="Dev-focused navigation with dashboard, repos, PRs, and issues")
        self.G.add_node("monaco_editor", label="Monaco Code Workspace", category="UI/UX", description="Tabbed multi-pane text editor with terminal sheet and syntax engine")
        
        # Category: Backend / Storage
        self.G.add_node("workspace_hierarchy", label="Multi-tenant Workspace Organization", category="Backend", description="Subdomain-level workspace isolation and workspace directories")
        self.G.add_node("block_storage", label="Block Database Storage", category="Storage", description="NoSQL block schema for modular page elements")
        self.G.add_node("git_host", label="Git Repository Hosting Node", category="Backend", description="Git commit manager, hooks, branch locker, merge tools")
        self.G.add_node("pubsub_chat", label="Websocket PubSub Messaging", category="Backend", description="Real-time message push, gateways, presence notifications, threads")
        self.G.add_node("webrtc_voice", label="Low-latency WebRTC Audio/Video", category="Backend", description="Low-latency huddles, video calling, and media routing gateways")
        self.G.add_node("auth_rbac", label="Role-Based Access Control (RBAC)", category="Authentication", description="Granular permissions settings from owner to public viewers")
        self.G.add_node("workflow_runner", label="CI/CD Action Pipeline Runner", category="Backend", description="Automated event-triggered worker executions")

        # 2. Define Edges (Dependencies, Extensions, Alternatives)
        # Syntax: self.G.add_edge(source, target, relation="...")
        self.G.add_edge("rich_text_editor", "block_storage", relation="depends_on")
        self.G.add_edge("drawing_canvas", "rich_text_editor", relation="extends")
        self.G.add_edge("sidebar_navigation", "workspace_hierarchy", relation="depends_on")
        self.G.add_edge("tabbed_navigation", "git_host", relation="depends_on")
        self.G.add_edge("monaco_editor", "git_host", relation="extends")
        self.G.add_edge("pubsub_chat", "auth_rbac", relation="depends_on")
        self.G.add_edge("webrtc_voice", "pubsub_chat", relation="enhances")
        self.G.add_edge("workflow_runner", "git_host", relation="depends_on")
        
        # Cross mappings
        self.G.add_edge("rich_text_editor", "pubsub_chat", relation="extends")

    def find_relevant_nodes(self, keywords: List[str]) -> List[str]:
        """Simple keyword matching to extract capability nodes"""
        matched = []
        for node, data in self.G.nodes(data=True):
            node_str = f"{node} {data.get('label', '')} {data.get('description', '')}".lower()
            if any(kw.lower() in node_str for kw in keywords):
                matched.append(node)
        return matched

    def get_subgraph(self, nodes: List[str]) -> Dict[str, Any]:
        """Extract nodes, their descendants, and ancestors to build the system architecture graph"""
        all_nodes = set(nodes)
        for node in nodes:
            if node in self.G:
                # Add descendants (dependencies)
                all_nodes.update(self.G.successors(node))
                # Add ancestors
                all_nodes.update(self.G.predecessors(node))

        sub_g = self.G.subgraph(all_nodes)
        
        # Convert to React Flow node/edge format
        nodes_list = []
        edges_list = []
        
        # Node placements (layout math for visual display in React Flow)
        import math
        count = len(sub_g)
        radius = 250
        angle_step = (2 * math.pi) / count if count > 0 else 0
        
        for i, (node, data) in enumerate(sub_g.nodes(data=True)):
            x = 400 + radius * math.cos(i * angle_step)
            y = 300 + radius * math.sin(i * angle_step)
            
            nodes_list.append({
                "id": node,
                "type": "customNode",
                "position": {"x": x, "y": y},
                "data": {
                    "label": data.get("label", node),
                    "category": data.get("category", "General"),
                    "description": data.get("description", "")
                }
            })
            
        for source, target, data in sub_g.edges(data=True):
            edges_list.append({
                "id": f"e-{source}-{target}",
                "source": source,
                "target": target,
                "label": data.get("relation", "connects"),
                "animated": True if data.get("relation") in ["depends_on", "extends"] else False
            })
            
        return {"nodes": nodes_list, "edges": edges_list}

capability_graph = CapabilityGraph()
