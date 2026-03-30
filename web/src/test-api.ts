// Quick API test - run this in browser console
import { api } from './api/client';

export async function testAPI() {
  console.log('Testing API connection...');
  
  try {
    const health = await api.health();
    console.log('Health check:', health);
    
    const testConfig = {
      project_info: {
        title: "Test",
        description: "Test description for validation",
        students: [{ name: "Test User", id: "123" }],
        university: "Test University"
      },
      report_profile: {
        report_type: "project_report" as const,
        language: "vi" as const
      }
    };
    
    const validation = await api.validate(testConfig);
    console.log('Validation:', validation);
    
    console.log('All API tests passed!');
  } catch (error) {
    console.error('API test failed:', error);
  }
}

// Auto-run on import
testAPI();
