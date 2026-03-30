import axios from 'axios';
import type { ReportConfig, ValidationResponse, JobStatus } from '../types/report';

const API_BASE = 'http://localhost:8000/api';

const client = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const api = {
  // Health check
  health: async () => {
    const response = await client.get('/health');
    return response.data;
  },

  // Validate config
  validate: async (config: ReportConfig): Promise<ValidationResponse> => {
    const response = await client.post<ValidationResponse>('/validate', { config });
    return response.data;
  },

  // Generate report
  generate: async (config: ReportConfig): Promise<JobStatus> => {
    const response = await client.post<JobStatus>('/generate', { config });
    return response.data;
  },

  // Get job status
  getJobStatus: async (jobId: string): Promise<JobStatus> => {
    const response = await client.get<JobStatus>(`/jobs/${jobId}`);
    return response.data;
  },

  // Download report
  downloadReport: (fileId: string): string => {
    return `${API_BASE}/download/${fileId}`;
  },

  // Import config (supports legacy)
  importConfig: async (config: any): Promise<ReportConfig> => {
    const response = await client.post<ReportConfig>('/import-config', config);
    return response.data;
  },
};
