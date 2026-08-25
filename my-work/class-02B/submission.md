# Student Submission - Class 02B

**Name:** Nageswara Rao  
**Date:** 2026-08-24  
**Commit Hash:** `49b2d5007c9b143484f1a473d706873f6736beb3`  

---

## 1. Overview of Accomplished Tasks

In this lab, we built and orchestrated multi-agent systems using **Google ADK 2.x** (`google-adk[gcp]==2.6.0`).

### Task 1: Environment Setup & ADK 2.x Authentication
- Installed ADK 2.x inside an isolated virtual environment (`.venv`).
- Configured `.env` with Gemini API authentication (`GOOGLE_GENAI_USE_VERTEXAI=FALSE`).
- Validated starter code using `python scripts/validate_starter.py`.

### Task 2: Parent and Sub-Agent Delegation & Explicit Routing
- Connected `root_agent` to `travel_brainstormer` and `attractions_planner` sub-agents via the `sub_agents` parameter.
- Configured explicit transfer instructions in `root_agent` prompt so the parent router accurately transfers control based on user intent.

### Task 3: Session State Management & Custom Tools
- Implemented `save_attractions_to_state` using `ToolContext` to read and append to `tool_context.state["attractions"]`.
- Added state-aware prompt templates (`{attractions?}`) in `attractions_planner` to dynamically retrieve saved session state.

### Task 4: Sequential Baseline Workflow
- Verified the base `SequentialAgent` pipeline: `researcher -> screenwriter -> file_writer`.

### Task 5: Iterative Refinement with `LoopAgent`
- Imported `exit_loop` from `google.adk.tools`.
- Created the `critic` agent to evaluate plot outlines and either append `CRITICAL_FEEDBACK` to state or call `exit_loop`.
- Wrapped `[researcher, screenwriter, critic]` in a `LoopAgent` (`writers_room`) with `max_iterations=5`.

### Task 6: Parallel Fan-Out and Gather with `ParallelAgent`
- Defined `box_office_researcher` (outputting to state key `box_office_report`) and `casting_agent` (outputting to state key `casting_report`).
- Combined them into `preproduction_team = ParallelAgent(sub_agents=[box_office_researcher, casting_agent])`.
- Updated `file_writer` to gather both reports from session state alongside `PLOT_OUTLINE` and compile the final pitch file.

---

## 2. Progress Verification Output

Running `python scripts/check_progress.py` returns:

```text
Task 2 delegation: PASS
Task 3 session-state tool: PASS
Task 4 sequential baseline: PASS ['writers_room', 'preproduction_team', 'file_writer']
Task 5 loop: PASS
Task 6 parallel fan-out/gather: PASS
```

---

## 3. Reflection & Architectural Learnings

1. **Why `description` matters for Sub-Agent Selection:**
   - The parent LLM relies on each sub-agent's `description` to decide which specialist to transfer control to during multi-agent routing.

2. **Loop Termination Strategy:**
   - `LoopAgent` requires both an explicit exit tool (`exit_loop`) to terminate early when requirements are met and a hard safety cap (`max_iterations=5`) to prevent infinite execution loops and runaway token usage.

3. **Parallel Fan-Out & State Gathering:**
   - Parallel agents execute independently without direct messaging between branches. Using `output_key` (e.g., `box_office_report`, `casting_report`) saves results into shared session state, enabling downstream agents (`file_writer`) to seamlessly gather all parallel outputs.
