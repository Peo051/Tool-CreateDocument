import { useReportStore } from '../../store/reportStore';

export default function Step3Tech() {
  const {
    algorithms, technologies, datasets,
    setAlgorithms, setTechnologies, setDatasets
  } = useReportStore();

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Technical Data</h2>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Algorithms (comma-separated)
        </label>
        <input
          type="text"
          value={algorithms.join(', ')}
          onChange={(e) => setAlgorithms(e.target.value.split(',').map(a => a.trim()).filter(Boolean))}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="BFS, DFS, A*, Dijkstra"
        />
        <p className="text-sm text-gray-500 mt-1">
          Enter algorithm names separated by commas
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Technologies (comma-separated)
        </label>
        <input
          type="text"
          value={technologies.join(', ')}
          onChange={(e) => setTechnologies(e.target.value.split(',').map(t => t.trim()).filter(Boolean))}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Python, React, TensorFlow"
        />
        <p className="text-sm text-gray-500 mt-1">
          Enter technologies used in the project
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Datasets (comma-separated)
        </label>
        <input
          type="text"
          value={datasets.join(', ')}
          onChange={(e) => setDatasets(e.target.value.split(',').map(d => d.trim()).filter(Boolean))}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="MNIST, CIFAR-10, ImageNet"
        />
        <p className="text-sm text-gray-500 mt-1">
          Enter datasets used in the project
        </p>
      </div>
    </div>
  );
}
