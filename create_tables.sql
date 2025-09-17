-- Table: public.player_stats

-- DROP TABLE IF EXISTS public.player_stats;

CREATE TABLE IF NOT EXISTS public.player_stats
(
    "Name" text COLLATE pg_catalog."default",
    "Team" text COLLATE pg_catalog."default",
    "PT_Attack" integer,
    "Err_Attack" integer,
    "Att_Attack" integer,
    "MAvg_Attack" double precision,
    "p_Attack" double precision,
    "Tot_Attack" integer,
    "Efficiency_Attack" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.player_stats
    OWNER to postgres;