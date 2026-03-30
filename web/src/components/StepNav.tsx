import { useReportStore } from '../store/reportStore';

interface StepNavProps {
  currentStep: number;
  totalSteps: number;
}

export default function StepNav({ currentStep, totalSteps }: StepNavProps) {
  const { nextStep, prevStep } = useReportStore();

  return (
    <div className="flex justify-between pt-6 border-t">
      <button
        onClick={prevStep}
        disabled={currentStep === 1}
        className="px-6 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Previous
      </button>
      
      {currentStep < totalSteps && (
        <button
          onClick={nextStep}
          className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Next
        </button>
      )}
    </div>
  );
}
