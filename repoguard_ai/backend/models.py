"""
Shared data models for RepoGuard AI.

These mirror the finding schema described in the paper (Section III):
each analysis agent emits Finding objects with a file, location,
issue type, severity, confidence, and explanation. The Orchestrator
later de-duplicates and ranks these using the priority function
P_i = alpha * S_i + beta * C_i.
"""
from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AgentName(str, Enum):
    STATIC = "static_analysis"
    SEMANTIC = "semantic_review"
    SECURITY = "security_assessment"
    SPEC = "specification_checker"


class Severity(int, Enum):
    INFO = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5


class SourceFile(BaseModel):
    path: str
    content: str


class Finding(BaseModel):
    id: str
    agent: AgentName
    file: str
    line: int = 0
    rule_id: str
    title: str
    description: str
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    cwe: Optional[str] = None
    suggestion: Optional[str] = None
    priority: Optional[float] = None
    spec_grounded: Optional[bool] = None


class ContextSnippet(BaseModel):
    file: str
    score: float
    preview: str


class AgentTiming(BaseModel):
    agent: str
    milliseconds: float


class Metrics(BaseModel):
    total_findings: int
    findings_by_agent: dict
    findings_by_severity: dict
    deduplicated_count: int
    coverage_percent: float
    coordination_overhead_ms: float
    hallucination_rate: Optional[float] = None
    agent_timings: List[AgentTiming]


class AnalyzeRequest(BaseModel):
    files: List[SourceFile]
    alpha: float = 0.7
    beta: float = 0.3
    use_llm: bool = False


class AnalyzeResponse(BaseModel):
    findings: List[Finding]
    context: dict
    metrics: Metrics
    spec: dict
