import { useReportStore } from '../../store/reportStore';

export default function Step4References() {
  const { references, setReferences } = useReportStore();

  const addReference = () => {
    setReferences([
      ...references,
      {
        id: `ref${references.length + 1}`,
        authors: [''],
        title: '',
        year: new Date().getFullYear(),
        source: '',
        url: '',
      },
    ]);
  };

  const removeReference = (index: number) => {
    setReferences(references.filter((_, i) => i !== index));
  };

  const updateReference = (index: number, field: string, value: any) => {
    const updated = [...references];
    updated[index] = { ...updated[index], [field]: value };
    setReferences(updated);
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold">References</h2>
        <button
          onClick={addReference}
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Add Reference
        </button>
      </div>

      {references.length === 0 ? (
        <div className="text-center py-8 text-gray-500">
          No references added yet. Click "Add Reference" to start.
        </div>
      ) : (
        <div className="space-y-4">
          {references.map((ref, index) => (
            <div key={index} className="p-4 border border-gray-200 rounded-lg">
              <div className="flex justify-between items-start mb-3">
                <h3 className="font-medium">Reference {index + 1}</h3>
                <button
                  onClick={() => removeReference(index)}
                  className="text-red-500 hover:text-red-700"
                >
                  Remove
                </button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Title
                  </label>
                  <input
                    type="text"
                    value={ref.title}
                    onChange={(e) => updateReference(index, 'title', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Reference title"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Authors (comma-separated)
                  </label>
                  <input
                    type="text"
                    value={ref.authors.join(', ')}
                    onChange={(e) =>
                      updateReference(
                        index,
                        'authors',
                        e.target.value.split(',').map((a) => a.trim()).filter(Boolean)
                      )
                    }
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Author 1, Author 2"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Year
                  </label>
                  <input
                    type="number"
                    value={ref.year}
                    onChange={(e) => updateReference(index, 'year', parseInt(e.target.value))}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="2024"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Source
                  </label>
                  <input
                    type="text"
                    value={ref.source || ''}
                    onChange={(e) => updateReference(index, 'source', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Journal, Conference, etc."
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    URL
                  </label>
                  <input
                    type="url"
                    value={ref.url || ''}
                    onChange={(e) => updateReference(index, 'url', e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="https://..."
                  />
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
