-- ====================================
-- 1. ENUM TYPES
-- ====================================
CREATE TYPE user_role AS ENUM ('DM','PLAYER');

-- ====================================
-- 2. CORE TABLES
-- ====================================

-- 2.1 users
CREATE TABLE users (
  id         UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(200) NOT NULL UNIQUE,
  password   TEXT         NOT NULL,
  role       user_role    NOT NULL
);

-- 2.2 player_sheet_status
CREATE TABLE player_sheet_status (
  id   SERIAL       PRIMARY KEY,
  name VARCHAR(50)  NOT NULL UNIQUE
);

-- 2.3 classes
CREATE TABLE classes (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(100) NOT NULL,
  description TEXT
);

-- 2.4 colleges
CREATE TABLE colleges (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(100) NOT NULL,
  description TEXT
);

-- 2.5 items
CREATE TABLE items (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(100) NOT NULL,
  description TEXT
);

-- 2.6 stores
CREATE TABLE stores (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(100) NOT NULL,
  location    VARCHAR(200)
);

-- 2.7 books
CREATE TABLE books (
  id       UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  title    VARCHAR(200) NOT NULL,
  section  VARCHAR(100),
  summary  TEXT
);

-- 2.8 news
CREATE TABLE news (
  id        UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  headline  VARCHAR(200) NOT NULL,
  body      TEXT,
  game_date DATE         NOT NULL
);

-- 2.9 maps
CREATE TABLE maps (
  id        UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  title     VARCHAR(100) NOT NULL,
  image_url TEXT         NOT NULL
);

-- 2.10 monsters
CREATE TABLE monsters (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name        VARCHAR(100) NOT NULL,
  stats       JSONB        NOT NULL,
  description TEXT
);

-- ====================================
-- 3. GAME DOMAIN TABLES
-- ====================================

-- 3.1 calendar_events
CREATE TABLE calendar_events (
  id             UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  title          VARCHAR(200) NOT NULL,
  description    TEXT,
  game_datetime  TIMESTAMPTZ  NOT NULL,
  is_exam        BOOLEAN      NOT NULL DEFAULT FALSE
);

-- 3.2 player_characters
CREATE TABLE player_characters (
  id               UUID       PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id          UUID       NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name             VARCHAR(100) NOT NULL,
  college_year     SMALLINT   NOT NULL,
  college_id       UUID       NOT NULL REFERENCES colleges(id) ON DELETE RESTRICT,
  class_id         UUID       NOT NULL REFERENCES classes(id)  ON DELETE RESTRICT,
  level            SMALLINT   NOT NULL DEFAULT 1 CHECK (level >= 1),
  sheet_status_id  INT        NOT NULL REFERENCES player_sheet_status(id) ON DELETE RESTRICT
);

-- 3.3 inventory_items
CREATE TABLE inventory_items (
  id            UUID      PRIMARY KEY DEFAULT gen_random_uuid(),
  character_id  UUID      NOT NULL REFERENCES player_characters(id) ON DELETE CASCADE,
  item_id       UUID      NOT NULL REFERENCES items(id)              ON DELETE RESTRICT,
  quantity      INTEGER   NOT NULL DEFAULT 1 CHECK (quantity >= 0),
  metadata      JSONB
);

-- 3.4 npcs
CREATE TABLE npcs (
  id         UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  name       VARCHAR(100) NOT NULL,
  bio        TEXT,
  is_secret  BOOLEAN      NOT NULL DEFAULT TRUE
);

-- 3.5 reputations (join character ↔ npc)
CREATE TABLE reputations (
  id            UUID      PRIMARY KEY DEFAULT gen_random_uuid(),
  character_id  UUID      NOT NULL REFERENCES player_characters(id) ON DELETE CASCADE,
  npc_id        UUID      NOT NULL REFERENCES npcs(id)              ON DELETE CASCADE,
  score         SMALLINT  NOT NULL DEFAULT 0
);

