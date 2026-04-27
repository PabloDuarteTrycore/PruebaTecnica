-- ============================================================
-- EVM Project Tracker — Database Initialization Script
-- PostgreSQL 15+
-- ============================================================
-- Execution order:
--   1. Enable extension
--   2. Create tables (respecting FK dependencies)
--   3. Create indexes
--   4. Create trigger function
--   5. Attach triggers
-- ============================================================


-- ============================================================
-- EXTENSION
-- ============================================================

CREATE EXTENSION IF NOT EXISTS "pgcrypto";


-- ============================================================
-- TABLE: projects
-- ============================================================

CREATE TABLE projects (
    id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);


-- ============================================================
-- TABLE: activities
-- ============================================================

CREATE TABLE activities (
    id               UUID           PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id       UUID           NOT NULL
                                        REFERENCES projects(id)
                                        ON DELETE CASCADE,
    name             VARCHAR(255)   NOT NULL,
    bac              NUMERIC(15, 2) NOT NULL,
    planned_progress NUMERIC(5, 2)  NOT NULL DEFAULT 0,
    actual_progress  NUMERIC(5, 2)  NOT NULL DEFAULT 0,
    actual_cost      NUMERIC(15, 2) NOT NULL DEFAULT 0,
    created_at       TIMESTAMPTZ    NOT NULL DEFAULT NOW(),
    updated_at       TIMESTAMPTZ    NOT NULL DEFAULT NOW(),

    CONSTRAINT chk_bac_non_negative
        CHECK (bac >= 0),

    CONSTRAINT chk_planned_progress_range
        CHECK (planned_progress >= 0 AND planned_progress <= 100),

    CONSTRAINT chk_actual_progress_range
        CHECK (actual_progress >= 0 AND actual_progress <= 100),

    CONSTRAINT chk_actual_cost_non_negative
        CHECK (actual_cost >= 0)
);


-- ============================================================
-- INDEXES
-- ============================================================

-- Primary lookup: all activities belonging to a project
CREATE INDEX idx_activities_project_id
    ON activities (project_id);

-- Ordered lookup: activities by project sorted by creation date (dashboard default view)
CREATE INDEX idx_activities_project_id_created_at
    ON activities (project_id, created_at DESC);


-- ============================================================
-- TRIGGER FUNCTION: automatic updated_at stamping
-- ============================================================

CREATE OR REPLACE FUNCTION fn_set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at := NOW();
    RETURN NEW;
END;
$$;


-- ============================================================
-- TRIGGERS
-- ============================================================

CREATE TRIGGER trg_projects_updated_at
    BEFORE UPDATE ON projects
    FOR EACH ROW
    EXECUTE FUNCTION fn_set_updated_at();

CREATE TRIGGER trg_activities_updated_at
    BEFORE UPDATE ON activities
    FOR EACH ROW
    EXECUTE FUNCTION fn_set_updated_at();
