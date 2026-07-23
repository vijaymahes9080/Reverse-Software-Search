'use client';

import React, { useMemo } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  Handle,
  Position,
  NodeProps,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

// Custom Node component for beautiful rendering
function CustomNode({ data }: NodeProps) {
  const getCategoryColor = (category?: string) => {
    switch (category?.toLowerCase()) {
      case 'ui/ux':
        return 'border-sky-500 text-sky-400 bg-sky-950/40';
      case 'backend':
        return 'border-emerald-500 text-emerald-400 bg-emerald-950/40';
      case 'storage':
        return 'border-rose-500 text-rose-400 bg-rose-950/40';
      case 'authentication':
        return 'border-purple-500 text-purple-400 bg-purple-950/40';
      case 'general':
      default:
        return 'border-amber-500 text-amber-400 bg-amber-950/40';
    }
  };

  return (
    <div className={`px-4 py-3 shadow-lg rounded-xl border-2 glass-card min-w-[200px] text-left transition-all ${getCategoryColor(data.category as string)}`}>
      <Handle type="target" position={Position.Top} className="!bg-border" />
      
      <div className="text-[10px] uppercase font-bold tracking-wider opacity-60 mb-0.5">
        {data.category as string || 'Module'}
      </div>
      <div className="text-sm font-bold text-gray-100 mb-1">
        {data.label as string}
      </div>
      {Boolean(data.description) && (
        <p className="text-[10px] text-gray-400 leading-normal max-w-[190px]">
          {String(data.description)}
        </p>
      )}

      <Handle type="source" position={Position.Bottom} className="!bg-border" />
    </div>
  );
}

interface ArchitectureGraphProps {
  graphData: {
    nodes: any[];
    edges: any[];
  };
}

export default function ArchitectureGraph({ graphData }: ArchitectureGraphProps) {
  const nodeTypes = useMemo(() => ({ customNode: CustomNode }), []);

  if (!graphData || !graphData.nodes || graphData.nodes.length === 0) {
    return (
      <div className="flex h-[400px] w-full items-center justify-center rounded-xl bg-gray-900/30 border border-gray-800">
        <p className="text-gray-500">No architecture graph data available.</p>
      </div>
    );
  }

  return (
    <div className="h-[500px] w-full border border-gray-800 rounded-xl bg-gray-950/50 overflow-hidden relative shadow-inner">
      <ReactFlow
        nodes={graphData.nodes}
        edges={graphData.edges}
        nodeTypes={nodeTypes}
        fitView
        className="text-gray-200"
      >
        <Background color="#374151" gap={16} size={1} />
        <Controls className="!bg-gray-900 !border-gray-800 !text-gray-200 fill-white" />
        <MiniMap 
          nodeColor="#1f2937" 
          maskColor="rgba(3, 7, 18, 0.7)"
          className="!bg-gray-900 !border-gray-800"
        />
      </ReactFlow>
    </div>
  );
}
