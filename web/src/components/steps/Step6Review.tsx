import { useState } from 'react';
import { useReportStore } from '../../store/reportStore';
import { api } from '../../api/client';

export default function Step6Review() {
  const {
    toConfig,
    validationErrors,
    validationWarnings,
    setValidationErrors,
    setValidationWarnings,
  } = useReportStore();

  const [isValidating, setIsValidating] = useState(false);
  const [validated, setValidated] = useState(false);

  const handleValidate = async () => {
    setIsValidating(true);
    setValidated(false);

    try {
      const config = toConfig();
      const result = await api.validate(config);

      setValidationErrors(result.errors);
      setValidationWarnings(result.warnings);
      setValidated(true);
    } catch (error) {
      setValidationErrors([`Validation failed: ${error}`]);
    } finally {
      setIsValidating(false);
    }
  };

  const config = toConfig();

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Review Configuration</h2>

      <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
        <h3 className="font-medium mb-3">Summary</h3>
        <dl className="space-y-2 text-sm">
          <div className="flex">
            <dt className="font-medium w-32">Report Type:</dt>
            <dd className="text-gray-700">{config.report_profile.report_type}</dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">Language:</dt>
            <dd className="text-gray-700">{config.report_profile.language}</dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">Title:</dt>
            <dd className="text-gray-700">{config.project_info.title || '(not set)'}</dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">Students:</dt>
            <dd className="text-gray-700">
              {config.project_info.students.filter(s => s.name).length} student(s)
            </dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">Algorithms:</dt>
            <dd className="text-gray-700">
              {config.technical_data?.algorithms?.length || 0} algorithm(s)
            </dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">References:</dt>
            <dd className="text-gray-700">
              {config.evidence?.references?.length || 0} reference(s)
            </dd>
          </div>
          <div className="flex">
            <dt className="font-medium w-32">Citation Style:</dt>
            <dd className="text-gray-700">{config.format_rules?.citation_style}</dd>
          </div>
        </dl>
      </div>

      <div>
        <button
          onClick={handleValidate}
          disabled={isValidating}
          className="w-full px-6 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
        >
          {isValidating ? 'Validating...' : 'Validate Configuration'}
        </button>
      </div>

      {validated && (
        <div className="space-y-3">
          {validationErrors.length === 0 && validationWarnings.length === 0 && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <div className="flex items-center">
                <span className="text-green-600 text-xl mr-2">✓</span>
                <span className="font-medium text-green-900">
                  Configuration is valid! Ready to generate.
                </span>
              </div>
            </div>
          )}

          {validationErrors.length > 0 && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <h4 className="font-medium text-red-900 mb-2">Errors</h4>
              <ul className="list-disc list-inside space-y-1 text-sm text-red-800">
                {validationErrors.map((error, i) => (
                  <li key={i}>{error}</li>
                ))}
              </ul>
            </div>
          )}

          {validationWarnings.length > 0 && (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
              <h4 className="font-medium text-yellow-900 mb-2">Warnings</h4>
              <ul className="list-disc list-inside space-y-1 text-sm text-yellow-800">
                {validationWarnings.map((warning, i) => (
                  <li key={i}>{warning}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      {validated && validationErrors.length === 0 && (
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
          <p className="text-sm text-blue-800">
            Click "Next" to proceed to report generation.
          </p>
        </div>
      )}
    </div>
  );
}
