# Data Models

## Prerequisites

* PostgreSQL 12+ (recommended).
* `pgcrypto` extension for `gen_random_uuid()`:

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
```

* `user_role` enum:

```sql
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'user_role') THEN
    CREATE TYPE user_role AS ENUM ('DM','PLAYER');
  END IF;
END$$;
```

---

## Table Reference

Each table section includes column name, type, nullability, default and a short description.

### `users`

| Column       |               Type |   Null?  | Default             | Description                       |
| ------------ | -----------------: | :------: | ------------------- | --------------------------------- |
| `id`         |             `UUID` | NOT NULL | `gen_random_uuid()` | Primary key                       |
| `name`       |     `varchar(255)` | NOT NULL | —                   | Full name                         |
| `email`      |     `varchar(255)` | NOT NULL | —                   | Unique user email                 |
| `password`   |     `varchar(255)` | NOT NULL | —                   | Password hash (store salted hash) |
| `role`       | `user_role` (enum) | NOT NULL | —                   | `DM` or `PLAYER`                  |
| `avatar_url` |             `text` |   NULL   | —                   | Avatar image URL                  |

**Notes:** `UNIQUE(email)` recommended.

---

### `colleges`

| Column        |           Type |   Null?  | Default             | Description     |
| ------------- | -------------: | :------: | ------------------- | --------------- |
| `id`          |         `UUID` | NOT NULL | `gen_random_uuid()` | PK              |
| `name`        | `varchar(255)` | NOT NULL | —                   | College name    |
| `description` |         `text` |   NULL   | —                   | Description     |
| `image_url`   |         `text` |   NULL   | —                   | Image/crest URL |

---

### `classes`

| Column        |           Type |   Null?  | Default             | FK                                   | Description       |
| ------------- | -------------: | :------: | ------------------- | ------------------------------------ | ----------------- |
| `id`          |         `UUID` | NOT NULL | `gen_random_uuid()` | —                                    | PK                |
| `name`        | `varchar(255)` | NOT NULL | —                   | —                                    | Class/course name |
| `description` |         `text` |   NULL   | —                   | —                                    | Class description |
| `college_id`  |         `UUID` |   NULL   | —                   | → `colleges.id` (ON DELETE SET NULL) | Parent college    |
| `image_url`   |         `text` |   NULL   | —                   | —                                    | Class icon        |

---

### `player_characters`

| Column             |           Type |   Null?  | Default             | FK                                   | Description                             |
| ------------------ | -------------: | :------: | ------------------- | ------------------------------------ | --------------------------------------- |
| `id`               |         `UUID` | NOT NULL | `gen_random_uuid()` | —                                    | PK                                      |
| `user_id`          |         `UUID` | NOT NULL | —                   | → `users.id` (ON DELETE CASCADE)     | Owner                                   |
| `name`             | `varchar(255)` | NOT NULL | —                   | —                                    | Character name                          |
| `image_url`        |         `text` |   NULL   | —                   | —                                    | Portrait URL                            |
| `college_year`     |          `int` |   NULL   | —                   | —                                    | In-world college year                   |
| `college_id`       |         `UUID` |   NULL   | —                   | → `colleges.id` (ON DELETE SET NULL) | Linked college                          |
| `enrolled_classes` |         `text` |   NULL   | —                   | —                                    | Free-text list (consider normalization) |
| `level`            |          `int` |   NULL   | —                   | —                                    | Character level                         |

**Suggestion:** normalize `enrolled_classes` into `character_classes(character_id, class_id)`.

---

### `character_sheet`

| Column               |                Type |   Null?  | Default             | FK                                           | Description                          |
| -------------------- | ------------------: | :------: | ------------------- | -------------------------------------------- | ------------------------------------ |
| `id`                 |              `UUID` | NOT NULL | `gen_random_uuid()` | —                                            | PK                                   |
| `character_id`       |              `UUID` | NOT NULL | —                   | → `player_characters.id` (ON DELETE CASCADE) | 1:1 reference (add UNIQUE if needed) |
| `strength`           |               `INT` |   NULL   | —                   | —                                            | Ability score                        |
| `dexterity`          |               `INT` |   NULL   | —                   | —                                            |                                      |
| `constitution`       |               `INT` |   NULL   | —                   | —                                            |                                      |
| `intelligence`       |               `INT` |   NULL   | —                   | —                                            |                                      |
| `wisdom`             |               `INT` |   NULL   | —                   | —                                            |                                      |
| `charisma`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `proficiency_bonus`  |               `INT` |   NULL   | —                   | —                                            |                                      |
| `armor_class`        |               `INT` |   NULL   | —                   | —                                            |                                      |
| `initiative`         |               `INT` |   NULL   | —                   | —                                            |                                      |
| `speed`              | `NUMERIC` / `FLOAT` |   NULL   | —                   | —                                            | Movement speed                       |
| `max_hit_points`     |               `INT` |   NULL   | —                   | —                                            |                                      |
| `current_hit_points` |               `INT` |   NULL   | —                   | —                                            |                                      |
| `temp_hit_points`    |               `INT` |   NULL   | —                   | —                                            |                                      |
| `hit_dice_total`     |               `INT` |   NULL   | —                   | —                                            |                                      |
| `hit_dice_current`   |               `INT` |   NULL   | —                   | —                                            |                                      |
| `save_str`           |               `INT` |   NULL   | —                   | —                                            | Saves                                |
| `save_dex`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `save_con`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `save_int`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `save_wis`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `save_cha`           |               `INT` |   NULL   | —                   | —                                            |                                      |
| `skills`             |              `text` |   NULL   | —                   | —                                            | Serialized structure                 |
| `background`         |              `text` |   NULL   | —                   | —                                            |                                      |
| `race`               |              `text` |   NULL   | —                   | —                                            |                                      |
| `alignment`          |              `text` |   NULL   | —                   | —                                            |                                      |
| `experience_points`  |               `INT` |   NULL   | —                   | —                                            |                                      |
| `languages`          |              `text` |   NULL   | —                   | —                                            |                                      |
| `features_traits`    |              `text` |   NULL   | —                   | —                                            |                                      |
| `proficiencies`      |              `text` |   NULL   | —                   | —                                            |                                      |
| `description`        |              `text` |   NULL   | —                   | —                                            | Free text                            |
| `created_at`         |         `timestamp` | NOT NULL | `now()`             | —                                            | Creation time                        |
| `updated_at`         |         `timestamp` | NOT NULL | `now()`             | —                                            | Last update                          |

**Note:** enforce `UNIQUE(character_id)` to guarantee true 1:1.

---

### `inventory_items`

| Column         |    Type |   Null?  | Default             | FK                                           | Description                               |
| -------------- | ------: | :------: | ------------------- | -------------------------------------------- | ----------------------------------------- |
| `id`           |  `UUID` | NOT NULL | `gen_random_uuid()` | —                                            | PK                                        |
| `character_id` |  `UUID` | NOT NULL | —                   | → `player_characters.id` (ON DELETE CASCADE) | Owner                                     |
| `item_id`      |  `UUID` |   NULL   | —                   | (optional → `items.id`)                      | Reference to global item catalog          |
| `amount`       |   `INT` |   NULL   | —                   | —                                            | Quantity                                  |
| `metadata`     | `JSONB` |   NULL   | —                   | —                                            | Flexible attributes (enchantments, notes) |

---

### `npcs`

| Column       |           Type |   Null?  | Default             | Description           |
| ------------ | -------------: | :------: | ------------------- | --------------------- |
| `id`         |         `UUID` | NOT NULL | `gen_random_uuid()` | PK                    |
| `name`       | `varchar(255)` | NOT NULL | —                   | NPC name              |
| `image_url`  |         `text` |   NULL   | —                   | Portrait URL          |
| `bio`        |         `text` |   NULL   | —                   | NPC biography         |
| `is_visible` |      `boolean` | NOT NULL | `true`              | Visibility to players |

---

### `npcs_reputation`

| Column         |   Type |   Null?  | Default             | FK                                           | Description      |
| -------------- | -----: | :------: | ------------------- | -------------------------------------------- | ---------------- |
| `id`           | `UUID` | NOT NULL | `gen_random_uuid()` | —                                            | PK               |
| `character_id` | `UUID` | NOT NULL | —                   | → `player_characters.id` (ON DELETE CASCADE) |                  |
| `npc_id`       | `UUID` | NOT NULL | —                   | → `npcs.id` (ON DELETE CASCADE)              |                  |
| `score`        |  `INT` |   NULL   | —                   | —                                            | Reputation value |

---

### `notes`

| Column           |        Type |   Null?  | Default             | Description       |
| ---------------- | ----------: | :------: | ------------------- | ----------------- |
| `id`             |      `UUID` | NOT NULL | `gen_random_uuid()` | PK                |
| `author_id`      |      `UUID` | NOT NULL | —                   | → `users.id`      |
| `content`        |      `text` | NOT NULL | —                   | Note body         |
| `is_master_only` |   `boolean` | NOT NULL | `false`             | DM-only flag      |
| `is_privative`   |   `boolean` | NOT NULL | `false`             | Private note flag |
| `created_at`     | `timestamp` | NOT NULL | `now()`             | Creation time     |
| `updated_at`     | `timestamp` | NOT NULL | `now()`             | Last update       |

---

### `character_notes` (junction)

| Column                                     |   Type |   Null?  | Default | FK                                           |
| ------------------------------------------ | -----: | :------: | ------- | -------------------------------------------- |
| `note_id`                                  | `UUID` | NOT NULL | —       | → `notes.id` (ON DELETE CASCADE)             |
| `character_id`                             | `UUID` | NOT NULL | —       | → `player_characters.id` (ON DELETE CASCADE) |
| **Primary Key:** `(note_id, character_id)` |        |          |         |                                              |

---

### `npc_notes` (junction)

| Column                               |   Type |   Null?  | Default | FK                               |
| ------------------------------------ | -----: | :------: | ------- | -------------------------------- |
| `note_id`                            | `UUID` | NOT NULL | —       | → `notes.id` (ON DELETE CASCADE) |
| `npc_id`                             | `UUID` | NOT NULL | —       | → `npcs.id` (ON DELETE CASCADE)  |
| `author_id`                          | `UUID` | NOT NULL | —       | → `users.id` (denormalized)      |
| **Primary Key:** `(note_id, npc_id)` |        |          |         |                                  |

---

### `event_notes` (junction)

| Column                                 |   Type |   Null?  | Default | FK                                 |
| -------------------------------------- | -----: | :------: | ------- | ---------------------------------- |
| `note_id`                              | `UUID` | NOT NULL | —       | → `notes.id` (ON DELETE CASCADE)   |
| `event_id`                             | `UUID` | NOT NULL | —       | → `calendar_notes.id`              |
| `author_id`                            | `UUID` | NOT NULL | —       | → `users.id`                       |
| **Primary Key:** `(note_id, event_id)` |        |          |         |                                    |

> Consider adding a FK to `calendar_notes.id` if `event_id` maps to that resource.

---

### `calendar_notes`

| Column          |           Type |   Null?  | Default             | Description        |
| --------------- | -------------: | :------: | ------------------- | ------------------ |
| `id`            |         `UUID` | NOT NULL | `gen_random_uuid()` | PK                 |
| `title`         | `varchar(255)` | NOT NULL | —                   | Event title        |
| `description`   |         `text` |   NULL   | —                   |                    |
| `game_datetime` |    `timestamp` |   NULL   | —                   | In-world date/time |
| `is_exam`       |      `boolean` | NOT NULL | `false`             | Domain flag        |

---

### `store`

| Column        |           Type |   Null?  | Default             | Description   |
| ------------- | -------------: | :------: | ------------------- | ------------- |
| `id`          |         `UUID` | NOT NULL | `gen_random_uuid()` | PK            |
| `name`        | `varchar(255)` | NOT NULL | —                   | Store name    |
| `location`    | `varchar(255)` |   NULL   | —                   | Location text |
| `description` |         `text` |   NULL   | —                   |               |
| `image_url`   |         `text` |   NULL   | —                   | Store image   |

---

### `store_items`

| Column        |            Type |   Null?  | Default             | FK                               | Description |
| ------------- | --------------: | :------: | ------------------- | -------------------------------- | ----------- |
| `id`          |          `UUID` | NOT NULL | `gen_random_uuid()` | —                                | PK          |
| `store_id`    |          `UUID` | NOT NULL | —                   | → `store.id` (ON DELETE CASCADE) |             |
| `name`        |  `varchar(255)` | NOT NULL | —                   | —                                |             |
| `description` |          `text` |   NULL   | —                   | —                                |             |
| `price`       | `decimal(10,2)` |   NULL   | —                   | —                                |             |
| `image_url`   |          `text` |   NULL   | —                   | —                                | Item image  |

---

### `books`

| Column      |           Type |   Null?  | Default             | Description     |
| ----------- | -------------: | :------: | ------------------- | --------------- |
| `id`        |         `UUID` | NOT NULL | `gen_random_uuid()` | PK              |
| `title`     | `varchar(255)` | NOT NULL | —                   | Book title      |
| `summary`   |         `text` |   NULL   | —                   |                 |
| `section`   | `varchar(255)` |   NULL   | —                   | Library section |
| `is_hidden` |      `boolean` | NOT NULL | `false`             | Visibility      |
| `image_url` |         `text` |   NULL   | —                   | Cover image     |

---

### `news`

| Column          |           Type |   Null?  | Default             | Description   |
| --------------- | -------------: | :------: | ------------------- | ------------- |
| `id`            |         `UUID` | NOT NULL | `gen_random_uuid()` | PK            |
| `headline`      | `varchar(255)` | NOT NULL | —                   | Headline      |
| `body`          |         `text` |   NULL   | —                   | Content       |
| `game_datetime` |    `timestamp` |   NULL   | —                   | In-world time |
| `image_url`     |         `text` |   NULL   | —                   | News image    |

---

### `maps`

| Column      |           Type |   Null?  | Default             | Description   |
| ----------- | -------------: | :------: | ------------------- | ------------- |
| `id`        |         `UUID` | NOT NULL | `gen_random_uuid()` | PK            |
| `title`     | `varchar(255)` | NOT NULL | —                   | Map title     |
| `image_url` |         `text` |   NULL   | —                   | Map image URL |

---

### `monsters`

| Column              |           Type |   Null?  | Default             | Description  |
| ------------------- | -------------: | :------: | ------------------- | ------------ |
| `id`                |         `UUID` | NOT NULL | `gen_random_uuid()` | PK           |
| `name`              | `varchar(255)` | NOT NULL | —                   | Monster name |
| `hit_points`        |          `INT` |   NULL   | —                   | HP           |
| `experience_points` |          `INT` |   NULL   | —                   | XP reward    |
| `strength`          |          `INT` |   NULL   | —                   | Stats        |
| `dexterity`         |          `INT` |   NULL   | —                   |              |
| `constitution`      |          `INT` |   NULL   | —                   |              |
| `intelligence`      |          `INT` |   NULL   | —                   |              |
| `wisdom`            |          `INT` |   NULL   | —                   |              |
| `charisma`          |          `INT` |   NULL   | —                   |              |
| `armor_class`       |          `INT` |   NULL   | —                   |              |
| `description`       |         `text` |   NULL   | —                   |              |
| `image_url`         |         `text` |   NULL   | —                   | Monster art  |

---

## Relationships (summary)

* `users (1) -> (M) player_characters` (`player_characters.user_id`), `ON DELETE CASCADE`.
* `player_characters (1) -> (1) character_sheet` (`character_sheet.character_id`) — consider `UNIQUE`.
* `player_characters (1) -> (M) inventory_items` (`inventory_items.character_id`), `ON DELETE CASCADE`.
* `player_characters (M) <-> (M) npcs` via `npcs_reputation` (with `score` attribute).
* `notes` attach to domain objects via junctions: `character_notes`, `npc_notes`, `event_notes`.
* `colleges (1) -> (M) classes` (`classes.college_id`) and `colleges (1) -> (M) player_characters` (`player_characters.college_id`), both `ON DELETE SET NULL`.
* `store (1) -> (M) store_items` (`ON DELETE CASCADE`).

## Mermaid

```mermaid
erDiagram
    %% =========================
    %% USERS & ROLES
    %% =========================
    USERS {
        uuid id PK
        string name
        string email
        string password
        enum role
        text avatar_url
    }

    %% =========================
    %% CAMPAIGN STRUCTURE
    %% =========================
    COLLEGES {
        uuid id PK
        string name
        text description
        text image_url
    }

    CLASSES {
        uuid id PK
        string name
        text description
        uuid college_id FK
        text image_url
    }

    PLAYER_CHARACTERS {
        uuid id PK
        uuid user_id FK
        string name
        text image_url
        int college_year
        uuid college_id FK
        text enrolled_classes
        int level
    }

    %% =========================
    %% INVENTORY & ITEMS
    %% =========================
    INVENTORY_ITEMS {
        uuid id PK
        uuid character_id FK
        uuid item_id
        int amount
        jsonb metadata
    }

    %% =========================
    %% CHARACTER SHEET
    %% =========================
    CHARACTER_SHEET {
        uuid id PK
        uuid character_id FK
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        int proficiency_bonus
        int armor_class
        int initiative
        numeric speed
        int max_hit_points
        int current_hit_points
        int temp_hit_points
        int hit_dice_total
        int hit_dice_current
        int save_str
        int save_dex
        int save_con
        int save_int
        int save_wis
        int save_cha
        text skills
        text background
        text race
        text alignment
        int experience_points
        text languages
        text features_traits
        text proficiencies
        text description
        timestamp created_at
        timestamp updated_at
    }

    %% =========================
    %% NPCs & REPUTATION
    %% =========================
    NPCS {
        uuid id PK
        string name
        text image_url
        text bio
        boolean is_visible
    }

    NPCS_REPUTATION {
        uuid id PK
        uuid character_id FK
        uuid npc_id FK
        int score
    }

    %% =========================
    %% NOTES SYSTEM
    %% =========================
    NOTES {
        uuid id PK
        uuid author_id FK
        text content
        boolean is_master_only
        boolean is_privative
        timestamp created_at
        timestamp updated_at
    }

    CHARACTER_NOTES {
        uuid note_id FK
        uuid character_id FK
    }

    NPC_NOTES {
        uuid note_id FK
        uuid npc_id FK
        uuid author_id FK
    }

    EVENT_NOTES {
        uuid note_id FK
        uuid event_id FK
        uuid author_id FK
    }

    CALENDAR_NOTES {
        uuid id PK
        string title
        text description
        timestamp game_datetime
        boolean is_exam
    }

    %% =========================
    %% STORES & ITEMS
    %% =========================
    STORE {
        uuid id PK
        string name
        string location
        text description
        text image_url
    }

    STORE_ITEMS {
        uuid id PK
        uuid store_id FK
        string name
        text description
        decimal price
        text image_url
    }

    %% =========================
    %% BOOKS
    %% =========================
    BOOKS {
        uuid id PK
        string title
        text summary
        string section
        boolean is_hidden
        text image_url
    }

    %% =========================
    %% NEWS
    %% =========================
    NEWS {
        uuid id PK
        string headline
        text body
        timestamp game_datetime
        text image_url
    }

    %% =========================
    %% MAPS
    %% =========================
    MAPS {
        uuid id PK
        string title
        text image_url
    }

    %% =========================
    %% MONSTERS
    %% =========================
    MONSTERS {
        uuid id PK
        string name
        int hit_points
        int experience_points
        int strength
        int dexterity
        int constitution
        int intelligence
        int wisdom
        int charisma
        int armor_class
        text description
        text image_url
    }

    %% =========================
    %% RELATIONSHIPS
    %% =========================
    USERS ||--o{ PLAYER_CHARACTERS : "has"
    USERS ||--o{ NOTES : "writes"
    COLLEGES ||--o{ CLASSES : "offers"
    COLLEGES ||--o{ PLAYER_CHARACTERS : "attended by"
    CLASSES ||--o{ PLAYER_CHARACTERS : "enrolled in"
    PLAYER_CHARACTERS ||--o{ INVENTORY_ITEMS : "owns"
    PLAYER_CHARACTERS ||--o{ CHARACTER_SHEET : "has"
    PLAYER_CHARACTERS ||--o{ NPCS_REPUTATION : "interacts with"
    PLAYER_CHARACTERS ||--o{ CHARACTER_NOTES : "has"
    NPCS ||--o{ NPCS_REPUTATION : "linked to"
    NPCS ||--o{ NPC_NOTES : "has notes"
    CALENDAR_NOTES ||--o{ EVENT_NOTES : "linked to"
    NOTES ||--o{ CHARACTER_NOTES : "relates to"
    NOTES ||--o{ NPC_NOTES : "relates to"
    NOTES ||--o{ EVENT_NOTES : "relates to"
    STORE ||--o{ STORE_ITEMS : "sells"
