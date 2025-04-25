# Photon3

## About

### 🧰 Modular Pygame Simulation Framework

A lightweight and extensible UI + simulation environment built in **Pygame**, designed to host multiple small scientific/engineering apps (e.g., particle systems, truss/beam simulators, combustion models, etc.) within a unified, custom-built interface.

### 💡 Project Goals

- Replace Dear PyGui with a fully custom, more predictable UI system
- Provide reusable UI components (buttons, sliders, toggles, etc.)
- Support modular loading of self-contained "apps"
- Enable quick prototyping and visualization of technical ideas
- Stay lightweight, minimal, and easy to debug

### 🔧 Core Features

- Custom UI framework (event handling, layout, themes, state)
- App/module loader system
- Shared UI state + button group logic
- Optional developer overlay/debug tools
- Clean separation between UI system and simulation logic


## Phases

### 🧱 Phase 1: Finalize Core UI System

- Finish base UI components: buttons, sliders, labels, etc.
- Ensure components handle:
  - Mouse events (click, hover)
  - State transitions (idle, hover, active, disabled)
  - Basic layout logic (anchoring, offset, simple row/column stacking)

---

### 📦 Phase 2: Modularize

- Refactor simulation apps into modules with a consistent structure:
  - `load()` → Setup UI and internal state
  - `update(dt)` → Update logic per frame
  - `draw(screen)` → Render visual output
  - `unload()` → Optional cleanup
- Implement a module manager:
  - Register and switch between modules
  - Manage state transitions and unloading

---

### 🧭 Phase 3: Define UI Behavior Logic

- Document button/group state behavior:
  - Toggle buttons
  - Radio groups (one active button per group)
  - Button-triggered visuals (e.g., table highlight)
- Create shared/global UI state patterns
- Add inline documentation or usage notes

---

### 🔌 Phase 4: Plug in the First Simulation App

- Choose a simple app (e.g., truss/beam simulator)
- Use your UI system to:
  - Build interactive controls (add node, apply force, etc.)
  - Render core simulation visuals (nodes, forces, beams)
- Use this as a reference implementation for future modules

---

### 📚 Phase 5: Developer Tools and Documentation

- Write a basic README or markdown doc for:
  - Creating new modules
  - Using UI components and their expected states
  - Common patterns and design decisions
- Optional: Build a developer overlay panel:
  - Show current module, FPS, UI debug info, etc.
