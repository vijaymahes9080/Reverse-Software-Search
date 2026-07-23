'use client';

import React, { useState, useEffect } from 'react';
import { 
  Sparkles, Search, ChevronRight, Download, Globe, Cpu, Database, 
  Layers, Play, Workflow, ArrowRight, ShieldCheck, RefreshCw, BarChart2,
  DollarSign, CheckCircle, AlertTriangle, ExternalLink, Lightbulb, BookOpen,
  Code, Menu, X, ArrowUpRight
} from 'lucide-react';
import confetti from 'canvas-confetti';
import ArchitectureGraph from '@/components/ArchitectureGraph';
import CodePreview from '@/components/CodePreview';

// Interface structures
interface Blueprint {
  id: string;
  prompt: string;
  title: string;
  tagline: string;
  summary: string;
  created_at: string;
  intent: any;
  genomes: any;
  graph: any;
  architecture: any;
  db: any;
  apis: any;
  ui: any;
  workflows: any;
  ai: any;
  deployment: any;
  costs: any;
  oss: any;
  innovations: any;
  startup: any;
  multi_agent?: any;
  files: Record<string, string>;
}

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState(0);
  const [blueprint, setBlueprint] = useState<Blueprint | null>(null);
  const [history, setHistory] = useState<any[]>([]);
  const [activeTab, setActiveTab] = useState('vision');
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const templates = [
    "🛡️ ZeroCost AI SaaS Architect: Self-hosted Datadog alternative",
    "🌉 Autonomous API Bridge Generator: Legacy REST to GraphQL SDKs",
    "⚡ Neural Architecture Simulator: 100k req/sec bottleneck stress tester",
    "🧬 AI Codebase Genome Scanner: GitHub repo modernizer & security auditor",
    "I want Canva + GitHub + Notion",
    "I want Discord for hospitals"
  ];

  const loadingSteps = [
    "Initializing Synthesis Engines...",
    "Extracting Intent Genomes...",
    "Constructing Capability Graph Nodes...",
    "Planning Microservices Service Mesh...",
    "Formulating PostgreSQL DDL tables...",
    "Defining REST & WebSockets OpenAPI specs...",
    "Creating layout components & Tailwind themes...",
    "Building sequence workflows & user journeys...",
    "Generating AI agent prompt chains...",
    "Compiling code files and packaging starter ZIP..."
  ];

  // Load history on mount
  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/v1/blueprints');
      if (res.ok) {
        const data = await res.json();
        setHistory(data);
      }
    } catch (err) {
      console.error("Failed to load history:", err);
    }
  };

  const handleSynthesize = async (searchPrompt: string) => {
    if (!searchPrompt.trim()) return;
    setLoading(true);
    setBlueprint(null);
    setLoadingStep(0);

    // Simulate progress steps
    const interval = setInterval(() => {
      setLoadingStep((prev) => {
        if (prev < loadingSteps.length - 1) return prev + 1;
        clearInterval(interval);
        return prev;
      });
    }, 1200);

    try {
      const res = await fetch('http://localhost:8000/api/v1/synthesize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: searchPrompt })
      });

      clearInterval(interval);

      if (res.ok) {
        const data = await res.json();
        setBlueprint(data);
        confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 } });
        fetchHistory();
      } else {
        alert("Synthesis failed. Check backend console.");
      }
    } catch (err) {
      clearInterval(interval);
      console.error(err);
      alert("Backend connection failed. Please ensure the backend server is running.");
    } finally {
      setLoading(false);
    }
  };

  const loadBlueprint = async (id: string) => {
    setLoading(true);
    try {
      const res = await fetch(`http://localhost:8000/api/v1/blueprints/${id}`);
      if (res.ok) {
        const data = await res.json();
        setBlueprint(data);
        setActiveTab('vision');
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen w-screen bg-[#030712] text-[#f3f4f6] overflow-hidden">
      {/* Sidebar - History */}
      <aside className={`flex flex-col border-r border-gray-800/80 bg-gray-950/70 backdrop-blur-md transition-all duration-300 ${
        sidebarOpen ? 'w-80' : 'w-0 border-none'
      } overflow-hidden`}>
        <div className="flex h-16 items-center justify-between px-6 border-b border-gray-800/80">
          <div className="flex items-center gap-2">
            <Sparkles className="text-blue-500" size={20} />
            <span className="font-extrabold text-lg tracking-wider bg-gradient-to-r from-blue-400 to-indigo-500 bg-clip-text text-transparent">
              RSS ENGINE
            </span>
          </div>
          <button onClick={() => setSidebarOpen(false)} className="text-gray-400 hover:text-white transition-colors">
            <X size={18} />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          <div className="px-2">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-widest mb-3">
              Synthesized History
            </h3>
            {history.length === 0 ? (
              <p className="text-xs text-gray-500 italic mt-2">No past synthesis runs yet.</p>
            ) : (
              <div className="space-y-2">
                {history.map((bp) => (
                  <button
                    key={bp.id}
                    onClick={() => loadBlueprint(bp.id)}
                    className={`w-full text-left p-3 rounded-xl border border-gray-800 bg-gray-900/40 hover:bg-gray-800/60 transition-all ${
                      blueprint?.id === bp.id ? 'border-blue-500/60 bg-blue-950/20' : ''
                    }`}
                  >
                    <div className="font-bold text-sm text-gray-200 truncate">{bp.title}</div>
                    <div className="text-xs text-gray-400 truncate mt-0.5">"{bp.prompt}"</div>
                    <div className="text-[10px] text-gray-500 mt-2">{new Date(bp.created_at).toLocaleString()}</div>
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        <div className="p-4 border-t border-gray-800/80 bg-gray-950/50">
          <div className="text-[10px] text-gray-500 text-center">
            Reverse Software Search © 2026
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden min-w-0">
        {/* Header */}
        <header className="flex h-16 items-center justify-between px-8 border-b border-gray-800/80 bg-gray-950/20">
          <div className="flex items-center gap-4">
            {!sidebarOpen && (
              <button onClick={() => setSidebarOpen(true)} className="p-2 hover:bg-gray-800 rounded-xl transition-all">
                <Menu size={20} />
              </button>
            )}
            <div className="text-sm text-gray-400">
              {blueprint ? `Blueprint: ${blueprint.title}` : "Software Synthesis Engine"}
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="inline-flex h-2 w-2 rounded-full bg-green-500 animate-pulse" />
            <span className="text-xs text-gray-400 font-medium">Core API Connected</span>
          </div>
        </header>

        {/* Dynamic content scrollable area */}
        <div className="flex-1 overflow-y-auto p-8 max-w-6xl w-full mx-auto space-y-8">
          
          {/* SEARCH PROMPT MODULE */}
          {!blueprint && !loading && (
            <div className="py-12 space-y-8 text-center max-w-2xl mx-auto">
              <div className="space-y-3">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold">
                  <Sparkles size={12} /> Describe software. Generate the product.
                </div>
                <h1 className="text-5xl font-black tracking-tight leading-none bg-gradient-to-r from-white via-gray-200 to-gray-500 bg-clip-text text-transparent">
                  Reverse Software Search
                </h1>
                <p className="text-lg text-gray-400 font-medium">
                  Input combinations of capabilities, domains, or workflows. Evolve standard clone blueprints into innovative new architectures.
                </p>
              </div>

              {/* Large Search Input */}
              <div className="relative glass-panel rounded-2xl p-2 shadow-2xl flex items-center border border-gray-800">
                <div className="pl-3 text-gray-500"><Search size={22} /></div>
                <input
                  type="text"
                  placeholder="e.g. I want Canva + GitHub + Notion..."
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSynthesize(prompt)}
                  className="flex-1 bg-transparent px-4 py-3 text-lg focus:outline-none placeholder-gray-500 text-white"
                />
                <button
                  onClick={() => handleSynthesize(prompt)}
                  className="px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl transition-all glow-btn cursor-pointer flex items-center gap-2"
                >
                  <span>Synthesize</span>
                  <ArrowRight size={16} />
                </button>
              </div>

              {/* Quick Template Prompts */}
              <div className="space-y-3">
                <h4 className="text-xs font-bold uppercase tracking-wider text-gray-500">
                  Try standard template combinations
                </h4>
                <div className="flex flex-wrap justify-center gap-2.5">
                  {templates.map((tpl) => (
                    <button
                      key={tpl}
                      onClick={() => {
                        setPrompt(tpl);
                        handleSynthesize(tpl);
                      }}
                      className="px-4 py-2 text-sm rounded-full glass-card hover:bg-gray-800/80 transition-all border border-gray-800 text-gray-300"
                    >
                      {tpl}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* LOADING SCREEN CONTAINER */}
          {loading && (
            <div className="glass-panel border border-gray-800 rounded-2xl p-8 max-w-xl mx-auto space-y-6 text-center shadow-2xl py-12">
              <div className="relative h-16 w-16 mx-auto">
                <div className="absolute inset-0 rounded-full border-4 border-blue-500/20 border-t-blue-500 animate-spin" />
              </div>
              <div className="space-y-2">
                <h3 className="text-xl font-bold text-white">Synthesizing Product Specs</h3>
                <p className="text-sm text-gray-400 italic">"Thinking like an experienced CTO..."</p>
              </div>

              <div className="w-full bg-gray-900 rounded-full h-1.5 overflow-hidden">
                <div 
                  className="bg-gradient-to-r from-blue-500 to-indigo-600 h-1.5 transition-all duration-500"
                  style={{ width: `${((loadingStep + 1) / loadingSteps.length) * 100}%` }}
                />
              </div>

              <div className="text-sm text-blue-400 font-semibold animate-pulse">
                {loadingSteps[loadingStep]}
              </div>
            </div>
          )}

          {/* SPECIFICATION DETAILED BOARD */}
          {blueprint && !loading && (
            <div className="space-y-6">
              
              {/* Product overview header board */}
              <div className="glass-panel border border-gray-800 rounded-2xl p-6 flex flex-col md:flex-row md:items-center justify-between gap-6 shadow-xl">
                <div className="space-y-2">
                  <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold">
                    <CheckCircle size={12} /> Successfully Synthesized
                  </div>
                  <h2 className="text-3xl font-black text-white tracking-tight">{blueprint.title}</h2>
                  <p className="text-gray-400 font-medium">{blueprint.tagline}</p>
                  <p className="text-xs text-gray-500 italic">Synthesized from: "{blueprint.prompt}"</p>
                </div>
                
                {/* Download Zip Codebase Action */}
                <div>
                  <a
                    href={`http://localhost:8000/api/v1/blueprints/${blueprint.id}/download`}
                    className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 font-bold text-sm shadow-lg shadow-blue-500/25 transition-all"
                  >
                    <Download size={18} />
                    <span>Download Starter Zip</span>
                  </a>
                </div>
              </div>

              {/* TABS ROW BAR */}
              <div className="flex overflow-x-auto border-b border-gray-800 gap-1 pb-1">
                {[
                  { id: 'vision', label: 'Vision & Innovation', icon: Lightbulb },
                  { id: 'council', label: 'AI Council Assessment', icon: ShieldCheck },
                  { id: 'graph', label: 'Capability Graph', icon: Globe },
                  { id: 'architecture', label: 'Service Arch', icon: Layers },
                  { id: 'db', label: 'Database DDL', icon: Database },
                  { id: 'api', label: 'APIs & Webhooks', icon: Cpu },
                  { id: 'workflow', label: 'Workflows', icon: Workflow },
                  { id: 'startup', label: 'Startup Strategy', icon: BarChart2 },
                  { id: 'cost', label: 'Costs & Servers', icon: DollarSign },
                  { id: 'code', label: 'Code Explorer & Sandbox', icon: Code }
                ].map((tab) => {
                  const Icon = tab.icon;
                  return (
                    <button
                      key={tab.id}
                      onClick={() => setActiveTab(tab.id)}
                      className={`flex items-center gap-2 px-4 py-2.5 text-xs font-bold rounded-lg border border-transparent whitespace-nowrap transition-all cursor-pointer ${
                        activeTab === tab.id
                          ? 'bg-blue-600/10 border-blue-500/30 text-blue-400 font-extrabold'
                          : 'text-gray-400 hover:text-gray-200 hover:bg-gray-900/50'
                      }`}
                    >
                      <Icon size={14} />
                      {tab.label}
                    </button>
                  );
                })}
              </div>

              {/* TAB CONTENT DETAIL */}
              <div className="space-y-6">
                
                {/* 1. VISION TAB */}
                {activeTab === 'vision' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 space-y-6">
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-lg font-bold text-white flex items-center gap-2 border-b border-gray-800 pb-2">
                          <BookOpen size={18} className="text-blue-500" />
                          Product Vision
                        </h3>
                        <p className="text-gray-300 leading-relaxed text-sm">
                          {blueprint.summary}
                        </p>
                        <div className="grid grid-cols-2 gap-4 pt-2">
                          <div className="bg-gray-950/40 p-4 rounded-xl border border-gray-900">
                            <span className="text-[10px] uppercase font-bold text-gray-500">Domain</span>
                            <p className="text-sm font-semibold text-gray-200 mt-1">{blueprint.intent.domain}</p>
                          </div>
                          <div className="bg-gray-950/40 p-4 rounded-xl border border-gray-900">
                            <span className="text-[10px] uppercase font-bold text-gray-500">Security Requirement</span>
                            <p className="text-sm font-semibold text-gray-200 mt-1">{blueprint.intent.security_level}</p>
                          </div>
                        </div>
                      </div>

                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-lg font-bold text-white flex items-center gap-2 border-b border-gray-800 pb-2">
                          <Lightbulb size={18} className="text-purple-400" />
                          30%+ Original Innovations ({blueprint.innovations.innovation_index})
                        </h3>
                        <div className="space-y-3">
                          {blueprint.innovations.innovations.map((inn: any, idx: number) => (
                            <div key={idx} className="p-3 bg-purple-950/10 rounded-xl border border-purple-500/10 space-y-1">
                              <span className="text-xs font-bold text-purple-400">{inn.feature}</span>
                              <p className="text-xs text-gray-300 leading-normal">{inn.description}</p>
                              <p className="text-[10px] text-gray-500 italic mt-1">Impact: {inn.impact}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>

                    <div className="space-y-6">
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Proprietary Genomes Matched
                        </h3>
                        <div className="flex flex-wrap gap-2">
                          {blueprint.genomes.matches.map((gen: string) => (
                            <span key={gen} className="px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold">
                              {gen} Genome
                            </span>
                          ))}
                        </div>
                      </div>

                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Open-Source Alternatives
                        </h3>
                        <div className="space-y-3">
                          {blueprint.oss.map((alt: any, idx: number) => (
                            <div key={idx} className="text-xs space-y-1">
                              <div className="flex justify-between font-bold">
                                <span className="text-gray-400">{alt.proprietary}</span>
                                <span className="text-gray-500">→</span>
                                <a 
                                  href={alt.url} 
                                  target="_blank" 
                                  rel="noopener noreferrer" 
                                  className="text-blue-400 hover:underline flex items-center gap-0.5"
                                >
                                  {alt.alternative}
                                  <ExternalLink size={10} />
                                </a>
                              </div>
                              <p className="text-gray-500 text-[10px] leading-tight">{alt.description}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* AI COUNCIL ASSESSMENT TAB */}
                {activeTab === 'council' && (
                  <div className="space-y-6">
                    {/* Overall Score Header Banner */}
                    <div className="glass-panel border border-gray-800 rounded-2xl p-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 shadow-xl">
                      <div className="space-y-2">
                        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold">
                          <ShieldCheck size={14} /> Multi-Agent Council Verdict: {blueprint.multi_agent?.grade || 'A+'}
                        </div>
                        <h3 className="text-2xl font-black text-white">Engineering Health & Governance Assessment</h3>
                        <p className="text-xs text-gray-400 max-w-2xl leading-relaxed">
                          {blueprint.multi_agent?.summary || "Evaluated by 4 AI Personas: Principal System Architect, FinOps Lead, Cybersecurity Officer, and UX Strategist."}
                        </p>
                      </div>

                      <div className="flex items-center gap-4 bg-gray-900/60 p-4 rounded-xl border border-gray-800">
                        <div className="text-center">
                          <div className="text-4xl font-black text-emerald-400">{blueprint.multi_agent?.overall_score || 95}</div>
                          <div className="text-[10px] text-gray-400 uppercase tracking-widest font-semibold">Health Score</div>
                        </div>
                        <div className="h-10 w-px bg-gray-800" />
                        <div className="text-center">
                          <div className="text-2xl font-bold text-white">{blueprint.multi_agent?.personae?.length || 4}</div>
                          <div className="text-[10px] text-gray-400 uppercase tracking-widest font-semibold">AI Personas</div>
                        </div>
                      </div>
                    </div>

                    {/* Personae Review Grid */}
                    <div className="grid md:grid-cols-2 gap-6">
                      {(blueprint.multi_agent?.personae || [
                        {
                          persona: "Principal System Architect",
                          avatar: "🏗️",
                          score: 96,
                          verdict: "APPROVED WITH OPTIMIZATIONS",
                          highlights: ["Modular microservices mesh handles scale spikes effectively."],
                          concerns: [{ severity: "WARNING", issue: "Single Point of Failure in Redis", recommendation: "Configure Sentinel or AWS ElastiCache Multi-AZ.", code_remediation: "redis_mode: sentinel" }]
                        },
                        {
                          persona: "FinOps & Cloud Cost Specialist",
                          avatar: "💰",
                          score: 92,
                          verdict: "HIGH COST EFFICIENCY",
                          highlights: ["Initial hosting burn under $20/mo."],
                          concerns: [{ severity: "CRITICAL", issue: "Token spikes on real-time summaries", recommendation: "Add rate-limiting middleware.", code_remediation: "@app.middleware('http')" }]
                        }
                      ]).map((persona: any, idx: number) => (
                        <div key={idx} className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4 shadow-lg hover:border-gray-700 transition-all flex flex-col justify-between">
                          <div className="space-y-3">
                            <div className="flex items-center justify-between border-b border-gray-800 pb-3">
                              <div className="flex items-center gap-2.5">
                                <span className="text-2xl">{persona.avatar}</span>
                                <div>
                                  <h4 className="text-sm font-bold text-white">{persona.persona}</h4>
                                  <span className="text-[10px] font-semibold text-gray-400">{persona.verdict}</span>
                                </div>
                              </div>
                              <span className="text-xs font-mono font-bold px-2.5 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400">
                                {persona.score}/100
                              </span>
                            </div>

                            {/* Highlights */}
                            <div className="space-y-1.5">
                              <span className="text-[10px] font-bold uppercase tracking-wider text-gray-500">Key Highlights</span>
                              {persona.highlights.map((hl: string, hIdx: number) => (
                                <div key={hIdx} className="flex items-start gap-2 text-xs text-gray-300">
                                  <CheckCircle size={13} className="text-emerald-400 shrink-0 mt-0.5" />
                                  <span>{hl}</span>
                                </div>
                              ))}
                            </div>

                            {/* Concerns & Code Fixes */}
                            {persona.concerns && persona.concerns.length > 0 && (
                              <div className="space-y-2 pt-2 border-t border-gray-900">
                                <span className="text-[10px] font-bold uppercase tracking-wider text-gray-500">Governance Findings</span>
                                {persona.concerns.map((concern: any, cIdx: number) => (
                                  <div key={cIdx} className="p-3 bg-gray-900/60 rounded-xl border border-gray-800 text-xs space-y-2">
                                    <div className="flex items-center justify-between">
                                      <span className={`text-[10px] font-extrabold px-2 py-0.5 rounded uppercase ${
                                        concern.severity === 'CRITICAL' ? 'bg-red-500/20 text-red-400 border border-red-500/30' :
                                        concern.severity === 'WARNING' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
                                        'bg-blue-500/20 text-blue-400 border border-blue-500/30'
                                      }`}>
                                        {concern.severity}
                                      </span>
                                      <span className="font-semibold text-gray-300 truncate max-w-[200px]">{concern.issue}</span>
                                    </div>
                                    <p className="text-gray-400 text-[11px] leading-relaxed">{concern.recommendation}</p>
                                    {concern.code_remediation && (
                                      <div className="p-2 bg-black/80 rounded-lg border border-gray-900 font-mono text-[10px] text-emerald-400 overflow-x-auto whitespace-pre">
                                        {concern.code_remediation}
                                      </div>
                                    )}
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 2. CAPABILITY GRAPH TAB */}
                {activeTab === 'graph' && (
                  <div className="space-y-4">
                    <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-2">
                      <h3 className="text-lg font-bold text-white flex items-center gap-2">
                        <Globe size={18} className="text-blue-500" />
                        Interactive Capability Graph
                      </h3>
                      <p className="text-xs text-gray-400">
                        Synthesized network connections indicating which capability blocks depend on, extend, or replace other service nodes.
                      </p>
                    </div>
                    <ArchitectureGraph graphData={blueprint.graph} />
                  </div>
                )}

                {/* 3. ARCHITECTURE TAB */}
                {activeTab === 'architecture' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                        Architecture Flowchart
                      </h3>
                      <pre className="p-4 bg-gray-950/60 border border-gray-900 rounded-xl overflow-auto text-xs text-gray-400 font-mono">
                        {blueprint.architecture.mermaid}
                      </pre>
                    </div>
                    <div className="space-y-6">
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Service Registry
                        </h3>
                        <div className="space-y-3">
                          {blueprint.architecture.services.map((srv: any, idx: number) => (
                            <div key={idx} className="text-xs space-y-1">
                              <span className="font-bold text-emerald-400">{srv.name}</span>
                              <div className="text-[10px] text-gray-500 font-mono">{srv.type}</div>
                              <p className="text-gray-400">{srv.responsibility}</p>
                            </div>
                          ))}
                        </div>
                      </div>

                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Decisions & Logic
                        </h3>
                        <p className="text-xs text-gray-400 whitespace-pre-line leading-relaxed">
                          {blueprint.architecture.reasoning}
                        </p>
                      </div>
                    </div>
                  </div>
                )}

                {/* 4. DATABASE TAB */}
                {activeTab === 'db' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                        PostgreSQL Schema Script (DDL)
                      </h3>
                      <pre className="p-4 bg-gray-950/60 border border-gray-900 rounded-xl overflow-auto text-xs text-blue-300 font-mono max-h-[400px]">
                        {blueprint.db.sql}
                      </pre>
                    </div>
                    <div className="space-y-6">
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Entity-Relationship Map
                        </h3>
                        <pre className="p-3 bg-gray-950/40 rounded-xl font-mono text-[11px] text-gray-400">
                          {blueprint.db.er_diagram}
                        </pre>
                      </div>
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Table Definitions
                        </h3>
                        <div className="space-y-3 overflow-y-auto max-h-[250px]">
                          {blueprint.db.tables.map((tbl: any, idx: number) => (
                            <div key={idx} className="text-xs space-y-1">
                              <span className="font-bold text-red-400">{tbl.name}</span>
                              <p className="text-[10px] text-gray-500 leading-normal">{tbl.description}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 5. API TAB */}
                {activeTab === 'api' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                        Endpoints Configuration
                      </h3>
                      <div className="space-y-3 overflow-y-auto max-h-[400px]">
                        {blueprint.apis.endpoints.map((ep: any, idx: number) => (
                          <div key={idx} className="p-3 bg-gray-900/40 border border-gray-900 rounded-xl text-xs space-y-2">
                            <div className="flex items-center gap-2">
                              <span className={`px-2 py-0.5 rounded font-mono text-[10px] font-extrabold ${
                                ep.method === 'POST' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' :
                                ep.method === 'GET' ? 'bg-blue-500/20 text-blue-400 border border-blue-500/30' :
                                'bg-purple-500/20 text-purple-400 border border-purple-500/30'
                              }`}>
                                {ep.method}
                              </span>
                              <span className="font-mono text-gray-200 font-semibold">{ep.path}</span>
                            </div>
                            <p className="text-gray-400 text-[11px]">{ep.description}</p>
                            {ep.request_body && (
                              <div className="text-[10px] text-gray-500">
                                <strong>Request:</strong> {JSON.stringify(ep.request_body)}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                    <div className="space-y-6">
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Webhooks Triggers
                        </h3>
                        <div className="space-y-3">
                          {blueprint.apis.webhooks.map((wh: any, idx: number) => (
                            <div key={idx} className="text-xs space-y-1">
                              <span className="font-bold text-purple-400">{wh.event}</span>
                              <p className="text-gray-400">{wh.description}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          Rate Limiting
                        </h3>
                        <div className="text-xs space-y-2">
                          <div className="flex justify-between"><span className="text-gray-500">Free Tier</span><span className="text-gray-300 font-mono">{blueprint.apis.rate_limiting.tier_free}</span></div>
                          <div className="flex justify-between"><span className="text-gray-500">Pro Tier</span><span className="text-gray-300 font-mono">{blueprint.apis.rate_limiting.tier_pro}</span></div>
                          <div className="flex justify-between"><span className="text-gray-500">Mechanism</span><span className="text-gray-300">{blueprint.apis.rate_limiting.algorithm}</span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 6. WORKFLOW TAB */}
                {activeTab === 'workflow' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                        WebSocket Session Sequence
                      </h3>
                      <pre className="p-4 bg-gray-950/60 border border-gray-900 rounded-xl overflow-auto text-xs text-gray-400 font-mono">
                        {blueprint.workflows.sequence_diagram}
                      </pre>
                    </div>
                    <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                        User Journeys
                      </h3>
                      <div className="space-y-4">
                        {blueprint.workflows.user_journeys.map((j: any, idx: number) => (
                          <div key={idx} className="text-xs space-y-1 border-l-2 border-blue-500 pl-3">
                            <span className="font-bold text-blue-400">{j.stage}</span>
                            <p className="text-gray-400 leading-normal mt-0.5">{j.actions}</p>
                            <span className="text-[10px] text-gray-500 font-mono">Duration: {j.duration}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {/* 7. STARTUP STRATEGY TAB */}
                {activeTab === 'startup' && (
                  <div className="space-y-6">
                    <div className="grid md:grid-cols-3 gap-6">
                      <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                          Investor Pitch Slides
                        </h3>
                        <div className="space-y-4">
                          {blueprint.startup.pitch_slides.map((slide: any) => (
                            <div key={slide.slide_num} className="p-4 bg-gray-900/40 border border-gray-900 rounded-xl space-y-2">
                              <span className="text-[10px] font-bold text-blue-400 uppercase tracking-widest">
                                Slide {slide.slide_num}: {slide.title}
                              </span>
                              <ul className="list-disc pl-4 space-y-1 text-xs text-gray-300">
                                {slide.bullets.map((b: string, i: number) => <li key={i}>{b}</li>)}
                              </ul>
                            </div>
                          ))}
                        </div>
                      </div>
                      <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                        <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                          SWOT Analysis
                        </h3>
                        <div className="grid grid-cols-2 gap-3 text-[10px]">
                          <div className="p-2.5 bg-green-950/10 border border-green-500/10 rounded-xl">
                            <span className="font-bold text-green-400">Strengths</span>
                            <ul className="list-disc pl-3 mt-1 space-y-1 text-gray-400">
                              {blueprint.startup.swot.strengths.slice(0,2).map((s: string, i: number) => <li key={i}>{s.substring(0, 45)}...</li>)}
                            </ul>
                          </div>
                          <div className="p-2.5 bg-red-950/10 border border-red-500/10 rounded-xl">
                            <span className="font-bold text-red-400">Weaknesses</span>
                            <ul className="list-disc pl-3 mt-1 space-y-1 text-gray-400">
                              {blueprint.startup.swot.weaknesses.slice(0,2).map((w: string, i: number) => <li key={i}>{w.substring(0, 45)}...</li>)}
                            </ul>
                          </div>
                          <div className="p-2.5 bg-blue-950/10 border border-blue-500/10 rounded-xl">
                            <span className="font-bold text-blue-400">Opportunities</span>
                            <ul className="list-disc pl-3 mt-1 space-y-1 text-gray-400">
                              {blueprint.startup.swot.opportunities.slice(0,2).map((o: string, i: number) => <li key={i}>{o.substring(0, 45)}...</li>)}
                            </ul>
                          </div>
                          <div className="p-2.5 bg-amber-950/10 border border-amber-500/10 rounded-xl">
                            <span className="font-bold text-amber-400">Threats</span>
                            <ul className="list-disc pl-3 mt-1 space-y-1 text-gray-400">
                              {blueprint.startup.swot.threats.slice(0,2).map((t: string, i: number) => <li key={i}>{t.substring(0, 45)}...</li>)}
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Pricing plans rows */}
                    <div className="grid md:grid-cols-3 gap-6">
                      {blueprint.startup.pricing.map((p: any, idx: number) => (
                        <div key={idx} className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-3 relative hover:border-blue-500/30 transition-all">
                          <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">{p.tier}</span>
                          <div className="text-2xl font-black text-white">{p.price}</div>
                          <p className="text-xs text-gray-400 leading-normal">{p.features}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 8. COSTS TAB */}
                {activeTab === 'cost' && (
                  <div className="grid md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-lg font-bold text-white border-b border-gray-800 pb-2">
                        Hosting Estimates (SaaS Scaling)
                      </h3>
                      <div className="space-y-4">
                        {blueprint.costs.hosting_tiers.map((tier: any, idx: number) => (
                          <div key={idx} className="p-4 bg-gray-900/40 border border-gray-900 rounded-xl text-xs space-y-2">
                            <span className="font-bold text-blue-400">{tier.scale}</span>
                            <div className="grid grid-cols-3 gap-2 text-gray-400">
                              <div><strong>Server:</strong> {tier.server}</div>
                              <div><strong>DB:</strong> {tier.database}</div>
                              <div><strong>Storage:</strong> {tier.storage}</div>
                            </div>
                            <div className="text-right font-bold text-white pt-1">
                              Estimate: {tier.total_estimate}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                    <div className="glass-panel border border-gray-800 rounded-2xl p-6 space-y-4">
                      <h3 className="text-md font-bold text-white border-b border-gray-800 pb-2">
                        Cost Optimizations
                      </h3>
                      <ul className="space-y-3 text-xs text-gray-400">
                        {blueprint.costs.optimizations.map((opt: string, i: number) => (
                          <li key={i} className="flex gap-2">
                            <span className="text-blue-400 font-bold">•</span>
                            <span>{opt}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                )}

                {/* 9. CODE EXPLORER TAB */}
                {activeTab === 'code' && (
                  <div className="space-y-4">
                    <div className="glass-panel border border-gray-800 rounded-2xl p-6 flex justify-between items-center shadow-lg">
                      <div className="space-y-1">
                        <h3 className="text-lg font-bold text-white flex items-center gap-2">
                          <Code size={18} className="text-blue-500" />
                          Synthesized Codebase Preview
                        </h3>
                        <p className="text-xs text-gray-400">
                          Complete directory architecture and files generated by the software genetics engine.
                        </p>
                      </div>
                      <a
                        href={`http://localhost:8000/api/v1/blueprints/${blueprint.id}/download`}
                        className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 font-bold text-xs text-white transition-all shadow-md cursor-pointer"
                      >
                        <Download size={14} />
                        <span>Download ZIP</span>
                      </a>
                    </div>
                    <CodePreview files={blueprint.files} />
                  </div>
                )}

              </div>
            </div>
          )}

        </div>
      </main>
    </div>
  );
}
