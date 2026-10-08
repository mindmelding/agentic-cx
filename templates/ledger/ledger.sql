-- The action ledger: one row per delegated action, with what a person did about it.
-- Columns from responsibilities/value.md. Postgres. The first five are the ones
-- ledger.md says cannot be skipped; ask product for those first.

create table if not exists action_ledger (
  id              bigserial primary key,
  time            timestamptz not null default now(),
  account         text        not null,
  action_class    text        not null,              -- the class name in specs/
  disposition     text        check (disposition in ('accepted', 'edited', 'ignored', 'reversed', 'blocked')),
  ref             text,                              -- the trace, message, or record the action changed

  build           text,                              -- the release that acted
  actor           text,                              -- who it acted for
  moment          text,                              -- floor playbook slug when a person was on the other end
  rung            smallint    check (rung between 0 and 3),
  held_by         text        check (held_by in ('agent', 'person')),
  context_cited   jsonb,                             -- ids of the facts the action used
  payload         jsonb,
  boundary_checks jsonb,                             -- which `never` lines were checked, and the result
  disposed_by     text,
  disposed_at     timestamptz,
  edit_diff       text,
  later_outcome   text,
  harm            text                               -- reach-based severity, when there was any
);

create index if not exists action_ledger_account_class_time on action_ledger (account, action_class, time desc);

-- Acceptance by class over the last 28 days, the number most of metrics.md starts from.
-- select action_class,
--        count(*) filter (where disposition is not null)                as disposed,
--        round(avg((disposition = 'accepted')::int) filter (where disposition is not null), 3) as acceptance
-- from action_ledger
-- where time > now() - interval '28 days'
-- group by action_class order by disposed desc;
