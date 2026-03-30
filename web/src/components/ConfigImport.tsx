import { useRef } from 'react';
import { useReportStore } from '../store/reportStore';
import { api } from '../api/client';

export default function ConfigImport() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { toConfig, fromConfig } = useReportStore();

  const handleImport = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    try {
      const text = await file.text();
      const json = JSON.parse(text);
      
      // Try to import through API (handles legacy format)
      const normalized = await api.importConfig(json);
      fromConfig(normalized);
      
      alert('Config imported successfully!');
    } catch (error) {
      alert(`Failed to import config: ${error}`);
    }
    
    // Reset input
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleExport = () => {
    const config = toConfig();
    const blob = new Blob([JSON.stringify(config, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'report-config.json';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="flex gap-4 justify-end">
      <input
        ref={fileInputRef}
        type="file"
        accept=".json"
        onChange={handleImport}
        className="hidden"
      />
      <button
        onClick={() => fileInputRef.current?.click()}
        className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
      >
        Import Config
      </button>
      <button
        onClick={handleExport}
        className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
      >
        Export Config
      </button>
    </div>
  );
}
