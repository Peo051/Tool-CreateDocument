import { useReportStore } from '../store/reportStore';
import StepIndicator from './StepIndicator';
import StepNav from './StepNav';
import ConfigImport from './ConfigImport';
import Step1Type from './steps/Step1Type';
import Step2Info from './steps/Step2Info';
import Step3Tech from './steps/Step3Tech';
import Step4References from './steps/Step4References';
import Step5Format from './steps/Step5Format';
import Step6Review from './steps/Step6Review';
import Step7Export from './steps/Step7Export';

const steps = [
  { number: 1, title: 'Report Type', component: Step1Type },
  { number: 2, title: 'Project Info', component: Step2Info },
  { number: 3, title: 'Technical Data', component: Step3Tech },
  { number: 4, title: 'References', component: Step4References },
  { number: 5, title: 'Format Options', component: Step5Format },
  { number: 6, title: 'Review', component: Step6Review },
  { number: 7, title: 'Generate', component: Step7Export },
];

export default function Wizard() {
  const currentStep = useReportStore((state) => state.currentStep);
  const CurrentStepComponent = steps[currentStep - 1].component;

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="mb-8">
        <ConfigImport />
      </div>
      
      <StepIndicator steps={steps} currentStep={currentStep} />
      
      <div className="mt-8 mb-8">
        <CurrentStepComponent />
      </div>
      
      <StepNav currentStep={currentStep} totalSteps={steps.length} />
    </div>
  );
}
