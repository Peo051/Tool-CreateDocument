import { useState, useEffect } from 'react';
import { useReportStore } from '../../store/reportStore';
import { api } from '../../api/client';
import type { JobStatus } from '../../types/report';

export default function Step7Export() {
  const { toConfig, validationErrors } = useReportStore();
  const [jobStatus, setJobStatus] = useState<JobStatus | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let interval: ReturnType<typeof setInterval>;

    if (jobStatus && jobStatus.status === 'running') {
      interval = setInterval(async () => {
        try {
          const status = await api.getJobStatus(jobStatus.job_id);
          setJobStatus(status);

          if (status.status === 'completed' || status.status === 'failed') {
            clearInterval(interval);
            setIsGenerating(false);
          }
        } catch (err) {
          console.error('Failed to fetch job status:', err);
        }
      }, 2000);
    }

    return () => {
      if (interval) clearInterval(interval);
    };
  }, [jobStatus]);

  const handleGenerate = async () => {
    if (validationErrors.length > 0) {
      setError('Please fix validation errors before generating');
      return;
    }

    setIsGenerating(true);
    setError(null);

    try {
      const config = toConfig();
      const job = await api.generate(config);
      setJobStatus(job);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to start generation');
      setIsGenerating(false);
    }
  };

  const handleDownload = () => {
    if (jobStatus?.file_id) {
      window.open(api.downloadReport(jobStatus.file_id), '_blank');
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed':
        return 'bg-green-50 border-green-200 text-green-900';
      case 'failed':
        return 'bg-red-50 border-red-200 text-red-900';
      case 'running':
        return 'bg-blue-50 border-blue-200 text-blue-900';
      default:
        return 'bg-gray-50 border-gray-200 text-gray-900';
    }
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Generate Report</h2>

      {!jobStatus && (
        <div>
          <button
            onClick={handleGenerate}
            disabled={isGenerating || validationErrors.length > 0}
            className="w-full px-6 py-3 bg-green-600 text-white rounded-md hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isGenerating ? 'Starting Generation...' : 'Generate Report'}
          </button>

          {validationErrors.length > 0 && (
            <p className="text-sm text-red-600 mt-2">
              Please go back and fix validation errors first.
            </p>
          )}
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-900">{error}</p>
        </div>
      )}

      {jobStatus && (
        <div className={`border rounded-lg p-4 ${getStatusColor(jobStatus.status)}`}>
          <div className="flex justify-between items-start mb-3">
            <div>
              <h3 className="font-medium">Job Status</h3>
              <p className="text-sm opacity-75">ID: {jobStatus.job_id}</p>
            </div>
            <span className="px-3 py-1 bg-white rounded-full text-sm font-medium">
              {jobStatus.status.toUpperCase()}
            </span>
          </div>

          <div className="space-y-2">
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span>Progress</span>
                <span>{jobStatus.progress}%</span>
              </div>
              <div className="w-full bg-white rounded-full h-2">
                <div
                  className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${jobStatus.progress}%` }}
                />
              </div>
            </div>

            <p className="text-sm">{jobStatus.message}</p>

            {jobStatus.error && (
              <div className="bg-white bg-opacity-50 rounded p-2 text-sm">
                <strong>Error:</strong> {jobStatus.error}
              </div>
            )}
          </div>

          {jobStatus.status === 'completed' && jobStatus.file_id && (
            <button
              onClick={handleDownload}
              className="mt-4 w-full px-6 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700"
            >
              Download Report
            </button>
          )}

          {jobStatus.status === 'failed' && (
            <button
              onClick={() => {
                setJobStatus(null);
                setError(null);
              }}
              className="mt-4 w-full px-6 py-3 bg-gray-600 text-white rounded-md hover:bg-gray-700"
            >
              Try Again
            </button>
          )}
        </div>
      )}

      <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
        <h3 className="font-medium mb-2">What happens next?</h3>
        <ol className="list-decimal list-inside space-y-1 text-sm text-gray-700">
          <li>Configuration will be validated</li>
          <li>Report outline will be planned</li>
          <li>Content will be generated for each section</li>
          <li>Evidence and references will be bound</li>
          <li>Final DOCX file will be rendered</li>
          <li>Quality review will be performed</li>
        </ol>
      </div>
    </div>
  );
}
