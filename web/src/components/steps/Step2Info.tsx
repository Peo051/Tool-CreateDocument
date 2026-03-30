import { useReportStore } from '../../store/reportStore';

export default function Step2Info() {
  const {
    title, subtitle, description, students, advisor, university, organization,
    faculty, className, githubRepo, demoUrl, keywords,
    setTitle, setSubtitle, setDescription, setStudents, setAdvisor,
    setUniversity, setOrganization, setFaculty, setClassName,
    setGithubRepo, setDemoUrl, setKeywords
  } = useReportStore();

  const addStudent = () => {
    setStudents([...students, { name: '', id: '' }]);
  };

  const removeStudent = (index: number) => {
    setStudents(students.filter((_, i) => i !== index));
  };

  const updateStudent = (index: number, field: 'name' | 'id', value: string) => {
    const updated = [...students];
    updated[index] = { ...updated[index], [field]: value };
    setStudents(updated);
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Project Information</h2>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Title <span className="text-red-500">*</span>
        </label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter project title"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Subtitle
        </label>
        <input
          type="text"
          value={subtitle}
          onChange={(e) => setSubtitle(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter subtitle (optional)"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Description <span className="text-red-500">*</span>
        </label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows={4}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter project description"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Students/Authors <span className="text-red-500">*</span>
        </label>
        {students.map((student, index) => (
          <div key={index} className="flex gap-2 mb-2">
            <input
              type="text"
              value={student.name}
              onChange={(e) => updateStudent(index, 'name', e.target.value)}
              className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Name"
            />
            <input
              type="text"
              value={student.id || ''}
              onChange={(e) => updateStudent(index, 'id', e.target.value)}
              className="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="ID"
            />
            {students.length > 1 && (
              <button
                onClick={() => removeStudent(index)}
                className="px-3 py-2 bg-red-500 text-white rounded-md hover:bg-red-600"
              >
                Remove
              </button>
            )}
          </div>
        ))}
        <button
          onClick={addStudent}
          className="mt-2 px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
        >
          Add Student
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Advisor
          </label>
          <input
            type="text"
            value={advisor}
            onChange={(e) => setAdvisor(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Advisor name"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            University
          </label>
          <input
            type="text"
            value={university}
            onChange={(e) => setUniversity(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="University name"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Organization
          </label>
          <input
            type="text"
            value={organization}
            onChange={(e) => setOrganization(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Organization name"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Faculty
          </label>
          <input
            type="text"
            value={faculty}
            onChange={(e) => setFaculty(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Faculty/Department"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Class
          </label>
          <input
            type="text"
            value={className}
            onChange={(e) => setClassName(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Class name"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            GitHub Repository
          </label>
          <input
            type="url"
            value={githubRepo}
            onChange={(e) => setGithubRepo(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="https://github.com/..."
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Demo URL
          </label>
          <input
            type="url"
            value={demoUrl}
            onChange={(e) => setDemoUrl(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="https://..."
          />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Keywords (comma-separated)
        </label>
        <input
          type="text"
          value={keywords.join(', ')}
          onChange={(e) => setKeywords(e.target.value.split(',').map(k => k.trim()).filter(Boolean))}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="AI, Machine Learning, Python"
        />
      </div>
    </div>
  );
}
