# Section Generators

Deterministic section generators with structured input/output and LLM-ready architecture.

## Package Structure

```
source/generators/
├── __init__.py                    # Package exports
├── base.py                        # Base interface
├── introduction.py                # Introduction generator
├── problem_statement.py           # Problem statement generator
├── methodology.py                 # Methodology generator
├── implementation.py              # Implementation generator
├── experiments.py                 # Experiments generator
├── results_analysis.py            # Results analysis generator
└── conclusion.py                  # Conclusion generator
```

## Base Interface

```python
from generators.base import SectionGenerator, GeneratedSection, Subsection

class SectionGenerator(ABC):
    def __init__(self, use_llm: bool = False, llm_client = None):
        pass
    
    @abstractmethod
    def generate(self, input_data: Dict[str, Any]) -> GeneratedSection:
        pass

@dataclass
class GeneratedSection:
    title: str
    content: str
    subsections: List[Subsection]
    metadata: Dict[str, Any]
```

## Usage

### Introduction

```python
from generators import IntroductionGenerator

gen = IntroductionGenerator()

input_data = {
    'title': 'AI-Powered Maze Game',
    'domain': 'Artificial Intelligence',
    'context': 'Game AI has become important...',
    'motivation': 'This project explores...',
    'objectives': ['Implement algorithms', 'Create AI'],
    'scope': 'Focuses on 2D maze navigation'
}

section = gen.generate(input_data)
print(section.title)  # "Introduction"
print(len(section.subsections))  # 4
```

### Problem Statement

```python
from generators import ProblemStatementGenerator

gen = ProblemStatementGenerator()

input_data = {
    'problem': 'Traditional game AI is predictable',
    'challenges': ['Creating fair AI', 'Balancing performance'],
    'current_solutions': [
        {
            'name': 'Rule-based AI',
            'description': 'Uses predefined rules',
            'limitations': ['Predictable', 'Not adaptive']
        }
    ],
    'gaps': ['Lack of learning', 'Poor performance']
}

section = gen.generate(input_data)
```

### Methodology

```python
from generators import MethodologyGenerator

gen = MethodologyGenerator()

input_data = {
    'approach': 'Multi-algorithm approach',
    'algorithms': [
        {'name': 'A*', 'purpose': 'Pathfinding', 'complexity': 'O(E log V)'}
    ],
    'tools': ['Python', 'NetworkX'],
    'workflow': ['Design', 'Implement', 'Test', 'Evaluate']
}

section = gen.generate(input_data)
```

### Implementation

```python
from generators import ImplementationGenerator

gen = ImplementationGenerator()

input_data = {
    'overview': 'Modular architecture',
    'components': [
        {
            'name': 'PathFinder',
            'description': 'Handles pathfinding',
            'responsibilities': ['A* search', 'Optimization']
        }
    ],
    'features': ['Real-time pathfinding', 'Multiple difficulty levels'],
    'technologies': ['Python 3.10', 'Pygame']
}

section = gen.generate(input_data)
```

### Experiments

```python
from generators import ExperimentsGenerator

gen = ExperimentsGenerator()

input_data = {
    'overview': 'Evaluate algorithm performance',
    'environment': {'hardware': 'Intel i7', 'os': 'Windows 11'},
    'metrics': ['Execution Time', 'Memory Usage'],
    'experiments': [
        {
            'name': 'Algorithm Comparison',
            'description': 'Compare A* vs Dijkstra',
            'results': 'A* was 30% faster'
        }
    ]
}

section = gen.generate(input_data)
```

### Results Analysis

```python
from generators import ResultsAnalysisGenerator

gen = ResultsAnalysisGenerator()

input_data = {
    'overview': 'Significant improvements',
    'findings': ['A* outperforms by 30%', 'Memory acceptable'],
    'performance': {'avg_time': '15ms', 'memory': '120MB'},
    'comparisons': [
        {
            'baseline': 'Dijkstra',
            'our_approach': 'A*',
            'improvement': '30% faster'
        }
    ]
}

section = gen.generate(input_data)
```

### Conclusion

```python
from generators import ConclusionGenerator

gen = ConclusionGenerator()

input_data = {
    'summary': 'Successfully implemented AI algorithms',
    'achievements': ['Implemented 5 algorithms', 'Real-time performance'],
    'contributions': ['Comparative analysis', 'Optimized implementation'],
    'future_work': ['Add ML', 'Implement multiplayer']
}

section = gen.generate(input_data)
```

## Features

✅ **Structured Input**: Each generator takes well-defined input data  
✅ **Structured Output**: Returns GeneratedSection with title, content, subsections  
✅ **No Generic Filler**: Content based on actual input data  
✅ **Deterministic**: Same input produces same output  
✅ **LLM-Ready**: Easy to plug in LLM via `use_llm` parameter  
✅ **Testable**: Simple interface, easy to test  

## Export to Dictionary

```python
section = gen.generate(input_data)
data = section.to_dict()

# Returns:
{
    'title': 'Introduction',
    'content': '...',
    'subsections': [
        {'title': 'Background', 'content': '...', 'level': 2}
    ],
    'metadata': {'domain': 'AI'}
}
```

## LLM Integration (Future)

```python
# Placeholder for future LLM integration
gen = IntroductionGenerator(use_llm=True, llm_client=my_llm)
section = gen.generate(input_data)
```

## Examples

See `examples/generators_usage.py` for comprehensive examples.

```bash
python examples/generators_usage.py
```

## Testing

All generators follow the same interface, making them easy to test:

```python
def test_introduction_generator():
    gen = IntroductionGenerator()
    input_data = {'title': 'Test', 'domain': 'AI', 'objectives': ['Obj1']}
    section = gen.generate(input_data)
    
    assert section.title == 'Introduction'
    assert len(section.subsections) > 0
    assert 'Test' in section.content
```
