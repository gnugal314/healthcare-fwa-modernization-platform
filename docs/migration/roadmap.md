# Phase-by-Phase Modernization Roadmap

## Phase 1 — Discovery

- Inventory Access databases, QueryDefs, macros, VBA, linked tables, Excel outputs.
- Identify report owners, clients, refresh cadence, SLAs, PHI fields, and KPI definitions.
- Produce source-to-target mapping and report criticality matrix.

## Phase 2 — Warehouse Build

- Stand up Bronze/Silver/Gold schemas.
- Build dimensional model and load synthetic then production-like data.
- Create audit and lineage tables.

## Phase 3 — KPI Validation

- Recreate legacy metrics as semantic views.
- Compare modern outputs against legacy Excel reports.
- Track variances by client, date, provider, scheme, and dollars.

## Phase 4 — Tableau Pilot

- Publish certified data sources.
- Build executive and client pilot dashboards.
- Validate RLS and subscription controls.

## Phase 5 — Full Migration

- Migrate report families by priority.
- Route client distribution through governed delivery.
- Freeze Access logic after acceptance.

## Phase 6 — Access Decommissioning

- Archive Access files and macros.
- Retire manual Excel distribution.
- Promote modern warehouse and Tableau semantic layer as system of record.
