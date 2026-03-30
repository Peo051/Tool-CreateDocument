import { useReportStore } from '../../store/reportStore';

export default function Step1Type() {
  const { reportType, language, setReportType, setLanguage } = useReportStore();

  const reportTypes = [
    { value: 'project_report', label: 'Project Report', desc: 'Standard project documentation' },
    { value: 'thesis', label: 'Thesis', desc: 'Academic thesis or dissertation' },
    { value: 'technical_report', label: 'Technical Report', desc: 'Technical documentation' },
    { value: 'business_report', label: 'Business Report', desc: 'Business analysis report' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-semibold mb-4">Select Report Type</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {reportTypes.map((type) => (
            <button
              key={type.value}
              onClick={() => setReportType(type.value as any)}
              className={`p-4 border-2 rounded-lg text-left transition ${
                reportType === type.value
                  ? 'border-blue-600 bg-blue-50'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
            >
              <div className="font-semibold">{type.label}</div>
              <div className="text-sm text-gray-600 mt-1">{type.desc}</div>
            </button>
          ))}
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Language
        </label>
        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value as 'vi' | 'en')}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="vi">Vietnamese</option>
          <option value="en">English</option>
        </select>
      </div>
    </div>
  );
}
