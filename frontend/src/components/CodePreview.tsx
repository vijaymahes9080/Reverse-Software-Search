'use client';

import React, { useState } from 'react';
import { File, Folder, FolderOpen, Copy, Check } from 'lucide-react';

interface CodePreviewProps {
  files: Record<str, string>;
}

export default function CodePreview({ files }: CodePreviewProps) {
  const filePaths = Object.keys(files);
  const [selectedFile, setSelectedFile] = useState<string>(filePaths[0] || '');
  const [copied, setCopied] = useState(false);

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
                onClick={() => setSelectedFile(file.fullPath)}
                className={`flex items-center gap-2 py-1 text-sm w-full text-left transition-colors pl-2 rounded-md ${
                  selectedFile === file.fullPath
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
        <h4 className="text-xs font-bold uppercase tracking-wider text-gray-500 mb-3 pl-2">
          Repository Files
        </h4>
        <div className="space-y-1">
          {Object.keys(folderTree.dirs).map((dirName) =>
            renderFolder(dirName, folderTree.dirs[dirName])
          )}
          {folderTree.files.map((file: any) => (
            <button
              key={file.fullPath}
              onClick={() => setSelectedFile(file.fullPath)}
              className={`flex items-center gap-2 py-1 text-sm w-full text-left pl-2 rounded-md transition-colors ${
                selectedFile === file.fullPath
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

      {/* Code Editor Window */}
      <div className="flex-1 flex flex-col bg-[#090d16] min-w-0">
        {/* Editor Tab Header */}
        <div className="flex items-center justify-between px-4 py-2 border-b border-gray-800 bg-gray-950">
          <div className="flex items-center gap-2">
            <span className="text-xs font-mono text-gray-400 truncate max-w-[300px]">
              {selectedFile || 'no active file'}
            </span>
          </div>
          <button
            onClick={handleCopy}
            disabled={!selectedFile}
            className="flex items-center gap-1.5 px-2 py-1 text-xs rounded-md bg-gray-900 border border-gray-800 hover:bg-gray-800 text-gray-300 hover:text-white transition-all cursor-pointer"
          >
            {copied ? (
              <>
                <Check size={12} className="text-green-400" />
                <span className="text-green-400 font-semibold">Copied!</span>
              </>
            ) : (
              <>
                <Copy size={12} />
                <span>Copy Code</span>
              </>
            )}
          </button>
        </div>

        {/* Editor Code Pane */}
        <div className="flex-1 p-4 font-mono text-xs overflow-auto leading-relaxed relative">
          <pre className="text-gray-300 flex">
            {/* Mock line numbers */}
            <div className="text-gray-600 text-right pr-4 select-none border-r border-gray-900 mr-4">
              {fileContent.split('\n').map((_, index) => (
                <div key={index}>{index + 1}</div>
              ))}
            </div>
            {/* Code content */}
            <code className="block flex-1 text-left select-text whitespace-pre">
              {fileContent}
            </code>
          </pre>
        </div>
      </div>
    </div>
  );
}
