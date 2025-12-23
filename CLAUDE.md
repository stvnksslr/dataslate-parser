# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Dataslate Parser is a FastAPI web application that transforms BattleScribe roster files (.rosz/.ros) into printer-friendly HTML sheets. It supports three game systems: Warhammer 40K, Kill Team, and Horus Heresy.

## Common Commands

```bash
# Setup
poetry install
poetry shell

# Run tests
pytest                          # Run all tests with random order
pytest src/parsers/w40k/w40k_test.py  # Run specific test file
pytest -k "test_name"           # Run tests matching pattern

# Linting and type checking
ruff check src/                 # Lint code
ruff check src/ --fix           # Auto-fix linting issues
mypy src/                       # Type check

# Run application
uvicorn src.main:app            # Start server (default port 8000)
uvicorn src.main:app --reload   # Start with hot reload
```

## Architecture

### Data Flow
```
User uploads .rosz → Unzip → Validate BattleScribe version →
Detect game system → Select parser → Parse XML to Pydantic models →
Render Jinja2 template → Return printable HTML
```

### Key Directories

- `src/main.py` - FastAPI entry point with two endpoints: `GET /` (upload form), `POST /files/` (process roster)
- `src/parsers/` - Game-specific XML parsers, each implementing `parse_units(soup)` and `get_rules_summary()`
  - `w40k/` - Warhammer 40K (hierarchical selections with units, weapons, abilities)
  - `killteam/` - Kill Team (flat operative list)
  - `heresy/` - Horus Heresy (units grouped by stat type: toughness/armored/hybrid)
- `src/models/` - Pydantic data models for units (`W40kUnit`, `KillteamUnit`, `HeresyUnit` extend base `Unit`)
- `src/utils/constants.py` - Game system ID mappings to parsers and templates
- `src/static/templates/` - Jinja2 HTML templates for each game system

### Adding a New Game System
1. Create parser module in `src/parsers/<game>/` with `parse_units()` and `get_rules_summary()`
2. Create Pydantic model in `src/models/`
3. Add Jinja2 template in `src/static/templates/`
4. Register game system ID, parser, and template in `src/utils/constants.py`

### Test Structure
Tests are co-located with source files (e.g., `w40k_test.py` alongside `w40k.py`). Test fixtures are in `test_rosters/` organized by game system.

## Configuration Notes

- Python 3.11+ required
- Ruff configured with 120 char line length
- pytest runs with `--random-order` by default
- BattleScribe version 2.03+ required for roster files
