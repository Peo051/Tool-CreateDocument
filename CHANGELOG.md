# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-03-30 - Repository Cleanup & Web UI

### 🧹 Repository Cleanup
- **Entry Points Clarified**
  - `source/main.py` - Official CLI entry point
  - `source/api.py` - Official API entry point
  - `source/main_v2.py` - Converted to compatibility wrapper (deprecated)
  - `source/legacy_main.py` - Converted to compatibility wrapper (deprecated)

- **Documentation Reorganization**
  - Moved 18 guide files from root to `docs/`
  - Moved completion/summary files to `docs/archive/`
  - Moved test artifacts to `test_artifacts/`
  - Cleaned up root directory (50+ files → 20 essential files)

- **README Rewrite**
  - Clear entry point documentation
  - Simplified quick start
  - Updated project structure
  - Removed ambiguity around multiple main files

- **New Documentation**
  - Added `CONTRIBUTING.md` - Contribution guidelines
  - Updated `README.md` - Clearer structure and usage

### 🌐 Web UI (Complete)
- **FastAPI Backend**
  - REST API with 6 endpoints
  - Background job processing
  - Config validation and migration
  - Report preview and generation
  - File download support

- **React Frontend**
  - 7-step wizard interface
  - TypeScript + Tailwind CSS
  - Zustand state management
  - localStorage draft persistence
  - Config import/export

### ✅ Testing
- 56 tests total, 54 passing (97%)
- Config validation tests
- Generator tests
- References engine tests
- Review engine tests
- Integration tests

### 📚 Documentation Moved to docs/
- `CHART_BUILDER_GUIDE.md`
- `CHART_QUICK_REFERENCE.md`
- `GENERATORS_README.md`
- `INTEGRATION_GUIDE.md`
- `LLM_INTEGRATION_GUIDE.md`
- `MIGRATION_GUIDE.md`
- `ORCHESTRATOR_GUIDE.md`
- `OUTLINE_PLANNER.md`
- `PDF_EXPORT_GUIDE.md`
- `QUICK_REFERENCE.md`
- `RENDERER_GUIDE.md`
- `RENDERER_QUICK_REFERENCE.md`
- `REVIEW_ENGINE_GUIDE.md`
- `REVIEW_ENGINE_INTEGRATION.md`
- `SKILLS_GUIDE.md`
- `TEMPLATE_QUICK_START.md`
- `TEMPLATE_SYSTEM_GUIDE.md`
- `WEB_UI_README.md`

### 🗂️ Files Archived to docs/archive/
- Completion summaries
- Task completion notes
- Refactor summaries
- Implementation notes

---

## [1.0.0] - 2025-01-XX - Initial Release

### ✨ Core Features
- Automated report generation for 4 report types
- 7-stage pipeline architecture
- Template-based content generation
- Chart generation with matplotlib
- References engine (APA, IEEE)
- Review engine with quality checks
- DOCX and PDF output formats

### 📊 Supported Algorithms
1. DFS - Depth-First Search
2. BFS - Breadth-First Search
3. A* - A-Star pathfinding
4. Dijkstra - Shortest path
5. CSP - Constraint Satisfaction
6. Graph Coloring
7. Tarjan - Articulation points
8. Influence Map
9. Minimax - Adversarial search

### 📁 Project Structure
- Modular pipeline architecture
- Pydantic v2 validation
- Jinja2 templates
- Multiple renderers
- Comprehensive test suite

### 📝 Documentation
- README.md - Quick start
- Multiple component guides
- Developer documentation
- Example configurations

---

## Roadmap

### Version 2.1 (Planned)
- [ ] Improve test coverage to 100%
- [ ] Add more citation styles (MLA, Chicago)
- [ ] Advanced chart types
- [ ] Template customization UI
- [ ] Batch report generation

### Version 3.0 (Future)
- [ ] HTML output format
- [ ] Real-time collaboration
- [ ] Cloud deployment
- [ ] Plugin system
- [ ] Mobile app
