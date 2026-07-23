from typing import Dict, Any, List

def generate_ui(prompt: str, intent: Dict[str, Any], genomes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate responsive views, color palettes, themes, and sample component code blocks.
    """
    title = intent["title"]
    design = genomes["synthesized_design"]

    screens = [
        {
            "name": "User Authentication Hub",
            "description": "Clean split-screen view with a canvas layout branding slide on the left, and login fields on the right.",
            "components": ["Input", "Button", "Card", "Label", "BrandLogo"]
        },
        {
            "name": "Central Workspace Dashboard",
            "description": "Multi-pane workspace showing a collapsible directory sidebar, document canvases, editor windows, and team active avatars.",
            "components": ["Sidebar", "ResizablePanel", "AvatarGroup", "Breadcrumb", "ScrollArea"]
        },
        {
            "name": "Visual Editing & Code Canvas",
            "description": "An interactive whiteboard with toolbar nodes (shapes, markdown blocks, terminal splits) mapping code structure to documentation.",
            "components": ["CanvasArea", "Toolbar", "MonacoEditor", "ReactFlowBoard", "DialogSheet"]
        }
    ]

    # Theme config (shadcn compatible)
    theme_variables = {
        "light": {
            "background": "0 0% 100%",
            "foreground": "240 10% 3.9%",
            "primary": "240 5.9% 10%",
            "primary-foreground": "0 0% 98%",
            "card": "0 0% 100%",
            "border": "240 5.9% 90%",
            "ring": "240 5.9% 10%"
        },
        "dark": {
            "background": "240 10% 3.9%",
            "foreground": "0 0% 98%",
            "primary": "0 0% 98%",
            "primary-foreground": "240 5.9% 10%",
            "card": "240 10% 3.9%",
            "border": "240 3.7% 15.9%",
            "ring": "240 4.9% 83.9%"
        }
    }

    # High quality component blueprint code (Tailwind React template)
    sample_component_code = """import React, { useState } from 'react';
import { PanelLeftClose, Plus, Settings, Sparkles } from 'lucide-react';

export default function WorkspaceLayout({ children }: { children: React.ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="flex h-screen w-screen overflow-hidden bg-background text-foreground">
      {/* Collapsible Sidebar */}
      <aside 
        className={`flex flex-col border-r border-border bg-card/60 backdrop-blur-md transition-all duration-300 ${
          sidebarOpen ? 'w-64' : 'w-0 border-none'
        } overflow-hidden`}
      >
        <div className="flex h-14 items-center justify-between px-4 border-b border-border">
          <span className="font-bold text-lg tracking-wider bg-gradient-to-r from-sky-400 to-indigo-500 bg-clip-text text-transparent">
            {title}
          </span>
          <button onClick={() => setSidebarOpen(false)} className="hover:text-primary transition-colors">
            <PanelLeftClose size={18} />
          </button>
        </div>
        
        {/* Navigation Elements */}
        <nav className="flex-1 space-y-1 p-2">
          <button className="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-sm bg-accent/50 font-medium">
            <Plus size={16} /> New Canvas Page
          </button>
          <div className="my-4 border-t border-border" />
          <div className="px-3 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Documents
          </div>
          <div className="mt-2 space-y-1 text-sm text-muted-foreground px-3">
            <div className="py-1 cursor-pointer hover:text-foreground">📄 Product Specification</div>
            <div className="py-1 cursor-pointer hover:text-foreground">📊 Interactive ER Diagram</div>
            <div className="py-1 cursor-pointer hover:text-foreground">🎨 Theme Configuration</div>
          </div>
        </nav>

        {/* User Footer info */}
        <div className="p-3 border-t border-border flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-full bg-indigo-600 flex items-center justify-center font-bold text-white text-xs">
              CTO
            </div>
            <div>
              <p className="text-xs font-semibold">Self-Hosted User</p>
              <p className="text-[10px] text-muted-foreground">Admin Workspace</p>
            </div>
          </div>
          <button className="p-1 hover:bg-accent rounded-md">
            <Settings size={14} />
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col min-w-0">
        <header className="flex h-14 items-center justify-between px-6 border-b border-border">
          {!sidebarOpen && (
            <button onClick={() => setSidebarOpen(true)} className="p-1 hover:bg-accent rounded-md">
              <Plus className="rotate-45" size={18} />
            </button>
          )}
          <div className="text-sm font-medium">Workspace / Home</div>
          <button className="flex items-center gap-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/20 px-3 py-1 text-xs text-indigo-400 font-semibold hover:bg-indigo-500/20 transition-all">
            <Sparkles size={12} /> AI Synthesizer
          </button>
        </header>

        <section className="flex-1 overflow-y-auto p-6">
          {children}
        </section>
      </main>
    </div>
  );
}
"""

    return {
        "screens": screens,
        "theme": {
            "style_mode": design["mode"],
            "colors": design["primary_color"],
            "variables": theme_variables
        },
        "sample_layout_code": sample_component_code
    }
