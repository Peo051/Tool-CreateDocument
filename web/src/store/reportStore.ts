import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { ReportConfig, Author } from '../types/report';

interface ReportState {
  // Form data
  reportType: 'thesis' | 'technical_report' | 'project_report' | 'business_report';
  language: 'vi' | 'en';
  title: string;
  subtitle: string;
  description: string;
  students: Author[];
  advisor: string;
  university: string;
  organization: string;
  faculty: string;
  className: string;
  githubRepo: string;
  demoUrl: string;
  keywords: string[];
  algorithms: string[];
  technologies: string[];
  datasets: string[];
  references: any[];
  citationStyle: 'APA' | 'IEEE' | 'MLA' | 'Chicago';
  fontSize: number;
  lineSpacing: number;
  
  // UI state
  currentStep: number;
  validationErrors: string[];
  validationWarnings: string[];
  
  // Actions
  setReportType: (type: ReportState['reportType']) => void;
  setLanguage: (lang: ReportState['language']) => void;
  setTitle: (title: string) => void;
  setSubtitle: (subtitle: string) => void;
  setDescription: (desc: string) => void;
  setStudents: (students: Author[]) => void;
  setAdvisor: (advisor: string) => void;
  setUniversity: (university: string) => void;
  setOrganization: (org: string) => void;
  setFaculty: (faculty: string) => void;
  setClassName: (className: string) => void;
  setGithubRepo: (repo: string) => void;
  setDemoUrl: (url: string) => void;
  setKeywords: (keywords: string[]) => void;
  setAlgorithms: (algorithms: string[]) => void;
  setTechnologies: (technologies: string[]) => void;
  setDatasets: (datasets: string[]) => void;
  setReferences: (references: any[]) => void;
  setCitationStyle: (style: ReportState['citationStyle']) => void;
  setFontSize: (size: number) => void;
  setLineSpacing: (spacing: number) => void;
  setCurrentStep: (step: number) => void;
  setValidationErrors: (errors: string[]) => void;
  setValidationWarnings: (warnings: string[]) => void;
  nextStep: () => void;
  prevStep: () => void;
  reset: () => void;
  
  // Config conversion
  toConfig: () => ReportConfig;
  fromConfig: (config: ReportConfig) => void;
}

const initialState = {
  reportType: 'project_report' as const,
  language: 'vi' as const,
  title: '',
  subtitle: '',
  description: '',
  students: [{ name: '', id: '' }],
  advisor: '',
  university: '',
  organization: '',
  faculty: '',
  className: '',
  githubRepo: '',
  demoUrl: '',
  keywords: [],
  algorithms: [],
  technologies: [],
  datasets: [],
  references: [],
  citationStyle: 'IEEE' as const,
  fontSize: 13,
  lineSpacing: 1.5,
  currentStep: 1,
  validationErrors: [],
  validationWarnings: [],
};

export const useReportStore = create<ReportState>()(
  persist(
    (set, get) => ({
      ...initialState,
      
      setReportType: (reportType) => set({ reportType }),
      setLanguage: (language) => set({ language }),
      setTitle: (title) => set({ title }),
      setSubtitle: (subtitle) => set({ subtitle }),
      setDescription: (description) => set({ description }),
      setStudents: (students) => set({ students }),
      setAdvisor: (advisor) => set({ advisor }),
      setUniversity: (university) => set({ university }),
      setOrganization: (organization) => set({ organization }),
      setFaculty: (faculty) => set({ faculty }),
      setClassName: (className) => set({ className }),
      setGithubRepo: (githubRepo) => set({ githubRepo }),
      setDemoUrl: (demoUrl) => set({ demoUrl }),
      setKeywords: (keywords) => set({ keywords }),
      setAlgorithms: (algorithms) => set({ algorithms }),
      setTechnologies: (technologies) => set({ technologies }),
      setDatasets: (datasets) => set({ datasets }),
      setReferences: (references) => set({ references }),
      setCitationStyle: (citationStyle) => set({ citationStyle }),
      setFontSize: (fontSize) => set({ fontSize }),
      setLineSpacing: (lineSpacing) => set({ lineSpacing }),
      setCurrentStep: (currentStep) => set({ currentStep }),
      setValidationErrors: (validationErrors) => set({ validationErrors }),
      setValidationWarnings: (validationWarnings) => set({ validationWarnings }),
      
      nextStep: () => set((state) => ({ currentStep: Math.min(state.currentStep + 1, 7) })),
      prevStep: () => set((state) => ({ currentStep: Math.max(state.currentStep - 1, 1) })),
      
      reset: () => set(initialState),
      
      toConfig: (): ReportConfig => {
        const state = get();
        return {
          project_info: {
            title: state.title,
            subtitle: state.subtitle || undefined,
            description: state.description,
            students: state.students.filter(s => s.name),
            advisor: state.advisor || undefined,
            university: state.university || undefined,
            organization: state.organization || undefined,
            faculty: state.faculty || undefined,
            class: state.className || undefined,
            github_repo: state.githubRepo || undefined,
            demo_url: state.demoUrl || undefined,
            keywords: state.keywords,
          },
          report_profile: {
            report_type: state.reportType,
            language: state.language,
          },
          technical_data: {
            algorithms: state.algorithms,
            technologies: state.technologies,
            datasets: state.datasets,
          },
          evidence: {
            references: state.references,
          },
          format_rules: {
            citation_style: state.citationStyle,
            font_size: state.fontSize,
            line_spacing: state.lineSpacing,
          },
        };
      },
      
      fromConfig: (config: ReportConfig) => {
        set({
          reportType: config.report_profile.report_type,
          language: config.report_profile.language,
          title: config.project_info.title,
          subtitle: config.project_info.subtitle || '',
          description: config.project_info.description,
          students: config.project_info.students.length > 0 ? config.project_info.students : [{ name: '', id: '' }],
          advisor: config.project_info.advisor || '',
          university: config.project_info.university || '',
          organization: config.project_info.organization || '',
          faculty: config.project_info.faculty || '',
          className: config.project_info.class || '',
          githubRepo: config.project_info.github_repo || '',
          demoUrl: config.project_info.demo_url || '',
          keywords: config.project_info.keywords || [],
          algorithms: config.technical_data?.algorithms || [],
          technologies: config.technical_data?.technologies || [],
          datasets: config.technical_data?.datasets || [],
          references: config.evidence?.references || [],
          citationStyle: config.format_rules?.citation_style || 'IEEE',
          fontSize: config.format_rules?.font_size || 13,
          lineSpacing: config.format_rules?.line_spacing || 1.5,
        });
      },
    }),
    {
      name: 'report-generator-storage',
    }
  )
);
