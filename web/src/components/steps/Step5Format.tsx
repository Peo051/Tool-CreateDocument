import { useReportStore } from '../../store/reportStore';

export default function Step5Format() {
  const {
    citationStyle, fontSize, lineSpacing,
    setCitationStyle, setFontSize, setLineSpacing
  } = useReportStore();

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Format Options</h2>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Citation Style
        </label>
        <select
          value={citationStyle}
          onChange={(e) => setCitationStyle(e.target.value as any)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="IEEE">IEEE</option>
          <option value="APA">APA</option>
          <option value="MLA">MLA</option>
          <option value="Chicago">Chicago</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Font Size: {fontSize}pt
        </label>
        <input
          type="range"
          min="8"
          max="20"
          value={fontSize}
          onChange={(e) => setFontSize(parseInt(e.target.value))}
          className="w-full"
        />
        <div className="flex justify-between text-xs text-gray-500">
          <span>8pt</span>
          <span>20pt</span>
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Line Spacing: {lineSpacing}
        </label>
        <input
          type="range"
          min="1.0"
          max="3.0"
          step="0.1"
          value={lineSpacing}
          onChange={(e) => setLineSpacing(parseFloat(e.target.value))}
          className="w-full"
        />
        <div className="flex justify-between text-xs text-gray-500">
          <span>1.0</span>
          <span>3.0</span>
        </div>
      </div>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <h3 className="font-medium text-blue-900 mb-2">Preview</h3>
        <div className="text-sm text-blue-800">
          <p>Citation Style: {citationStyle}</p>
          <p>Font Size: {fontSize}pt</p>
          <p>Line Spacing: {lineSpacing}</p>
        </div>
      </div>
    </div>
  );
}
