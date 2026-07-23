'use client';

import React, { useState } from 'react';
import { File, Folder, FolderOpen, Copy, Check, Play, Terminal, Cpu, RefreshCw, CheckCircle2 } from 'lucide-react';

interface CodePreviewProps {
  files: Record<string, string>;
}

export default function CodePreview({ files }: CodePreviewProps) {
  const filePaths = Object.keys(files);
  const [selectedFile, setSelectedFile] = useState<string>(filePaths[0] || '');
  const [copied, setCopied] = useState(false);
  const [activeView, setActiveView] = useState<'editor' | 'sandbox'>('editor');
  const [isRunning, setIsRunning] = useState(false);
  const [logs, setLogs] = useState<string[]>([
    "[Sandbox] Virtual WebContainer engine initialized.",
    "[Sandbox] Ready to simulate application runtime execution."
  ]);

  // Group files into folder structure
  const folderTree = React.useMemo(() => {
    const root: Record<string, any> = { files: [], dirs: {} };
    filePaths.forEach((path) => {
      const parts = path.split('/');
      let current = root;
      for (let i = 0; i < parts.length; i++) {
        const part = parts[i];
        if (i === parts.length - 1) {
          current.files.push({ name: part, fullPath: path });
        } else {
          if (!current.dirs[part]) {
            current.dirs[part] = { files: [], dirs: {} };
          }
          current = current.dirs[part];
        }
      }
    });
    return root;
  }, [filePaths]);

  const handleCopy = () => {
    if (!selectedFile) return;
    navigator.clipboard.writeText(files[selectedFile]);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const runSandboxExecution = () => {
    setIsRunning(true);
    setLogs((prev) => [
      ...prev,
      `[Run] Spawning Node.js v20 runtime process...`,
      `[Run] Mounting virtual workspace files (${filePaths.length} files)...`,
      `[Build] Compiling dependencies... Done (0.84s).`,
      `[Server] Starting FastAPI backend on http://localhost:8000 ...`,
      `[Server] Next.js dev server listening on http://localhost:3000 ...`,
      `[Health] Application status: ONLINE - HTTP 200 OK`
    ]);
    setTimeout(() => {
      setIsRunning(false);
    }, 1200);
  };

  // Recursive folder renderer
  const renderFolder = (name: string, folder: any, depth: number = 0) => {
    const [isOpen, setIsOpen] = useState(true);

    return (
      <div key={name} style={{ paddingLeft: `${depth * 8}px` }}>
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="flex items-center gap-2 py-1 text-sm text-gray-300 hover:text-white transition-colors w-full text-left"
        >
          {isOpen ? <FolderOpen size={16} className="text-yellow-500" /> : <Folder size={16} className="text-yellow-600" />}
          <span className="font-medium truncate">{name}</span>
        </button>

        {isOpen && (
          <div className="border-l border-gray-800 ml-2 pl-2">
            {Object.keys(folder.dirs).map((dirName) =>
              renderFolder(dirName, folder.dirs[dirName], depth + 1)
            )}
            {folder.files.map((file: any) => (
              <button
                key={file.fullPath}
                onClick={() => {
                  setSelectedFile(file.fullPath);
                  setActiveView('editor');
                }}
                className={`flex items-center gap-2 py-1 text-sm w-full text-left transition-colors pl-2 rounded-md ${
                  selectedFile === file.fullPath && activeView === 'editor'
                    ? 'bg-blue-600/20 text-blue-400 font-semibold'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
              >
                <File size={14} className={selectedFile === file.fullPath ? 'text-blue-400' : 'text-gray-500'} />
                <span className="truncate">{file.name}</span>
              </button>
            ))}
          </div>
        )}
      </div>
    );
  };

  const fileContent = selectedFile ? files[selectedFile] : '// Select a file from the explorer';

  return (
    <div className="flex border border-gray-800 rounded-xl bg-gray-950 overflow-hidden h-[550px] shadow-2xl">
      {/* File Explorer Sidebar */}
      <div className="w-64 border-r border-gray-800 bg-gray-950/80 p-4 overflow-y-auto select-none">
        <div className="flex items-center justify-between mb-3 pl-2">
          <h4 className="text-xs font-bold uppercase tracking-wider text-gray-500">
            Repository Files
          </h4>
          <span className="text-[10px] bg-blue-500/10 text-blue-400 px-1.5 py-0.5 rounded font-mono">
            {filePaths.length} files
          </span>
        </div>
        <div className="space-y-1">
          {Object.keys(folderTree.dirs).map((dirName) =>
            renderFolder(dirName, folderTree.dirs[dirName])
          )}
          {folderTree.files.map((file: any) => (
            <button
              key={file.fullPath}
              onClick={() => {
                setSelectedFile(file.fullPath);
                setActiveView('editor');
              }}
              className={`flex items-center gap-2 py-1 text-sm w-full text-left pl-2 rounded-md transition-colors ${
                selectedFile === file.fullPath && activeView === 'editor'
                  ? 'bg-blue-600/20 text-blue-400 font-semibold'
                  : 'text-gray-400 hover:text-gray-200'
              }`}
            >
              <File size={14} className={selectedFile === file.fullPath ? 'text-blue-400' : 'text-gray-500'} />
              <span className="truncate">{file.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Main Code Editor & Sandbox Area */}
      <div className="flex-1 flex flex-col bg-[#090d16] min-w-0">
        {/* Top Header Controls */}
        <div className="flex items-center justify-between px-4 py-2 border-b border-gray-800 bg-gray-950">
          <div className="flex items-center gap-2">
            <button
              onClick={() => setActiveView('editor')}
              className={`px-3 py-1 text-xs rounded-md font-medium transition-all ${
                activeView === 'editor'
                  ? 'bg-gray-800 text-white shadow-sm'
                  : 'text-gray-400 hover:text-gray-200'
              }`}
            >
              Code Editor
            </button>
            <button
              onClick={() => setActiveView('sandbox')}
              className={`flex items-center gap-1.5 px-3 py-1 text-xs rounded-md font-medium transition-all ${
                activeView === 'sandbox'
                  ? 'bg-emerald-950/80 border border-emerald-800 text-emerald-400 shadow-sm'
                  : 'text-gray-400 hover:text-emerald-400'
              }`}
            >
              <Terminal size={12} />
              <span>Live WebContainer Sandbox</span>
            </button>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={runSandboxExecution}
              disabled={isRunning}
              className="flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-md bg-emerald-600 hover:bg-emerald-500 text-white font-medium shadow transition-all cursor-pointer disabled:opacity-50"
            >
              {isRunning ? (
                <>
                  <RefreshCw size={12} className="animate-spin" />
                  <span>Running...</span>
                </>
              ) : (
                <>
                  <Play size={12} />
                  <span>Run Sandbox</span>
                </>
              )}
            </button>
            <button
              onClick={handleCopy}
              disabled={!selectedFile}
              className="flex items-center gap-1.5 px-2.5 py-1 text-xs rounded-md bg-gray-900 border border-gray-800 hover:bg-gray-800 text-gray-300 hover:text-white transition-all cursor-pointer"
            >
              {copied ? (
                <>
                  <Check size={12} className="text-green-400" />
                  <span className="text-green-400 font-semibold">Copied!</span>
                </>
              ) : (
                <>
                  <Copy size={12} />
                  <span>Copy File</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* Editor Body */}
        {activeView === 'editor' ? (
          <div className="flex-1 p-4 font-mono text-xs overflow-auto leading-relaxed relative">
            <pre className="text-gray-300 flex">
              <div className="text-gray-600 text-right pr-4 select-none border-r border-gray-900 mr-4">
                {fileContent.split('\n').map((_, index) => (
                  <div key={index}>{index + 1}</div>
                ))}
              </div>
              <code className="block flex-1 text-left select-text whitespace-pre">
                {fileContent}
              </code>
            </pre>
          </div>
        ) : (
          /* Live Terminal Sandbox Body */
          <div className="flex-1 flex flex-col p-4 bg-black/90 font-mono text-xs overflow-auto">
            <div className="flex items-center justify-between text-gray-500 border-b border-gray-900 pb-2 mb-3">
              <span className="flex items-center gap-2">
                <Cpu size={14} className="text-emerald-500" />
                <span className="text-emerald-400 font-semibold">Virtual Node.js Sandbox Terminal</span>
              </span>
              <span className="text-[10px] text-gray-600">PORT 8000 / 3000 ACTIVE</span>
            </div>
            <div className="space-y-1.5 flex-1 overflow-y-auto font-mono text-emerald-400/90 leading-relaxed">
              {logs.map((log, index) => (
                <div key={index} className="flex items-start gap-2">
                  <span className="text-gray-600 select-none">&gt;</span>
                  <span>{log}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
