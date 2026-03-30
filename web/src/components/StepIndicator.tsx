interface Step {
  number: number;
  title: string;
}

interface StepIndicatorProps {
  steps: Step[];
  currentStep: number;
}

export default function StepIndicator({ steps, currentStep }: StepIndicatorProps) {
  return (
    <div className="flex items-center justify-between">
      {steps.map((step, index) => (
        <div key={step.number} className="flex items-center flex-1">
          <div className="flex flex-col items-center">
            <div
              className={`w-10 h-10 rounded-full flex items-center justify-center font-semibold ${
                step.number === currentStep
                  ? 'bg-blue-600 text-white'
                  : step.number < currentStep
                  ? 'bg-green-500 text-white'
                  : 'bg-gray-200 text-gray-600'
              }`}
            >
              {step.number < currentStep ? '✓' : step.number}
            </div>
            <span className="text-xs mt-2 text-gray-600">{step.title}</span>
          </div>
          {index < steps.length - 1 && (
            <div
              className={`flex-1 h-1 mx-2 ${
                step.number < currentStep ? 'bg-green-500' : 'bg-gray-200'
              }`}
            />
          )}
        </div>
      ))}
    </div>
  );
}