-- 3.6 player_sheet_stats
CREATE TABLE player_sheet_stats (
  id                 UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  character_id       UUID        NOT NULL REFERENCES player_characters(id) ON DELETE CASCADE,
  strength           SMALLINT    NOT NULL CHECK (strength BETWEEN 1 AND 30),
  dexterity          SMALLINT    NOT NULL CHECK (dexterity BETWEEN 1 AND 30),
  constitution       SMALLINT    NOT NULL CHECK (constitution BETWEEN 1 AND 30),
  intelligence       SMALLINT    NOT NULL CHECK (intelligence BETWEEN 1 AND 30),
  wisdom             SMALLINT    NOT NULL CHECK (wisdom BETWEEN 1 AND 30),
  charisma           SMALLINT    NOT NULL CHECK (charisma BETWEEN 1 AND 30),
  proficiency_bonus  SMALLINT    NOT NULL,
  armor_class        SMALLINT    NOT NULL,
  initiative         SMALLINT    NOT NULL,
  speed              SMALLINT    NOT NULL,
  max_hit_points     SMALLINT    NOT NULL,
  current_hit_points SMALLINT    NOT NULL,
  temp_hit_points    SMALLINT    NOT NULL DEFAULT 0,
  hit_dice_total     VARCHAR(20) NOT NULL,
  hit_dice_current   SMALLINT    NOT NULL,
  save_str           BOOLEAN     NOT NULL DEFAULT FALSE,
  save_dex           BOOLEAN     NOT NULL DEFAULT FALSE,
  save_con           BOOLEAN     NOT NULL DEFAULT FALSE,
  save_int           BOOLEAN     NOT NULL DEFAULT FALSE,
  save_wis           BOOLEAN     NOT NULL DEFAULT FALSE,
  save_cha           BOOLEAN     NOT NULL DEFAULT FALSE,
  skills             JSONB       NOT NULL DEFAULT '{}',
  background         VARCHAR(100) NOT NULL,
  race               VARCHAR(100) NOT NULL,
  alignment          VARCHAR(50)  NOT NULL,
  experience_points  INTEGER     NOT NULL DEFAULT 0,
  languages          TEXT[]      NOT NULL DEFAULT '{}',
  features_traits    JSONB       NOT NULL DEFAULT '[]',
  proficiencies      TEXT[]      NOT NULL DEFAULT '{}',
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ====================================
-- 4. NOTES INFRASTRUCTURE
-- ====================================

-- 4.1 base notes table
CREATE TABLE notes (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  author_id       UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  content         TEXT        NOT NULL,
  is_master_only  BOOLEAN     NOT NULL DEFAULT FALSE,
  is_player_only  BOOLEAN     NOT NULL DEFAULT TRUE,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 4.2 join tables for notes

CREATE TABLE character_notes (
  note_id      UUID NOT NULL REFERENCES notes(id)            ON DELETE CASCADE,
  character_id UUID NOT NULL REFERENCES player_characters(id) ON DELETE CASCADE,
  PRIMARY KEY (note_id, character_id)
);

CREATE TABLE npc_notes (
  note_id UUID NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
  npc_id  UUID NOT NULL REFERENCES npcs(id)  ON DELETE CASCADE,
  PRIMARY KEY (note_id, npc_id)
);

CREATE TABLE event_notes (
  note_id  UUID NOT NULL REFERENCES notes(id)           ON DELETE CASCADE,
  event_id UUID NOT NULL REFERENCES calendar_events(id) ON DELETE CASCADE,
  PRIMARY KEY (note_id, event_id)
);

-- ====================================
-- 5. STORE-RELATED TABLES
-- ====================================

-- store_items join
CREATE TABLE store_items (
  id       UUID      PRIMARY KEY DEFAULT gen_random_uuid(),
  store_id UUID      NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
  item_id  UUID      NOT NULL REFERENCES items(id)  ON DELETE RESTRICT,
  price    NUMERIC(10,2) NOT NULL
);

-- ====================================
-- Relationship Summary
-- ====================================
-- users (1) ── (N) player_characters
-- player_sheet_status (1) ── (N) player_characters
-- classes (1) ── (N) player_characters
-- colleges (1) ── (N) player_characters
-- player_characters (1) ── (N) inventory_items ── (1) items
-- stores (1) ── (N) store_items ── (1) items
-- player_characters (N) ── (N) npcs via reputations
-- player_characters (1) ── (1) player_sheet_stats
-- calendar_events (1) ── (N) event_notes ── (1) notes
-- player_characters (1) ── (N) character_notes ── (1) notes
-- npcs (1) ── (N) npc_notes ── (1) notes
-- notes (N) ── (1) users (author)