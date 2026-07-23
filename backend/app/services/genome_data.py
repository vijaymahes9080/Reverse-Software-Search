from typing import Dict, Any, List

GENOME_DATABASE: Dict[str, Dict[str, Any]] = {
    "notion": {
        "name": "Notion",
        "tagline": "The all-in-one workspace for notes, tasks, wikis, and databases.",
        "category": "Productivity & Collaboration",
        "design_language": {
            "mode": "minimalist",
            "primary_color": "#ffffff",
            "text_color": "#37352f",
            "font_family": "system-ui, -apple-system, sans-serif",
            "ui_style": "clean, flat borders, soft emoji icons, slash commands, inline tooltips"
        },
        "core_features": [
            "Hierarchical workspace document pages",
            "Slash command editor (/page, /todo, /database)",
            "Inline editable databases with multiple views (Table, Board, Calendar, Gallery)",
            "Rich text formatting & markdown styling",
            "Real-time co-authoring and commenting",
            "Public page publishing and custom domains"
        ],
        "navigation": {
            "type": "collapsible sidebar",
            "hierarchy": ["Workspace settings", "Favorites section", "Private pages list", "Public pages list", "Trash/Archive"]
        },
        "permissions": {
            "roles": ["Owner", "Workspace Admin", "Member", "Guest", "Viewer"],
            "access_levels": ["Full access", "Can edit", "Can comment", "Can view"]
        },
        "business_logic": {
            "workspace_sharing": True,
            "revision_history": True,
            "billing_limits": "Based on block count or workspace members"
        },
        "data_model": {
            "entities": [
                {"name": "Workspace", "attributes": ["id", "name", "owner_id", "created_at"]},
                {"name": "Page", "attributes": ["id", "parent_id", "title", "content_blocks", "emoji", "cover_url"]},
                {"name": "Block", "attributes": ["id", "page_id", "type", "content", "properties"]},
                {"name": "Database", "attributes": ["id", "page_id", "schema", "views"]},
                {"name": "Comment", "attributes": ["id", "block_id", "user_id", "text", "created_at"]}
            ]
        },
        "tech_stack": {
            "frontend": ["React", "TypeScript", "Next.js", "Zustand"],
            "backend": ["Node.js", "Express", "GraphQL"],
            "database": ["PostgreSQL", "Redis", "Elasticsearch"],
            "caching": ["Redis"]
        },
        "strengths": ["Extreme customizability", "Powerful database views", "Simple sidebar organization"],
        "weaknesses": ["Performance lag with large pages", "Steep initial learning curve", "Poor offline functionality"],
        "scalability": "Requires deep block indexing and caching database views in memory.",
        "performance": "Client-side block rendering can be heavy; virtualized lists are critical.",
        "security": "Needs block-level permissions and encrypted backups."
    },
    "github": {
        "name": "GitHub",
        "tagline": "The complete developer platform to build, scale, and deliver secure software.",
        "category": "Developer Tools & Version Control",
        "design_language": {
            "mode": "dark-theme-preferred",
            "primary_color": "#24292f",
            "text_color": "#adbac7",
            "font_family": "-apple-system, BlinkMacSystemFont, sans-serif",
            "ui_style": "tabbed navigation, code-focused tables, markdown rendering, developer icons"
        },
        "core_features": [
            "Git repository hosting and branch management",
            "Pull requests with code reviews and inline commenting",
            "Issues board and project tracking cards",
            "CI/CD automation via GitHub Actions",
            "Package registry and release distribution",
            "Activity streams and profile contributions grid"
        ],
        "navigation": {
            "type": "top navigation with tabbed sub-headers",
            "hierarchy": ["Global search", "Dashboard feed", "Repository tabs (Code, Issues, Pull Requests, Actions, Projects, Wiki, Settings)"]
        },
        "permissions": {
            "roles": ["Owner", "Admin", "Write / Developer", "Read / Collaborator", "Public Viewer"],
            "access_levels": ["Direct push", "Fork and PR", "Branch protection rules", "Issue creation only"]
        },
        "business_logic": {
            "branch_locks": True,
            "status_checks_required": True,
            "pr_approvals": True
        },
        "data_model": {
            "entities": [
                {"name": "Organization", "attributes": ["id", "name", "billing_email"]},
                {"name": "Repository", "attributes": ["id", "org_id", "name", "is_private", "git_url"]},
                {"name": "Commit", "attributes": ["sha", "repo_id", "author_id", "message", "timestamp"]},
                {"name": "PullRequest", "attributes": ["id", "repo_id", "source_branch", "target_branch", "status"]},
                {"name": "Issue", "attributes": ["id", "repo_id", "title", "body", "state", "labels"]}
            ]
        },
        "tech_stack": {
            "frontend": ["React", "TypeScript", "Primer Design System"],
            "backend": ["Ruby on Rails", "Go"],
            "database": ["MySQL", "Elasticsearch", "Spokes Git Server"],
            "caching": ["Memcached", "Redis"]
        },
        "strengths": ["Standardized code review flow", "Immense ecosystem integration", "Powerful automation engine"],
        "weaknesses": ["Complex interface for beginners", "High cost for large enterprise teams"],
        "scalability": "Requires distributed Git servers (spokes architecture) and highly robust queue routing.",
        "performance": "Extremely fast code-view loading using server-side caching of tree nodes.",
        "security": "Enforces GPG signing, two-factor auth, SSO, and secrets scanning."
    },
    "canva": {
        "name": "Canva",
        "tagline": "Empowering the world to design anything and publish anywhere.",
        "category": "Visual Design & Media",
        "design_language": {
            "mode": "creative-vibrant",
            "primary_color": "#00c4cc",
            "text_color": "#0e1318",
            "font_family": "League Spartan, Montserrat, sans-serif",
            "ui_style": "canvas drag-and-drop workspace, floating formatting toolbar, side panels for assets"
        },
        "core_features": [
            "Drag-and-drop graphic canvas layout builder",
            "Vector asset search and photo templates library",
            "Interactive resizing, filters, effects, and masking",
            "Multiplayer real-time asset editing and locking",
            "Brand kit creator (logos, palettes, custom typography)",
            "Direct-to-social publishing and print-on-demand export"
        ],
        "navigation": {
            "type": "fixed workspace with drawer navigation",
            "hierarchy": ["Dashboard Templates", "Projects Folder", "Brand Hub", "Content Planner", "Editor (Canvas, Toolbar, Asset Tray)"]
        },
        "permissions": {
            "roles": ["Owner", "Brand Administrator", "Template Designer", "Team Member", "External Client"],
            "access_levels": ["Edit element level", "Template creation only", "View and leave comments"]
        },
        "business_logic": {
            "asset_licensing": True,
            "export_dimensions_limit": True,
            "brand_guideline_checks": True
        },
        "data_model": {
            "entities": [
                {"name": "Design", "attributes": ["id", "title", "width", "height", "elements_json", "thumbnail_url"]},
                {"name": "Element", "attributes": ["id", "design_id", "type", "x", "y", "width", "height", "z_index"]},
                {"name": "Asset", "attributes": ["id", "url", "file_type", "license_type", "tags"]},
                {"name": "Team", "attributes": ["id", "name", "branding_palette", "fonts_list"]}
            ]
        },
        "tech_stack": {
            "frontend": ["HTML5 Canvas", "React", "TypeScript", "WebAssembly"],
            "backend": ["Java", "Spring Boot", "Go"],
            "database": ["PostgreSQL", "Amazon S3", "OpenSearch"],
            "caching": ["Redis"]
        },
        "strengths": ["Super intuitive drag-drop UI", "Massive stock library", "Real-time canvas sharing"],
        "weaknesses": ["Limited precise editing tools compared to Figma", "Struggles with large print layouts"],
        "scalability": "Requires heavy CDN edge caching for assets and custom rasterization microservices.",
        "performance": "Uses requestAnimationFrame, WebGL context, and WebAssembly for heavy canvas math.",
        "security": "Asset isolation, watermark security, and license enforcement."
    },
    "discord": {
        "name": "Discord",
        "tagline": "Where you can talk, chat, and hang out with friends and communities.",
        "category": "Communication & Community",
        "design_language": {
            "mode": "gamers-dark",
            "primary_color": "#5865F2",
            "text_color": "#dbdee1",
            "font_family": "gg sans, Whitney, Helvetica Neue, sans-serif",
            "ui_style": "three-column layout, rounded server icons, status badges, voice status bar"
        },
        "core_features": [
            "Guild server separation with text and voice channels",
            "Low-latency WebRTC group voice and video streaming",
            "Role permissions system with color hierarchy",
            "Rich embeds, markdown chat, emojis, and stickers",
            "Developer API with slash command bots",
            "Overlay game panel and activity statuses"
        ],
        "navigation": {
            "type": "multi-pane columns",
            "hierarchy": ["Leftmost server rail", "Channels sidebar with voice status block", "Main chat window / video feed", "Rightmost active members list"]
        },
        "permissions": {
            "roles": ["Guild Owner", "Administrator", "Moderator", "Verified Member", "Everyone"],
            "access_levels": ["Manage channels", "Mute/Deafen members", "Attach files", "Send messages"]
        },
        "business_logic": {
            "presence_broadcast": True,
            "voice_channel_bitrate": True,
            "custom_server_emojis": True
        },
        "data_model": {
            "entities": [
                {"name": "Guild", "attributes": ["id", "name", "owner_id", "icon_url"]},
                {"name": "Channel", "attributes": ["id", "guild_id", "name", "type", "position"]},
                {"name": "Message", "attributes": ["id", "channel_id", "author_id", "content", "attachments_json"]},
                {"name": "Role", "attributes": ["id", "guild_id", "name", "permissions_bitmask", "color"]}
            ]
        },
        "tech_stack": {
            "frontend": ["React", "TypeScript", "Electron", "Flux"],
            "backend": ["Elixir", "Python", "Rust", "Go"],
            "database": ["Cassandra", "ScyllaDB", "PostgreSQL"],
            "caching": ["Redis"]
        },
        "strengths": ["Extremely fast low-latency voice", "High structural permissions control", "Rich developer APIs"],
        "weaknesses": ["Voice quality depends heavily on region", "Prone to bot spamming", "No search history without database indexing"],
        "scalability": "Requires massive message queuing, Gateway WebSockets (in Elixir/Rust), and WebRTC media gateways.",
        "performance": "UI handles millions of elements through optimized list virtualization and WebRTC audio processing.",
        "security": "IP masking, DDoS protection on voice media gateways, end-to-end user isolation."
    },
    "slack": {
        "name": "Slack",
        "tagline": "Welcome to your new digital HQ, making work life simpler, more pleasant, and more productive.",
        "category": "Enterprise Communication",
        "design_language": {
            "mode": "professional-clean",
            "primary_color": "#4a154b",
            "text_color": "#1d1c1d",
            "font_family": "Larsseit, Slack-Lato, sans-serif",
            "ui_style": "two-column workspace, thread sidebar pane, search console, emoji reactions picker"
        },
        "core_features": [
            "Channels, private groups, and direct messaging",
            "Threaded message conversations to keep topics tidy",
            "Slack Huddles for rapid audio/video connections",
            "File search indexing inside PDFs and text documents",
            "Enterprise integrations (Google Drive, Jira, GitHub)",
            "Automated workflows using the Workflow Builder"
        ],
        "navigation": {
            "type": "collapsible team navigation sidebar",
            "hierarchy": ["Workspace drop-down menu", "Home dashboard listing channels and DMs", "Thread drawer panel", "Activity feed"]
        },
        "permissions": {
            "roles": ["Primary Owner", "Admin", "Member", "Multi-Channel Guest", "Single-Channel Guest"],
            "access_levels": ["Post in default channels", "Create new channels", "Invite guests", "Approve app installations"]
        },
        "business_logic": {
            "retention_policy_compliance": True,
            "workspace_federation": True,
            "export_history_logs": True
        },
        "data_model": {
            "entities": [
                {"name": "Workspace", "attributes": ["id", "name", "subdomain", "settings_json"]},
                {"name": "Channel", "attributes": ["id", "workspace_id", "name", "is_private"]},
                {"name": "Message", "attributes": ["id", "channel_id", "user_id", "content", "thread_ts", "reactions"]},
                {"name": "User", "attributes": ["id", "display_name", "status_emoji", "avatar_url"]}
            ]
        },
        "tech_stack": {
            "frontend": ["React", "TypeScript", "Electron"],
            "backend": ["PHP (HHVM/Hack)", "Java", "Go"],
            "database": ["Vitess (MySQL shard)", "Elasticsearch"],
            "caching": ["Redis", "Memcached"]
        },
        "strengths": ["Enterprise compliance readiness", "Intuitive threading system", "Superb third-party app ecosystem"],
        "weaknesses": ["Very high RAM consumption (Electron)", "Search can feel slow with large teams", "Expensive pricing per user"],
        "scalability": "Requires Vitess horizontal database partitioning and real-time pub/sub synchronization.",
        "performance": "Utilizes windowed rendering and localized state management to speed up channel switches.",
        "security": "Enforces HIPAA compliance, Enterprise Key Management (EKM), and custom retention rules."
    },
    "vscode": {
        "name": "VSCode",
        "tagline": "Code editing. Redefined.",
        "category": "Developer Tools & Editors",
        "design_language": {
            "mode": "dark-editor",
            "primary_color": "#1e1e1e",
            "text_color": "#d4d4d4",
            "font_family": "Consolas, 'Courier New', monospace",
            "ui_style": "multi-pane code workspace, sidebar activity bar, integrated terminal bottom sheet, code editor window"
        },
        "core_features": [
            "Extensible text editor with syntax highlighting and autocomplete (IntelliSense)",
            "Integrated terminal pane supporting multiple shells",
            "Built-in Git stage management and merge conflict resolver",
            "Visual debugger panel with variables and call stack view",
            "Marketplace for third-party extensions and programming languages",
            "Remote development SSH/WSL and container support"
        ],
        "navigation": {
            "type": "side activity bar with sidebar view drawer",
            "hierarchy": ["Leftmost icon bar (Explorer, Search, Source Control, Run/Debug, Extensions)", "Sidebar list panel", "Editor grid view with split panels", "Bottom status bar"]
        },
        "permissions": {
            "roles": ["User / Developer"],
            "access_levels": ["Full local access", "Workspace trusted folder setting", "Extension installation clearance"]
        },
        "business_logic": {
            "trusted_workspaces": True,
            "extension_sandbox": True,
            "telemetry_opt_out": True
        },
        "data_model": {
            "entities": [
                {"name": "WorkspaceSetting", "attributes": ["key", "value", "scope"]},
                {"name": "Extension", "attributes": ["id", "publisher", "name", "version", "is_disabled"]},
                {"name": "FileNode", "attributes": ["path", "name", "is_directory", "size", "last_modified"]},
                {"name": "Breakpoint", "attributes": ["id", "file_path", "line_number", "condition"]}
            ]
        },
        "tech_stack": {
            "frontend": ["HTML5/CSS", "TypeScript", "Electron", "Monaco Editor"],
            "backend": ["Node.js", "C++ (Extension Host process)"],
            "database": ["Local Filesystem", "IndexedDB", "SQLite (state store)"],
            "caching": ["V8 Code cache"]
        },
        "strengths": ["Enormous library of extensions", "Highly optimized text editor (Monaco)", "Flexible layouts"],
        "weaknesses": ["High RAM usage (Electron-based)", "Extensions can cause slow startup times"],
        "scalability": "Scales through multi-process architecture (extension host, terminal runner, and main UI render separated).",
        "performance": "Monaco editor uses offscreen canvases, character measuring cache, and CSS hardware acceleration.",
        "security": "Enforces workspace trust prompts to block automated script execution in untrusted paths."
    }
}
