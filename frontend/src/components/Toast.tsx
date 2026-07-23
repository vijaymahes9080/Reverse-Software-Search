'use client';

import React from 'react';
import { CheckCircle2, AlertCircle, Info, X } from 'lucide-react';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'info';
  onClose: () => void;
}

export default function Toast({ message, type = 'success', onClose }: ToastProps) {
  const getStyles = () => {
    switch (type) {
      case 'error':
        return 'bg-red-950/80 border-red-800 text-red-300';
      case 'info':
        return 'bg-blue-950/80 border-blue-800 text-blue-300';
      case 'success':
      default:
        return 'bg-emerald-950/80 border-emerald-800 text-emerald-300';
    }
  };

  const getIcon = () => {
    switch (type) {
      case 'error':
        return <AlertCircle size={16} className="text-red-400" />;
      case 'info':
        return <Info size={16} className="text-blue-400" />;
      case 'success':
      default:
        return <CheckCircle2 size={16} className="text-emerald-400" />;
    }
  };

  return (
    <div className={`fixed bottom-6 right-6 flex items-center gap-3 px-4 py-3 rounded-xl border shadow-2xl backdrop-blur-md text-xs font-semibold z-50 animate-bounce ${getStyles()}`}>
      {getIcon()}
      <span>{message}</span>
      <button onClick={onClose} className="hover:opacity-75 transition-opacity ml-2">
        <X size={14} />
      </button>
    </div>
  );
}
