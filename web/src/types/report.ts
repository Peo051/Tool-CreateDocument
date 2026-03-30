// TypeScript types matching backend config_models.py

export interface Author {
  name: string;
  id?: string;
  email?: string;
  role?: string;
}

export interface ProjectInfo {
  title: string;
  subtitle?: string;
  description: string;
  students: Author[];
  advisor?: string;
  university?: string;
  organization?: string;
  faculty?: string;
  class?: string;
  github_repo?: string;
  demo_url?: string;
  keywords?: string[];
}

export interface ReportProfile {
  report_type: 'thesis' | 'technical_report' | 'project_report' | 'business_report';
  language: 'vi' | 'en';
  target_pages?: number;
}

export interface ContentRequirements {
  include_cover?: boolean;
  include_acknowledgment?: boolean;
  include_commitment?: boolean;
  include_toc?: boolean;
  include_references?: boolean;
  custom_sections?: string[];
}

export interface Algorithm {
  name: string;
  category?: string;
  complexity?: string;
}

export interface TechnicalData {
  algorithms?: string[];
  technologies?: string[];
  datasets?: string[];
  algorithm_details?: Algorithm[];
}

export interface Chart {
  id: string;
  title: string;
  type: 'bar' | 'line' | 'pie' | 'scatter';
  data?: any;
}

export interface Table {
  id: string;
  title: string;
  headers: string[];
  rows: any[][];
}

export interface Figure {
  id: string;
  title: string;
  path: string;
  caption?: string;
}

export interface Reference {
  id: string;
  authors: string[];
  title: string;
  year: number;
  source?: string;
  url?: string;
}

export interface Evidence {
  charts?: Chart[];
  tables?: Table[];
  figures?: Figure[];
  references?: Reference[];
}

export interface FormatRules {
  citation_style?: 'APA' | 'IEEE' | 'MLA' | 'Chicago';
  font_name?: string;
  font_size?: number;
  line_spacing?: number;
  margin_left?: number;
  margin_right?: number;
  margin_top?: number;
  margin_bottom?: number;
}

export interface ReportConfig {
  project_info: ProjectInfo;
  report_profile: ReportProfile;
  content_requirements?: ContentRequirements;
  technical_data?: TechnicalData;
  evidence?: Evidence;
  format_rules?: FormatRules;
  version?: string;
  created_at?: string;
}

// API Response Types
export interface ValidationResponse {
  valid: boolean;
  errors: string[];
  warnings: string[];
}

export interface JobStatus {
  job_id: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  progress: number;
  message: string;
  file_id?: string;
  error?: string;
  created_at: string;
  updated_at: string;
}
